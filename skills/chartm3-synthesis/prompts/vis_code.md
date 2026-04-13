# 可视化代码生成 Prompt

## 用途

根据可视化方案和样例代码，生成符合要求的可视化代码。

## Prompt 模板

```
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
```

## 样式选项

### 默认样式
```
图表中所有文本内容（标题、图例、坐标轴标签等）请全部使用英文。
```

### 无标注样式（用于特定任务）
```
所有文本内容请全部使用英文。【注意，与样例不同，本次生成的图表不要添加任何caption文字，包括标题、图中文本、标注数字等！请在生成代码时不要添加相关语句！】
```

## 代码结构要求

生成的代码必须包含两个函数：

```python
def preprocess(data):
    """
    数据预处理函数
    
    Args:
        data: 原始 pandas DataFrame
    
    Returns:
        处理后的 DataFrame
    """
    # 数据预处理逻辑
    processed_data = data.copy()
    # ...
    return processed_data


def plot(data):
    """
    绑图函数
    
    Args:
        data: 原始 pandas DataFrame
    """
    # 调用预处理
    processed_data = preprocess(data)
    
    # 绑图逻辑
    # ...
    
    # 保存图片
    plt.savefig('plot.png')
    plt.close()
```

## 执行说明

1. 生成的代码只包含函数定义，不包含 import 语句和 main 块
2. 系统会自动拼接必要的 import 语句和调用代码
3. 执行失败时会使用 code_fix.md 进行修复

## 样例代码来源

样例代码存储在 Skill 的 `./reference/templates/` 目录下，每种图表类型对应一个 Python 文件：

| 图表类型 | 样例文件 |
|---------|----------|
| 基础折线图 | `基础折线图_multi.py` |
| 基础条形图 | `基础条形图_multi.py` |
| 蚯蝴图 | `蚯蝴图_multi1.py` |
| 不等宽直方图 | `不等宽直方图_multi1.py` |
| ... | ... |

**使用方式**:
1. 根据目标图表类型，读取对应的 `*_multi*.py` 文件
2. 提取其中的 `plot()` 函数作为 `{sample_code}` 参数
3. 提取对应的 `.csv` 文件作为 `{sample_data_head}` 参数

**样例文件结构**:
```python
# 每个样例文件包含：
def preprocess(data):    # 数据预处理
    ...

def plot(data):          # 基础绘图函数（作为样例使用）
    ...

def plot_1(data):        # 风格变体 1：商务蓝
    ...

def plot_2(data):        # 风格变体 2：活泼彩虹
    ...
# ... plot_3 ~ plot_5 更多风格
```
