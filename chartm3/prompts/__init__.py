"""Prompt templates for each pipeline stage."""

from .topic_prompts import TOPIC_GENERATION_PROMPT, format_topic_prompt
from .data_prompts import (
    DATA_GENERATION_PROMPT,
    format_data_prompt,
)
from .visualization_prompts import (
    VISUALIZATION_PROMPT,
    format_visualization_prompt,
)
from .qa_prompts import (
    QA_GENERATION_PROMPT,
    QA_GENERATION_PROMPT_LONGDATA,
    CODE_QA_STEP1_PROMPT,
    CODE_QA_STEP2_PROMPT,
    EXTRACTION_QA_PROMPT,
    TASK_GROUPS,
    get_task_definition,
    format_qa_prompt,
    format_code_qa_step1_prompt,
    format_code_qa_step2_prompt,
)
from .evaluation_prompts import (
    RELEVANCE_EVALUATION_PROMPT,
    COMPREHENSIVE_EVALUATION_PROMPT,
    VERIFICATION_EVALUATION_PROMPT,
    EVALUATION_MODES,
    format_evaluation_prompt,
    get_evaluation_modes,
)

__all__ = [
    # Topic prompts
    "TOPIC_GENERATION_PROMPT",
    "format_topic_prompt",
    # Data prompts
    "DATA_GENERATION_PROMPT",
    "format_data_prompt",
    # Visualization prompts
    "VISUALIZATION_PROMPT",
    "format_visualization_prompt",
    # QA prompts
    "QA_GENERATION_PROMPT",
    "QA_GENERATION_PROMPT_LONGDATA",
    "CODE_QA_STEP1_PROMPT",
    "CODE_QA_STEP2_PROMPT",
    "EXTRACTION_QA_PROMPT",
    "TASK_GROUPS",
    "get_task_definition",
    "format_qa_prompt",
    "format_code_qa_step1_prompt",
    "format_code_qa_step2_prompt",
    # Evaluation prompts
    "RELEVANCE_EVALUATION_PROMPT",
    "COMPREHENSIVE_EVALUATION_PROMPT",
    "VERIFICATION_EVALUATION_PROMPT",
    "EVALUATION_MODES",
    "format_evaluation_prompt",
    "get_evaluation_modes",
]
