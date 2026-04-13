"""
Chart Quality Evaluation Module for ChartM3.

This module provides tools for evaluating the visual quality of generated charts.
It supports two evaluation modes:
1. Classifier mode: Uses a fine-tuned Qwen2-VL-2B model for fast binary classification
2. VLM mode: Uses VLM API for detailed quality assessment

Usage:
    from chartm3.quality import create_evaluator, QualityResult, QualityLevel
    
    # Using VLM evaluator
    evaluator = create_evaluator(mode="vlm", base_url="http://...", model="Qwen2.5-VL-72B")
    
    # Using classifier evaluator
    evaluator = create_evaluator(mode="classifier", model_path="/path/to/classifier")
    
    with evaluator:
        result = evaluator.evaluate("chart.png", chart_type="条形图")
        if result.is_high_quality():
            print("Chart passes quality check")
"""

from .base import (
    QualityLevel,
    QualityResult,
    BaseQualityEvaluator,
    parse_quality_from_string,
)

from .vlm_evaluator import (
    VLMQualityEvaluator,
    create_evaluator,
)

from .prompts import (
    CHART_QUALITY_PROMPT,
    CHART_QUALITY_PROMPT_WITH_TYPE,
    CLASSIFIER_PROMPT,
    CLASSIFIER_PROMPT_WITH_TYPE,
)

__all__ = [
    # Base classes and types
    "QualityLevel",
    "QualityResult",
    "BaseQualityEvaluator",
    "parse_quality_from_string",
    # Evaluators
    "VLMQualityEvaluator",
    "create_evaluator",
    # Prompts
    "CHART_QUALITY_PROMPT",
    "CHART_QUALITY_PROMPT_WITH_TYPE",
    "CLASSIFIER_PROMPT",
    "CLASSIFIER_PROMPT_WITH_TYPE",
]

# Lazy import for classifier (requires additional dependencies)
def get_classifier():
    """Get the classifier evaluator class (lazy import)."""
    from .classifier import ChartQualityClassifier
    return ChartQualityClassifier
