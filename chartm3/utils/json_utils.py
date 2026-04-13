"""
JSON utility functions for ChartM3 pipeline.
"""

import json
import re
import ast
from typing import Any, Optional, List, Dict, Union


def extract_json_from_text(text: str, tag: str = "json") -> str:
    """
    Extract JSON content from markdown-formatted text.
    
    Args:
        text: Text containing JSON block
        tag: Code block tag (default: "json")
    
    Returns:
        Extracted JSON string
    """
    # Try to find ```json ... ``` block
    pattern = rf"```{tag}\s*(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # Try generic code block
    pattern = r"```\s*(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    return text


def extract_json_array(text: str) -> Optional[List[Any]]:
    """
    Extract a JSON array from text.
    
    Args:
        text: Text containing a JSON array
    
    Returns:
        Parsed list, or None if parsing fails
    """
    try:
        # Find the array boundaries
        start = text.find('[')
        end = text.rfind(']') + 1
        
        if start == -1 or end == 0:
            return None
        
        json_str = text[start:end]
        
        # Try ast.literal_eval first (safer)
        try:
            return ast.literal_eval(json_str)
        except (ValueError, SyntaxError):
            pass
        
        # Fall back to json.loads
        return json.loads(json_str)
    except Exception:
        return None


def safe_json_loads(text: str) -> Optional[Any]:
    """
    Safely parse JSON text with multiple fallback strategies.
    
    Args:
        text: JSON string to parse
    
    Returns:
        Parsed object, or None if all parsing attempts fail
    """
    # First extract from markdown if needed
    extracted = extract_json_from_text(text)
    
    # Try direct JSON parsing
    try:
        return json.loads(extracted)
    except json.JSONDecodeError:
        pass
    
    # Try ast.literal_eval
    try:
        return ast.literal_eval(extracted)
    except (ValueError, SyntaxError):
        pass
    
    # Try fixing common issues
    fixed = _fix_json_quotes(extracted)
    try:
        return json.loads(fixed)
    except json.JSONDecodeError:
        pass
    
    return None


def _fix_json_quotes(text: str) -> str:
    """
    Fix common JSON quote issues (single quotes to double quotes).
    
    Args:
        text: JSON-like string
    
    Returns:
        Fixed JSON string
    """
    try:
        # Replace key-value pairs with single quotes
        pattern = r"'([^']*)':\s*'([^']*)'"
        text = re.sub(pattern, r'"\1": "\2"', text)
        
        # Replace standalone keys with single quotes
        pattern = r"'([^']*)':\s*"
        text = re.sub(pattern, r'"\1": ', text)
        
        # Replace standalone values with single quotes
        pattern = r':\s*\'([^\']*)\'([,}\n])'
        text = re.sub(pattern, r': "\1"\2', text)
        
        # Replace array elements with single quotes
        pattern = r'\[\'([^\']*)\'\]'
        text = re.sub(pattern, r'["\1"]', text)
        
        # Replace remaining single quotes
        pattern = r"'([^']*)'"
        text = re.sub(pattern, r'"\1"', text)
        
        return text
    except Exception:
        return text


def csv_to_markdown(csv_data: List[Dict[str, Any]]) -> str:
    """
    Convert CSV-like data (list of dicts) to markdown table.
    
    Args:
        csv_data: List of dictionaries representing rows
    
    Returns:
        Markdown table string
    """
    if not csv_data:
        return ""
    
    headers = list(csv_data[0].keys())
    
    # Build header row
    markdown = "| " + " | ".join(headers) + " |\n"
    markdown += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    
    # Build data rows
    for row in csv_data:
        markdown += "| " + " | ".join(str(row.get(h, "")) for h in headers) + " |\n"
    
    return markdown


def save_json(data: Any, filepath: str, indent: int = 4) -> None:
    """
    Save data to a JSON file.
    
    Args:
        data: Data to save
        filepath: Output file path
        indent: Indentation level (default: 4)
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def load_json(filepath: str) -> Any:
    """
    Load data from a JSON file.
    
    Args:
        filepath: Input file path
    
    Returns:
        Loaded data
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_jsonl(data: List[Any], filepath: str) -> None:
    """
    Save data to a JSONL file (one JSON object per line).
    
    Args:
        data: List of data items
        filepath: Output file path
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        for item in data:
            json_str = json.dumps(item, ensure_ascii=False)
            f.write(json_str + '\n')


def load_jsonl(filepath: str) -> List[Any]:
    """
    Load data from a JSONL file.
    
    Args:
        filepath: Input file path
    
    Returns:
        List of loaded data items
    """
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


def merge_json_data(base: Dict, update: Dict) -> Dict:
    """
    Merge two dictionaries, with update values taking precedence.
    
    Args:
        base: Base dictionary
        update: Dictionary with updates
    
    Returns:
        Merged dictionary
    """
    result = base.copy()
    result.update(update)
    return result


def select_random_task(task_table: str) -> str:
    """
    Select a random task from a tab-separated task definition table.
    
    Args:
        task_table: Tab-separated task definition string
    
    Returns:
        JSON string with randomly selected task
    """
    import random
    
    lines = task_table.strip().split('\n')
    headers = lines[0].split('\t')
    data_lines = lines[1:]
    
    if not data_lines:
        return "[]"
    
    sample_line = random.choice(data_lines)
    values = sample_line.split('\t')
    row_dict = dict(zip(headers, values))
    
    return json.dumps([row_dict], ensure_ascii=False, indent=2)
