"""
VLM-based chart quality evaluator using API calls.

This evaluator uses Vision-Language Models (like Qwen2-VL) via API
to assess chart quality through prompt-based evaluation.
"""

import json
import base64
import logging
import re
from pathlib import Path
from typing import Optional, List, Dict, Any

from .base import BaseQualityEvaluator, QualityResult, QualityLevel, parse_quality_from_string
from .prompts import CHART_QUALITY_PROMPT, CHART_QUALITY_PROMPT_WITH_TYPE

logger = logging.getLogger(__name__)


class VLMQualityEvaluator(BaseQualityEvaluator):
    """
    Chart quality evaluator using VLM API calls.
    
    This evaluator sends chart images to a VLM API and parses
    the response to determine quality.
    """
    
    def __init__(
        self,
        base_url: str = "http://127.0.0.1:8005/v1",
        api_key: str = "",
        model: str = "Qwen2.5-VL-72B",
        temperature: float = 0.3,
        max_tokens: int = 1024,
        timeout: int = 60,
        device: str = "cpu",  # Not used for API-based evaluation
    ):
        """
        Initialize the VLM evaluator.
        
        Args:
            base_url: Base URL for the VLM API
            api_key: API key for authentication
            model: Model name to use
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
            timeout: Request timeout in seconds
            device: Not used (for API compatibility)
        """
        super().__init__(device=device)
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        
        self._session = None
    
    def initialize(self) -> None:
        """Initialize the HTTP session."""
        if self._initialized:
            return
        
        import httpx
        self._session = httpx.Client(timeout=self.timeout)
        self._initialized = True
        logger.info(f"VLM evaluator initialized with model: {self.model}")
    
    def _encode_image(self, image_path: str) -> str:
        """Encode image to base64."""
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    
    def _get_image_media_type(self, image_path: str) -> str:
        """Get media type from image path."""
        ext = Path(image_path).suffix.lower()
        media_types = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".webp": "image/webp",
        }
        return media_types.get(ext, "image/png")
    
    def _parse_response(self, response_text: str) -> Dict[str, Any]:
        """
        Parse JSON response from VLM.
        
        Args:
            response_text: Raw response text from VLM
            
        Returns:
            Parsed dictionary with quality, issues
        """
        # Try to extract JSON from response
        try:
            # First try direct JSON parse
            return json.loads(response_text)
        except json.JSONDecodeError:
            pass
        
        # Try to find JSON in the response
        json_match = re.search(r'\{[^{}]*\}', response_text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group())
            except json.JSONDecodeError:
                pass
        
        # Fallback: try to extract quality from text
        response_lower = response_text.lower()
        if "high" in response_lower or "高质量" in response_lower:
            return {"quality": "high", "issues": []}
        elif "low" in response_lower or "低质量" in response_lower:
            return {"quality": "low", "issues": ["Quality issues detected"]}
        
        # Cannot parse
        return {"quality": "unknown", "issues": ["Failed to parse response"]}
    
    def evaluate(self, image_path: str, chart_type: Optional[str] = None) -> QualityResult:
        """
        Evaluate chart quality using VLM API.
        
        Args:
            image_path: Path to the chart image
            chart_type: Optional chart type for context
            
        Returns:
            QualityResult with quality assessment
        """
        if not self._initialized:
            self.initialize()
        
        # Prepare prompt
        if chart_type:
            prompt = CHART_QUALITY_PROMPT_WITH_TYPE.format(chart_type=chart_type)
        else:
            prompt = CHART_QUALITY_PROMPT
        
        # Encode image
        try:
            image_base64 = self._encode_image(image_path)
            media_type = self._get_image_media_type(image_path)
        except Exception as e:
            logger.error(f"Error encoding image {image_path}: {e}")
            return QualityResult(
                quality=QualityLevel.UNKNOWN,
                method="vlm",
                issues=[f"Image encoding error: {str(e)}"]
            )
        
        # Prepare API request
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{media_type};base64,{image_base64}"
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
        
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }
        
        headers = {
            "Content-Type": "application/json",
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        try:
            response = self._session.post(
                f"{self.base_url}/chat/completions",
                json=payload,
                headers=headers,
            )
            response.raise_for_status()
            
            result = response.json()
            response_text = result["choices"][0]["message"]["content"]
            
            # Parse response
            parsed = self._parse_response(response_text)
            
            quality = parse_quality_from_string(parsed.get("quality", "unknown"))
            issues = parsed.get("issues", [])
            
            return QualityResult(
                quality=quality,
                method="vlm",
                issues=issues,
                raw_output=response_text
            )
            
        except Exception as e:
            logger.error(f"API error evaluating {image_path}: {e}")
            return QualityResult(
                quality=QualityLevel.UNKNOWN,
                method="vlm",
                issues=[f"API error: {str(e)}"]
            )
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up HTTP session."""
        if self._session:
            self._session.close()
            self._session = None


def create_evaluator(
    mode: str = "vlm",
    **kwargs
) -> BaseQualityEvaluator:
    """
    Factory function to create a quality evaluator.
    
    Args:
        mode: Evaluation mode - "classifier" or "vlm"
        **kwargs: Additional arguments for the evaluator
        
    Returns:
        Configured quality evaluator
    """
    if mode == "classifier":
        from .classifier import ChartQualityClassifier
        return ChartQualityClassifier(**kwargs)
    elif mode == "vlm":
        return VLMQualityEvaluator(**kwargs)
    else:
        raise ValueError(f"Unknown evaluation mode: {mode}. Use 'classifier' or 'vlm'.")
