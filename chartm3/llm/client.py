"""
LLM and VLM API clients for ChartM3 pipeline.

Provides unified interfaces for calling LLM and Vision-Language Model APIs.
Uses OpenAI official client library.
"""

import io
import json
import time
import base64
import logging
from PIL import Image
from typing import Optional, List, Dict, Any, Union
from dataclasses import dataclass

try:
    from openai import OpenAI
except ImportError:
    raise ImportError(
        "OpenAI package is required. Install with: pip install openai"
    )


logger = logging.getLogger(__name__)


@dataclass
class LLMResponse:
    """Response from LLM API."""
    content: str
    raw_response: Dict[str, Any]
    success: bool = True
    error: Optional[str] = None


class LLMClient:
    """
    Client for calling LLM APIs (OpenAI-compatible format).
    """
    
    def __init__(
        self,
        base_url: str = "http://127.0.0.1:8004/v1",
        api_key: str = "",
        model: str = "Qwen2.5-72B-Instruct",
        temperature: float = 0.7,
        max_tokens: int = 4096,
        timeout: int = 120
    ):
        """
        Initialize LLM client.
        
        Args:
            base_url: API base URL (e.g., "https://dashscope.aliyuncs.com/compatible-mode/v1")
            api_key: API key for authentication
            model: Model name to use
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
            timeout: Request timeout in seconds
        """
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        
        # Token usage statistics
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        
        # Initialize OpenAI client
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout
        )
    
    def get_token_stats(self) -> dict:
        """Get accumulated token usage statistics."""
        return {
            "prompt_tokens": self.total_prompt_tokens,
            "completion_tokens": self.total_completion_tokens,
            "total_tokens": self.total_prompt_tokens + self.total_completion_tokens,
        }
    
    def chat(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        enable_thinking: bool = False
    ) -> str:
        """
        Send a chat completion request.
        
        Args:
            prompt: User message/prompt
            system_prompt: Optional system message
            temperature: Override default temperature
            max_tokens: Override default max_tokens
            enable_thinking: Enable model native thinking mode
        
        Returns:
            Response content string (empty string on failure)
        """
        messages = []
        
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })
        
        messages.append({
            "role": "user",
            "content": prompt
        })
        
        resp = self._call_api(
            messages,
            temperature=temperature,
            max_tokens=max_tokens,
            enable_thinking=enable_thinking
        )
        if not resp.success:
            logger.error(f"LLM call failed: {resp.error}")
        return resp.content
    
    def chat_with_history(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        enable_thinking: bool = False
    ) -> str:
        """
        Send a chat completion request with message history.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            temperature: Override default temperature
            max_tokens: Override default max_tokens
            enable_thinking: Enable model native thinking mode
        
        Returns:
            Response content string (empty string on failure)
        """
        resp = self._call_api(
            messages,
            temperature=temperature,
            max_tokens=max_tokens,
            enable_thinking=enable_thinking
        )
        if not resp.success:
            logger.error(f"LLM call failed: {resp.error}")
        return resp.content
    
    def _call_api(
        self,
        messages: List[Dict],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        enable_thinking: bool = False
    ) -> LLMResponse:
        """Internal method to call the API using OpenAI client."""
        start_time = time.time()
        
        try:
            # Use OpenAI client to create chat completion
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature or self.temperature,
                max_tokens=max_tokens or self.max_tokens,
                extra_body={"enable_thinking": enable_thinking}
            )
            
            elapsed = time.time() - start_time
            logger.debug(f"LLM response received in {elapsed:.2f}s")
            
            # Accumulate token usage
            if completion.usage:
                self.total_prompt_tokens += completion.usage.prompt_tokens or 0
                self.total_completion_tokens += completion.usage.completion_tokens or 0
            
            # Convert completion to dict for raw_response
            data = completion.model_dump()
            
            if completion.choices and len(completion.choices) > 0:
                content = completion.choices[0].message.content or ""
                return LLMResponse(
                    content=content,
                    raw_response=data,
                    success=True
                )
            else:
                return LLMResponse(
                    content="",
                    raw_response=data,
                    success=False,
                    error="No choices in response"
                )
        
        except Exception as e:
            return LLMResponse(
                content="",
                raw_response={},
                success=False,
                error=str(e)
            )


class VLMClient:
    """
    Client for calling Vision-Language Model APIs.
    """
    
    def __init__(
        self,
        base_url: str = "http://127.0.0.1:8005/v1/chat/completions",
        api_key: str = "",
        model: str = "Qwen2.5-VL-72B",
        temperature: float = 0.7,
        max_tokens: int = 4096,
        max_image_pixels: int = 1024 * 28 * 28,
        timeout: int = 180
    ):
        """
        Initialize VLM client.
        
        Args:
            base_url: API base URL
            api_key: API key for authentication
            model: Model name to use
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
            max_image_pixels: Maximum image pixels after resize
            timeout: Request timeout in seconds
        """
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.max_image_pixels = max_image_pixels
        self.timeout = timeout
        
        # Token usage statistics
        self.total_prompt_tokens = 0
        self.total_completion_tokens = 0
        
        # Initialize OpenAI client
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout
        )
    
    def get_token_stats(self) -> dict:
        """Get accumulated token usage statistics."""
        return {
            "prompt_tokens": self.total_prompt_tokens,
            "completion_tokens": self.total_completion_tokens,
            "total_tokens": self.total_prompt_tokens + self.total_completion_tokens,
        }
    
    def chat(
        self,
        prompt: str = None,
        image_paths: Union[str, List[str]] = None,
        messages: List[Dict] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        enable_thinking: bool = False
    ) -> str:
        """
        Unified chat interface for VLM.
        
        Supports:
          - prompt + image_paths: single-turn with images
          - messages + image_paths: multi-turn with images
        
        Args:
            prompt: Text prompt (for single-turn)
            image_paths: Path(s) to image file(s)
            messages: Message history (for multi-turn)
            temperature: Override default temperature
            max_tokens: Override default max_tokens
            enable_thinking: Enable model native thinking mode
        
        Returns:
            Response content string (empty string on failure)
        """
        if messages is not None:
            return self.chat_with_history_and_images(
                messages=messages,
                image_paths=image_paths or [],
                temperature=temperature,
                max_tokens=max_tokens,
                enable_thinking=enable_thinking
            )
        else:
            return self.chat_with_image(
                prompt=prompt,
                image_paths=image_paths or [],
                temperature=temperature,
                max_tokens=max_tokens,
                enable_thinking=enable_thinking
            )
    
    def chat_with_image(
        self,
        prompt: str,
        image_paths: Union[str, List[str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        enable_thinking: bool = False
    ) -> str:
        """
        Send a chat request with images.
        
        Args:
            prompt: Text prompt
            image_paths: Path(s) to image file(s)
            temperature: Override default temperature
            max_tokens: Override default max_tokens
        
        Returns:
            Response content string (empty string on failure)
        """
        if isinstance(image_paths, str):
            image_paths = [image_paths]
        
        content = []
        
        # Add images first
        for img_path in image_paths:
            b64_image = self._encode_image(img_path)
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{b64_image}"
                }
            })
        
        # Add text prompt
        content.append({
            "type": "text",
            "text": prompt
        })
        
        messages = [{
            "role": "user",
            "content": content
        }]
        
        resp = self._call_api(
            messages,
            temperature=temperature,
            max_tokens=max_tokens,
            enable_thinking=enable_thinking
        )
        if not resp.success:
            logger.error(f"VLM call failed: {resp.error}")
        return resp.content
    
    def chat_with_history_and_images(
        self,
        messages: List[Dict],
        image_paths: Union[str, List[str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        enable_thinking: bool = False
    ) -> str:
        """
        Send a multi-turn chat request with images.
        
        The images are added to the first user message.
        
        Args:
            messages: List of message dicts
            image_paths: Path(s) to image file(s)
            temperature: Override default temperature
            max_tokens: Override default max_tokens
        
        Returns:
            Response content string (empty string on failure)
        """
        if isinstance(image_paths, str):
            image_paths = [image_paths]
        
        # Make a copy to avoid modifying original
        messages = [m.copy() for m in messages]
        
        # Find first user message and add images
        for msg in messages:
            if msg.get("role") == "user":
                # Convert content to list format if needed
                if isinstance(msg.get("content"), str):
                    msg["content"] = [{"type": "text", "text": msg["content"]}]
                elif not isinstance(msg.get("content"), list):
                    msg["content"] = []
                
                # Add images at the beginning
                for img_path in image_paths:
                    b64_image = self._encode_image(img_path)
                    msg["content"].insert(0, {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{b64_image}"
                        }
                    })
                break
        
        resp = self._call_api(
            messages,
            temperature=temperature,
            max_tokens=max_tokens,
            enable_thinking=enable_thinking
        )
        if not resp.success:
            logger.error(f"VLM call failed: {resp.error}")
        return resp.content
    
    def _encode_image(self, image_path: str) -> str:
        """Encode image to base64 with resizing."""
        img = Image.open(image_path).convert('RGB')
        
        # Resize if needed
        width, height = img.size
        total_pixels = width * height
        
        if total_pixels > self.max_image_pixels:
            scale = (self.max_image_pixels / total_pixels) ** 0.5
            new_width = int(width * scale)
            new_height = int(height * scale)
            img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Encode to base64
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=85)
        return base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    def _call_api(
        self,
        messages: List[Dict],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        enable_thinking: bool = False
    ) -> LLMResponse:
        """Internal method to call the API using OpenAI client."""
        start_time = time.time()
        
        try:
            # Use OpenAI client to create chat completion
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature or self.temperature,
                max_tokens=max_tokens or self.max_tokens,
                extra_body={"enable_thinking": enable_thinking}
            )
            
            elapsed = time.time() - start_time
            logger.debug(f"VLM response received in {elapsed:.2f}s")
            
            # Accumulate token usage
            if completion.usage:
                self.total_prompt_tokens += completion.usage.prompt_tokens or 0
                self.total_completion_tokens += completion.usage.completion_tokens or 0
            
            # Convert completion to dict for raw_response
            data = completion.model_dump()
            
            if completion.choices and len(completion.choices) > 0:
                content = completion.choices[0].message.content or ""
                return LLMResponse(
                    content=content,
                    raw_response=data,
                    success=True
                )
            else:
                return LLMResponse(
                    content="",
                    raw_response=data,
                    success=False,
                    error="No choices in response"
                )
        
        except Exception as e:
            return LLMResponse(
                content="",
                raw_response={},
                success=False,
                error=str(e)
            )


def create_llm_client_from_config(config) -> LLMClient:
    """
    Create an LLM client from a Config object.
    
    Args:
        config: Config object with llm settings
    
    Returns:
        LLMClient instance
    """
    return LLMClient(
        base_url=config.llm.base_url,
        api_key=config.llm.api_key,
        model=config.llm.model,
        temperature=config.llm.temperature,
        max_tokens=config.llm.max_tokens,
        timeout=config.llm.timeout
    )


def create_vlm_client_from_config(config) -> VLMClient:
    """
    Create a VLM client from a Config object.
    
    Args:
        config: Config object with vlm settings
    
    Returns:
        VLMClient instance
    """
    return VLMClient(
        base_url=config.vlm.base_url,
        api_key=config.vlm.api_key,
        model=config.vlm.model,
        temperature=config.vlm.temperature,
        max_tokens=config.vlm.max_tokens,
        max_image_pixels=config.vlm.max_image_pixels,
        timeout=config.vlm.timeout
    )
