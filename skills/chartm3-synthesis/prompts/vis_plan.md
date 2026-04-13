# 可视化方案设计 Prompt

## 用途

分析数据特点，为指定的图表类型设计合理的可视化方案。

## Prompt 模板

```
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
{
    "analysis": "数据特点分析与需求思考过程",
    "guidance": "可视化设计方案（包括坐标轴、图例、标题、图表风格等）"
}
```
```

## 示例

**输入**:
- 数据: 大学招生趋势数据
- 图表类型: 基础折线图

**输出**:
```json
{
    "analysis": "The dataset contains enrollment data for 5 major universities from 2015 to 2024. Key observations:\n- Time series data with yearly intervals\n- Multiple universities for comparison\n- Numeric enrollment values showing growth trends\n- Suitable for line chart to show temporal patterns",
    "guidance": "Visualization Design:\n- Title: 'University Enrollment Trends (2015-2024)'\n- X-axis: Year (2015-2024)\n- Y-axis: Total Enrollment\n- Legend: University names with distinct colors\n- Style: Clean academic style with grid\n- Line markers to highlight data points\n- Consider using seaborn-v0_8-whitegrid style"
}
```

## 参数说明

| 参数 | 类型 | 说明 |
|-----|------|------|
| file_name | string | 数据文件名/标题 |
| data_head | string | data.head() 的输出 |
| data_describe | string | data.describe() 的输出 |
| data_describe_object | string | data.describe(include='object') 的输出 |
| target_chart_type | string | 目标图表类型名称 |
| visual_definition | string | 图表的视觉定义和数据特征 |
