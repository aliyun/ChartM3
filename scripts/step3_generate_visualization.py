#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Step 3: Generate Visualization Code

This script generates visualization code based on data from Step 2
and template examples, then executes the code to render charts.

Input:
    - data/output/raw_data/{name}.json (metadata)
    - data/output/raw_data/{name}.csv (data)
    - data/database/{chart_type}.py (template code)
    - data/database/{chart_type}.csv (template data)

Output:
    - data/output/visualizations/{name}/{name}.py (visualization code)
    - data/output/visualizations/{name}/{name}.csv (processed data)
    - data/output/visualizations/{name}/plot.png (rendered chart)

Usage:
    python scripts/step3_generate_visualization.py --config configs/default.yaml
    python scripts/step3_generate_visualization.py --workers 4
"""

import argparse
import json
import logging
import os
import random
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional, Tuple

import pandas as pd
from PIL import Image


# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from chartm3.config import Config
from chartm3.llm.client import LLMClient
from chartm3.prompts.visualization_prompts import (
    format_vis_plan_prompt,
    format_visualization_prompt,
    format_code_fix_prompt,
)
from chartm3.utils.code_utils import (
    execute_code_safely,
    post_process_visualization_code,
    extract_code_block,
)
from chartm3.utils.json_utils import extract_json_from_text

# Configure logging - 默认INFO级别，可通过环境变量覆盖
log_level = os.environ.get("CHARTM3_LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("step3_generate_visualization.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)


# Main code template for execution
MAIN_TEMPLATE = """
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

{llm_gen_functions}

if __name__ == "__main__":
    test_data = pd.read_csv("{data_path}", skipinitialspace=True)
    try:
        data = preprocess(test_data)
        data.to_csv("{output_csv}", index=False)
    except Exception as e:
        print(f"Preprocess error: {{e}}")
        data = test_data
    plot(test_data)
"""

MAX_IMAGE_LONG_SIDE = 1000  # 图片长边最大像素


def extract_plot_functions(code: str) -> list:
    """
    Extract plot function bodies from template code.
    
    Extracts plot, plot_1, plot_2, etc. functions and renames them to 'plot'.
    Returns a list of function bodies for random selection.
    
    Args:
        code: Full source code from template file
        
    Returns:
        List of plot function bodies (as strings)
    """
    # Pattern to match plot functions: def plot(...): ... (until next def or end of code)
    # Use re.DOTALL to make . match newlines, and match until next function definition
    pattern = r"(def plot(?:_\d+)?\([^)]*\):)(.*?)(?=\ndef |\ndef\w|\Z)"
    
    matches = re.finditer(pattern, code, re.DOTALL)
    
    results = []
    for match in matches:
        func_decl = match.group(1)
        func_body = match.group(2)
        
        # Rename function to 'plot'
        modified_decl = re.sub(r'def plot(?:_\d+)?', 'def plot', func_decl)
        
        # Combine declaration and body, strip trailing whitespace
        func_code = (modified_decl + func_body).rstrip()
        results.append(func_code)
    
    return results if results else [code]


def load_template_examples(template_dir: str) -> dict:
    """
    Load template examples from the database directory.
    
    Loads {chart_type}_multi.py or {chart_type}_multi1.py files,
    mapping them to the base chart_type name (e.g. '基础条形图').
    
    Returns a dict mapping chart type to {data_head, code} info.
    """
    examples = {}
    
    if not os.path.exists(template_dir):
        logger.warning(f"Template directory not found: {template_dir}")
        return examples
    
    for filename in os.listdir(template_dir):
        if not filename.endswith(".py"):
            continue
        
        # Extract base chart type: "基础条形图_multi.py" -> "基础条形图"
        raw_name = filename.replace(".py", "")
        # Strip _multi / _multi1 suffixes to get the base chart type
        base_chart_type = re.sub(r'_multi\d*$', '', raw_name)
        
        code_file = os.path.join(template_dir, filename)
        data_file = os.path.join(template_dir, f"{base_chart_type}.csv")
        
        try:
            with open(code_file, "r", encoding="utf-8") as f:
                code = f.read()
            
            # Extract plot functions (plot, plot_1, plot_2, etc.)
            plot_functions = extract_plot_functions(code)
            
            data_head = ""
            if os.path.exists(data_file):
                df = pd.read_csv(data_file)
                data_head = df.head().to_markdown()
            
            if base_chart_type in examples:
                # Append additional plot variants
                examples[base_chart_type]["code"].extend(plot_functions)
            else:
                examples[base_chart_type] = {
                    "code": plot_functions,
                    "data_head": data_head,
                }
        except Exception as e:
            logger.warning(f"Error loading template for {filename}: {e}")
    
    logger.info(f"Loaded {len(examples)} template examples")
    return examples


def load_chart_type_info(filepath: str) -> pd.DataFrame:
    """Load chart type information from CSV."""
    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    return pd.DataFrame()


def _resize_image(image_path: str, max_long_side: int) -> None:
    """
    Resize image so that the long side <= max_long_side, keeping aspect ratio.
    Overwrites the original file.
    """
    try:
        with Image.open(image_path) as img:
            w, h = img.size
            long_side = max(w, h)
            if long_side <= max_long_side:
                return  # No resize needed
            scale = max_long_side / long_side
            new_w = int(w * scale)
            new_h = int(h * scale)
            img_resized = img.resize((new_w, new_h), Image.LANCZOS)
            img_resized.save(image_path)
            logger.info(f"Resized {os.path.basename(image_path)}: {w}x{h} -> {new_w}x{new_h}")
    except Exception as e:
        logger.warning(f"Failed to resize {image_path}: {e}")


def generate_visualization_code(
    client: LLMClient,
    data_file: str,
    meta_file: str,
    examples: dict,
    chart_type_info: pd.DataFrame,
    output_dir: str,
    skip_existing: bool = True,
) -> Optional[str]:
    """
    Generate visualization code for a single data file.
    
    Args:
        client: LLM client instance
        data_file: Path to the CSV data file
        meta_file: Path to the JSON metadata file
        examples: Template examples dict
        chart_type_info: Chart type info DataFrame
        output_dir: Output directory for visualizations
        skip_existing: Whether to skip existing files
    
    Returns:
        Output directory path if successful, None otherwise
    """
    base_name = os.path.splitext(os.path.basename(data_file))[0]
    item_output_dir = os.path.join(output_dir, base_name)
    output_py = os.path.join(item_output_dir, f"{base_name}.py")
    output_png = os.path.join(item_output_dir, "plot.png")
    output_csv = os.path.join(item_output_dir, f"{base_name}.csv")
    
    # Skip if exists
    if skip_existing and os.path.exists(output_png):
        logger.debug(f"Skipping existing: {output_png}")
        return item_output_dir
    
    try:
        # Load metadata
        if not os.path.exists(meta_file):
            logger.warning(f"Metadata file not found: {meta_file}")
            return None
        
        with open(meta_file, "r", encoding="utf-8") as f:
            meta = json.load(f)
        
        chart_type = meta.get("chart_type", "")
        
        # Check if we have template for this chart type
        if chart_type not in examples:
            logger.warning(f"No template found for chart type: {chart_type}")
            return None
        
        # Load data
        test_data = pd.read_csv(data_file)
        
        # Get visual definition
        vis_definition = ""
        data_characteristics = ""
        try:
            info_row = chart_type_info[chart_type_info["细分类"] == chart_type]
            if not info_row.empty:
                vis_definition = f"图表视觉定义：{info_row['视觉定义'].values[0]}"
                data_characteristics = f"\n图表数据要求：{info_row['数据特征'].values[0]}"
        except Exception as e:
            logger.debug(f"Could not get visual definition: {e}")
        
        # Prepare data descriptions
        data_head = test_data.head().to_markdown()
        data_describe = test_data.describe().to_markdown()
        try:
            data_describe_object = test_data.describe(include="object").to_markdown()
        except:
            data_describe_object = ""
        
        # =====================================================================
        # Stage 1: Generate visualization plan
        # =====================================================================
        plan_prompt = format_vis_plan_prompt(
            file_name=meta.get("title", base_name),
            data_head=data_head,
            data_describe=data_describe,
            data_describe_object=data_describe_object,
            target_chart_type=chart_type,
            visual_definition=vis_definition + data_characteristics,
        )
        
        logger.debug(f"{'='*80}")
        logger.debug(f"[PROMPT] Stage 1 - Plan: {base_name}")
        logger.debug(f"{'='*80}")
        logger.debug(f"{plan_prompt}")
        logger.debug(f"{'='*80}")
        
        plan_response = client.chat(plan_prompt)
        
        logger.debug(f"[RESPONSE] Stage 1 - Plan: {base_name}")
        logger.debug(f"{'='*80}")
        logger.debug(f"{plan_response}")
        logger.debug(f"{'='*80}")
        
        # Extract a plan from response
        vis_guidance = ""
        if plan_response:
            json_str = extract_json_from_text(plan_response)
            if json_str:
                try:
                    plan_data = json.loads(json_str)
                    if "guidance" in plan_data:
                        vis_guidance = plan_data["guidance"]
                        logger.info(f"Extracted guidance for {base_name}")
                except json.JSONDecodeError as e:
                    logger.warning(f"Failed to parse plan JSON for {base_name}: {e}")
                    logger.info(f"JSON content that failed to parse: {json_str[:1000]}")
        
        if not vis_guidance:
            logger.warning(f"No plan generated for {base_name}, using seed_description as fallback")
            vis_guidance = meta.get("seed_description", "")
        
        # =====================================================================
        # Stage 2: Generate visualization code
        # =====================================================================
        sample_code = random.choice(examples[chart_type]["code"])
        
        prompt = format_visualization_prompt(
            target_chart_type=chart_type,
            visual_definition=vis_definition + data_characteristics,
            sample_data_head=examples[chart_type]["data_head"],
            sample_code=sample_code,
            file_name=meta.get("title", base_name),
            seed_description=meta.get("seed_description", ""),
            data_head=data_head,
            data_describe=data_describe,
            data_describe_object=data_describe_object,
            vis_guidance=vis_guidance,
        )
        
        # DEBUG: Log the complete prompt sent to LLM
        logger.debug(f"{'='*80}")
        logger.debug(f"[PROMPT] Stage 2 - Code: {base_name}")
        logger.debug(f"{'='*80}")
        logger.debug(f"{prompt}")
        logger.debug(f"{'='*80}")
        
        # Call LLM
        response = client.chat(prompt)
        
        # DEBUG: Log the complete response from LLM
        logger.debug(f"[RESPONSE] Stage 2 - Code: {base_name}")
        logger.debug(f"{'='*80}")
        logger.debug(f"{response}")
        logger.debug(f"{'='*80}")
        
        if not response:
            logger.error(f"Empty response for {base_name}")
            return None
        
        # Extract code from response
        code = extract_code_block(response, tag="python")
        
        if not code:
            logger.error(f"Failed to extract code for {base_name}")
            # Save raw response for debugging
            os.makedirs(item_output_dir, exist_ok=True)
            with open(os.path.join(item_output_dir, "response_raw.txt"), "w") as f:
                f.write(response)
            return None
        
        # Post-process code
        code = post_process_visualization_code(code)
        
        # Replace all plt.savefig(...) calls with absolute path version (thread-safe)
        abs_plot_path = os.path.abspath(output_png)
        code = re.sub(
            r"plt\.savefig\([^)]*\)",
            f"plt.savefig('{abs_plot_path}', dpi=150, bbox_inches='tight')",
            code,
        )
        
        # Replace plotly's write_image calls with absolute path
        # Covers: fig.write_image("plot.png"), pio.write_image(fig, "plot.png"), write_image(fig, "plot.png")
        code = re.sub(
            r"(fig\.write_image\(\s*)(['\"])(plot\.png)\2(\s*[,)])",
            lambda m: f"{m.group(1)}{m.group(2)}{abs_plot_path}{m.group(2)}{m.group(4)}",
            code,
        )
        code = re.sub(
            r"(pio\.write_image\(\s*fig\s*,\s*)(['\"])(plot\.png)\2(\s*[,)])",
            lambda m: f"{m.group(1)}{m.group(2)}{abs_plot_path}{m.group(2)}{m.group(4)}",
            code,
        )
        code = re.sub(
            r"(?<![a-zA-Z0-9_.])(write_image\(\s*fig\s*,\s*)(['\"])(plot\.png)\2(\s*[,)])",
            lambda m: f"{m.group(1)}{m.group(2)}{abs_plot_path}{m.group(2)}{m.group(4)}",
            code,
        )
        
        # Create output directory
        os.makedirs(item_output_dir, exist_ok=True)
        
        # Copy original data
        shutil.copy2(data_file, output_csv)
        
        # Create executable script using absolute paths (thread-safe, no os.chdir needed)
        full_code = MAIN_TEMPLATE.format(
            llm_gen_functions=code,
            data_path=os.path.abspath(output_csv),
            output_csv=os.path.abspath(output_csv),
        )
        
        # Save code
        with open(output_py, "w", encoding="utf-8") as f:
            f.write(full_code)
        
        # =====================================================================
        # Stage 3: Execute code with retry on failure
        # =====================================================================
        max_retries = 5
        attempt = 0
        success = False
        exec_output = ""
        
        while attempt < max_retries and not success:
            attempt += 1
            
            # Determine which file to execute
            if attempt == 1:
                current_output_py = output_py
            else:
                current_output_py = os.path.join(item_output_dir, f"{base_name}_fix{attempt-1}.py")
            
            # Execute code in subprocess (matplotlib pyplot is NOT thread-safe,
            # so exec() in ThreadPoolExecutor causes blank images)
            try:
                result = subprocess.run(
                    [sys.executable, current_output_py],
                    capture_output=True, text=True, timeout=60,
                )
                success = result.returncode == 0
                exec_output = result.stdout + result.stderr
            except subprocess.TimeoutExpired:
                success = False
                exec_output = "Timeout: code execution exceeded 60 seconds"
            except Exception as e:
                success = False
                exec_output = str(e)
            
            # Save execution output for this attempt
            exec_log_file = os.path.join(item_output_dir, f"exec_attempt{attempt}.log")
            with open(exec_log_file, "w", encoding="utf-8") as f:
                f.write(f"Exit code: {result.returncode if 'result' in locals() else 'N/A'}\n")
                f.write(f"Success: {success}\n")
                f.write(f"PNG exists: {os.path.exists(output_png)}\n")
                f.write(f"\n--- Output ---\n{exec_output}\n")
            
            if success and os.path.exists(output_png):
                logger.info(f"Code execution succeeded for {base_name} on attempt {attempt}")
                break
            
            # Execution failed, prepare for retry
            if attempt < max_retries:
                logger.warning(
                    f"Code execution failed for {base_name} (attempt {attempt}/{max_retries}): {exec_output[:200]}"
                )
                
                # Read current code for fix prompt
                with open(current_output_py, "r", encoding="utf-8") as f:
                    current_code = f.read()
                
                # Build fix prompt
                fix_prompt = format_code_fix_prompt(
                    code=current_code,
                    error_log=exec_output,
                    chart_type=chart_type,
                )
                
                logger.info(f"Requesting code fix for {base_name} (attempt {attempt})")
                logger.debug(f"[PROMPT] Fix attempt {attempt}: {base_name}")
                logger.debug(f"{'='*80}")
                logger.debug(f"{fix_prompt}")
                logger.debug(f"{'='*80}")
                
                # Call LLM for fix
                fix_response = client.chat(fix_prompt)
                
                logger.debug(f"[RESPONSE] Fix attempt {attempt}: {base_name}")
                logger.debug(f"{'='*80}")
                logger.debug(f"{fix_response}")
                logger.debug(f"{'='*80}")
                
                if fix_response:
                    # Extract fixed code
                    fixed_code = extract_code_block(fix_response, tag="python")
                    if fixed_code:
                        # Post-process and update code
                        fixed_code = post_process_visualization_code(fixed_code)
                        
                        # Replace plt.savefig calls
                        fixed_code = re.sub(
                            r"plt\.savefig\([^)]*\)",
                            f"plt.savefig('{abs_plot_path}', dpi=150, bbox_inches='tight')",
                            fixed_code,
                        )
                        
                        # Replace plotly's write_image calls with absolute path
                        # Covers: fig.write_image("plot.png"), pio.write_image(fig, "plot.png"), write_image(fig, "plot.png")
                        fixed_code = re.sub(
                            r"(fig\.write_image\(\s*)(['\"])(plot\.png)\2(\s*[,)])",
                            lambda m: f"{m.group(1)}{m.group(2)}{abs_plot_path}{m.group(2)}{m.group(4)}",
                            fixed_code,
                        )
                        fixed_code = re.sub(
                            r"(pio\.write_image\(\s*fig\s*,\s*)(['\"])(plot\.png)\2(\s*[,)])",
                            lambda m: f"{m.group(1)}{m.group(2)}{abs_plot_path}{m.group(2)}{m.group(4)}",
                            fixed_code,
                        )
                        fixed_code = re.sub(
                            r"(?<![a-zA-Z0-9_.])(write_image\(\s*fig\s*,\s*)(['\"])(plot\.png)\2(\s*[,)])",
                            lambda m: f"{m.group(1)}{m.group(2)}{abs_plot_path}{m.group(2)}{m.group(4)}",
                            fixed_code,
                        )
                        
                        # Recreate full code
                        full_code = MAIN_TEMPLATE.format(
                            llm_gen_functions=fixed_code,
                            data_path=os.path.abspath(output_csv),
                            output_csv=os.path.abspath(output_csv),
                        )
                        
                        # Save fixed code to new file
                        fix_output_py = os.path.join(item_output_dir, f"{base_name}_fix{attempt}.py")
                        with open(fix_output_py, "w", encoding="utf-8") as f:
                            f.write(full_code)
                        
                        logger.info(f"Applied code fix for {base_name} (attempt {attempt}), saved to {fix_output_py}")
                    else:
                        logger.warning(f"Failed to extract fixed code for {base_name} (attempt {attempt})")
                else:
                    logger.warning(f"Empty fix response for {base_name} (attempt {attempt})")
            else:
                # All retries exhausted
                logger.error(f"Code execution failed for {base_name} after {max_retries} attempts")
        
        # Final result handling
        if not success:
            logger.warning(f"Code execution failed for {base_name}: {exec_output}")
            with open(os.path.join(item_output_dir, "error.txt"), "w") as f:
                f.write(exec_output)
        elif not os.path.exists(output_png):
            logger.warning(f"Chart not generated for {base_name}")
        else:
            # Resize image: long side <= MAX_IMAGE_LONG_SIDE, keep aspect ratio
            _resize_image(output_png, MAX_IMAGE_LONG_SIDE)
            logger.info(f"Generated visualization: {output_png}")
        
        return item_output_dir
        
    except Exception as e:
        logger.error(f"Error generating visualization for {base_name}: {e}")
        return None


def generate_all_visualizations(
    config: Config,
    chart_type_filter: Optional[list] = None,
    workers: int = 4,
    skip_existing: bool = True,
) -> dict:
    """
    Generate visualizations for all data files.
    
    Args:
        config: Configuration object
        chart_type_filter: List of chart types to filter (None for all)
        workers: Number of parallel workers
        skip_existing: Whether to skip existing files
    
    Returns:
        Statistics dict
    """
    # Load templates and chart type info
    examples = load_template_examples(config.paths.template_dir)
    chart_type_info = load_chart_type_info(config.paths.chart_type_file)
    
    # Find data files
    raw_data_dir = os.path.join(config.paths.output_dir, "raw_data")
    data_files = list(Path(raw_data_dir).glob("*.csv"))
    
    if chart_type_filter:
        data_files = [
            f for f in data_files
            if any(ct in f.stem for ct in chart_type_filter)
        ]
    
    logger.info(f"Found {len(data_files)} data files to process")
    
    # Prepare output directory
    output_dir = os.path.join(config.paths.output_dir, "visualizations")
    os.makedirs(output_dir, exist_ok=True)
    
    # Create client
    client = LLMClient(
        api_key=config.llm.api_key,
        base_url=config.llm.base_url,
        model=config.llm.model,
        temperature=config.llm.temperature,
        max_tokens=config.llm.max_tokens,
    )
    
    stats = {"success": 0, "failed": 0}
    
    # Build file pairs (data + meta)
    file_pairs = []
    for data_file in data_files:
        meta_file = data_file.with_suffix(".json")
        if meta_file.exists():
            file_pairs.append((str(data_file), str(meta_file)))
        else:
            logger.debug(f"No metadata for {data_file}")
    
    if workers <= 1:
        # Sequential processing
        for data_file, meta_file in file_pairs:
            result = generate_visualization_code(
                client=client,
                data_file=data_file,
                meta_file=meta_file,
                examples=examples,
                chart_type_info=chart_type_info,
                output_dir=output_dir,
                skip_existing=skip_existing,
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
                    generate_visualization_code,
                    client, data_file, meta_file,
                    examples, chart_type_info, output_dir, skip_existing
                ): (data_file, meta_file)
                for data_file, meta_file in file_pairs
            }
            
            for future in as_completed(futures):
                data_file, meta_file = futures[future]
                try:
                    result = future.result()
                    if result:
                        stats["success"] += 1
                    else:
                        stats["failed"] += 1
                except Exception as e:
                    logger.error(f"Error processing {data_file}: {e}")
                    stats["failed"] += 1
    
    logger.info(f"Visualization generation complete. Success: {stats['success']}, Failed: {stats['failed']}")
    stats["token_stats"] = client.get_token_stats()
    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Generate visualization code and render charts"
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
    stats = generate_all_visualizations(
        config=config,
        chart_type_filter=args.chart_type,
        workers=args.workers,
        skip_existing=not args.no_skip,
    )
    
    # Print summary
    print("\n" + "=" * 50)
    print("Visualization Generation Summary")
    print("=" * 50)
    print(f"Success: {stats['success']}")
    print(f"Failed:  {stats['failed']}")
    print(f"Output:  {os.path.join(config.paths.output_dir, 'visualizations')}")
    ts = stats.get("token_stats", {})
    print(f"Tokens:  prompt={ts.get('prompt_tokens', 0):,} completion={ts.get('completion_tokens', 0):,} total={ts.get('total_tokens', 0):,}")
    print("=" * 50)


if __name__ == "__main__":
    main()
