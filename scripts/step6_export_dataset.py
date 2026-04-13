#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Step 6: Export Dataset

This script archives all generated data and exports it to training-ready
formats (e.g., LLaVA JSONL format).

Input:
    - data/output/visualizations/{name}/plot.png
    - data/output/qa_evaluated/{name}_{task_id}.json (evaluated Q&A with decision)

Output:
    - data/output/final/train.jsonl
    - data/output/final/test.jsonl
    - data/output/final/images/ (copied images)
    - data/output/final/statistics.json

Usage:
    python scripts/step6_export_dataset.py --config configs/default.yaml
    python scripts/step6_export_dataset.py --format llava --test-ratio 0.1
"""

import argparse
import json
import logging
import os
import random
import shutil
import sys
from collections import defaultdict
from pathlib import Path
from typing import Optional



# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from chartm3.config import Config

# Configure logging - 默认INFO级别，可通过环境变量覆盖
log_level = os.environ.get("CHARTM3_LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("step6_export_dataset.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)


def format_llava_conversation(
    question: str,
    answer: str,
    explanation: str = "",
    options: str = "",
    include_explanation: bool = True,
) -> list:
    """
    Format Q&A as LLaVA conversation format.
    
    Args:
        question: Question text
        answer: Answer text
        explanation: Explanation/reasoning
        options: Multiple choice options
        include_explanation: Whether to include explanation in response
    
    Returns:
        List of conversation turns
    """
    # Build full question
    full_question = question
    if options:
        if isinstance(options, list):
            options = "\n".join(options)
        full_question = f"{question}\n{options}"
    
    # Build response
    if include_explanation and explanation:
        response = f"{explanation}\n\nAnswer: {answer}"
    else:
        response = answer
    
    return [
        {
            "from": "human",
            "value": f"<image>\n{full_question}"
        },
        {
            "from": "gpt", 
            "value": response
        }
    ]


def format_llava_item(
    qa_data: dict,
    image_path: str,
    item_id: str,
    include_explanation: bool = True,
) -> Optional[dict]:
    """
    Format a single Q&A item to LLaVA format.
    
    Args:
        qa_data: Q&A data dict
        image_path: Path to image (relative to output)
        item_id: Unique item ID
        include_explanation: Whether to include explanation
    
    Returns:
        LLaVA format dict, or None if invalid
    """
    if "qa" not in qa_data:
        return None
    
    qa = qa_data["qa"]
    
    question = qa.get("question", "")
    answer = qa.get("answer", "")
    
    if not question or not answer:
        return None
    
    conversations = format_llava_conversation(
        question=question,
        answer=answer,
        explanation=qa.get("explanation", ""),
        options=qa.get("options", ""),
        include_explanation=include_explanation,
    )
    
    return {
        "id": item_id,
        "image": image_path,
        "conversations": conversations,
        "metadata": {
            "task_type": qa.get("task_type", ""),
            "question_type": qa.get("question_type", ""),
            "difficulty": qa.get("difficulty", ""),
            "chart_type": qa_data.get("chart_type", ""),
        }
    }


def collect_qa_files(qa_dir: str, only_passed: bool = True) -> list:
    """
    Collect all valid Q&A files.
    
    Args:
        qa_dir: Q&A pairs directory
        only_passed: Only include files with decision="yes"
    
    Returns:
        List of (qa_file_path, qa_data) tuples
    """
    qa_files = []
    
    for qa_file in Path(qa_dir).glob("*.json"):
        # Skip subdirectories
        if qa_file.parent != Path(qa_dir):
            continue
        
        try:
            with open(qa_file, "r", encoding="utf-8") as f:
                qa_data = json.load(f)
            
            # Skip if no Q&A data
            if "qa" not in qa_data:
                continue
            
            # Skip if not passed evaluation (when filtering)
            if only_passed:
                decision = qa_data.get("decision", "")
                if decision != "yes":
                    continue
            
            # Check if image exists
            image_path = qa_data.get("image_file_path", "")
            if not os.path.exists(image_path):
                continue
            
            qa_files.append((str(qa_file), qa_data))
            
        except Exception as e:
            logger.warning(f"Error loading {qa_file}: {e}")
    
    return qa_files


def export_dataset(
    config: Config,
    output_format: str = "llava",
    only_passed: bool = True,
    include_explanation: bool = True,
    seed: int = 42,
) -> dict:
    """
    Export dataset to specified format.
    
    Args:
        config: Configuration object
        output_format: Output format ("llava" or "raw")
        only_passed: Only include passed Q&A pairs
        include_explanation: Include explanation in response
        seed: Random seed for shuffling
    
    Returns:
        Statistics dict
    """
    # Collect Q&A files
    qa_dir = os.path.join(config.paths.output_dir, "qa_evaluated")
    qa_files = collect_qa_files(qa_dir, only_passed=only_passed)
    
    logger.info(f"Collected {len(qa_files)} valid Q&A pairs")
    
    if not qa_files:
        logger.error("No valid Q&A pairs found")
        return {"total": 0}
    
    # Prepare output directory
    final_dir = os.path.join(config.paths.output_dir, "final")
    images_dir = os.path.join(final_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    
    # Process and format data
    all_items = []
    stats = {
        "task_type": defaultdict(int),
        "question_type": defaultdict(int),
        "difficulty": defaultdict(int),
        "chart_type": defaultdict(int),
    }
    
    for qa_file, qa_data in qa_files:
        try:
            # Generate item ID
            base_name = os.path.splitext(os.path.basename(qa_file))[0]
            item_id = f"chartm3_{base_name}"
            
            # Get and copy image
            src_image = qa_data.get("image_file_path", "")
            if not os.path.exists(src_image):
                continue
            
            # Use visualization name (not QA file name) as image filename
            # so the same plot.png is only copied once per visualization
            viz_name = os.path.basename(os.path.dirname(src_image))
            image_filename = f"{viz_name}.png"
            dst_image = os.path.join(images_dir, image_filename)
            
            # Copy image if not exists
            if not os.path.exists(dst_image):
                shutil.copy2(src_image, dst_image)
            
            # Format item
            if output_format == "llava":
                item = format_llava_item(
                    qa_data=qa_data,
                    image_path=f"images/{image_filename}",
                    item_id=item_id,
                    include_explanation=include_explanation,
                )
            else:
                # Raw format
                item = {
                    "id": item_id,
                    "image": f"images/{image_filename}",
                    "qa": qa_data["qa"],
                    "metadata": {
                        "chart_type": qa_data.get("chart_type", ""),
                        "task_group": qa_data.get("task_group", ""),
                    }
                }
            
            if item:
                all_items.append(item)
                
                # Collect statistics
                if "qa" in qa_data:
                    qa = qa_data["qa"]
                    stats["task_type"][qa.get("task_type", "unknown")] += 1
                    stats["question_type"][qa.get("question_type", "unknown")] += 1
                    stats["difficulty"][qa.get("difficulty", "unknown")] += 1
                    stats["chart_type"][qa_data.get("chart_type", "unknown")] += 1
                    
        except Exception as e:
            logger.warning(f"Error processing {qa_file}: {e}")
    
    logger.info(f"Processed {len(all_items)} items")
    
    # Shuffle for randomness
    random.seed(seed)
    random.shuffle(all_items)
    
    # Save JSONL file (all data as train)
    train_file = os.path.join(final_dir, "train.jsonl")
    
    with open(train_file, "w", encoding="utf-8") as f:
        for item in all_items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    
    logger.info(f"Saved {len(all_items)} samples to {train_file}")
    
    # Save statistics
    stats_dict = {
        "total": len(all_items),
        "task_type": dict(stats["task_type"]),
        "question_type": dict(stats["question_type"]),
        "difficulty": dict(stats["difficulty"]),
        "chart_type": dict(stats["chart_type"]),
    }
    
    stats_file = os.path.join(final_dir, "statistics.json")
    with open(stats_file, "w", encoding="utf-8") as f:
        json.dump(stats_dict, f, ensure_ascii=False, indent=2)
    
    return stats_dict


def main():
    parser = argparse.ArgumentParser(
        description="Export dataset to training-ready formats"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="configs/default.yaml",
        help="Path to configuration file",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["llava", "raw"],
        default="llava",
        help="Output format (default: llava)",
    )
    parser.add_argument(
        "--include-all",
        action="store_true",
        help="Include all Q&A pairs, not just passed ones",
    )
    parser.add_argument(
        "--no-explanation",
        action="store_true",
        help="Don't include explanation in response",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for train/test split (default: 42)",
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
    
    # Run export
    stats = export_dataset(
        config=config,
        output_format=args.format,
        only_passed=not args.include_all,
        include_explanation=not args.no_explanation,
        seed=args.seed,
    )
    
    # Print summary
    print("\n" + "=" * 50)
    print("Dataset Export Summary")
    print("=" * 50)
    print(f"Total samples: {stats['total']}")
    print(f"Output:        {os.path.join(config.paths.output_dir, 'final')}")
    print("=" * 50)
    
    # Print distribution summary
    for category in ["task_type", "question_type", "difficulty", "chart_type"]:
        dist = stats.get(category, {})
        if dist:
            print(f"\n{category}:")
            for name, count in sorted(dist.items(), key=lambda x: -x[1]):
                print(f"  {name}: {count}")


if __name__ == "__main__":
    main()
