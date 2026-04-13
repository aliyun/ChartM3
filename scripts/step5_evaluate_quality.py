#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Step 5: Evaluate Q&A Quality

This script evaluates the quality of generated Q&A pairs using VLM
to verify answers against chart images.

Input:
    - data/output/qa_pairs/{name}_{task_id}.json

Output:
    - data/output/qa_pairs/{name}_{task_id}.json (updated with decision field)
    - data/output/qa_pairs/rejected/{name}_{task_id}.json (rejected Q&A pairs)

Usage:
    python scripts/step5_evaluate_quality.py --config configs/default.yaml
    python scripts/step5_evaluate_quality.py --mode verification --workers 8
"""

import argparse
import json
import logging
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional



# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from chartm3.config import Config
from chartm3.llm.client import VLMClient
from chartm3.prompts.evaluation_prompts import (
    format_evaluation_prompt,
    get_evaluation_modes,
)
from chartm3.utils.json_utils import extract_json_from_text

# Configure logging - 默认INFO级别，可通过环境变量覆盖
log_level = os.environ.get("CHARTM3_LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("step5_evaluate_quality.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)


def evaluate_qa_pair(
    vlm_client: VLMClient,
    qa_file: str,
    mode: str = "verification",
    skip_evaluated: bool = True,
) -> Optional[dict]:
    """
    Evaluate a single Q&A pair.
    
    Args:
        vlm_client: VLM client instance
        qa_file: Path to Q&A JSON file
        mode: Evaluation mode
        skip_evaluated: Whether to skip already evaluated files
    
    Returns:
        Result dict with decision, None if error
    """
    try:
        # Load Q&A file
        with open(qa_file, "r", encoding="utf-8") as f:
            qa_data = json.load(f)
        
        # Check if already evaluated
        if skip_evaluated and "decision" in qa_data:
            logger.debug(f"Skipping already evaluated: {qa_file}")
            return {"decision": qa_data["decision"], "skipped": True}
        
        # Check if Q&A data exists
        if "qa" not in qa_data:
            logger.warning(f"No Q&A data in {qa_file}")
            return None
        
        qa = qa_data["qa"]
        
        # Get image path
        image_path = qa_data.get("image_file_path", "")
        if not os.path.exists(image_path):
            # Try to find from code file path
            code_path = qa_data.get("code_file_path", "")
            if code_path:
                image_path = os.path.join(os.path.dirname(code_path), "plot.png")
        
        if not os.path.exists(image_path):
            logger.warning(f"Image not found for {qa_file}")
            return None
        
        # Extract Q&A fields
        question = qa.get("question", "")
        explanation = qa.get("explanation", "")
        answer = qa.get("answer", "")
        options = qa.get("options", "")
        
        if not question or not answer:
            logger.warning(f"Missing question or answer in {qa_file}")
            return None
        
        # Format evaluation prompt
        prompt = format_evaluation_prompt(
            question=question,
            explanation=explanation,
            answer=answer,
            options=options,
            mode=mode,
        )
        
        # DEBUG: Log the complete prompt sent to VLM
        logger.debug(f"{'='*80}")
        logger.debug(f"[PROMPT] evaluate_qa {qa_file}")
        logger.debug(f"{'='*80}")
        logger.debug(f"{prompt}")
        logger.debug(f"{'='*80}")
        
        # Call VLM with image
        response = vlm_client.chat(prompt, image_paths=[image_path], enable_thinking=True)
        
        # DEBUG: Log the complete response from VLM
        logger.debug(f"[RESPONSE] evaluate_qa {qa_file}")
        logger.debug(f"{'='*80}")
        logger.debug(f"{response}")
        logger.debug(f"{'='*80}")
        
        if not response:
            logger.error(f"Empty response for {qa_file}")
            return None
        
        # Extract decision from response
        json_str = extract_json_from_text(response)
        decision = "unknown"
        
        if json_str:
            try:
                result_json = json.loads(json_str)
                decision = result_json.get("decision", "unknown")
            except json.JSONDecodeError:
                pass
        
        # Also try to extract from response text
        if decision == "unknown":
            response_lower = response.lower()
            if '"decision": "yes"' in response_lower or '"decision":"yes"' in response_lower:
                decision = "yes"
            elif '"decision": "no"' in response_lower or '"decision":"no"' in response_lower:
                decision = "no"
        
        return {
            "decision": decision,
            "evalqa_content_raw": response,
        }
        
    except Exception as e:
        logger.error(f"Error evaluating {qa_file}: {e}")
        return None


def process_qa_file(
    vlm_client: VLMClient,
    qa_file: str,
    output_dir: str,
    mode: str = "verification",
    skip_evaluated: bool = True,
) -> dict:
    """
    Process a single Q&A file and save evaluation result to output_dir.
    
    Args:
        vlm_client: VLM client instance
        qa_file: Path to Q&A JSON file
        output_dir: Directory to save evaluated results
        mode: Evaluation mode
        skip_evaluated: Whether to skip already evaluated files
    
    Returns:
        Statistics dict
    """
    stats = {"passed": 0, "rejected": 0, "error": 0, "skipped": 0}
    
    # Check if already evaluated in output_dir
    output_file = os.path.join(output_dir, os.path.basename(qa_file))
    if skip_evaluated and os.path.exists(output_file):
        try:
            with open(output_file, "r", encoding="utf-8") as f:
                existing = json.load(f)
            if "decision" in existing:
                logger.debug(f"Skipping already evaluated: {output_file}")
                stats["skipped"] += 1
                return stats
        except Exception:
            pass
    
    result = evaluate_qa_pair(
        vlm_client=vlm_client,
        qa_file=qa_file,
        mode=mode,
        skip_evaluated=False,  # We handle skip logic above
    )
    
    if result is None:
        stats["error"] += 1
        return stats
    
    if result.get("skipped"):
        stats["skipped"] += 1
        return stats
    
    # Load original data and save with evaluation result to output_dir
    try:
        with open(qa_file, "r", encoding="utf-8") as f:
            qa_data = json.load(f)
        
        # Add evaluation result
        qa_data["decision"] = result["decision"]
        qa_data["evalqa_content_raw"] = result.get("evalqa_content_raw", "")
        
        # Save to output_dir (not overwriting original)
        os.makedirs(output_dir, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(qa_data, f, ensure_ascii=False, indent=2)
        
        # Track stats
        if result["decision"] == "yes":
            stats["passed"] += 1
            logger.info(f"Passed: {output_file}")
        else:
            stats["rejected"] += 1
            logger.info(f"Rejected: {output_file}")
            
    except Exception as e:
        logger.error(f"Error saving evaluation result for {qa_file}: {e}")
        stats["error"] += 1
    
    return stats


def evaluate_all_qa(
    config: Config,
    mode: str = "verification",
    workers: int = 8,
    skip_evaluated: bool = True,
) -> dict:
    """
    Evaluate all Q&A pairs.
    
    Args:
        config: Configuration object
        mode: Evaluation mode
        workers: Number of parallel workers
        skip_evaluated: Whether to skip already evaluated files
    
    Returns:
        Statistics dict
    """
    # Find Q&A files
    qa_dir = os.path.join(config.paths.output_dir, "qa_pairs")
    qa_files = list(Path(qa_dir).glob("*.json"))
    
    # Filter out files in subdirectories (like rejected/)
    qa_files = [f for f in qa_files if f.parent == Path(qa_dir)]
    
    logger.info(f"Found {len(qa_files)} Q&A files to evaluate")
    
    # Prepare output directory for evaluated results
    eval_output_dir = os.path.join(config.paths.output_dir, "qa_evaluated")
    os.makedirs(eval_output_dir, exist_ok=True)
    
    # Create VLM client
    vlm_client = VLMClient(
        api_key=config.vlm.api_key,
        base_url=config.vlm.base_url,
        model=config.vlm.model,
        temperature=0.01,  # Low temperature for consistent evaluation
        max_tokens=config.vlm.max_tokens,
    )
    
    total_stats = {"passed": 0, "rejected": 0, "error": 0, "skipped": 0}
    
    if workers <= 1:
        # Sequential processing
        for qa_file in qa_files:
            stats = process_qa_file(
                vlm_client=vlm_client,
                qa_file=str(qa_file),
                output_dir=eval_output_dir,
                mode=mode,
                skip_evaluated=skip_evaluated,
            )
            for key in total_stats:
                total_stats[key] += stats.get(key, 0)
    else:
        # Parallel processing
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {
                executor.submit(
                    process_qa_file,
                    vlm_client, str(qa_file), eval_output_dir, mode, skip_evaluated
                ): qa_file
                for qa_file in qa_files
            }
            
            for future in as_completed(futures):
                qa_file = futures[future]
                try:
                    stats = future.result()
                    for key in total_stats:
                        total_stats[key] += stats.get(key, 0)
                except Exception as e:
                    logger.error(f"Error processing {qa_file}: {e}")
                    total_stats["error"] += 1
    
    logger.info(
        f"Evaluation complete. Passed: {total_stats['passed']}, "
        f"Rejected: {total_stats['rejected']}, Error: {total_stats['error']}, "
        f"Skipped: {total_stats['skipped']}"
    )
    total_stats["token_stats"] = vlm_client.get_token_stats()
    return total_stats


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate Q&A pair quality using VLM"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="configs/default.yaml",
        help="Path to configuration file",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=list(get_evaluation_modes().keys()),
        default="verification",
        help="Evaluation mode",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Number of parallel workers (default: 8)",
    )
    parser.add_argument(
        "--no-skip",
        action="store_true",
        help="Re-evaluate already evaluated files",
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
    
    # Print available modes
    modes = get_evaluation_modes()
    logger.info(f"Using evaluation mode: {args.mode} - {modes[args.mode]['description']}")
    
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
    
    # Run evaluation
    stats = evaluate_all_qa(
        config=config,
        mode=args.mode,
        workers=args.workers,
        skip_evaluated=not args.no_skip,
    )
    
    # Print summary
    total = stats["passed"] + stats["rejected"] + stats["error"]
    pass_rate = stats["passed"] / total * 100 if total > 0 else 0
    
    print("\n" + "=" * 50)
    print("Q&A Evaluation Summary")
    print("=" * 50)
    print(f"Passed:   {stats['passed']} ({pass_rate:.1f}%)")
    print(f"Rejected: {stats['rejected']}")
    print(f"Error:    {stats['error']}")
    print(f"Skipped:  {stats['skipped']}")
    print(f"Total:    {total}")
    ts = stats.get("token_stats", {})
    print(f"Tokens:   prompt={ts.get('prompt_tokens', 0):,} completion={ts.get('completion_tokens', 0):,} total={ts.get('total_tokens', 0):,}")
    print("=" * 50)


if __name__ == "__main__":
    main()
