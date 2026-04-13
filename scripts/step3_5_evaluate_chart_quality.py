#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Step 3.5: Evaluate Chart Quality

This script evaluates the visual quality of generated charts from Step 3.
It supports two evaluation modes:
1. Classifier mode: Uses a fine-tuned Qwen2-VL-2B model for binary classification
2. VLM mode: Uses VLM API for detailed quality assessment

Low-quality charts are marked (not deleted) for optional filtering in later steps.

Input:
    - data/output/visualizations/{name}/plot.png (chart images)
    - data/output/visualizations/{name}/{name}.json (metadata)

Output:
    - data/output/visualizations/{name}/quality.json (quality assessment)
    - Updated metadata with quality information

Usage:
    # Using VLM mode (default)
    python scripts/step3_5_evaluate_chart_quality.py --config configs/default.yaml

    # Using classifier mode
    python scripts/step3_5_evaluate_chart_quality.py --mode classifier --classifier-path /path/to/model

    # With parallel workers
    python scripts/step3_5_evaluate_chart_quality.py --workers 8

    # Filter specific chart types
    python scripts/step3_5_evaluate_chart_quality.py --chart-types 条形图,折线图
"""

import argparse
import json
import logging
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple



# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from chartm3.config import Config
from chartm3.quality import (
    create_evaluator,
    QualityResult,
    QualityLevel,
    BaseQualityEvaluator,
)

# Configure logging
log_level = os.environ.get("CHARTM3_LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("step3_5_evaluate_quality.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)


def find_visualization_folders(
    vis_dir: Path,
    chart_types: Optional[List[str]] = None,
) -> List[Path]:
    """
    Find all visualization folders that need quality evaluation.
    
    Args:
        vis_dir: Root visualization directory
        chart_types: Optional list of chart types to filter
        
    Returns:
        List of folder paths containing visualizations
    """
    folders = []
    
    if not vis_dir.exists():
        logger.warning(f"Visualization directory not found: {vis_dir}")
        return folders
    
    for folder in vis_dir.iterdir():
        if not folder.is_dir():
            continue
        
        # Check if folder has a plot.png
        plot_path = folder / "plot.png"
        if not plot_path.exists():
            continue
        
        # Filter by chart type if specified
        if chart_types:
            folder_name = folder.name
            chart_type = folder_name.split("_")[0] if "_" in folder_name else folder_name
            if chart_type not in chart_types:
                continue
        
        # Check if already evaluated (skip if quality.json exists and not forcing re-evaluation)
        quality_path = folder / "quality.json"
        if quality_path.exists():
            continue
        
        folders.append(folder)
    
    return folders


def extract_chart_type(folder_name: str) -> Optional[str]:
    """
    Extract chart type from folder name.
    
    Folder names are typically: {chart_type}_{topic}_{index}
    """
    parts = folder_name.split("_")
    if parts:
        return parts[0]
    return None


def evaluate_single_chart(
    folder: Path,
    evaluator: BaseQualityEvaluator,
) -> Tuple[Path, Optional[QualityResult], Optional[str]]:
    """
    Evaluate quality of a single chart.
    
    Args:
        folder: Folder containing the visualization
        evaluator: Quality evaluator instance
        
    Returns:
        Tuple of (folder_path, result, error_message)
    """
    plot_path = folder / "plot.png"
    
    try:
        # Extract chart type from folder name
        chart_type = extract_chart_type(folder.name)
        
        # Evaluate
        result = evaluator.evaluate(str(plot_path), chart_type=chart_type)
        
        # Save quality result
        quality_path = folder / "quality.json"
        with open(quality_path, "w", encoding="utf-8") as f:
            json.dump(result.to_dict(), f, ensure_ascii=False, indent=2)
        
        # Update metadata if exists
        meta_files = list(folder.glob("*.json"))
        for meta_file in meta_files:
            if meta_file.name == "quality.json":
                continue
            try:
                with open(meta_file, "r", encoding="utf-8") as f:
                    metadata = json.load(f)
                metadata["quality"] = result.to_dict()
                with open(meta_file, "w", encoding="utf-8") as f:
                    json.dump(metadata, f, ensure_ascii=False, indent=2)
            except Exception as e:
                logger.debug(f"Could not update metadata {meta_file}: {e}")
        
        return folder, result, None
        
    except Exception as e:
        error_msg = f"Error evaluating {folder}: {e}"
        logger.error(error_msg)
        return folder, None, error_msg


def evaluate_charts_batch(
    folders: List[Path],
    evaluator: BaseQualityEvaluator,
    batch_size: int = 8,
) -> Dict[str, Any]:
    """
    Evaluate charts in batches (for classifier mode).
    
    Args:
        folders: List of folders to evaluate
        evaluator: Quality evaluator
        batch_size: Batch size for processing
        
    Returns:
        Statistics dictionary
    """
    stats = {
        "total": len(folders),
        "high_quality": 0,
        "low_quality": 0,
        "unknown": 0,
        "errors": 0,
    }
    
    for i in range(0, len(folders), batch_size):
        batch_folders = folders[i:i + batch_size]
        image_paths = [str(f / "plot.png") for f in batch_folders]
        chart_types = [extract_chart_type(f.name) for f in batch_folders]
        
        try:
            results = evaluator.evaluate_batch(image_paths, chart_types)
            
            for folder, result in zip(batch_folders, results):
                # Save result
                quality_path = folder / "quality.json"
                with open(quality_path, "w", encoding="utf-8") as f:
                    json.dump(result.to_dict(), f, ensure_ascii=False, indent=2)
                
                # Update stats
                if result.quality == QualityLevel.HIGH:
                    stats["high_quality"] += 1
                elif result.quality == QualityLevel.LOW:
                    stats["low_quality"] += 1
                else:
                    stats["unknown"] += 1
                    
        except Exception as e:
            logger.error(f"Batch evaluation error: {e}")
            stats["errors"] += len(batch_folders)
    
    return stats


def evaluate_charts_parallel(
    folders: List[Path],
    evaluator: BaseQualityEvaluator,
    num_workers: int = 4,
) -> Dict[str, Any]:
    """
    Evaluate charts in parallel using thread pool.
    
    Args:
        folders: List of folders to evaluate
        evaluator: Quality evaluator
        num_workers: Number of parallel workers
        
    Returns:
        Statistics dictionary
    """
    stats = {
        "total": len(folders),
        "high_quality": 0,
        "low_quality": 0,
        "unknown": 0,
        "errors": 0,
    }
    
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = {
            executor.submit(evaluate_single_chart, folder, evaluator): folder
            for folder in folders
        }
        
        for future in as_completed(futures):
            folder, result, error = future.result()
            
            if error:
                stats["errors"] += 1
            elif result:
                if result.quality == QualityLevel.HIGH:
                    stats["high_quality"] += 1
                elif result.quality == QualityLevel.LOW:
                    stats["low_quality"] += 1
                else:
                    stats["unknown"] += 1
    
    return stats


def main():
    parser = argparse.ArgumentParser(description="Step 3.5: Evaluate Chart Quality")
    parser.add_argument("--config", type=str, default="configs/default.yaml",
                        help="Path to configuration file")
    parser.add_argument("--mode", type=str, choices=["classifier", "vlm"], default="vlm",
                        help="Evaluation mode: classifier or vlm (default: vlm)")
    parser.add_argument("--classifier-path", type=str, default=None,
                        help="Path to classifier model (required for classifier mode)")
    parser.add_argument("--base-model-path", type=str, default="Qwen/Qwen2-VL-2B-Instruct",
                        help="Path to base Qwen2-VL model for classifier mode")
    parser.add_argument("--workers", type=int, default=4,
                        help="Number of parallel workers")
    parser.add_argument("--batch-size", type=int, default=8,
                        help="Batch size for classifier mode")
    parser.add_argument("--chart-types", type=str, default=None,
                        help="Comma-separated list of chart types to evaluate")
    parser.add_argument("--input-dir", type=str, default=None,
                        help="Input visualization directory (overrides config)")
    parser.add_argument("--force", action="store_true",
                        help="Force re-evaluation of all charts")
    parser.add_argument("--device", type=str, default="cuda",
                        help="Device for classifier mode (cuda/cpu)")
    
    args = parser.parse_args()
    
    # Load configuration
    config = Config(args.config)
    
    # Determine input directory
    vis_dir = Path(args.input_dir) if args.input_dir else config.paths.visualizations_dir
    
    logger.info(f"Evaluation mode: {args.mode}")
    logger.info(f"Input directory: {vis_dir}")
    
    # Parse chart types filter
    chart_types = None
    if args.chart_types:
        chart_types = [ct.strip() for ct in args.chart_types.split(",")]
        logger.info(f"Filtering chart types: {chart_types}")
    
    # Find folders to evaluate
    folders = find_visualization_folders(vis_dir, chart_types)
    
    if args.force:
        # If forcing, include folders that already have quality.json
        all_folders = []
        for folder in vis_dir.iterdir():
            if folder.is_dir() and (folder / "plot.png").exists():
                if chart_types:
                    chart_type = extract_chart_type(folder.name)
                    if chart_type not in chart_types:
                        continue
                all_folders.append(folder)
        folders = all_folders
    
    if not folders:
        logger.info("No charts to evaluate")
        return
    
    logger.info(f"Found {len(folders)} charts to evaluate")
    
    # Create evaluator
    if args.mode == "classifier":
        if not args.classifier_path:
            logger.error("Classifier path is required for classifier mode")
            logger.error("Use: --classifier-path /path/to/classifier/model")
            sys.exit(1)
        
        from chartm3.quality import get_classifier
        ChartQualityClassifier = get_classifier()
        evaluator = ChartQualityClassifier(
            model_path=args.classifier_path,
            base_model_path=args.base_model_path,
            device=args.device,
            batch_size=args.batch_size,
        )
    else:  # VLM mode
        evaluator = create_evaluator(
            mode="vlm",
            base_url=config.vlm.base_url,
            api_key=config.vlm.api_key,
            model=config.vlm.model,
            temperature=0.3,  # Lower temperature for more consistent evaluation
            timeout=config.vlm.timeout,
        )
    
    # Run evaluation
    with evaluator:
        if args.mode == "classifier":
            # Use batch evaluation for classifier
            stats = evaluate_charts_batch(folders, evaluator, args.batch_size)
        else:
            # Use parallel evaluation for VLM
            stats = evaluate_charts_parallel(folders, evaluator, args.workers)
    
    # Print summary
    logger.info("=" * 50)
    logger.info("Quality Evaluation Summary")
    logger.info("=" * 50)
    logger.info(f"Total evaluated: {stats['total']}")
    logger.info(f"High quality: {stats['high_quality']} ({100*stats['high_quality']/max(1,stats['total']):.1f}%)")
    logger.info(f"Low quality: {stats['low_quality']} ({100*stats['low_quality']/max(1,stats['total']):.1f}%)")
    logger.info(f"Unknown: {stats['unknown']}")
    logger.info(f"Errors: {stats['errors']}")
    logger.info("=" * 50)
    
    # Save summary
    summary_path = vis_dir / "quality_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    logger.info(f"Summary saved to: {summary_path}")


if __name__ == "__main__":
    main()
