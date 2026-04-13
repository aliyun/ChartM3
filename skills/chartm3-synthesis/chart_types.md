# ChartM3 支持的图表类型

共支持 63 种图表类型，分为以下类别：

## 1. 条形图/柱状图系列 (Bar Charts)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 基础条形图 | Single Bar Chart | 比较,分布 | 比较不同类别的数值大小、展示排名分布 | Matplotlib |
| 分组条形图 | Grouped Bar Chart | 比较,分布 | 多个系列在不同类别下的数值对比 | Matplotlib |
| 堆叠条形图 | Stacked Bar Chart | 比较,分布,组成 | 展示整体与部分的关系 | Matplotlib |
| 正负条形图 | Positive-Negative Bar Chart | 比较 | 展示具有正负值的对比数据 | Plotly |
| 双向柱图 | Bidirectional Bar Chart | 比较,分布 | 展示两个相对维度的数据对比 | Plotly |
| 蝴蝶图 | Butterfly Diagram | 比较,分布 | 人口结构分析、对称性比较 | Plotly |
| 区间柱状图 | Range Bar Chart | 比较,分布 | 展示数据的波动范围、置信区间 | Matplotlib |
| 瀑布图 | Waterfall Plot | 组成,流向 | 分析财务报表、成本构成 | Matplotlib |
| 蜡烛图 | Candlestick Plot | 分布,趋势 | 金融市场价格走势分析 | Plotly |

## 2. 直方图与分布图 (Distribution Charts)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 基础直方图 | Single Histograms | 分布 | 展示连续型数值变量的分布情况 | Matplotlib |
| 矩形漏斗图 | Rectangular Funnel Chart | 组成,流向 | 展示层级关系的转化流程 | Plotly |
| 箱线图 | Box Plot | 比较,分布 | 展示数据分布特征、识别异常值 | Matplotlib |
| 误差柱图 | Error Bars Chart | 比较,分布 | 展示测量数据的精确度、置信区间 | Matplotlib |
| 子弹图 | Bullet Chart | 比较 | 展示目标完成情况、性能指标对比 | Plotly |
| 嵌套柱形图 | Nested Bar Chart | 比较,组成 | 展示整体与部分的关系 | Plotly |

## 3. 比较图 (Comparison Charts)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 滑珠图 | Dumbbell Plot | 比较 | 展示同一指标在不同时间点的变化 | Matplotlib |
| 杠铃图 | Barbell Chart | 比较 | 比较同一对象在不同条件下的表现 | Plotly |
| 棒棒糖图 | Lollipop Plot | 比较 | 展示单一变量的分布情况 | Matplotlib |

## 4. 折线图系列 (Line Charts)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 基础折线图 | Single Line Chart | 趋势 | 展示时间序列数据的变化趋势 | Matplotlib |
| 多列折线图 | Grouped Line Chart | 比较,趋势 | 比较多个指标随时间的变化 | Plotly |
| 堆叠折线图 | Stacked Line Chart | 组成,趋势 | 展示整体与部分随时间的累积变化 | Plotly |
| 斜率图 | Slope Graph | 比较,趋势 | 比较多个对象在两个时间点之间的变化 | Plotly |
| 阶梯线图 | Step Chart | 比较,趋势 | 展示离散变化或状态突变的数据 | Plotly |

## 5. 面积图系列 (Area Charts)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 基础面积图 | Single Area Chart | 趋势 | 展示单个指标随时间的变化趋势 | Plotly |
| 多列面积图 | Grouped Area Chart | 比较,趋势 | 比较多个指标随时间的变化 | Plotly |
| 堆叠面积图 | Stacked Area Chart | 组成,趋势 | 展示整体随时间的变化及各部分占比 | Plotly |
| 双向面积图 | Bilateral Area Chart | 比较,趋势 | 对比两个相对的数据系列 | Plotly |
| 区间面积图 | Range Area Chart | 分布,趋势 | 展示数据的变化区间、置信区间 | Plotly |
| 河流图 | Streamgraph | 趋势,流向 | 展示多个类别随时间的变化趋势及占比 | Matplotlib |
| 误差带图 | Error Bands Chart | 分布,趋势 | 展示数据趋势及其不确定性范围 | Matplotlib |
| 密度图 | Density Plot | 分布 | 展示连续型数据的分布特征 | Matplotlib |

## 6. 饼图/环形图系列 (Pie Charts)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 基础饼图 | Single Pie Chart | 比较,组成 | 展示部分与整体的关系 | Plotly |
| 嵌套饼图 | Multidimensional Pie Chart | 比较,组成,层级 | 展示层级关系的占比数据 | Plotly |
| 环形图 | Donut Pie Chart | 比较,组成 | 展示单一维度的占比关系 | Matplotlib |
| 双层环图 | Multilevel Donut Chart | 比较,组成,层级 | 展示两个相关维度的占比关系 | Plotly |
| 旭日图 | Sunburst Chart | 组成,层级 | 展示多层级结构的数据占比 | Plotly |

## 7. 雷达图系列 (Radar Charts)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 基础雷达图 | Single Radar Chart | 比较 | 多维度指标的综合评估分析 | Plotly |
| 分组雷达图 | Grouped Radar Chart | 比较 | 多个对象在相同维度下的对比分析 | Plotly |
| 堆叠雷达图 | Stacked Radar Chart | 比较,组成 | 展示各维度的构成要素及贡献度 | Plotly |

## 8. 玫瑰图系列 (Rose Charts)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 基础玫瑰图 | Single Rose Chart | 比较 | 展示周期性数据、环形数据分布 | Matplotlib |
| 分组玫瑰图 | Grouped Rose Chart | 比较 | 展示分组属性的周期性数据 | Matplotlib |
| 堆叠玫瑰图 | Stacked Rose Chart | 比较,组成 | 展示层次关系的周期性数据 | Matplotlib |

## 9. 散点图系列 (Scatter Charts)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 基础散点图 | Scatter Plot | 分布 | 分析两个连续变量之间的相关性 | Matplotlib |
| 气泡图 | Bubble Plot | 分布 | 同时展示三个数值变量的关系 | Plotly |
| 象限图 | Quadrant Plot | 分布 | 战略分析、产品组合评估 | Plotly |
| 分类散点图 | stripplot | 比较,分布 | 展示各类别下数据分布情况 | Matplotlib |
| 成簇散点图 | swarmplot | 比较,分布 | 观察各类别中数据点的密度分布 | Matplotlib |
| 小提琴图 | Violin Plot | 比较,分布 | 展示数据分布的概率密度 | Matplotlib |

## 10. 热力图系列 (Heatmaps)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 基础热力图 | Heatmap Plot | 分布 | 展示二维数据关系强度、相关性分析 | Matplotlib |
| 日历图 | Calendar Heatmap | 分布,趋势 | 展示按日期统计的数据变化趋势 | Matplotlib |

## 11. 其他图表 (Other Charts)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 华夫图 | Waffle Chart | 组成 | 展示百分比数据或计数数据 | Matplotlib |
| 仪表盘图 | Gauge graph | 比较 | 展示单个指标在范围内的表现程度 | Plotly |
| 半圆环进度图 | Semi-circular Progress Chart | 比较 | 展示任务完成度、目标达成率 | Matplotlib |
| 条形进度图 | Bar Progress Chart | 比较 | 展示项目进度、目标达成率 | Plotly |
| 圆环进度图 | Circular Progress Chart | 比较 | 展示任务完成进度、资源使用占比 | Matplotlib |

## 12. 组合图系列 (Combination Charts)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 折线-柱状图 | Line-Column Combination Chart | 比较,分布,趋势 | 对比分析两种不同量级的数据变化 | Plotly |
| 折线-面积图 | Line-Area Combination Chart | 比较,分布,趋势 | 展示趋势同时强调数值体量 | Plotly |
| 双Y轴折线图 | Dual Y-Axis Line Chart | 比较,趋势 | 比较不同量级指标的变化趋势 | Plotly |
| 双Y轴柱状图 | Dual Y-Axis Bar Chart | 比较,分布 | 展示两组不同量级或单位的数据 | Plotly |

## 13. 多子图系列 (Multiple Subplots)

| 中文名称 | 英文名称 | 可视化目的 | 适用场景 | 渲染库 |
|---------|---------|-----------|---------|-------|
| 多子图柱状图 | Multiple Subplot Bar Chart | 比较,分布 | 同一页面展示多个相关数据对比 | Plotly |
| 多子图面积图 | Multiple Subplot Area Chart | 比较,趋势 | 对比多个指标的面积趋势变化 | Plotly |
| 多子图折线图 | Multiple Subplot Line Chart | 比较,趋势 | 对比多个相关时间序列数据 | Plotly |
| 多子图饼图 | Multiple Subplot Pie Chart | 比较,组成 | 对比多个相关的占比分布 | Plotly |

---

## 图表选择指南

### 按目的选择

| 可视化目的 | 推荐图表类型 |
|-----------|-------------|
| **比较** | 条形图、雷达图、玫瑰图、子弹图 |
| **趋势** | 折线图、面积图、阶梯线图 |
| **分布** | 直方图、箱线图、散点图、热力图 |
| **组成** | 饼图、堆叠图、华夫图、旭日图 |
| **层级** | 旭日图、嵌套饼图、双层环图 |
| **流向** | 瀑布图、河流图、漏斗图 |

### 按数据类型选择

| 数据类型 | 推荐图表类型 |
|---------|-------------|
| **时间序列** | 折线图、面积图、日历图 |
| **分类对比** | 条形图、棒棒糖图、雷达图 |
| **占比关系** | 饼图、环形图、华夫图 |
| **相关分析** | 散点图、气泡图、热力图 |
| **分布分析** | 直方图、箱线图、小提琴图 |
| **进度展示** | 仪表盘、进度图、子弹图 |
| **金融数据** | 蜡烛图、瀑布图 |

### 按数据量选择

| 数据量 | 推荐图表类型 |
|-------|-------------|
| **少量类别 (<8)** | 饼图、环形图、基础条形图 |
| **中等类别 (8-20)** | 分组条形图、多列折线图 |
| **大量数据** | 热力图、密度图、散点图 |
