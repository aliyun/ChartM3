"""
Code utility functions for ChartM3 pipeline.

Includes functions for extracting, executing, and post-processing Python code.
"""

import ast
import re
import sys
import contextlib
from io import StringIO
from typing import Dict, List, Optional, Any


def extract_functions_from_source(
    source_code: str,
    function_names: List[str]
) -> Dict[str, str]:
    """
    Extract specific functions from Python source code.
    
    Args:
        source_code: Python source code string
        function_names: List of function names to extract
    
    Returns:
        Dictionary mapping function names to their source code
    """
    try:
        tree = ast.parse(source_code)
    except SyntaxError:
        return {name: "" for name in function_names}
    
    extracted_functions = {name: "" for name in function_names}
    source_lines = source_code.splitlines()
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in function_names:
            start_lineno = node.lineno
            # Python 3.8+ has end_lineno
            if hasattr(node, 'end_lineno'):
                end_lineno = node.end_lineno
            else:
                # Fallback for older Python versions
                end_lineno = node.body[-1].lineno if node.body else start_lineno
            
            func_lines = source_lines[start_lineno - 1:end_lineno]
            extracted_functions[node.name] = "\n".join(func_lines)
    
    return extracted_functions


def extract_code_block(text: str, tag: str = "python") -> str:
    """
    Extract code block from markdown-formatted text.
    
    Args:
        text: Text containing code blocks
        tag: Code block tag (default: "python")
    
    Returns:
        Extracted code string, or original text if no code block found
    """
    pattern = rf"```{tag}\s*(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # Try without specific tag
    pattern = r"```\s*(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    return text


@contextlib.contextmanager
def capture_stdout():
    """
    Context manager to capture stdout output.
    
    Yields:
        StringIO object containing captured output
    """
    stdout = StringIO()
    old_stdout = sys.stdout
    sys.stdout = stdout
    try:
        yield stdout
    finally:
        sys.stdout = old_stdout


def execute_code_safely(
    code: str,
    globals_dict: Optional[Dict[str, Any]] = None,
    timeout: int = 60,
    allowed_modules: Optional[List[str]] = None
) -> tuple:
    """
    Execute Python code safely with output capture.
    
    Args:
        code: Python code to execute
        globals_dict: Global variables for execution context
        timeout: Execution timeout in seconds (not enforced, for documentation)
        allowed_modules: List of allowed module names (for documentation)
    
    Returns:
        Tuple of (success: bool, output: str)
    """
    if globals_dict is None:
        globals_dict = {}
    
    # Add common imports to the execution context
    exec_globals = {
        '__builtins__': __builtins__,
        '__name__': '__main__',
    }
    exec_globals.update(globals_dict)
    
    try:
        with capture_stdout() as output:
            # Use single namespace for both globals and locals
            # so that function definitions are visible to subsequent code
            exec(code, exec_globals)
        
        return True, output.getvalue()
    except Exception as e:
        return False, str(e)


def post_process_visualization_code(code: str, contains_chinese: bool = None) -> str:
    """
    Post-process visualization code for proper rendering.
    
    Adds Chinese font support and other fixes.

    Args:
        code: Python visualization code
        contains_chinese: Whether to add Chinese font support. 
                         If None, auto-detect from code.

    Returns:
        Post-processed code
    """
    # Auto-detect Chinese characters if not specified
    if contains_chinese is None:
        contains_chinese = _contains_chinese_in_code(code)
    
    # Remove problematic plot calls
    code = _remove_plot_calls(code)
    
    # Fix deprecated seaborn styles
    code = _fix_seaborn_style(code)
    
    # Remove duplicate if __name__ == "__main__": blocks
    code = _remove_duplicate_main_blocks(code)
    
    # Add Chinese font support if needed
    if contains_chinese:
        code = _add_chinese_font_support(code)
    
    return code


def _remove_duplicate_main_blocks(code: str) -> str:
    """
    Remove duplicate if __name__ == "__main__": blocks.
    
    LLM sometimes outputs original code + fixed code, resulting in
    duplicate main blocks. This function keeps only the LAST one,
    since the last one is typically the corrected version.
    
    Args:
        code: Python code string
        
    Returns:
        Code with only one if __name__ == "__main__": block
    """
    # Find all occurrences of if __name__ == "__main__":
    main_pattern = r'^if __name__ == ["\']__main__["\']:\s*$'
    lines = code.split('\n')
    
    main_block_indices = []
    for i, line in enumerate(lines):
        if re.match(main_pattern, line.strip()):
            main_block_indices.append(i)
    
    # If more than one main block, keep only the LAST one
    if len(main_block_indices) > 1:
        # Keep function definitions (before first main) + last main block
        first_main_start = main_block_indices[0]
        last_main_start = main_block_indices[-1]
        
        # Keep: lines before first main block + last main block to end
        result_lines = lines[:first_main_start] + lines[last_main_start:]
        code = '\n'.join(result_lines)
    
    return code


def _contains_chinese_in_code(code: str) -> bool:
    """
    Check if code contains Chinese characters (excluding comments).
    
    Args:
        code: Python code string
    
    Returns:
        True if Chinese characters are found
    """
    for line in code.split('\n'):
        for char in line:
            if char == '#':
                break  # Skip rest of line (comment)
            if '\u4e00' <= char <= '\u9fff':
                return True
    return False


def _remove_plot_calls(code: str) -> str:
    """Remove problematic plot function calls."""
    # Remove lines like plot_0(), plot_1(), etc.
    pattern = r'^plot_\d.*?$'
    return re.sub(pattern, '', code, flags=re.MULTILINE)


def _fix_seaborn_style(code: str) -> str:
    """Fix deprecated seaborn style names.
    
    Converts old style names like 'seaborn-whitegrid' to 'seaborn-v0_8-whitegrid'.
    Does NOT modify already correct names like 'seaborn-v0_8-whitegrid'.
    """
    # Only match 'seaborn' followed directly by style suffix (not '-v0_8')
    # Matches: seaborn-whitegrid, seaborn-white, seaborn-darkgrid, etc.
    # Does NOT match: seaborn-v0_8-whitegrid (already correct)
    pattern = r"plt\.style\.use\('seaborn(?!-v0_8)([^']*)'\)"
    replacement = r"plt.style.use('seaborn-v0_8\1')"
    return re.sub(pattern, replacement, code)


def _add_chinese_font_support(code: str) -> str:
    """Add Chinese font configuration to matplotlib code."""
    
    # Try to insert after style settings with proper indentation
    style_pattern = r"(^([ \t]*)(?:sns\.set_style|plt\.style\.use)\([^)]*\)\s*(#.*)?(\n))"
    
    def insert_after_style(match):
        indent = match.group(2)  # Capture the indentation of the style line
        font_config = f"{indent}plt.rcParams['font.sans-serif'] = ['SimHei']\n{indent}plt.rcParams['axes.unicode_minus'] = False\n"
        return match.group(0) + font_config
    
    modified = re.sub(style_pattern, insert_after_style, code, flags=re.MULTILINE)
    
    # If no style setting found, insert before plt.savefig
    if modified == code:
        savefig_pattern = r"(^[ \t]*)(plt\.savefig[^\n]*)"
        
        def insert_before_savefig(match):
            indent = match.group(1)
            return f"{indent}plt.rcParams['font.sans-serif'] = ['SimHei']\n{indent}plt.rcParams['axes.unicode_minus'] = False\n{indent}{match.group(2)}"
        
        modified = re.sub(savefig_pattern, insert_before_savefig, code, flags=re.MULTILINE)
    
    return modified


def normalize_csv_path_in_code(code: str, target_filename: str = "data.csv") -> str:
    """
    Replace all CSV file paths in code with a target filename.
    
    Args:
        code: Python code string
        target_filename: Target filename to use (default: "data.csv")
    
    Returns:
        Modified code with normalized CSV paths
    """
    pattern = r"'[^']*\.csv'"
    return re.sub(pattern, f"'{target_filename}'", code)


def create_visualization_script(
    llm_functions: str,
    data_path: str,
    output_csv_name: str
) -> str:
    """
    Create a complete visualization script from LLM-generated functions.
    
    Args:
        llm_functions: LLM-generated preprocess and plot functions
        data_path: Path to input CSV data
        output_csv_name: Name for output CSV file
    
    Returns:
        Complete Python script as string
    """
    template = '''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

{llm_gen_functions}

if __name__ == "__main__":
    test_data = pd.read_csv("{data_path}", skipinitialspace=True)
    try:
        data = preprocess(test_data)
        data.to_csv("./{output_csv_name}.csv")
    except:
        try:
            with open("./{output_csv_name}.txt", "a", encoding="utf-8") as f:
                f.write(str(data) + "\\n")
        except:
            print("Failed to save data for {output_csv_name}!")
            pass
    test_data = pd.read_csv("{data_path}", skipinitialspace=True)
    plot(test_data)
'''
    return template.format(
        llm_gen_functions=llm_functions,
        data_path=data_path,
        output_csv_name=output_csv_name
    )
