# 代码修复 Prompt

## 用途

当生成的代码执行失败时，根据错误信息修复代码。

## Prompt 模板

```
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
```

## 常见错误及修复策略

### 1. KeyError / 列名错误
- 检查 data.columns 中的实际列名
- 修正代码中引用的列名

### 2. ValueError / 数据类型错误
- 添加适当的类型转换
- 检查数据预处理逻辑

### 3. matplotlib 样式错误
- 使用正确的样式名称：`seaborn-v0_8-*`
- 检查样式名称拼写

### 4. 文件保存路径错误
- 确保使用 `plot.png` 作为文件名
- 不要自定义输出目录

### 5. 语法错误
- 检查缩进
- 检查括号匹配
- 检查字符串引号

## 重要约束

**绝对禁止**:
- 不要输出 `if __name__ == "__main__":` 块
- 不要输出 import 语句
- 不要自定义保存路径

**必须包含**:
- `def preprocess(data):` 函数
- `def plot(data):` 函数
- 图片保存语句 `plt.savefig('plot.png')` 或 `fig.write_image('plot.png')`

## 重试机制

- 最多重试 5 次
- 每次重试都会传入最新的错误信息
- 如果 5 次后仍然失败，标记为生成失败
