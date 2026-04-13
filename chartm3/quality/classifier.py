"""
Classifier-based chart quality evaluator using Qwen2-VL-2B.

This evaluator uses a fine-tuned Qwen2-VL model for binary classification
of chart quality (high/low).
"""

import os
import torch
import logging
from pathlib import Path
from typing import Optional, List, Dict, Any
from dataclasses import dataclass

from .base import BaseQualityEvaluator, QualityResult, QualityLevel
from .prompts import CLASSIFIER_PROMPT, CLASSIFIER_PROMPT_WITH_TYPE

logger = logging.getLogger(__name__)


@dataclass
class ClassifierConfig:
    """Configuration for the classifier evaluator."""
    model_path: str  # Path to the fine-tuned classifier model
    base_model_path: str = "Qwen/Qwen2-VL-2B-Instruct"  # Base Qwen2-VL model
    num_labels: int = 2  # Binary classification: 0=low, 1=high
    use_mlp: bool = True  # Whether the model uses MLP projection
    batch_size: int = 8
    use_flash_attention: bool = True
    max_length: int = 32768


class ChartQualityClassifier(BaseQualityEvaluator):
    """
    Chart quality evaluator using fine-tuned Qwen2-VL classifier.
    
    This evaluator loads a pre-trained classification model that directly
    outputs quality predictions without requiring text generation.
    """
    
    # Label mapping: model output -> quality level
    # 0 = low quality (has problems), 1 = high quality (no problems)
    LABEL_TO_QUALITY = {
        0: QualityLevel.LOW,
        1: QualityLevel.HIGH,
    }
    
    def __init__(
        self,
        model_path: str,
        base_model_path: str = "Qwen/Qwen2-VL-2B-Instruct",
        device: str = "cuda",
        use_mlp: bool = True,
        batch_size: int = 8,
        use_flash_attention: bool = True,
    ):
        """
        Initialize the classifier evaluator.
        
        Args:
            model_path: Path to the fine-tuned classifier weights
            base_model_path: Path to base Qwen2-VL model
            device: Device to run inference on
            use_mlp: Whether the model uses MLP projection layer
            batch_size: Batch size for inference
            use_flash_attention: Whether to use flash attention
        """
        super().__init__(device=device)
        self.model_path = model_path
        self.base_model_path = base_model_path
        self.use_mlp = use_mlp
        self.batch_size = batch_size
        self.use_flash_attention = use_flash_attention
        
        self.model = None
        self.tokenizer = None
        self.processor = None
    
    def initialize(self) -> None:
        """Load the classifier model and processor."""
        if self._initialized:
            return
        
        logger.info(f"Loading classifier model from {self.model_path}")
        
        try:
            from transformers import AutoConfig, AutoProcessor, AutoTokenizer
            from safetensors.torch import load_file
            from .models import LLMForSequenceClassificationConfig, LLMForSequenceClassification
            
            # Load base LLM config
            llm_config = AutoConfig.from_pretrained(
                self.base_model_path,
                trust_remote_code=False
            )
            llm_config.use_cache = False
            
            if self.use_flash_attention:
                llm_config._attn_implementation = 'flash_attention_2'
                llm_config.vision_config._attn_implementation = 'flash_attention_2'
            
            # Create classification config and model
            config = LLMForSequenceClassificationConfig(
                num_labels=2,
                llm_config=llm_config,
                use_mlp=self.use_mlp
            )
            
            self.model = LLMForSequenceClassification(config).bfloat16().to(self.device)
            
            # Load fine-tuned weights
            weights_path = os.path.join(self.model_path, 'model.safetensors')
            if os.path.exists(weights_path):
                state_dict = load_file(weights_path)
                msg = self.model.load_state_dict(state_dict, strict=False)
                logger.info(f"Loaded weights: {msg}")
            else:
                raise FileNotFoundError(f"Model weights not found: {weights_path}")
            
            # Set causal attention based on model type
            for layer_idx in range(config.llm_config.num_hidden_layers):
                self.model.llm.model.layers[layer_idx].self_attn.is_causal = 'bid' not in self.model_path
            
            # Load tokenizer and processor
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
            self.processor = AutoProcessor.from_pretrained(self.model_path)
            
            self.model.eval()
            self._initialized = True
            logger.info("Classifier model loaded successfully")
            
        except ImportError as e:
            raise ImportError(
                f"Required packages not installed: {e}. "
                "Please install: pip install transformers safetensors qwen-vl-utils"
            )
    
    def evaluate(self, image_path: str, chart_type: Optional[str] = None) -> QualityResult:
        """
        Evaluate chart quality using the classifier.
        
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
            prompt = CLASSIFIER_PROMPT_WITH_TYPE.format(chart_type=chart_type)
        else:
            prompt = CLASSIFIER_PROMPT
        
        # Process image and text
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image_path},
                    {"type": "text", "text": prompt}
                ]
            }
        ]
        
        try:
            # Apply chat template
            text = self.processor.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
            
            # Process inputs
            from qwen_vl_utils import process_vision_info
            image_inputs, video_inputs = process_vision_info(messages)
            
            inputs = self.processor(
                text=[text],
                images=image_inputs,
                videos=video_inputs,
                padding=True,
                return_tensors="pt",
            )
            
            # Move to device
            inputs = {k: v.to(self.device) if v is not None else v for k, v in inputs.items()}
            
            # Inference
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits = outputs.logits
                pred = torch.argmax(logits, dim=-1).item()
            
            # Map prediction to quality level
            quality = self.LABEL_TO_QUALITY.get(pred, QualityLevel.UNKNOWN)
            
            return QualityResult(
                quality=quality,
                method="classifier",
                issues=[] if quality == QualityLevel.HIGH else ["Quality issues detected by classifier"],
                raw_output={"prediction": pred, "logits": logits.cpu().tolist()}
            )
            
        except Exception as e:
            logger.error(f"Error evaluating {image_path}: {e}")
            return QualityResult(
                quality=QualityLevel.UNKNOWN,
                method="classifier",
                issues=[f"Evaluation error: {str(e)}"]
            )
    
    def evaluate_batch(
        self,
        image_paths: List[str],
        chart_types: Optional[List[str]] = None
    ) -> List[QualityResult]:
        """
        Evaluate multiple images in batches for efficiency.
        
        Args:
            image_paths: List of image paths
            chart_types: Optional list of chart types
            
        Returns:
            List of QualityResult objects
        """
        if not self._initialized:
            self.initialize()
        
        if chart_types is None:
            chart_types = [None] * len(image_paths)
        
        results = []
        
        # Process in batches
        for i in range(0, len(image_paths), self.batch_size):
            batch_paths = image_paths[i:i + self.batch_size]
            batch_types = chart_types[i:i + self.batch_size]
            
            batch_results = self._evaluate_batch_internal(batch_paths, batch_types)
            results.extend(batch_results)
        
        return results
    
    def _evaluate_batch_internal(
        self,
        image_paths: List[str],
        chart_types: List[Optional[str]]
    ) -> List[QualityResult]:
        """Internal batch evaluation."""
        from qwen_vl_utils import process_vision_info
        
        results = []
        batch_messages = []
        valid_indices = []
        
        # Prepare all messages
        for idx, (img_path, chart_type) in enumerate(zip(image_paths, chart_types)):
            try:
                if chart_type:
                    prompt = CLASSIFIER_PROMPT_WITH_TYPE.format(chart_type=chart_type)
                else:
                    prompt = CLASSIFIER_PROMPT
                
                messages = [
                    {
                        "role": "user",
                        "content": [
                            {"type": "image", "image": img_path},
                            {"type": "text", "text": prompt}
                        ]
                    }
                ]
                batch_messages.append(messages)
                valid_indices.append(idx)
            except Exception as e:
                logger.warning(f"Error preparing {img_path}: {e}")
        
        if not batch_messages:
            return [QualityResult(
                quality=QualityLevel.UNKNOWN,
                method="classifier",
                issues=["Failed to prepare image"]
            )] * len(image_paths)
        
        try:
            # Process all messages
            texts = [
                self.processor.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
                for msgs in batch_messages
            ]
            
            all_images = []
            for msgs in batch_messages:
                images, _ = process_vision_info(msgs)
                all_images.extend(images if images else [])
            
            inputs = self.processor(
                text=texts,
                images=all_images if all_images else None,
                padding=True,
                return_tensors="pt",
            )
            
            inputs = {k: v.to(self.device) if v is not None else v for k, v in inputs.items()}
            
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits = outputs.logits
                preds = torch.argmax(logits, dim=-1)
            
            # Create result for each valid image
            batch_results = {}
            for i, idx in enumerate(valid_indices):
                pred = preds[i].item()
                quality = self.LABEL_TO_QUALITY.get(pred, QualityLevel.UNKNOWN)
                
                batch_results[idx] = QualityResult(
                    quality=quality,
                    method="classifier",
                    issues=[] if quality == QualityLevel.HIGH else ["Quality issues detected"]
                )
            
            # Fill in results in order
            for idx in range(len(image_paths)):
                if idx in batch_results:
                    results.append(batch_results[idx])
                else:
                    results.append(QualityResult(
                        quality=QualityLevel.UNKNOWN,
                        method="classifier",
                        issues=["Processing failed"]
                    ))
            
            return results
            
        except Exception as e:
            logger.error(f"Batch evaluation error: {e}")
            return [QualityResult(
                quality=QualityLevel.UNKNOWN,
                method="classifier",
                issues=[f"Batch error: {str(e)}"]
            )] * len(image_paths)
