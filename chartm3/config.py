"""
Configuration management for ChartM3 pipeline.

Supports loading from YAML files and environment variables.
"""

import os
import yaml
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class LLMConfig:
    """Configuration for LLM API."""
    base_url: str = "http://127.0.0.1:8004/v1/chat/completions"
    api_key: str = ""
    model: str = "Qwen2.5-72B-Instruct"
    temperature: float = 0.7
    max_tokens: int = 4096
    timeout: int = 120


@dataclass
class VLMConfig:
    """Configuration for Vision-Language Model API."""
    base_url: str = "http://127.0.0.1:8005/v1/chat/completions"
    api_key: str = ""
    model: str = "Qwen2.5-VL-72B"
    temperature: float = 0.7
    max_tokens: int = 4096
    max_image_pixels: int = 1024 * 28 * 28
    timeout: int = 180


@dataclass
class PathConfig:
    """Configuration for file paths."""
    project_root: Path = field(default_factory=lambda: Path(__file__).parent.parent)
    database_dir: Path = field(default_factory=lambda: Path(__file__).parent.parent / "data" / "database")
    template_dir: Path = field(default_factory=lambda: Path(__file__).parent.parent / "data" / "database")
    data_dir: Path = field(default_factory=lambda: Path(__file__).parent.parent / "data")
    output_dir: Path = field(default_factory=lambda: Path(__file__).parent.parent / "data" / "output")
    
    # Input files
    seed_field_file: Path = field(default_factory=lambda: Path(__file__).parent.parent / "data" / "seed_field.json")
    chart_type_file: Path = field(default_factory=lambda: Path(__file__).parent.parent / "data" / "chart_type.csv")
    
    # Output directories
    topics_dir: Path = field(default_factory=lambda: Path(__file__).parent.parent / "data" / "output" / "topics")
    raw_data_dir: Path = field(default_factory=lambda: Path(__file__).parent.parent / "data" / "output" / "raw_data")
    visualizations_dir: Path = field(default_factory=lambda: Path(__file__).parent.parent / "data" / "output" / "visualizations")
    qa_pairs_dir: Path = field(default_factory=lambda: Path(__file__).parent.parent / "data" / "output" / "qa_pairs")
    final_dir: Path = field(default_factory=lambda: Path(__file__).parent.parent / "data" / "output" / "final")


@dataclass
class PipelineConfig:
    """Configuration for pipeline execution."""
    num_threads: int = 8
    topics_per_domain: int = 20
    max_samples_per_topic: int = 15
    enable_resume: bool = True  # Enable checkpoint/resume
    log_level: str = "INFO"


class Config:
    """Main configuration class for ChartM3 pipeline."""
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize configuration.
        
        Args:
            config_file: Path to YAML configuration file (optional)
        """
        self.llm = LLMConfig()
        self.vlm = VLMConfig()
        self.paths = PathConfig()
        self.pipeline = PipelineConfig()
        
        # Load from config file if provided
        if config_file and os.path.exists(config_file):
            self._load_from_yaml(config_file)
        
        # Override with environment variables
        self._load_from_env()
        
        # Ensure all directories exist
        self._ensure_directories()
    
    def _load_from_yaml(self, config_file: str) -> None:
        """Load configuration from YAML file."""
        with open(config_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if 'llm' in data:
            for key, value in data['llm'].items():
                if hasattr(self.llm, key):
                    setattr(self.llm, key, value)
        
        if 'vlm' in data:
            for key, value in data['vlm'].items():
                if hasattr(self.vlm, key):
                    setattr(self.vlm, key, value)
        
        if 'paths' in data:
            for key, value in data['paths'].items():
                if hasattr(self.paths, key):
                    setattr(self.paths, key, Path(value))
        
        if 'pipeline' in data:
            for key, value in data['pipeline'].items():
                if hasattr(self.pipeline, key):
                    setattr(self.pipeline, key, value)
    
    def _load_from_env(self) -> None:
        """Load configuration from environment variables."""
        # LLM configuration
        if os.getenv('CHARTM3_LLM_BASE_URL'):
            self.llm.base_url = os.getenv('CHARTM3_LLM_BASE_URL')
        if os.getenv('CHARTM3_LLM_API_KEY'):
            self.llm.api_key = os.getenv('CHARTM3_LLM_API_KEY')
        if os.getenv('CHARTM3_LLM_MODEL'):
            self.llm.model = os.getenv('CHARTM3_LLM_MODEL')
        
        # VLM configuration
        if os.getenv('CHARTM3_VLM_BASE_URL'):
            self.vlm.base_url = os.getenv('CHARTM3_VLM_BASE_URL')
        if os.getenv('CHARTM3_VLM_API_KEY'):
            self.vlm.api_key = os.getenv('CHARTM3_VLM_API_KEY')
        if os.getenv('CHARTM3_VLM_MODEL'):
            self.vlm.model = os.getenv('CHARTM3_VLM_MODEL')
        
        # Pipeline configuration
        if os.getenv('CHARTM3_NUM_THREADS'):
            self.pipeline.num_threads = int(os.getenv('CHARTM3_NUM_THREADS'))
    
    def _ensure_directories(self) -> None:
        """Ensure all output directories exist."""
        for attr_name in ['topics_dir', 'raw_data_dir', 'visualizations_dir', 
                          'qa_pairs_dir', 'final_dir']:
            path = getattr(self.paths, attr_name)
            path.mkdir(parents=True, exist_ok=True)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            'llm': {
                'base_url': self.llm.base_url,
                'model': self.llm.model,
                'temperature': self.llm.temperature,
                'max_tokens': self.llm.max_tokens,
            },
            'vlm': {
                'base_url': self.vlm.base_url,
                'model': self.vlm.model,
                'temperature': self.vlm.temperature,
                'max_tokens': self.vlm.max_tokens,
            },
            'paths': {
                'database_dir': str(self.paths.database_dir),
                'output_dir': str(self.paths.output_dir),
            },
            'pipeline': {
                'num_threads': self.pipeline.num_threads,
                'enable_resume': self.pipeline.enable_resume,
            }
        }
    
    @classmethod
    def from_yaml(cls, config_file: str) -> 'Config':
        """Create Config instance from YAML file."""
        return cls(config_file=config_file)


# Global default configuration instance
_default_config: Optional[Config] = None


def get_config(config_file: Optional[str] = None) -> Config:
    """
    Get or create the global configuration instance.
    
    Args:
        config_file: Path to YAML configuration file (optional)
    
    Returns:
        Config instance
    """
    global _default_config
    if _default_config is None or config_file is not None:
        _default_config = Config(config_file=config_file)
    return _default_config
