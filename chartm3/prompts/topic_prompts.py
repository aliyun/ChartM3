"""
主题/问题生成的 Prompt 模板
"""

TOPIC_GENERATION_PROMPT = """
你是一名资深的商业分析专家和数据可视化专家，请基于以下要求，设计{num_topics}个需要通过图表分析才能回答的高质量业务问题，并给出对应图表标题和图表内容描述。

【基础信息】
专业领域：{field}
图表类型：{chart_type}（{chart_type_en}）
图表类型的具体描述：
- 视觉定义: {chart_def_visual}
- 适用场景: {chart_def_scenario}
- 数据特征: {chart_def_data}

【问题设计要求】
1. 确保问题具有明确的业务分析目的，重点关注问题的实际应用价值
2. 每张图表只生成一个问题，问题必须基于该图表，有唯一确定的答案
3. 问题应引导深入思考，鼓励问题通过多步推理回答
4. 鼓励图表在不影响可读性的情况下适当复杂或有更多的数据
5. 充分考虑实际场景中的约束条件

【问题设计参考】
1. 业务场景要素:
- 关联具体KPI指标
- 对应明确的决策场景
- 指向特定的分析对象

2. 分析视角:
- 时间维度分析
- 结构对比分析
- 因果关系分析
- 预警阈值分析

### Example Start ###
输入：
专业领域：教育
图表类型：分组条形图（Grouped Bar Chart）

输出：
[
    {{
        "question": "在2022年和2023年，不同学科的课程报名人数变化趋势如何，哪些学科的增长幅度最大？",
        "topic": "2022年与2023年各学科课程报名人数对比",
        "description": "图表展示2022年和2023年各学科的课程报名人数，每组条形图代表一个学科，包含两年的数据。通过观察条形长度的变化，可以分析出哪些学科的需求增长最快。",
        "field": "教育"
    }},
    {{
        "question": "2023年不同教学模式的满意度评分是否存在季节性波动？",
        "topic": "2023年各季度不同教学模式满意度评分对比",
        "description": "图表展示2023年四个季度中，不同教学模式（线上、线下、混合）的满意度评分。每组条形图代表一个季度，分别显示三种教学模式的评分数据，用于分析满意度的季节性和模式差异。",
        "field": "教育"
    }}
    ...
]
### Example End ###

【输出格式】
以JSON格式输出结果，输出在带有"json"标头的代码块中；不要输出任何其他内容。
参考格式如下:

```json
[
    {{
        "question":"业务问题",
        "topic":"图表标题",
        "description":"图表内容描述",
        "field":"专业领域"
    }}
]
```
"""


# Prompt for add mode (appending to existing topics)
TOPIC_ADD_PROMPT = """
你是一名资深的商业分析专家和数据可视化专家，请基于以下要求，设计{num_topics}个需要通过图表分析才能回答的高质量业务问题，并给出对应图表标题和图表内容描述。

【基础信息】
专业领域：{field}
图表类型：{chart_type}（{chart_type_en}）
图表类型的具体描述：
- 视觉定义: {chart_def_visual}
- 适用场景: {chart_def_scenario}
- 数据特征: {chart_def_data}

【已存在的问题】
以下是已经生成过的问题，请确保新问题不与这些重复：
{existing_topics}

【问题设计要求】
1. 确保问题具有明确的业务分析目的，重点关注问题的实际应用价值
2. 每张图表只生成一个问题，问题必须基于该图表，有唯一确定的答案
3. 问题应引导深入思考，鼓励问题通过多步推理回答
4. 鼓励图表在不影响可读性的情况下适当复杂或有更多的数据
5. 充分考虑实际场景中的约束条件
6. 新问题必须与已存在的问题完全不同，避免相似或重复的主题

【问题设计参考】
1. 业务场景要素:
- 关联具体KPI指标
- 对应明确的决策场景
- 指向特定的分析对象

2. 分析视角:
- 时间维度分析
- 结构对比分析
- 因果关系分析
- 预警阈值分析

【输出格式】
以JSON格式输出结果，输出在带有"json"标头的代码块中；不要输出任何其他内容。
参考格式如下:

```json
[
    {{
        "question":"业务问题",
        "topic":"图表标题",
        "description":"图表内容描述",
        "field":"专业领域"
    }}
]
```
"""


def format_topic_prompt(
    field: str,
    chart_type: str,
    chart_type_en: str,
    chart_def_visual: str,
    chart_def_scenario: str,
    chart_def_data: str,
    num_topics: int = 20,
    existing_topics: str = ""
) -> str:
    """
    Format the topic generation prompt with given parameters.
    
    Args:
        field: Domain/field name
        chart_type: Chinese chart type name
        chart_type_en: English chart type name
        chart_def_visual: Visual definition of the chart type
        chart_def_scenario: Usage scenarios
        chart_def_data: Data characteristics
        num_topics: Number of topics to generate (default: 20)
        existing_topics: JSON string of existing topics for add mode (default: "")
    
    Returns:
        Formatted prompt string
    """
    if existing_topics:
        # Use add mode prompt
        return TOPIC_ADD_PROMPT.format(
            num_topics=num_topics,
            field=field,
            chart_type=chart_type,
            chart_type_en=chart_type_en,
            chart_def_visual=chart_def_visual,
            chart_def_scenario=chart_def_scenario,
            chart_def_data=chart_def_data,
            existing_topics=existing_topics
        )
    else:
        # Use normal prompt
        return TOPIC_GENERATION_PROMPT.format(
            num_topics=num_topics,
            field=field,
            chart_type=chart_type,
            chart_type_en=chart_type_en,
            chart_def_visual=chart_def_visual,
            chart_def_scenario=chart_def_scenario,
            chart_def_data=chart_def_data
        )
