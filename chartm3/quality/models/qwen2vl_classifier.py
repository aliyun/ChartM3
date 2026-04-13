"""
Qwen2-VL based sequence classification model for chart quality evaluation.

This model adapts Qwen2-VL for binary classification (high/low quality).
Based on the original implementation from ChartM3 project.
"""

from transformers import (
    Qwen2VLForConditionalGeneration,
    AutoConfig,
    PreTrainedModel,
    PretrainedConfig,
)
from transformers.modeling_outputs import SequenceClassifierOutput
from transformers.models.qwen2_vl.modeling_qwen2_vl import Qwen2RMSNorm
import torch
import torch.nn as nn
from typing import Optional, List


class LLMForSequenceClassificationConfig(PretrainedConfig):
    """Configuration for LLM-based sequence classification."""
    
    model_type = "llm_for_sequence_classification"

    def __init__(
        self,
        num_labels: int = 2,
        llm_config: Optional[PretrainedConfig] = None,
        use_mlp: bool = False,
        **kwargs
    ):
        """
        Initialize classification config.
        
        Args:
            num_labels: Number of classification labels (default 2 for binary)
            llm_config: Configuration for the underlying LLM
            use_mlp: Whether to use MLP projection layer
        """
        super().__init__(**kwargs)
        self.llm_config = llm_config
        self.num_labels = num_labels
        self.use_mlp = use_mlp


class LLMForSequenceClassification(PreTrainedModel):
    """
    Qwen2-VL model adapted for sequence classification.
    
    This model removes the language modeling head and adds a classification head
    on top of the last hidden state.
    """
    
    config_class = LLMForSequenceClassificationConfig
    
    def __init__(self, config: LLMForSequenceClassificationConfig):
        """
        Initialize the classification model.
        
        Args:
            config: Model configuration
        """
        super().__init__(config)
        self.num_labels = config.num_labels
        
        # Initialize the base LLM and remove the LM head
        self.llm = Qwen2VLForConditionalGeneration(config.llm_config)
        del self.llm.lm_head
        
        # Add classification head
        if config.use_mlp:
            self.mlp = nn.Sequential(
                nn.Linear(config.llm_config.hidden_size, config.llm_config.hidden_size * 4),
                nn.GELU(),
                nn.Linear(config.llm_config.hidden_size * 4, config.llm_config.hidden_size),
            )
            self.norm = Qwen2RMSNorm(config.llm_config.hidden_size, eps=config.llm_config.rms_norm_eps)
            self.lm_head = nn.Linear(config.llm_config.hidden_size, config.num_labels, bias=False)
        else:
            self.lm_head = nn.Linear(config.llm_config.hidden_size, config.num_labels, bias=False)
        
        self.gradient_checkpointing = False

    def forward(
        self,
        input_ids: torch.LongTensor = None,
        attention_mask: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.LongTensor] = None,
        past_key_values: Optional[List[torch.FloatTensor]] = None,
        inputs_embeds: Optional[torch.FloatTensor] = None,
        labels: Optional[torch.LongTensor] = None,
        use_cache: Optional[bool] = None,
        output_attentions: Optional[bool] = None,
        output_hidden_states: Optional[bool] = None,
        return_dict: Optional[bool] = None,
        pixel_values: Optional[torch.Tensor] = None,
        pixel_values_videos: Optional[torch.FloatTensor] = None,
        image_grid_thw: Optional[torch.LongTensor] = None,
        video_grid_thw: Optional[torch.LongTensor] = None,
        rope_deltas: Optional[torch.LongTensor] = None,
    ) -> SequenceClassifierOutput:
        """
        Forward pass for classification.
        
        Args:
            input_ids: Input token IDs
            attention_mask: Attention mask
            position_ids: Position IDs
            past_key_values: Cached key-value states
            inputs_embeds: Pre-computed input embeddings
            labels: Ground truth labels for loss computation
            use_cache: Whether to use cache
            output_attentions: Whether to output attention weights
            output_hidden_states: Whether to output hidden states
            return_dict: Whether to return a dict
            pixel_values: Image pixel values
            pixel_values_videos: Video pixel values
            image_grid_thw: Image grid dimensions
            video_grid_thw: Video grid dimensions
            rope_deltas: RoPE position deltas
            
        Returns:
            SequenceClassifierOutput with loss, logits, hidden_states, attentions
        """
        output_attentions = output_attentions if output_attentions is not None else self.config.output_attentions
        output_hidden_states = (
            output_hidden_states if output_hidden_states is not None else self.config.output_hidden_states
        )
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        # Compute input embeddings
        if inputs_embeds is None:
            inputs_embeds = self.llm.model.embed_tokens(input_ids)
            
            # Process image inputs
            if pixel_values is not None:
                pixel_values = pixel_values.type(self.llm.visual.get_dtype())
                image_embeds = self.llm.visual(pixel_values, grid_thw=image_grid_thw).to(inputs_embeds.device)
                image_mask = input_ids == self.config.llm_config.image_token_id
                inputs_embeds[image_mask] = image_embeds
            
            # Process video inputs
            if pixel_values_videos is not None:
                pixel_values_videos = pixel_values_videos.type(self.llm.visual.get_dtype())
                video_embeds = self.llm.visual(pixel_values_videos, grid_thw=video_grid_thw).to(inputs_embeds.device)
                video_mask = input_ids == self.config.llm_config.video_token_id
                inputs_embeds[video_mask] = video_embeds
            
            if attention_mask is not None:
                attention_mask = attention_mask.to(inputs_embeds.device)

        # Forward through the transformer
        outputs = self.llm.model(
            input_ids=None,
            position_ids=position_ids,
            attention_mask=attention_mask,
            past_key_values=past_key_values,
            inputs_embeds=inputs_embeds,
            use_cache=use_cache,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )

        # Get last hidden state and compute logits
        hidden_states = outputs[0]
        logits = self.lm_head(hidden_states[:, -1, :])  # Use last token for classification
        logits = logits.float()

        # Compute loss if labels provided
        loss = None
        if labels is not None:
            loss_fct = nn.CrossEntropyLoss()
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))

        if not return_dict:
            output = (logits,)
            return ((loss,) + output) if loss is not None else output

        return SequenceClassifierOutput(
            loss=loss,
            logits=logits,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )
