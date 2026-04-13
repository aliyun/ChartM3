"""
可视化代码生成的 Prompt 模板

Stage 1: 生成可视化方案（分析数据特点 + 设计可视化方案）
Stage 2: 根据方案生成可视化代码
"""

# =============================================================================
# Stage 1: 可视化方案生成
# =============================================================================

VIS_PLAN_PROMPT = """
你是一名数据可视化专家，现在有一个可视化方案推荐任务，需要根据用户数据的特点，为用户推荐合适的可视化方案。
具体要求如下：
1. 用户的数据已读取到内存中的`data`变量中，类型为pandas.DataFrame，不需要进行额外的数据读取。
2. 使用matplotlib包中的函数生成可视化代码，必要时也可以使用numpy等库进行数据处理，但请保证代码的准确性和可执行性。
3. 请首先分析用户的数据特点，判断用户数据适合从哪些角度进行可视化，并生成数据展示的背景故事。在生成过程中，最大程度发挥想象力和创造力。
4. 基于背景故事和目标图表类型，设计合理的可视化方案，包括坐标轴、图例、标题、图表风格等。可视化方案必须是可实现的，不要使用数据集中不存在的字段内容。

下面是用户数据的特征描述：
{file_name}

data.head()：
{data_head}

data.describe()：
{data_describe}

data.describe(include='object')：
{data_describe_object}

目标图表类型: {target_chart_type}
{visual_definition}

现在，请开始分析并输出一个JSON字符串，包含以下两个字段（均为纯文本，要点之间请换行）：
- `analysis`：需求分析阶段的思考过程
- `guidance`：可视化设计阶段的方案（注意：不需要生成实际的可视化代码）

【重要提示】
1. JSON 字符串中的值不要包含英文双引号(")，如需引用文本请使用单引号(')或其他方式
2. 确保输出的 JSON 格式合法，可以被标准 JSON 解析器正确解析

【输出格式】
请直接以JSON格式输出结果，不要输出任何其他内容。结果请简洁精炼，避免过多赘述。

```json
{{{{
    "analysis": "数据特点分析与需求思考过程",
    "guidance": "可视化设计方案（包括坐标轴、图例、标题、图表风格等）"
}}}}
```
"""

# =============================================================================
# Stage 2: 可视化代码生成
# =============================================================================

VISUALIZATION_PROMPT = """
你是一名数据可视化专家，现在有一个Python可视化代码生成任务，需要你首先阅读样例代码，然后参考用户数据和需求，实现对于用户数据的可视化代码。

## 样例开始
目标图表类型: {target_chart_type}
{visual_definition}

样例数据格式：
{sample_data_head}

样例绘图代码：
{sample_code}
## 样例结束

下面，给出用户数据的特点和用户需求。
## 用户数据开始
标题：{file_name}
目标：{seed_description}

data.head()：
{data_head}

data.describe()：
{data_describe}

data.describe(include='object')：
{data_describe_object}
## 用户数据结束

现在，请参考样例并结合用户数据的实际情况和可视化需求，生成符合要求的可视化代码。

实际可视化需求：{vis_guidance}

具体要求如下：
1. 用户的数据已读取到内存中的`data`变量中，类型为pandas.DataFrame，不要输出任何数据读取、数据声明相关代码。
2. 图表风格与样例尽可能保持一致，但在配色、布局、元素类型等方面可以根据实际数据领域做简单调整。长文本时，注意避免x轴、图例等位置的文字重叠。
3. 请生成两个python函数：`def preprocess(data):`，用于绘图数据的预处理，输入为原始dataframe，输出为预处理后的数据dataframe；`def plot(data):`，用于绘制对应的图表。注意最终只生成一张图（可以有多个子图）。
4. preprocess函数需要在plot函数中被调用。只需要生成函数体，不需要生成调用plot函数的代码。
5. 请在preprocess函数中完成所有的绘图数据预处理（包括小数位数设置），在plot函数中不要进行任何数据处理操作！
6. 请将结果保存到文件中，文件名为"plot.png"。Matplotlib请使用plt.savefig('plot.png')，Plotly请使用fig.write_image('plot.png')。禁止自定义输出目录路径逻辑。
7. {styling_prompt}
8. 【重要】如果使用 plt.style.use() 设置样式，请确保使用正确的样式名称。有效的 seaborn 样式包括：'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid' 等。
9. 最重要的，请确保代码是可被正确执行的，因此对于各种方法调用参数请尽可能与样例保持一致。请将所有的代码生成在同一个 ```python 代码块中。
"""

STYLING_PROMPT_DEFAULT = "图表中所有文本内容（标题、图例、坐标轴标签等）请全部使用英文。"

STYLING_PROMPT_NO_CAPTION = "所有文本内容请全部使用英文。【注意，与样例不同，本次生成的图表不要添加任何caption文字，包括标题、图中文本、标注数字等！请在生成代码时不要添加相关语句！】"


def format_vis_plan_prompt(
    file_name: str,
    data_head: str,
    data_describe: str,
    data_describe_object: str,
    target_chart_type: str,
    visual_definition: str = "",
) -> str:
    """
    Format the Stage 1 visualization plan prompt.
    
    Args:
        file_name: User's data file name/title
        data_head: User's data.head() output
        data_describe: User's data.describe() output
        data_describe_object: User's data.describe(include='object') output
        target_chart_type: Target chart type name
        visual_definition: Visual definition of the chart type
    
    Returns:
        Formatted prompt string
    """
    return VIS_PLAN_PROMPT.format(
        file_name=file_name,
        data_head=data_head,
        data_describe=data_describe,
        data_describe_object=data_describe_object,
        target_chart_type=target_chart_type,
        visual_definition=visual_definition,
    )


def format_visualization_prompt(
    target_chart_type: str,
    visual_definition: str,
    sample_data_head: str,
    sample_code: str,
    file_name: str,
    seed_description: str,
    data_head: str,
    data_describe: str,
    data_describe_object: str,
    vis_guidance: str = "",
    styling_prompt: str = STYLING_PROMPT_DEFAULT
) -> str:
    """
    Format the Stage 2 visualization code generation prompt.
    
    Args:
        target_chart_type: Target chart type name
        visual_definition: Visual definition of the chart type
        sample_data_head: Sample data format
        sample_code: Sample visualization code
        file_name: User's data file name/title
        seed_description: Goal/description
        data_head: User's data.head() output
        data_describe: User's data.describe() output
        data_describe_object: User's data.describe(include='object') output
        vis_guidance: Visualization plan/guidance from Stage 1
        styling_prompt: Styling instructions
    
    Returns:
        Formatted prompt string
    """
    return VISUALIZATION_PROMPT.format(
        target_chart_type=target_chart_type,
        visual_definition=visual_definition,
        sample_data_head=sample_data_head,
        sample_code=sample_code,
        file_name=file_name,
        seed_description=seed_description,
        data_head=data_head,
        data_describe=data_describe,
        data_describe_object=data_describe_object,
        vis_guidance=vis_guidance,
        styling_prompt=styling_prompt
    )


def get_visual_definition_text(chart_type_info: dict) -> str:
    """
    Generate visual definition text from chart type info dict.
    
    Args:
        chart_type_info: Dictionary with chart type metadata
    
    Returns:
        Formatted visual definition string
    """
    parts = []
    if chart_type_info.get('视觉定义'):
        parts.append(f"Chart Visual Definition: {chart_type_info['视觉定义']}")
    if chart_type_info.get('数据特征'):
        parts.append(f"Data Requirements: {chart_type_info['数据特征']}")
    return "\n".join(parts)


# =============================================================================
# Code Fix Prompt (for retry on execution failure)
# =============================================================================

CODE_FIX_PROMPT = """
你是一名Python数据可视化专家。之前生成的可视化代码执行时出现了错误，请根据错误信息修复代码。

【图表类型】
{chart_type}

【原始代码】
```python
{code}
```

【错误日志】
```
{error_log}
```

【修复要求】
1. 分析错误原因，修复代码中的问题
2. 保持原有的可视化逻辑和样式设计
3. 确保代码可以正确执行并生成plot.png
4. 只输出修复后的代码，不要输出解释说明
5. 代码必须包含完整的preprocess和plot函数
6. Matplotlib请使用plt.savefig('plot.png')，Plotly请使用fig.write_image('plot.png')。禁止自定义输出目录路径逻辑。
7. 【重要】不要输出if __name__ == "__main__":块，也不要输出import语句。只输出函数定义（preprocess、plot等函数），import和main块会自动拼接。

【输出格式】
请直接输出修复后的Python代码，放在```python代码块中。
"""


def format_code_fix_prompt(code: str, error_log: str, chart_type: str) -> str:
    """
    Format the code fix prompt for retry on execution failure.
    
    Args:
        code: The original code that failed
        error_log: The error message from execution
        chart_type: The chart type being generated
    
    Returns:
        Formatted prompt string
    """
    return CODE_FIX_PROMPT.format(
        code=code,
        error_log=error_log,
        chart_type=chart_type,
    )
