# QA 生成 Prompt

## 用途

基于图表和数据生成高质量的问答对，用于训练视觉语言模型。

## 任务类型定义

### 1. 基础理解任务 (visual)
```
任务类型	英文	任务类型描述与要求	指定题型
类型分类	Type Classification	识别图表的可视化类型	单选题
标题识别	Title Identification	提取图表主标题和副标题	填空题
轴标签识别	Axis Label Recognition	识别坐标轴标题及计量单位	填空题
图表元素计数	Chart Element Counting	统计图表核心元素数量	单选题,填空题
轴刻度识别	Axis Scale Recognition	识别坐标轴刻度信息	单选题,填空题
颜色识别	Color Identification	识别图表元素颜色	单选题,填空题
图例识别	Legend Identification	列举图例项名称	填空题
```

### 2. 数据检索任务 (code_driven)
```
任务类型	英文	任务类型描述与要求	指定题型
数据查询	Data Query	基于坐标或标签检索数值	单选题,填空题
最值查询	Extreme Value Query	识别数值极值	单选题,填空题
条件查询	Conditional Query	查找满足条件的数据	单选题,填空题
数学计算	Calculation	执行数值运算	单选题,填空题
比较	Comparison	执行数据间关系判断	单选题,判断题
排序	Sorting	按数值大小输出排序结果	问答题
相关性分析	Correlation Analysis	判断变量间关系类型	单选题,判断题
异常检测	Anomaly Detection	识别异常数据点	判断题,问答题
趋势分析	Trend Analysis	验证趋势描述正确性	判断题,问答题
推论判断	Inferential Judgment	验证逻辑推论	判断题,问答题
```

### 3. 数据提取任务 (extraction)
```
任务类型	英文	任务类型描述与要求	指定题型
数据提取	Chart to Data	提取图表数据为markdown格式	问答题
```

## 主 Prompt 模板

```
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
3. 推理过程中如果某个计算过程涉及4个或更多数据，请将其分解为多个子步骤

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
{
    "task_type": "任务类型",
    "question_type": "题型",
    "difficulty": "S/M/H",
    "question": "问题文本",
    "explanation": "分析推理过程",
    "options": "选项文本(字符串，非单选题为空）",
    "answer": "标准答案"
}
```

【原始代码和数据】
图表类型: {chart_type}

代码:
{code}

数据:
{data}
```

## 数据提取专用 Prompt

```
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
{
    "task_type": "Chart to Data",
    "question_type": "Short-answer",
    "difficulty": "M",
    "question": "Extract all data from the chart and present it in markdown table format.",
    "explanation": "The data was extracted from the chart by identifying all visible data points and organizing them into a structured markdown table.",
    "options": "",
    "answer": "markdown表格内容"
}
```

【原始代码和数据】
图表类型: {chart_type}

代码:
{code}

数据:
{data}
```

## 任务组配置

| 任务组 | 包含任务 | 适用场景 |
|-------|---------|---------|
| visual | 基础理解 + 视觉识别 | 不需要代码执行 |
| code_driven | 数据检索 + 数据分析 + 高级分析 | 需要代码验证答案 |
| subplot | 子图相关任务 | 多子图图表 |
| extraction | 数据提取 | 部分支持的图表类型 |
| all | visual + code_driven | 完整覆盖 |

## 输出示例

```json
{
    "task_type": "Data Query",
    "question_type": "Fill-in-the-blank",
    "difficulty": "S",
    "question": "What was Harvard's enrollment in 2020?",
    "explanation": "Looking at the line chart, I locate the Harvard line (blue) and find the data point at year 2020. The y-axis value at this point is approximately 21,500.",
    "options": "",
    "answer": "21500"
}
```
