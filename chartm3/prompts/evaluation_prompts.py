"""
Quality Evaluation Prompts for ChartM3.

This module contains prompts for evaluating the quality of
generated Q&A pairs against chart images.
"""

# =============================================================================
# Basic Relevance Evaluation
# =============================================================================

RELEVANCE_EVALUATION_PROMPT = """
你是一位专精于图表分析和可视化的资深数据分析专家。你的任务是通过检查以下图表、问题、推理过程和答案，评估问答对与图表的相关性。

具体的，你需要分析在推理过程和答案中提到的所有元素（如标签、坐标轴、图例、数据点等）是否确实存在于图表中，如果存在则结论为yes，不存在为no。

注意:
1. 你只需要判断这些元素是否在图表中被找到，而不需要考虑数值是否正确和答案是否正确。
2. 如果图表中没有直接标注出具体数值，但是可以根据数据点位置和坐标轴进行估算，也算该数据点存在于图表中。

【输入问答对】
问题：{question}
推理过程：{explanation}
答案：{answer}

【输出格式】
请务必使用英文输出所有内容。
请直接以JSON格式输出结果，不要输出任何其他内容。

```json
{{
    "decision": "yes/no"
}}
```
"""

# =============================================================================
# Comprehensive Quality Evaluation
# =============================================================================

COMPREHENSIVE_EVALUATION_PROMPT = """
你是一位专精于图表分析和可视化的资深数据分析专家。你的任务是评估以下图表、问题、推理过程和答案的质量。

请从以下几个方面进行分析，任意一条不满足则为no，全部满足为yes：

1. 绘图质量评价
- 数据可视化是否完整，所有图例项对应的可视化数据点是否都能在图表中看到
- 图表元素不能出现明显遮挡、重叠或比例失调问题

2. 图表相关性
- 推理过程和答案中提到的所有元素（如标签、坐标轴、图例、数据点等）是否确实存在于图表中
- 对于未直接标注数值的情况,是否可通过坐标轴进行合理估算
- 所有必要的数据是否都可从图表中获取

3. 数据准确性
- 对于标注了具体数值的数据点,引用值是否与图表一致
- 对于需要估算的数据点,误差是否在允许范围内(≤10%)

4. 逻辑一致性
- 推理过程是否遵循清晰合理的分析步骤
- 分析结论是否与问题直接相关
- 问题、推理和结论之间是否存在逻辑断层

5. 特殊情况处理
- 如果问题无法从图表中得到有效答案，直接返回"no"
- 如果是选择题且所有选项均不正确，或者有多个选项符合但只给出一个答案，直接返回"no"

【输入问答对】
问题：{question}
推理过程：{explanation}
答案：{answer}

【输出格式】
请直接以JSON格式输出结果，不要输出任何其他内容。

```json
{{
    "decision": "yes/no"
}}
```
"""

# =============================================================================
# Independent Verification (Criticize Mode)
# =============================================================================

VERIFICATION_EVALUATION_PROMPT = """
你是一位专精于图表分析和可视化的资深数据分析专家。你的任务是分三步完成图表分析:
1. 从图片中提取关键数据信息
2. 独立计算得出标准答案 
3. 判断小明同学的回答是否正确

【问题】
{question}

【小明的回答】
{explanation}
{answer}

【注意】
1. 小明是一个数据分析水平很差的同学，请在计算标准答案时完全忽略小明的解答，基于你自己的专业分析得出标准答案。
2. 你分析图表的能力足够强大，请独立完成题目并充分相信你的回答就是标准答案。
3. 允许的误差范围:
   - 当图表有明确数值标注时,答案必须完全准确
   - 当需要通过坐标轴估算时,允许±10%的误差范围
4. 答案格式要求:
   - 数值带不带单位都视为正确(如"5"和"5米"等价)
   - 百分比表示法通用(如"5%"和"5"等价) 
   - 数量级表示法通用(如"5"和"500万"等价)
5. 如遇以下情况直接判定为错误(decision="no"):
   - 题目条件不足导致无法求解
   - 题目本身存在明显错误
   - 图表信息模糊不清

【输出格式】
请直接以JSON格式输出结果，不要输出任何其他内容。

```json
{{
    "decision": "yes/no"
}}
```
"""

# =============================================================================
# Evaluation Mode Definitions
# =============================================================================

EVALUATION_MODES = {
    "relevance": {
        "name": "Relevance Check",
        "description": "Check if Q&A elements exist in the chart",
        "prompt": RELEVANCE_EVALUATION_PROMPT,
    },
    "comprehensive": {
        "name": "Comprehensive Evaluation",
        "description": "Full quality assessment including accuracy and logic",
        "prompt": COMPREHENSIVE_EVALUATION_PROMPT,
    },
    "verification": {
        "name": "Independent Verification",
        "description": "Independently solve and verify the answer",
        "prompt": VERIFICATION_EVALUATION_PROMPT,
    },
}


def format_evaluation_prompt(
    question: str,
    explanation: str,
    answer: str,
    options: str = "",
    mode: str = "verification"
) -> str:
    """
    Format the evaluation prompt based on mode.
    
    Args:
        question: The question text
        explanation: The reasoning/explanation
        answer: The answer
        options: Multiple choice options (if any)
        mode: Evaluation mode ("relevance", "comprehensive", or "verification")
    
    Returns:
        Formatted prompt string
    """
    if mode not in EVALUATION_MODES:
        raise ValueError(f"Unknown evaluation mode: {mode}. "
                        f"Available modes: {list(EVALUATION_MODES.keys())}")
    
    # Add options to question if present
    full_question = question
    if options:
        if isinstance(options, list):
            options = " ".join(options)
        full_question = f"{question}\n{options}"
    
    template = EVALUATION_MODES[mode]["prompt"]
    return template.format(
        question=full_question,
        explanation=explanation,
        answer=answer
    )


def get_evaluation_modes() -> dict:
    """
    Get available evaluation modes and their descriptions.
    
    Returns:
        Dictionary of evaluation mode information
    """
    return {
        mode: {
            "name": info["name"],
            "description": info["description"]
        }
        for mode, info in EVALUATION_MODES.items()
    }
