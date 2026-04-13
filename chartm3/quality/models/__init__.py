"""
Model definitions for chart quality classification.
"""

from .qwen2vl_classifier import (
    LLMForSequenceClassificationConfig,
    LLMForSequenceClassification,
)

__all__ = [
    "LLMForSequenceClassificationConfig",
    "LLMForSequenceClassification",
]
