#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Step 1: Generate Topics and Questions

This script generates business questions and chart topics based on
chart types and professional domains.

Input:
    - data/seed_field.json: Domain definitions
    - data/chart_type.csv: Chart type definitions

Output:
    - data/output/topics/{chart_type}_{domain}.json

Usage:
    python scripts/step1_generate_topics.py --config configs/default.yaml
    python scripts/step1_generate_topics.py --chart-type "折线图" --domain "金融"
    python scripts/step1_generate_topics.py --workers 4
"""

import argparse
import json
import logging
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

import pandas as pd


# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from chartm3.config import Config
from chartm3.llm.client import LLMClient
from chartm3.prompts.topic_prompts import format_topic_prompt
from chartm3.utils.json_utils import extract_json_from_text

# Configure logging - 默认INFO级别，可通过环境变量覆盖
log_level = os.environ.get("CHARTM3_LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("step1_generate_topics.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)


def load_seed_fields(filepath: str) -> list:
    """Load domain/field definitions from JSON file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def load_chart_types(filepath: str) -> list:
    """Load chart type definitions from CSV file."""
    df = pd.read_csv(filepath)
    return json.loads(df.to_json(orient="records", force_ascii=False))


def generate_topics_for_combination(
    client: LLMClient,
    chart_type_data: dict,
    field: str,
    output_dir: str,
    skip_existing: bool = True,
    num_topics: int = 20,
    add_mode: bool = False,
) -> Optional[str]:
    """
    Generate topics for a single chart type and domain combination.
    
    Args:
        client: LLM client instance
        chart_type_data: Chart type definition dict
        field: Domain/field name
        output_dir: Output directory path
        skip_existing: Whether to skip existing files
        num_topics: Number of topics to generate
        add_mode: If True, append to existing file instead of overwriting
    
    Returns:
        Output file path if successful, None otherwise
    """
    chart_type = chart_type_data.get("细分类", "")
    chart_type_en = chart_type_data.get("英文", "") or ""
    
    # Prepare output path
    output_file = os.path.join(output_dir, f"{chart_type}_{field}.json")
    
    # Handle add mode
    existing_topics_str = ""
    existing_topics_list = []
    if add_mode and os.path.exists(output_file):
        try:
            with open(output_file, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
            existing_topics_list = existing_data.get("topics", [])
            if existing_topics_list:
                # Format existing topics for prompt
                existing_topics_str = json.dumps(
                    [{"question": t.get("question", ""), "topic": t.get("topic", "")} 
                     for t in existing_topics_list],
                    ensure_ascii=False, indent=2
                )
                logger.debug(f"Add mode: found {len(existing_topics_list)} existing topics")
        except Exception as e:
            logger.warning(f"Could not load existing topics: {e}")
    elif not add_mode and skip_existing and os.path.exists(output_file):
        # Skip if exists (normal mode)
        logger.debug(f"Skipping existing: {output_file}")
        return output_file
    
    try:
        # Format prompt
        prompt = format_topic_prompt(
            field=field,
            chart_type=chart_type,
            chart_type_en=chart_type_en,
            chart_def_visual=chart_type_data.get("视觉定义", ""),
            chart_def_scenario=chart_type_data.get("适用场景", ""),
            chart_def_data=chart_type_data.get("数据特征", ""),
            num_topics=num_topics,
            existing_topics=existing_topics_str,
        )
        
        # DEBUG: Log the complete prompt sent to LLM
        logger.debug(f"{'='*80}")
        logger.debug(f"[PROMPT] ChartType: {chart_type}, Field: {field}")
        logger.debug(f"{'='*80}")
        logger.debug(f"{prompt}")
        logger.debug(f"{'='*80}")
        
        # Call LLM
        response = client.chat(prompt)
        
        # DEBUG: Log the complete response from LLM
        logger.debug(f"[RESPONSE] ChartType: {chart_type}, Field: {field}")
        logger.debug(f"{'='*80}")
        logger.debug(f"{response}")
        logger.debug(f"{'='*80}")
        
        if not response:
            logger.error(f"Empty response for {chart_type}_{field}")
            return None
        
        # Extract JSON from response
        json_str = extract_json_from_text(response)
        if not json_str:
            logger.error(f"Failed to extract JSON for {chart_type}_{field}")
            # Save raw response for debugging
            debug_file = output_file.replace(".json", "_raw.txt")
            with open(debug_file, "w", encoding="utf-8") as f:
                f.write(response)
            return None
        
        # Parse and validate
        topics = json.loads(json_str)
        
        if not isinstance(topics, list):
            topics = [topics]
        
        # Add metadata
        all_topics = existing_topics_list + topics if add_mode else topics
        
        result = {
            "chart_type": chart_type,
            "chart_type_en": chart_type_en,
            "field": field,
            "topics": all_topics,
        }
        
        # Save result
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Generated {len(topics)} new topics (total: {len(all_topics)}): {output_file}")
        return output_file
        
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error for {chart_type}_{field}: {e}")
        return None
    except Exception as e:
        logger.error(f"Error generating topics for {chart_type}_{field}: {e}")
        return None


def generate_all_topics(
    config: Config,
    chart_types: Optional[list] = None,
    domains: Optional[list] = None,
    workers: int = 4,
    skip_existing: bool = True,
    num_topics: int = 20,
    add_mode: bool = False,
) -> dict:
    """
    Generate topics for all chart type and domain combinations.
    
    Args:
        config: Configuration object
        chart_types: List of chart type names to process (None for all)
        domains: List of domain names to process (None for all)
        workers: Number of parallel workers
        skip_existing: Whether to skip existing files
        num_topics: Number of topics to generate per combination
        add_mode: If True, append to existing files
    
    Returns:
        Statistics dict with success/failure counts
    """
    # Load data
    seed_fields = load_seed_fields(config.paths.seed_field_file)
    all_chart_types = load_chart_types(config.paths.chart_type_file)
    
    # Filter chart types if specified
    if chart_types:
        all_chart_types = [
            ct for ct in all_chart_types
            if ct.get("细分类") in chart_types
        ]
    
    # Filter domains if specified
    if domains:
        seed_fields = [f for f in seed_fields if f.get("field_cn") in domains]
    
    logger.info(f"Processing {len(all_chart_types)} chart types x {len(seed_fields)} domains")
    
    # Prepare output directory
    output_dir = os.path.join(config.paths.output_dir, "topics")
    os.makedirs(output_dir, exist_ok=True)
    
    # Create client
    client = LLMClient(
        api_key=config.llm.api_key,
        base_url=config.llm.base_url,
        model=config.llm.model,
        temperature=config.llm.temperature,
        max_tokens=config.llm.max_tokens,
    )
    
    # Generate combinations
    combinations = [
        (chart_type_data, field_data.get("field", ""))
        for chart_type_data in all_chart_types
        for field_data in seed_fields
    ]
    
    stats = {"success": 0, "failed": 0, "skipped": 0}
    
    if workers <= 1:
        # Sequential processing
        for chart_type_data, field in combinations:
            result = generate_topics_for_combination(
                client, chart_type_data, field, output_dir, skip_existing,
                num_topics=num_topics, add_mode=add_mode
            )
            if result:
                stats["success"] += 1
            else:
                stats["failed"] += 1
    else:
        # Parallel processing
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {
                executor.submit(
                    generate_topics_for_combination,
                    client, chart_type_data, field, output_dir, skip_existing,
                    num_topics, add_mode
                ): (chart_type_data.get("细分类"), field)
                for chart_type_data, field in combinations
            }
            
            for future in as_completed(futures):
                chart_type, field = futures[future]
                try:
                    result = future.result()
                    if result:
                        stats["success"] += 1
                    else:
                        stats["failed"] += 1
                except Exception as e:
                    logger.error(f"Error processing {chart_type}_{field}: {e}")
                    stats["failed"] += 1
    
    logger.info(f"Generation complete. Success: {stats['success']}, Failed: {stats['failed']}")
    stats["token_stats"] = client.get_token_stats()
    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Generate topics and questions for chart types and domains"
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
        "--domain",
        type=str,
        nargs="+",
        help="Specific domain(s) to process",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Number of parallel workers (default: 4)",
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
    parser.add_argument(
        "--num-topics",
        type=int,
        default=20,
        help="Number of topics to generate per combination (default: 20)",
    )
    parser.add_argument(
        "--add",
        action="store_true",
        help="Add mode: append new topics to existing files instead of overwriting",
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
    stats = generate_all_topics(
        config=config,
        chart_types=args.chart_type,
        domains=args.domain,
        workers=args.workers,
        skip_existing=not args.no_skip and not args.add,
        num_topics=args.num_topics,
        add_mode=args.add,
    )
    
    # Print summary
    print("\n" + "=" * 50)
    print("Topic Generation Summary")
    print("=" * 50)
    print(f"Success: {stats['success']}")
    print(f"Failed:  {stats['failed']}")
    print(f"Output:  {os.path.join(config.paths.output_dir, 'topics')}")
    ts = stats.get("token_stats", {})
    print(f"Tokens:  prompt={ts.get('prompt_tokens', 0):,} completion={ts.get('completion_tokens', 0):,} total={ts.get('total_tokens', 0):,}")
    print("=" * 50)


if __name__ == "__main__":
    main()
