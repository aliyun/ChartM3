#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Step 4: Generate Q&A Pairs

This script generates question-answer pairs based on chart images,
visualization code, and data.

Input:
    - data/output/visualizations/{name}/{name}.py (visualization code)
    - data/output/visualizations/{name}/{name}.csv (data)
    - data/output/visualizations/{name}/plot.png (chart image)

Output:
    - data/output/qa_pairs/{name}_{task_id}.json

Usage:
    python scripts/step4_generate_qa.py --config configs/default.yaml
    python scripts/step4_generate_qa.py --task-group analysis --workers 4
    python scripts/step4_generate_qa.py --code-driven  # Use code to compute answers
"""

import argparse
import json
import logging
import os
import random
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

import pandas as pd


# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from chartm3.config import Config
from chartm3.llm.client import LLMClient, VLMClient
from chartm3.prompts.qa_prompts import (
    get_task_definition,
    format_qa_prompt,
    format_code_qa_step1_prompt,
    format_code_qa_step2_prompt,
    EXTRACTION_QA_PROMPT,
)
from chartm3.utils.code_utils import (
    extract_functions_from_source,
    execute_code_safely,
)
from chartm3.utils.json_utils import extract_json_from_text
from chartm3.utils.code_utils import extract_code_block

# Configure logging - 默认INFO级别，可通过环境变量覆盖
log_level = os.environ.get("CHARTM3_LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("step4_generate_qa.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)


def _load_extraction_allowed_chart_types(config: Config) -> set:
    """
    Load chart types that are allowed for extraction tasks from chart_type.csv.
    Only chart types with extraction=1 can generate extraction QA.
    """
    extraction_allowed = set()
    chart_type_file = os.path.join(config.paths.project_root, "data", "chart_type.csv")
    
    if not os.path.exists(chart_type_file):
        logger.warning(f"chart_type.csv not found: {chart_type_file}")
        return extraction_allowed
    
    try:
        df = pd.read_csv(chart_type_file)
        if "细分类" in df.columns and "extraction" in df.columns:
            extraction_allowed = set(df[df["extraction"] == 1]["细分类"].tolist())
            logger.info(f"Loaded {len(extraction_allowed)} chart types allowed for extraction tasks")
        else:
            logger.warning("chart_type.csv missing required columns: 细分类, extraction")
    except Exception as e:
        logger.error(f"Error loading chart_type.csv: {e}")
    
    return extraction_allowed


def select_random_task(task_definitions: list) -> dict:
    """Select a random task from task definitions."""
    # Parse TSV format task definitions
    all_tasks = []
    for task_def in task_definitions:
        lines = task_def.strip().split("\n")
        if len(lines) < 2:
            continue
        headers = lines[0].split("\t")
        for line in lines[1:]:
            values = line.split("\t")
            if len(values) >= len(headers):
                task = dict(zip(headers, values))
                all_tasks.append(task)
    
    if all_tasks:
        return random.choice(all_tasks)
    return {}


def generate_qa_standard(
    vlm_client: VLMClient,
    code: str,
    data: str,
    chart_type: str,
    image_path: str,
    task_def: str,
    is_long_data: bool = False,
) -> Optional[dict]:
    """
    Generate Q&A using standard method (VLM + image).
    
    Args:
        vlm_client: VLM client instance
        code: Visualization code
        data: Data content
        chart_type: Chart type name
        image_path: Path to chart image
        task_def: Task definition string
        is_long_data: Whether data is large
    
    Returns:
        Q&A dict if successful, None otherwise
    """
    # Format prompt
    prompt = format_qa_prompt(
        code=code,
        data=data,
        chart_type=chart_type,
        task=task_def,
        is_long_data=is_long_data,
    )
    
    # DEBUG: Log the complete prompt sent to VLM
    logger.debug(f"{'='*80}")
    logger.debug(f"[PROMPT] generate_qa_standard")
    logger.debug(f"{'='*80}")
    logger.debug(f"{prompt}")
    logger.debug(f"{'='*80}")
    
    # Call VLM with image
    response = vlm_client.chat(prompt, image_paths=[image_path], enable_thinking=True)
    
    # DEBUG: Log the complete response from VLM
    logger.debug(f"[RESPONSE] generate_qa_standard")
    logger.debug(f"{'='*80}")
    logger.debug(f"{response}")
    logger.debug(f"{'='*80}")
    
    if not response:
        return None
    
    # Extract JSON from response
    json_str = extract_json_from_text(response)
    if not json_str:
        return {"content_raw": response, "parse_error": True}
    
    try:
        qa = json.loads(json_str)
        return {"qa": qa, "content_raw": response}
    except json.JSONDecodeError:
        return {"content_raw": response, "parse_error": True}


def generate_qa_extraction(
    vlm_client: VLMClient,
    code: str,
    data: str,
    chart_type: str,
    image_path: str,
) -> Optional[dict]:
    """
    Generate Q&A for data extraction task (Chart to Data).
    
    Args:
        vlm_client: VLM client instance
        code: Visualization code
        data: Data content
        chart_type: Chart type name
        image_path: Path to chart image
    
    Returns:
        Q&A dict if successful, None otherwise
    """
    # Format extraction-specific prompt
    prompt = EXTRACTION_QA_PROMPT.format(
        code=code,
        data=data,
        chart_type=chart_type,
    )
    
    # DEBUG: Log the complete prompt sent to VLM
    logger.debug(f"{'='*80}")
    logger.debug(f"[PROMPT] generate_qa_extraction")
    logger.debug(f"{'='*80}")
    logger.debug(f"{prompt}")
    logger.debug(f"{'='*80}")
    
    # Call VLM with image
    response = vlm_client.chat(prompt, image_paths=[image_path], enable_thinking=True)
    
    # DEBUG: Log the complete response from VLM
    logger.debug(f"[RESPONSE] generate_qa_extraction")
    logger.debug(f"{'='*80}")
    logger.debug(f"{response}")
    logger.debug(f"{'='*80}")
    
    if not response:
        return None
    
    # Extract JSON from response
    json_str = extract_json_from_text(response)
    if not json_str:
        return {"content_raw": response, "parse_error": True}
    
    try:
        qa = json.loads(json_str)
        return {"qa": qa, "content_raw": response}
    except json.JSONDecodeError:
        return {"content_raw": response, "parse_error": True}


def generate_qa_code_driven(
    vlm_client: VLMClient,
    code: str,
    data_path: str,
    chart_type: str,
    image_path: str,
    task_def: str,
) -> Optional[dict]:
    """
    Generate Q&A using code-driven method (generate code to compute answer).
    
    Args:
        vlm_client: VLM client instance
        code: Visualization code
        data_path: Path to data file
        chart_type: Chart type name
        image_path: Path to chart image
        task_def: Task definition string
    
    Returns:
        Q&A dict if successful, None otherwise
    """
    # Load data sample
    try:
        df = pd.read_csv(data_path)
        data_sample = df.head().to_markdown()
    except Exception as e:
        logger.warning(f"Failed to load data: {e}")
        return None
    
    # Step 1: Generate question and code
    prompt1 = format_code_qa_step1_prompt(
        code=code,
        data=data_sample,
        data_path=data_path,
        chart_type=chart_type,
        task=task_def,
        extra="",
    )
    
    # DEBUG: Log step1 prompt
    logger.debug(f"{'='*80}")
    logger.debug(f"[PROMPT] code_driven_step1")
    logger.debug(f"{'='*80}")
    logger.debug(f"{prompt1}")
    logger.debug(f"{'='*80}")
    
    response1 = vlm_client.chat(prompt1, image_paths=[image_path], enable_thinking=True)
    
    # DEBUG: Log step1 response
    logger.debug(f"[RESPONSE] code_driven_step1")
    logger.debug(f"{'='*80}")
    logger.debug(f"{response1}")
    logger.debug(f"{'='*80}")
    
    if not response1:
        return None
    
    result = {"content_raw_step1": response1}
    
    # Extract code from step 1 response
    answer_code = extract_code_block(response1, tag="python")
    
    if not answer_code:
        logger.warning("Failed to extract code from step 1 response")
        return result
    
    # Execute code to get answer
    success, code_output = execute_code_safely(
        answer_code,
        timeout=30,
        allowed_modules=["numpy", "pandas"],
    )
    
    result["code_output"] = code_output
    
    if not success:
        logger.warning(f"Code execution failed: {code_output}")
        return result
    
    # Step 2: Generate explanation and final answer
    prompt2 = format_code_qa_step2_prompt(code_output=code_output)
    
    # Build conversation for step 2
    messages = [
        {"role": "user", "content": prompt1},
        {"role": "assistant", "content": response1},
        {"role": "user", "content": prompt2},
    ]
    
    # DEBUG: Log step2 prompt
    logger.debug(f"{'='*80}")
    logger.debug(f"[PROMPT] code_driven_step2")
    logger.debug(f"{'='*80}")
    logger.debug(f"{prompt2}")
    logger.debug(f"{'='*80}")
    
    response2 = vlm_client.chat(messages=messages, image_paths=[image_path], enable_thinking=True)
    
    # DEBUG: Log step2 response
    logger.debug(f"[RESPONSE] code_driven_step2")
    logger.debug(f"{'='*80}")
    logger.debug(f"{response2}")
    logger.debug(f"{'='*80}")
    
    if not response2:
        return result
    
    result["content_raw_step2"] = response2
    
    # Extract JSON from step 2 response
    json_str = extract_json_from_text(response2)
    if json_str:
        try:
            qa = json.loads(json_str)
            result["qa"] = qa
        except json.JSONDecodeError:
            pass
    
    return result


def _load_viz_context(viz_dir: str) -> Optional[dict]:
    """
    Load code, data, and metadata for a single visualization directory.
    
    Returns:
        Context dict with keys: base_name, code_file, data_file, image_file,
        select_code, data, is_long_data, chart_type. None if files missing.
    """
    base_name = os.path.basename(viz_dir)
    code_file = os.path.join(viz_dir, f"{base_name}.py")
    data_file = os.path.join(viz_dir, f"{base_name}.csv")
    image_file = os.path.join(viz_dir, "plot.png")
    
    if not all(os.path.exists(f) for f in [code_file, data_file, image_file]):
        logger.debug(f"Missing files for {base_name}")
        return None
    
    try:
        with open(code_file, "r", encoding="utf-8") as f:
            code = f.read()
        functions = extract_functions_from_source(code, ["plot", "preprocess"])
        select_code = functions.get("preprocess", "") + "\n\n" + functions.get("plot", "")
        
        with open(data_file, "r", encoding="utf-8") as f:
            data = f.read()
        
        return {
            "base_name": base_name,
            "code_file": code_file,
            "data_file": data_file,
            "image_file": image_file,
            "select_code": select_code,
            "data": data,
            "is_long_data": len(data.splitlines()) > 100 or len(data) > 5000,
            "chart_type": base_name.split("_")[0],
        }
    except Exception as e:
        logger.error(f"Error loading files for {base_name}: {e}")
        return None


def _generate_single_qa(
    vlm_client: VLMClient,
    ctx: dict,
    task_group: str,
    task_idx: int,
    task_def: str,
    output_dir: str,
    skip_existing: bool = True,
) -> bool:
    """
    Generate a single Q&A pair for one (image, task) combination.
    
    Returns:
        True if Q&A was successfully generated with valid qa field.
    """
    base_name = ctx["base_name"]
    output_file = os.path.join(output_dir, f"{base_name}_{task_group}_{task_idx}.json")
    
    if skip_existing and os.path.exists(output_file):
        logger.debug(f"Skipping existing: {output_file}")
        return True
    
    try:
        if task_group == "code_driven":
            result = generate_qa_code_driven(
                vlm_client=vlm_client,
                code=ctx["select_code"],
                data_path=ctx["data_file"],
                chart_type=ctx["chart_type"],
                image_path=ctx["image_file"],
                task_def=task_def,
            )
        elif task_group == "extraction":
            # Use extraction-specific prompt for Chart to Data tasks
            data_content = ctx["data"] if not ctx["is_long_data"] else f"数据量较大，代码已提供\n{ctx['select_code']}"
            result = generate_qa_extraction(
                vlm_client=vlm_client,
                code=ctx["select_code"],
                data=data_content,
                chart_type=ctx["chart_type"],
                image_path=ctx["image_file"],
            )
        else:
            data_content = ctx["data"] if not ctx["is_long_data"] else f"数据量较大，代码已提供\n{ctx['select_code']}"
            result = generate_qa_standard(
                vlm_client=vlm_client,
                code=ctx["select_code"],
                data=data_content,
                chart_type=ctx["chart_type"],
                image_path=ctx["image_file"],
                task_def=task_def,
                is_long_data=ctx["is_long_data"],
            )
        
        if result:
            result["data_file_path"] = ctx["data_file"]
            result["code_file_path"] = ctx["code_file"]
            result["image_file_path"] = ctx["image_file"]
            result["chart_type"] = ctx["chart_type"]
            result["task_group"] = task_group
            result["task_idx"] = task_idx
            
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            
            if "qa" in result:
                logger.info(f"Generated Q&A: {output_file}")
                return True
        
        return False
    except Exception as e:
        logger.error(f"Error generating Q&A for {base_name}_{task_group}_{task_idx}: {e}")
        return False


def generate_all_qa(
    config: Config,
    task_groups: list = None,
    workers: int = 4,
    skip_existing: bool = True,
) -> dict:
    """
    Generate Q&A pairs for all visualizations.
    
    Flattens all (image × task) combinations first, then distributes
    them evenly across workers for maximum concurrency.
    
    Args:
        config: Configuration object
        task_groups: List of task group names (None for "all")
        workers: Number of parallel workers
        skip_existing: Whether to skip existing files
    
    Returns:
        Statistics dict
    """
    if task_groups is None:
        task_groups = ["all"]
    
    # Find visualization directories
    viz_dir = os.path.join(config.paths.output_dir, "visualizations")
    viz_dirs = [
        d for d in Path(viz_dir).iterdir()
        if d.is_dir() and (d / "plot.png").exists()
    ]
    
    logger.info(f"Found {len(viz_dirs)} visualization directories")
    
    # Load extraction allowed chart types if extraction task is requested
    extraction_allowed = set()
    if "extraction" in task_groups or "all" in task_groups:
        extraction_allowed = _load_extraction_allowed_chart_types(config)
    
    # Prepare output directory
    output_dir = os.path.join(config.paths.output_dir, "qa_pairs")
    os.makedirs(output_dir, exist_ok=True)
    
    # Create VLM client
    vlm_client = VLMClient(
        api_key=config.vlm.api_key,
        base_url=config.vlm.base_url,
        model=config.vlm.model,
        temperature=config.vlm.temperature,
        max_tokens=config.vlm.max_tokens,
    )
    
    # =========================================================================
    # Flatten all (image × task) combinations for maximum concurrency
    # =========================================================================
    all_jobs = []  # list of (ctx, task_group, task_idx, task_def)
    skipped_extraction = 0
    for viz_path in viz_dirs:
        ctx = _load_viz_context(str(viz_path))
        if ctx is None:
            continue
        for tg in task_groups:
            # Skip extraction tasks for chart types not allowed
            if tg == "extraction" and ctx["chart_type"] not in extraction_allowed:
                skipped_extraction += 1
                logger.debug(f"Skipping extraction task for {ctx['chart_type']} (not allowed)")
                continue
            task_definitions = get_task_definition(tg)
            for task_idx, task_def in enumerate(task_definitions):
                all_jobs.append((ctx, tg, task_idx, task_def))
    
    if skipped_extraction > 0:
        logger.info(f"Skipped {skipped_extraction} extraction tasks for unsupported chart types")
    
    logger.info(f"Total jobs: {len(all_jobs)} (images × tasks), workers: {workers}")
    
    total_stats = {"success": 0, "failed": 0}
    
    if workers <= 1:
        for ctx, tg, task_idx, task_def in all_jobs:
            ok = _generate_single_qa(
                vlm_client, ctx, tg, task_idx, task_def, output_dir, skip_existing
            )
            total_stats["success" if ok else "failed"] += 1
    else:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {
                executor.submit(
                    _generate_single_qa,
                    vlm_client, ctx, tg, task_idx, task_def,
                    output_dir, skip_existing,
                ): (ctx["base_name"], tg, task_idx)
                for ctx, tg, task_idx, task_def in all_jobs
            }
            
            for future in as_completed(futures):
                label = futures[future]
                try:
                    ok = future.result()
                    total_stats["success" if ok else "failed"] += 1
                except Exception as e:
                    logger.error(f"Error processing {label}: {e}")
                    total_stats["failed"] += 1
    
    logger.info(f"Q&A generation complete. Success: {total_stats['success']}, Failed: {total_stats['failed']}")
    total_stats["token_stats"] = vlm_client.get_token_stats()
    return total_stats


def main():
    parser = argparse.ArgumentParser(
        description="Generate Q&A pairs based on chart visualizations"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="configs/default.yaml",
        help="Path to configuration file",
    )
    parser.add_argument(
        "--task-group",
        type=str,
        nargs="+",
        choices=["visual", "code_driven", "subplot", "extraction", "all"],
        default=["all"],
        help="Task groups to generate Q&A for",
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
    stats = generate_all_qa(
        config=config,
        task_groups=args.task_group,
        workers=args.workers,
        skip_existing=not args.no_skip,
    )
    
    # Print summary
    print("\n" + "=" * 50)
    print("Q&A Generation Summary")
    print("=" * 50)
    print(f"Success: {stats['success']}")
    print(f"Failed:  {stats['failed']}")
    print(f"Output:  {os.path.join(config.paths.output_dir, 'qa_pairs')}")
    ts = stats.get("token_stats", {})
    print(f"Tokens:  prompt={ts.get('prompt_tokens', 0):,} completion={ts.get('completion_tokens', 0):,} total={ts.get('total_tokens', 0):,}")
    print("=" * 50)


if __name__ == "__main__":
    main()
