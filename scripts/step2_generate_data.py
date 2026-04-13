#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Step 2: Generate Data

This script generates data for chart visualization based on topics
generated in Step 1.

Input:
    - data/output/topics/{chart_type}_{domain}.json
    - data/database/{chart_type}.csv (template data)

Output:
    - data/output/raw_data/{name}.json (metadata + data description)
    - data/output/raw_data/{name}.csv (raw data)

Usage:
    python scripts/step2_generate_data.py --config configs/default.yaml
    python scripts/step2_generate_data.py --chart-type "折线图" --workers 4
"""

import argparse
import csv
import json
import logging
import os
import re
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

import pandas as pd


# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from chartm3.config import Config
from chartm3.llm.client import LLMClient
from chartm3.prompts.data_prompts import format_data_prompt
from chartm3.utils.json_utils import extract_json_from_text
from chartm3.utils.file_utils import find_files_by_pattern
from chartm3.utils.code_utils import extract_functions_from_source, normalize_csv_path_in_code

# Configure logging - 默认INFO级别，可通过环境变量覆盖
log_level = os.environ.get("CHARTM3_LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("step2_generate_data.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)


def load_chart_types(filepath: str) -> dict:
    """Load chart type definitions as a dictionary keyed by chart type name."""
    df = pd.read_csv(filepath)
    records = json.loads(df.to_json(orient="records", force_ascii=False))
    return {r.get("细分类", ""): r for r in records}


def load_template_code(template_dir: str, chart_type: str) -> str:
    """
    Load template code for a chart type.
    
    Reads the {chart_type}_multi1.py or {chart_type}_multi.py file,
    extracts the preprocess function, and formats it as example code.
    """
    # Try _multi1.py first, fallback to _multi.py
    template_file = os.path.join(template_dir, f"{chart_type}_multi1.py")
    if not os.path.exists(template_file):
        template_file = os.path.join(template_dir, f"{chart_type}_multi.py")
    if not os.path.exists(template_file):
        logger.warning(f"Template code file not found for: {chart_type}")
        return ""
    
    with open(template_file, "r", encoding="utf-8") as f:
        code = f.read()
    
    # Extract the preprocess function using AST
    functions = extract_functions_from_source(code, ["preprocess"])
    preprocess_code = functions.get("preprocess", "")
    if not preprocess_code:
        logger.warning(f"No preprocess function found in: {template_file}")
        return ""
    
    # Build example code block
    select_code = (
        "```python\nimport pandas as pd\nimport numpy as np\n\n"
        + preprocess_code
        + '\n\nif __name__ == "__main__":\n    preprocess()\n```\n'
    )
    # Normalize all .csv paths to 'data.csv'
    select_code = normalize_csv_path_in_code(select_code)
    
    return select_code


def generate_data_for_topic(
    client: LLMClient,
    topic_data: dict,
    chart_type_info: dict,
    template_code: str,
    output_dir: str,
    base_name: str,
    topic_index: int,
    skip_existing: bool = True,
) -> Optional[str]:
    """
    Generate data for a single topic.
    
    Args:
        client: LLM client instance
        topic_data: Topic definition dict
        chart_type_info: Chart type definition dict
        template_code: Example code string for prompt
        output_dir: Output directory path
        base_name: Base name for output files
        topic_index: Index of topic in the list
        skip_existing: Whether to skip existing files
    
    Returns:
        Output file path if successful, None otherwise
    """
    output_file = os.path.join(output_dir, f"{base_name}_{topic_index}.json")
    csv_file = os.path.join(output_dir, f"{base_name}_{topic_index}.csv")
    
    # Skip if exists
    if skip_existing and os.path.exists(output_file) and os.path.exists(csv_file):
        logger.debug(f"Skipping existing: {output_file}")
        return output_file
    
    try:
        chart_type = chart_type_info.get("细分类", "")
        chart_type_en = chart_type_info.get("英文", "") or ""
        
        # Format prompt
        prompt = format_data_prompt(
            key_question=topic_data.get("question", ""),
            chart_type=f"{chart_type}{chart_type_en}",
            domain=topic_data.get("field", ""),
            topic=f"{topic_data.get('topic', '')}, {topic_data.get('description', '')}",
            chart_def_visual=chart_type_info.get("视觉定义", ""),
            chart_def_scenario=chart_type_info.get("适用场景", ""),
            chart_def_data=chart_type_info.get("数据特征", ""),
            example_code=template_code,
        )
        
        # DEBUG: Log the complete prompt sent to LLM
        logger.debug(f"{'='*80}")
        logger.debug(f"[PROMPT] {base_name}_{topic_index}")
        logger.debug(f"{'='*80}")
        logger.debug(f"{prompt}")
        logger.debug(f"{'='*80}")
        
        # Call LLM
        response = client.chat(prompt, enable_thinking=True)
        
        # DEBUG: Log the complete response from LLM
        logger.debug(f"[RESPONSE] {base_name}_{topic_index}")
        logger.debug(f"{'='*80}")
        logger.debug(f"{response}")
        logger.debug(f"{'='*80}")
        
        if not response:
            logger.error(f"Empty response for {base_name}_{topic_index}")
            return None
        
        # Build result
        result = {
            "content": response,
            "seed_field": topic_data.get("field", ""),
            "seed_topic": topic_data.get("topic", ""),
            "seed_description": topic_data.get("description", ""),
            "chart_type": chart_type,
            "question": topic_data.get("question", ""),
        }
        
        # Extract JSON from response
        json_str = extract_json_from_text(response)
        if json_str:
            try:
                content_json = json.loads(json_str)
                result["content_json"] = content_json
                
                # Handle array or single object
                data_items = content_json if isinstance(content_json, list) else [content_json]
                
                # Extract and execute data_code to generate CSV
                for item in data_items:
                    if "data_code" in item:
                        data_code = item["data_code"]
                        # Fix common issues in generated code
                        data_code = data_code.replace(
                            "apply(lambda x: int", "apply(lambda x: float"
                        )
                        # Normalize all CSV paths to 'data.csv'
                        data_code = normalize_csv_path_in_code(data_code)
                        
                        # Execute code in a temp directory to generate CSV
                        csv_generated = _execute_data_code(
                            data_code, csv_file, f"{base_name}_{topic_index}"
                        )
                        
                        if csv_generated:
                            # Store additional metadata
                            result["title"] = item.get("title", "")
                            result["description"] = item.get("description", "")
                            result["data_code"] = data_code
                            break
                        else:
                            logger.warning(
                                f"Code execution failed for {base_name}_{topic_index}"
                            )
                    elif "data" in item:
                        # Fallback: handle raw CSV data if LLM returns it
                        raw_data = item["data"]
                        if "```csv" in raw_data:
                            raw_data = raw_data.replace("```csv", "").replace("```", "")
                        if "```" in raw_data:
                            raw_data = raw_data.replace("```", "")
                        raw_data = raw_data.strip()
                        
                        with open(csv_file, "w", newline="", encoding="utf-8") as f:
                            writer = csv.writer(f)
                            for line in raw_data.split("\n"):
                                if line.strip():
                                    writer.writerow(line.split(","))
                        
                        result["title"] = item.get("title", "")
                        result["description"] = item.get("description", "")
                        break
                        
            except json.JSONDecodeError as e:
                logger.warning(f"Failed to parse JSON for {base_name}_{topic_index}: {e}")
        
        # Save JSON result
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Generated data: {output_file}")
        return output_file
        
    except Exception as e:
        logger.error(f"Error generating data for {base_name}_{topic_index}: {e}")
        return None


def _execute_data_code(data_code: str, target_csv_path: str, label: str) -> bool:
    """
    Execute LLM-generated data code in a temp directory to produce CSV.
    
    Args:
        data_code: Python code that generates data.csv
        target_csv_path: Where to save the generated CSV
        label: Label for logging
    
    Returns:
        True if CSV was successfully generated
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        original_dir = os.getcwd()
        # Convert target path to absolute before chdir
        target_csv_path = os.path.abspath(target_csv_path)
        try:
            os.chdir(tmpdir)
            exec(data_code, {"__builtins__": __builtins__, "__name__": "__main__"})
            
            # Check if data.csv was generated
            tmp_csv = os.path.join(tmpdir, "data.csv")
            if os.path.exists(tmp_csv):
                os.makedirs(os.path.dirname(target_csv_path), exist_ok=True)
                # Read and write to target (instead of rename across filesystems)
                with open(tmp_csv, "r", encoding="utf-8") as src:
                    content = src.read()
                with open(target_csv_path, "w", encoding="utf-8") as dst:
                    dst.write(content)
                logger.info(f"CSV generated successfully: {target_csv_path}")
                return True
            else:
                logger.error(f"[{label}] Code executed but data.csv not found in temp dir")
                return False
        except Exception as e:
            logger.error(f"[{label}] Code execution error: {e}")
            return False
        finally:
            os.chdir(original_dir)


def process_topic_file(
    client: LLMClient,
    topic_file: str,
    chart_types: dict,
    template_dir: str,
    output_dir: str,
    max_topics: int = 15,
    skip_existing: bool = True,
) -> dict:
    """
    Process a single topic file and generate data for its topics.
    
    Args:
        client: LLM client instance
        topic_file: Path to topic JSON file
        chart_types: Chart type definitions dict
        template_dir: Template data directory
        output_dir: Output directory
        max_topics: Maximum number of topics to process per file
        skip_existing: Whether to skip existing files
    
    Returns:
        Statistics dict
    """
    stats = {"success": 0, "failed": 0}
    
    try:
        # Load topic file
        with open(topic_file, "r", encoding="utf-8") as f:
            topic_data = json.load(f)
        
        # Handle both formats: {topics: [...]} or direct list
        if isinstance(topic_data, dict):
            chart_type = topic_data.get("chart_type", "")
            topics = topic_data.get("topics", [])
        else:
            topics = topic_data
            # Try to extract chart type from filename
            filename = os.path.basename(topic_file)
            chart_type = filename.split("_")[0]
        
        # Get chart type info
        chart_type_info = chart_types.get(chart_type, {})
        if not chart_type_info:
            # Try to find by partial match
            for ct_name, ct_info in chart_types.items():
                if ct_name in chart_type or chart_type in ct_name:
                    chart_type_info = ct_info
                    break
        
        if not chart_type_info:
            logger.warning(f"Chart type info not found for: {chart_type}")
            chart_type_info = {"细分类": chart_type}
        
        # Load template code (example preprocess function)
        template_code = load_template_code(template_dir, chart_type)
        
        # Base name for output files
        base_name = os.path.splitext(os.path.basename(topic_file))[0]
        
        # Process topics
        for i, topic in enumerate(topics[:max_topics]):
            result = generate_data_for_topic(
                client=client,
                topic_data=topic,
                chart_type_info=chart_type_info,
                template_code=template_code,
                output_dir=output_dir,
                base_name=base_name,
                topic_index=i,
                skip_existing=skip_existing,
            )
            if result:
                stats["success"] += 1
            else:
                stats["failed"] += 1
                
    except Exception as e:
        logger.error(f"Error processing topic file {topic_file}: {e}")
        stats["failed"] += 1
    
    return stats


def generate_all_data(
    config: Config,
    chart_type_filter: Optional[list] = None,
    workers: int = 4,
    max_topics: int = 15,
    skip_existing: bool = True,
) -> dict:
    """
    Generate data for all topic files.
    
    Args:
        config: Configuration object
        chart_type_filter: List of chart types to filter (None for all)
        workers: Number of parallel workers
        max_topics: Maximum topics per file
        skip_existing: Whether to skip existing files
    
    Returns:
        Statistics dict
    """
    # Load chart types
    chart_types = load_chart_types(config.paths.chart_type_file)
    
    # Find topic files
    topics_dir = os.path.join(config.paths.output_dir, "topics")
    topic_files = list(Path(topics_dir).glob("*.json"))
    
    if chart_type_filter:
        topic_files = [
            f for f in topic_files
            if any(ct in f.stem for ct in chart_type_filter)
        ]
    
    logger.info(f"Found {len(topic_files)} topic files to process")
    
    # Prepare output directory
    output_dir = os.path.join(config.paths.output_dir, "raw_data")
    os.makedirs(output_dir, exist_ok=True)
    
    # Create client
    client = LLMClient(
        api_key=config.llm.api_key,
        base_url=config.llm.base_url,
        model=config.llm.model,
        temperature=config.llm.temperature,
        max_tokens=config.llm.max_tokens,
    )
    
    total_stats = {"success": 0, "failed": 0}
    
    if workers <= 1:
        # Sequential processing
        for topic_file in topic_files:
            stats = process_topic_file(
                client=client,
                topic_file=str(topic_file),
                chart_types=chart_types,
                template_dir=config.paths.template_dir,
                output_dir=output_dir,
                max_topics=max_topics,
                skip_existing=skip_existing,
            )
            total_stats["success"] += stats["success"]
            total_stats["failed"] += stats["failed"]
    else:
        # Parallel processing (process files in parallel)
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {
                executor.submit(
                    process_topic_file,
                    client, str(topic_file), chart_types,
                    config.paths.template_dir, output_dir,
                    max_topics, skip_existing
                ): topic_file
                for topic_file in topic_files
            }
            
            for future in as_completed(futures):
                topic_file = futures[future]
                try:
                    stats = future.result()
                    total_stats["success"] += stats["success"]
                    total_stats["failed"] += stats["failed"]
                except Exception as e:
                    logger.error(f"Error processing {topic_file}: {e}")
                    total_stats["failed"] += 1
    
    logger.info(f"Data generation complete. Success: {total_stats['success']}, Failed: {total_stats['failed']}")
    total_stats["token_stats"] = client.get_token_stats()
    return total_stats


def main():
    parser = argparse.ArgumentParser(
        description="Generate data for chart visualization based on topics"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="configs/default.yaml",
        help="Path to configuration file",
    )
    parser.add_argument(
        "--chart-type",
        type=str,
        nargs="+",
        help="Specific chart type(s) to process",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Number of parallel workers (default: 4)",
    )
    parser.add_argument(
        "--max-topics",
        type=int,
        default=15,
        help="Maximum topics to process per file (default: 15)",
    )
    parser.add_argument(
        "--no-skip",
        action="store_true",
        help="Don't skip existing files, regenerate all",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        help="Override output directory",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging",
    )
    
    args = parser.parse_args()
    
    # Set log level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Load configuration
    config_path = Path(args.config)
    if config_path.exists():
        config = Config.from_yaml(str(config_path))
    else:
        logger.warning(f"Config file not found: {config_path}, using defaults")
        config = Config()
    
    # Override output directory if specified
    if args.output_dir:
        config.paths.output_dir = args.output_dir
    
    # Run generation
    stats = generate_all_data(
        config=config,
        chart_type_filter=args.chart_type,
        workers=args.workers,
        max_topics=args.max_topics,
        skip_existing=not args.no_skip,
    )
    
    # Print summary
    print("\n" + "=" * 50)
    print("Data Generation Summary")
    print("=" * 50)
    print(f"Success: {stats['success']}")
    print(f"Failed:  {stats['failed']}")
    print(f"Output:  {os.path.join(config.paths.output_dir, 'raw_data')}")
    ts = stats.get("token_stats", {})
    print(f"Tokens:  prompt={ts.get('prompt_tokens', 0):,} completion={ts.get('completion_tokens', 0):,} total={ts.get('total_tokens', 0):,}")
    print("=" * 50)


if __name__ == "__main__":
    main()
