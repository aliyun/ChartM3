"""
Base classes and data structures for chart quality evaluation.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from pathlib import Path
from enum import Enum


class QualityLevel(Enum):
    """Quality level enumeration."""
    HIGH = "high"
    LOW = "low"
    UNKNOWN = "unknown"


@dataclass
class QualityResult:
    """Result of chart quality evaluation."""
    quality: QualityLevel
    method: str  # "classifier" or "vlm"
    issues: List[str] = field(default_factory=list)
    raw_output: Optional[Any] = None
    
    def is_high_quality(self) -> bool:
        """Check if the chart is high quality."""
        return self.quality == QualityLevel.HIGH
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "quality": self.quality.value,
            "method": self.method,
            "issues": self.issues,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QualityResult':
        """Create from dictionary."""
        return cls(
            quality=QualityLevel(data["quality"]),
            method=data["method"],
            issues=data.get("issues", []),
        )


class BaseQualityEvaluator(ABC):
    """Abstract base class for chart quality evaluators."""
    
    def __init__(self, device: str = "cuda"):
        """
        Initialize the evaluator.
        
        Args:
            device: Device to run evaluation on ("cuda", "cpu", etc.)
        """
        self.device = device
        self._initialized = False
    
    @abstractmethod
    def initialize(self) -> None:
        """
        Initialize the evaluator (load models, etc.).
        Should be called before evaluate().
        """
        pass
    
    @abstractmethod
    def evaluate(self, image_path: str, chart_type: Optional[str] = None) -> QualityResult:
        """
        Evaluate the quality of a chart image.
        
        Args:
            image_path: Path to the chart image
            chart_type: Optional chart type for context
            
        Returns:
            QualityResult with quality assessment
        """
        pass
    
    def evaluate_batch(self, image_paths: List[str], chart_types: Optional[List[str]] = None) -> List[QualityResult]:
        """
        Evaluate multiple chart images.
        
        Args:
            image_paths: List of paths to chart images
            chart_types: Optional list of chart types
            
        Returns:
            List of QualityResult objects
        """
        if chart_types is None:
            chart_types = [None] * len(image_paths)
        
        results = []
        for img_path, chart_type in zip(image_paths, chart_types):
            try:
                result = self.evaluate(img_path, chart_type)
            except Exception as e:
                # Return unknown quality on error
                result = QualityResult(
                    quality=QualityLevel.UNKNOWN,
                    method=self.__class__.__name__,
                    issues=[f"Evaluation error: {str(e)}"]
                )
            results.append(result)
        
        return results
    
    @property
    def is_initialized(self) -> bool:
        """Check if the evaluator has been initialized."""
        return self._initialized
    
    def __enter__(self):
        """Context manager entry."""
        if not self._initialized:
            self.initialize()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        pass


def parse_quality_from_string(quality_str: str) -> QualityLevel:
    """
    Parse quality level from string.
    
    Args:
        quality_str: String like "high", "low", "0", "1"
        
    Returns:
        QualityLevel enum value
    """
    quality_str = quality_str.lower().strip()
    
    if quality_str in ("high", "1", "good", "pass"):
        return QualityLevel.HIGH
    elif quality_str in ("low", "0", "bad", "fail"):
        return QualityLevel.LOW
    else:
        return QualityLevel.UNKNOWN
