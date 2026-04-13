"""
File utility functions for ChartM3 pipeline.
"""

import os
import re
from pathlib import Path
from typing import List, Optional, Callable, Any


def find_files_by_pattern(
    directory: str,
    pattern: str = "*.json",
    recursive: bool = True
) -> List[str]:
    """
    Find files matching a pattern in a directory.
    
    Args:
        directory: Directory to search in
        pattern: Glob pattern to match (default: "*.json")
        recursive: Whether to search recursively (default: True)
    
    Returns:
        List of matching file paths
    """
    directory = Path(directory)
    if recursive:
        return [str(p) for p in directory.rglob(pattern)]
    return [str(p) for p in directory.glob(pattern)]


def find_files_by_keyword(
    directory: str,
    keyword: str,
    extension: str = ".json"
) -> List[str]:
    """
    Find files containing a keyword in their name.
    
    Args:
        directory: Directory to search in
        keyword: Keyword to search for in filename
        extension: File extension to filter (default: ".json")
    
    Returns:
        List of matching file paths
    """
    matched_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension) and keyword in file:
                full_path = os.path.join(root, file)
                matched_files.append(full_path)
    return matched_files


def ensure_dir(path: str) -> Path:
    """
    Ensure a directory exists, creating it if necessary.
    
    Args:
        path: Directory path
    
    Returns:
        Path object for the directory
    """
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def split_list_for_threading(lst: List[Any], num_parts: int) -> List[List[Any]]:
    """
    Split a list into approximately equal parts for multi-threaded processing.
    
    Args:
        lst: List to split
        num_parts: Number of parts to split into
    
    Returns:
        List of sublists
    """
    if num_parts <= 0:
        return [lst]
    
    k, m = divmod(len(lst), num_parts)
    return [
        lst[i * k + min(i, m):(i + 1) * k + min(i + 1, m)]
        for i in range(num_parts)
    ]


def get_chart_type_from_name(name: str) -> str:
    """
    Extract chart type from a file name.
    
    Chart names are typically formatted as: {chart_type}_{field}_{index}
    
    Args:
        name: File name or path
    
    Returns:
        Chart type string
    """
    # Get just the filename without extension
    basename = Path(name).stem
    # Split by underscore and take first part
    return basename.split('_')[0]


def get_name_without_task_id(filename: str) -> str:
    """
    Remove the task ID suffix from a filename.
    
    Example: "基础条形图_Education_0_3.json" -> "基础条形图_Education_0"
    
    Args:
        filename: Filename to process
    
    Returns:
        Name without task ID
    """
    name_without_ext = Path(filename).stem
    parts = name_without_ext.rsplit('_', 1)
    if len(parts) > 1 and parts[1].isdigit():
        return parts[0]
    return name_without_ext


def is_long_data(file_path: str, line_threshold: int = 100, char_threshold: int = 5000) -> bool:
    """
    Check if a data file is considered "long" based on line count or character count.
    
    Args:
        file_path: Path to the data file
        line_threshold: Maximum lines before considered long (default: 100)
        char_threshold: Maximum characters before considered long (default: 5000)
    
    Returns:
        True if the file is considered long
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            line_count = len(content.splitlines())
            return line_count > line_threshold or len(content) > char_threshold
    except Exception:
        return False


def copy_file(src: str, dst: str) -> None:
    """
    Copy a file from source to destination.
    
    Args:
        src: Source file path
        dst: Destination file path
    """
    import shutil
    # Ensure destination directory exists
    ensure_dir(str(Path(dst).parent))
    shutil.copy2(src, dst)


def list_subdirectories(directory: str) -> List[str]:
    """
    List all subdirectories in a directory.
    
    Args:
        directory: Directory to list
    
    Returns:
        List of subdirectory paths
    """
    directory = Path(directory)
    return [str(p) for p in directory.iterdir() if p.is_dir()]


def check_required_files(directory: str, required_extensions: List[str]) -> bool:
    """
    Check if a directory contains files with all required extensions.
    
    Args:
        directory: Directory to check
        required_extensions: List of required extensions (e.g., ['.csv', '.py', '.png'])
    
    Returns:
        True if all required extensions are present
    """
    directory = Path(directory)
    if not directory.is_dir():
        return False
    
    extensions = {p.suffix.lower() for p in directory.iterdir() if p.is_file()}
    return set(required_extensions).issubset(extensions)
