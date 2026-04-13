"""
Q&A Generation Prompts for ChartM3.

This module contains prompts and task definitions for generating
question-answer pairs based on chart images and data.
"""

# =============================================================================
# Task Type Definitions
# =============================================================================

# Task Group 1: Basic Chart Understanding
TASK_BASIC = """
任务类型	英文	任务类型描述与要求	指定题型
类型分类	Type Classification	识别图表的可视化类型（如折线图、柱状图、饼图等），对复合图表需完整列举所有组成类型的名称，并说明复合结构（如双轴图、组合图等）。	单选题
标题识别	Title Identification	提取图表主标题和副标题的完整文本内容，需保持原标题的大小写格式与特殊符号，不添加解释性文字。	填空题
轴标签识别	Axis Label Recognition	识别坐标轴标题及其计量单位，需区分X/Y轴并规范提取格式（例："GDP（万亿美元）"）。若存在双轴或多轴需分别标注。	填空题
图表元素计数	Chart Element Counting	统计图表核心元素数量（如独立数据序列数、子图数量、图例项总数等）。	单选题,填空题
"""

# Task Group 2: Data Retrieval
TASK_DATA_RETRIEVAL = """
任务类型	英文	任务类型描述与要求	指定题型
数据查询	Data Query	基于特定坐标（X/Y值）或分类标签（如国家、年份）检索精确数值。	单选题,填空题
最值查询	Extreme Value Query	识别全局/局部条件的数值极值，需同时提取极值数值、对应类别标签。	单选题,填空题
条件查询	Conditional Query	查找满足要求数值条件(大于、小于、等于等)的所有数据点或个数。	单选题,填空题
"""

# Task Group 3: Data Analysis
TASK_DATA_ANALYSIS = """
任务类型	英文	任务类型描述与要求	指定题型
数学计算	Calculation	执行基于数据点的数值运算,如求和、求差、倍数、平均值、增长率等。	单选题,填空题
比较	Comparison	执行数据间相对关系判断（如A比B高X），或某个数据相对于均值或指定基准值的相对大小。	单选题,判断题
排序	Sorting	按数值大小输出排序结果，需规定排序方向（升序/降序），排序结果使用逗号分隔。	问答题
"""

# Task Group 4: Advanced Analysis
TASK_ADVANCED_ANALYSIS = """
任务类型	英文	任务类型描述与要求	指定题型
相关性分析	Correlation Analysis	判断变量间关系类型（正/负/无相关），需基于统计显著性或视觉趋势特征。	单选题,判断题
异常检测	Anomaly Detection	识别偏离常规模式的数据点，需明确异常判定标准（如3σ原则、箱线图四分位距法）并说明异常方向。	判断题,问答题
趋势分析	Trend Analysis	根据图表数据趋势验证某个描述是否正确。	判断题,问答题
推论判断	Inferential Judgment	验证基于图表数据的逻辑推论，需区分直接证据支持（显性数据）和间接推测（隐性趋势）。	判断题,问答题
"""

# Task Group 5: Visual Recognition
TASK_VISUAL = """
任务类型	英文	任务类型描述与要求	指定题型
轴刻度识别	Axis Scale Recognition	识别图像中X或Y坐标轴信息，例如最左侧/右侧度数、取值范围、刻度间隔、刻度个数。	单选题,填空题
颜色识别	Color Identification	识别指定图表元素对应颜色，或指定颜色对应的元素，或指定颜色数据在特定坐标下的精确数值。	单选题,填空题
图例识别	Legend Identification	完整列举图例项名称，按图例原始顺序输出。	填空题
"""

# Task Group 6: Subplot Tasks
TASK_SUBPLOT_BASIC = """
任务类型	英文	任务类型描述与要求	指定题型
标题识别	Title Identification	提取指定行列位置子图的标题完整文本内容，需保持原标题的大小写格式与特殊符号，不添加解释性文字。指定位置的描述可以是最上方/从下往上数第几个/第几行(如果只有一列)/第几行第几列（如果是多行多列）等。	填空题
轴标签识别	Axis Label Recognition	识别指定行列位置子图的坐标轴标题及其计量单位，需区分X/Y轴并规范提取格式（例："GDP（万亿美元）"）。指定位置的描述可以是最上方/从下往上数第几个/第几行(如果只有一列)/第几行第几列（如果是多行多列）等。	填空题
"""

TASK_SUBPLOT_VISUAL = """
任务类型	英文	任务类型描述与要求	指定题型
图表元素计数	Chart Element Counting	统计图表中子图数量，子图布局（几行几列）。	单选题,填空题
轴刻度识别	Axis Scale Recognition	识别指定行列位置子图中X或Y坐标轴信息，例如最左侧/右侧度数、取值范围、刻度间隔、刻度个数。指定位置的描述可以是最上方/从下往上数第几个/第几行(如果只有一列)/第几行第几列（如果是多行多列）等。	单选题,填空题
颜色识别	Color Identification	识别指定行列位置子图中某个元素对应颜色，或指定颜色对应的元素，或指定颜色数据在特定坐标下的精确数值。指定位置的描述可以是最上方/从下往上数第几个/第几行(如果只有一列)/第几行第几列（如果是多行多列）等。	单选题,填空题
"""

# Task Group 7: Extra Tasks
TASK_VISUAL_EXTRA = """
任务类型	英文	任务类型描述与要求	指定题型
图表元素位置	Chart Element Position	分析数据元素在图中的相对位置信息，例如识别折线图是否相交/某条直线是否一直在某条直线上方。	判断题,填空题
图表元素位置	Chart Element Position	分析坐标轴在图中的相对位置信息，例如x轴从左往右数第几个是什么标签/y轴从上往下数第几个是什么标签等。	单选题,填空题
图表元素计数    Chart Element Counting  统计图表某个视觉元素个数（如x轴或y轴标签个数/x轴与y轴相加总个数/折线图中线段条数/柱状图中柱子个数/子图布局为几行几列（如果只有一张图则为1行1列）等）。	单选题,填空题
"""

TASK_DATA_EXTRACTION = """
任务类型	英文	任务类型描述与要求	指定题型
数据提取	Chart to Data	提取图表中所有数据内容并转为markdown格式，不要输出颜色和其他无法在图表上展示的列。	问答题
"""

# Extraction-specific prompt for data extraction tasks
EXTRACTION_QA_PROMPT = """
你是一位数据提取专家。你的任务是基于图表的原始代码和数据，生成一个数据提取型问答对。

【任务说明】
数据提取任务要求将图表中的数据完整提取出来，转换为结构化的markdown表格格式。
这不是计算或分析任务，而是数据转换任务。

【数据提取要求】
1. 提取图表中展示的所有核心数据（类别、数值等）
2. 将数据转换为markdown表格格式
3. 不要包含颜色、样式等视觉属性
4. 只提取图表上实际展示的数据列
5. 保持数据的原始顺序和结构

【问答题型】
问答题（Short-answer）: 问题是"请将图表中的数据提取为markdown格式"，答案是markdown表格

【输出格式】
请务必使用英文输出所有内容。
请直接以JSON格式输出结果，不要输出任何其他内容。

```json
{{
    "task_type": "Chart to Data",
    "question_type": "Short-answer",
    "difficulty": "M",
    "question": "Extract all data from the chart and present it in markdown table format.",
    "explanation": "The data was extracted from the chart by identifying all visible data points and organizing them into a structured markdown table.",
    "options": "",
    "answer": "markdown表格内容"
}}
```

【原始代码和数据】
图表类型: {chart_type}

代码:
{code}

数据:
{data}
"""

# Task collections for different use cases
TASK_GROUPS = {
    # 1) 不需要code生成：基础识别 + 视觉理解
    "visual": [TASK_BASIC, TASK_VISUAL, TASK_VISUAL_EXTRA],
    # 2) 需要生成code：数据检索 + 数据分析 + 高级分析
    "code_driven": [TASK_DATA_RETRIEVAL, TASK_DATA_ANALYSIS, TASK_ADVANCED_ANALYSIS],
    # 3) 子图专用：子图基础 + 子图视觉
    "subplot": [TASK_SUBPLOT_BASIC, TASK_SUBPLOT_VISUAL],
    # 4) 数据提取型（仅部分图表支持）
    "extraction": [TASK_DATA_EXTRACTION],
    # 便捷组合：all = visual + code_driven
    "all": [TASK_BASIC, TASK_VISUAL, TASK_VISUAL_EXTRA,
            TASK_DATA_RETRIEVAL, TASK_DATA_ANALYSIS, TASK_ADVANCED_ANALYSIS],
}


QA_GENERATION_PROMPT = """
你是一位拥有丰富数据分析和可视化经验的高级商业分析师。你的任务是基于图表的原始代码和数据生成一条高质量的分析问答对，该问答对反映实际业务场景中的数据分析需求，将用于提升AI模型的图表理解能力。

【数据质量前提】
1. 可视化代码和数据绝对正确，完全可以信赖
2. 请先分析代码画图时使用了哪些原始数据，不要使用任何没有在代码中使用到的数据生成问题、推理过程或回答
3. 需注意实际训练模型时只能看到渲染后的图表图片，无法看到原始图表代码和数据
4. 如果代码没有在图上添加数值标注，避免进行精确数值查询与计算

【任务类型要求】
请严格按照以下任务类型出题
{task}

【问答题型规范】
1. 单选题（Multiple-choice）: 问题是单选题且包含ABCD四个选项，答案是单个大写字母(A/B/C/D)，其余选项必须是错误的
2. 判断题（True/False）: 问题是疑问句，答案是Yes或No
3. 填空题（Fill-in-the-blank）: 问题是疑问句或填空形式，答案是具体的数值、单词或短语
4. 问答题（Short-answer）: 问题是疑问句，答案是完整的一句话,不超过50字

【问题生成要求】 
1. 确保问题具有明确的业务分析目的，重点关注问题的实际应用价值
2. 问题应该引导深入思考而非简单描述，鼓励生成需要多步推理才能回答的问题
3. 问题必须有唯一确定的答案
4. 对于问题中出现的统计学词汇或包括异常值、偏离值、显著峰值等特殊描述，需要同时给出明确的名词解释或判定标准

【答案生成要求】 
1. 所有结论必须直接来源于图表图片中存在的视觉信息
2. 避免主观臆测，或给出不存在的前提
3. 回答中不能出现代码语言或颜色编码

【推理过程生成要求】
1. 回答问题前需要提供清晰的分析推理过程，在explanation中给出
2. 推理过程按步骤提供，每一步都要有明确的依据
3. 推理过程中如果某个计算过程涉及4个或更多数据，请将其分解为多个子步骤，每次只处理2-3个数据，并显示完整的计算过程和中间结果

【难度分级标准】
简单难度(S)特征：
- 基于单个维度的信息
- 无需进行推理过程
- 无需进行数学计算
- 答案可以直接从图表读取

中等难度(M)特征：
- 需要整合2-3个维度的信息
- 包含基本的推理分析
- 涉及简单的数学运算
- 答案可以通过直接观察获得

高等难度(H)特征：
- 需要综合多个维度的信息
- 包含多步的推理过程
- 需要进行多步数学运算或复杂计算过程
- 答案需要深入分析才能得出

【输出格式】
请务必使用英文输出所有内容。
请直接以JSON格式输出结果，不要输出任何其他内容。

```json
{{
    "task_type": "任务类型",
    "question_type": "题型",
    "difficulty": "S/M/H",
    "question": "问题文本",
    "explanation": "分析推理过程",
    "options": "选项文本(字符串，非单选题为空）",
    "answer": "标准答案"
}}
```

【原始代码和数据】
图表类型: {chart_type}

代码:
{code}

数据:
{data}
"""

QA_GENERATION_PROMPT_LONGDATA = """
你是一位拥有丰富数据分析和可视化经验的高级商业分析师。你的任务是基于图表的原始代码和数据生成一条高质量的分析问答对。

【数据质量前提】
1. 可视化代码和数据绝对正确，完全可以信赖
2. 请先分析代码画图时使用了哪些原始数据，不要使用任何没有在代码中使用到的数据生成问题、推理过程或回答
3. 需注意实际训练模型时只能看到渲染后的图表图片，无法看到原始图表代码和数据
4. 该图表数据量较大，推理过程和答案中涉及的数据只进行横向对比或定性分析，请避免查询某条数据的精确数值

【任务类型要求】
请严格按照以下任务类型出题
{task}

【问答题型规范】
1. 单选题（Multiple-choice）: 问题是单选题且包含ABCD四个选项，答案是单个大写字母(A/B/C/D)
2. 判断题（True/False）: 问题是疑问句，答案是Yes或No
3. 填空题（Fill-in-the-blank）: 答案是具体的数值、单词或短语
4. 问答题（Short-answer）: 答案是完整的一句话,不超过50字

【难度分级标准】
简单难度(S)：基于单个维度信息，无需计算，可直接读取
中等难度(M)：整合2-3个维度，包含基本推理和简单运算
高等难度(H)：综合多维度，多步推理和复杂计算

【输出格式】
请务必使用英文输出所有内容。
请直接以JSON格式输出结果，不要输出任何其他内容。

```json
{{
    "task_type": "任务类型",
    "question_type": "题型",
    "difficulty": "S/M/H",
    "question": "问题文本",
    "explanation": "分析推理过程",
    "options": "选项文本(字符串，非单选题为空）",
    "answer": "标准答案"
}}
```

【原始代码和数据】
图表类型: {chart_type}

代码:
{code}

数据:
{data}
"""

# =============================================================================
# Code-Driven Q&A Generation (Two-Step Process)
# =============================================================================

CODE_QA_STEP1_PROMPT = """
你是一位拥有丰富数据分析和可视化经验的高级商业分析师。你的任务是基于图表可视化代码和数据生成一个高质量的分析问题，并编写python代码来计算答案。

【数据说明】
图表类型: {chart_type}

可视化代码: 
{code}

数据路径: {data_path}

数据格式样例：
{data}

【任务类型】
请严格生成以下任务类型要求的问题。
{task}

【问题生成要求】
1. 确保问题具有明确的业务分析和实际应用价值
2. 优先生成需要多步计算或统计分析的问题
3. 注意做题者只能看到图表图片，无法看到原始图表代码和数据真值
4. 在满足任务类型要求的前提下，适当生成更加复杂困难的问题，例如：
   - 需要综合多个维度（>3）的信息
   - 包含多步的推理过程
   - 需要进行多步数学运算或复杂统计分析过程
5. 对于统计个数的任务，禁止生成答案大于20的问题
6. 请优先生成需要多步推理或复杂计算的中高难度问题
{extra}

【代码要求】
1. 使用pandas和numpy等库进行数据处理
2. 代码需要包含清晰的注释
3. 确保代码的计算结果准确可靠
4. 只能使用提供的原始数据
5. 输出必要的中间计算结果
6. 代码风格要规范,变量命名要有意义

【问答题型】
1. 单选题（Multiple-choice）: 答案是单个大写字母(A/B/C/D)
2. 判断题（True/False）: 答案是Yes或No
3. 填空题（Fill-in-the-blank）: 答案是具体的数值、单词或短语
4. 问答题（Short-answer）: 答案是完整的一句话,不超过50字

【输出格式】
请务必使用英文输出所有内容。
请直接以JSON格式输出结果，不要输出任何其他内容。

```json
{{
    "task_type": "任务类型",
    "question_type": "题型",
    "question": "问题文本",
    "options": "选项文本(字符串，非单选题为空）"
}}
```

```python
# Import required libraries
import pandas as pd
import numpy as np

# Loading Data from csv file
data_file_path = "{data_path}"
df = pd.read_csv(data_file_path)

# Data processing and calculation code
...

# Print intermediate results
print("Average of metric a:", average_a)

# Print final results
print("Final result:", result)
```
"""

CODE_QA_STEP2_PROMPT = """
该代码的执行结果为：
{code_output}

请将其作为数据支撑，对该问题进行详细的推理过程分析并生成最终答案。
特别的，对于选择题，如果你认为所有选项都不正确或者有多个选项正确，请修改选项内容以保证：最终答案完全正确，且除答案外其余选项均错误。

【生成要求】
1. 请完全相信代码执行结果的正确性。
2. 所有推理过程都应表达为对图表视觉信息进行分析计算的过程，不要提及你参考了代码或输出结果
3. 按步骤提供必要的推理过程，不要省略相似过程，计算过程需要给出公式和答案
4. 所有推理过程语言流畅并尽可能使用足够精简的描述
5. 最后给出简洁且明确的答案，符合问答题型的答案格式要求
6. 不能出现代码语言片段或颜色编码

【输出格式】
```json
{{
    "task_type": "任务类型",
    "question_type": "题型",
    "difficulty": "S/M/H",
    "question": "问题文本",
    "options": "选项文本(字符串，非单选题为空）",
    "explanation": "详细的分步推理过程",
    "answer": "最终答案"
}}
```
"""

def get_task_definition(task_group: str = "all") -> list:
    """
    Get task definitions for Q&A generation.
    
    Args:
        task_group: Task group name, one of:
            - "basic": Basic chart understanding tasks
            - "retrieval": Data retrieval tasks  
            - "analysis": Data analysis tasks
            - "visual": Visual recognition tasks
            - "subplot": Subplot-specific tasks
            - "extraction": Data extraction tasks
            - "all": All standard tasks
            - "code_driven": Tasks suitable for code-driven generation
    
    Returns:
        List of task definition strings
    """
    return TASK_GROUPS.get(task_group, TASK_GROUPS["all"])


def format_qa_prompt(
    code: str,
    data: str,
    chart_type: str,
    task: str,
    is_long_data: bool = False
) -> str:
    """
    Format the Q&A generation prompt.
    
    Args:
        code: Visualization code
        data: Data content or sample
        chart_type: Chart type name
        task: Task definition string
        is_long_data: Whether the data is large
    
    Returns:
        Formatted prompt string
    """
    template = QA_GENERATION_PROMPT_LONGDATA if is_long_data else QA_GENERATION_PROMPT
    return template.format(
        code=code,
        data=data,
        chart_type=chart_type,
        task=task
    )


def format_code_qa_step1_prompt(
    code: str,
    data: str,
    data_path: str,
    chart_type: str,
    task: str,
    extra: str = ""
) -> str:
    """
    Format the code-driven Q&A generation step 1 prompt.
    
    Args:
        code: Visualization code
        data: Data sample
        data_path: Path to the data file
        chart_type: Chart type name
        task: Task definition string
        extra: Extra requirements
    
    Returns:
        Formatted prompt string
    """
    return CODE_QA_STEP1_PROMPT.format(
        code=code,
        data=data,
        data_path=data_path,
        chart_type=chart_type,
        task=task,
        extra=extra
    )


def format_code_qa_step2_prompt(code_output: str) -> str:
    """
    Format the code-driven Q&A generation step 2 prompt.
    
    Args:
        code_output: Output from executing the generated code
    
    Returns:
        Formatted prompt string
    """
    return CODE_QA_STEP2_PROMPT.format(code_output=code_output)
