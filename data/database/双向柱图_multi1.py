import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    """生成双向柱状图所需的演示数据"""
    # 定义年龄段
    age_groups = ['<20', '20-30', '30-40', '40-50', '50-60', '>60']
    
    # 生成模拟数据
    np.random.seed(42)
    positive = np.random.normal(loc=500, scale=100, size=len(age_groups)).astype(int)
    negative = -np.random.normal(loc=300, scale=80, size=len(age_groups)).astype(int)
    
    # 创建DataFrame
    df = pd.DataFrame({
        'age_group': age_groups,
        'positive': positive,
        'negative': negative
    })
    
    # 保存数据
    df.to_csv('双向柱图.csv', index=False)
    return df

def plot(data, 
         title='Age Group Product Reviews Distribution',
         color_positive='#2ecc71',
         color_negative='#e74c3c',
         opacity=0.8,
         fig_width=900,
         fig_height=500):
    """绘制双向柱状图"""
    
    # 创建图形对象
    fig = go.Figure()
    
    # 添加正向柱形
    fig.add_trace(go.Bar(
        name='Positive Reviews',
        x=data['age_group'],
        y=data['positive'],
        marker_color=color_positive,
        opacity=opacity
    ))
    
    # 添加负向柱形
    fig.add_trace(go.Bar(
        name='Negative Reviews',
        x=data['age_group'],
        y=data['negative'],
        marker_color=color_negative,
        opacity=opacity
    ))
    
    # 更新布局
    fig.update_layout(
        title={
            'text': title,
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title='Age Groups',
        yaxis_title='Number of Reviews',
        barmode='relative',
        width=fig_width,
        height=fig_height,
        plot_bgcolor='white',
        
        # 添加网格线
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(0,0,0,0.1)',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='rgba(0,0,0,0.3)'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(0,0,0,0.1)',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='rgba(0,0,0,0.3)'
        )
    )
    
    # 添加数值标签
    annotations = []
    for trace_data in [data['positive'], data['negative']]:
        for i, value in enumerate(trace_data):
            annotations.append(dict(
                x=data['age_group'][i],
                y=value,
                text=str(abs(value)),
                font=dict(size=10),
                showarrow=False,
                yshift=10 if value > 0 else -20
            ))
    
    fig.update_layout(annotations=annotations)
    
    # 保存图表
    fig.write_image("双向柱图.png")
    return fig


def plot_1(data, title='Age Group Product Reviews - Business Style'):
    """商务专业风格"""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Positive Reviews',
        x=data['age_group'],
        y=data['positive'],
        marker_color='#1f77b4',
        opacity=0.9,
        marker_line_width=1,
        marker_line_color='#1f77b4'
    ))
    
    fig.add_trace(go.Bar(
        name='Negative Reviews',
        x=data['age_group'],
        y=data['negative'],
        marker_color='#ff7f0e',
        opacity=0.9,
        marker_line_width=1,
        marker_line_color='#ff7f0e'
    ))
    
    fig.update_layout(
        title={
            'text': title,
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Arial Bold')
        },
        xaxis_title='Age Groups',
        yaxis_title='Number of Reviews',
        barmode='relative',
        width=900,
        height=500,
        plot_bgcolor='white',
        font=dict(family='Arial'),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(0,0,0,0.1)',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='rgba(0,0,0,0.3)'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(0,0,0,0.1)',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='rgba(0,0,0,0.3)'
        )
    )
    
    fig.write_image("双向柱图_style_1.png")
    return fig

def plot_2(data, title='Age Group Product Reviews - Modern Style'):
    """现代科技风格"""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Positive Reviews',
        x=data['age_group'],
        y=data['positive'],
        marker_color='#00ff88',
        opacity=0.8,
        marker_line_width=0
    ))
    
    fig.add_trace(go.Bar(
        name='Negative Reviews',
        x=data['age_group'],
        y=data['negative'],
        marker_color='#ff3366',
        opacity=0.8,
        marker_line_width=0
    ))
    
    fig.update_layout(
        title={
            'text': title,
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='white')
        },
        xaxis_title='Age Groups',
        yaxis_title='Number of Reviews',
        barmode='relative',
        width=900,
        height=500,
        plot_bgcolor='rgb(17,17,17)',
        paper_bgcolor='rgb(17,17,17)',
        font=dict(color='white'),
        showlegend=True,
        legend=dict(
            bgcolor='rgba(0,0,0,0)',
            bordercolor='rgba(0,0,0,0)'
        ),
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(255,255,255,0.1)',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='rgba(255,255,255,0.3)'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(255,255,255,0.1)',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='rgba(255,255,255,0.3)'
        )
    )
    
    fig.write_image("双向柱图_style_2.png")
    return fig

def plot_3(data, title='Age Group Product Reviews - Natural Style'):
    """自然环保风格"""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Positive Reviews',
        x=data['age_group'],
        y=data['positive'],
        marker_color='#7cb342',
        opacity=0.85,
        marker_line_width=1,
        marker_line_color='#558b2f'
    ))
    
    fig.add_trace(go.Bar(
        name='Negative Reviews',
        x=data['age_group'],
        y=data['negative'],
        marker_color='#ff8f00',
        opacity=0.85,
        marker_line_width=1,
        marker_line_color='#ef6c00'
    ))
    
    fig.update_layout(
        title={
            'text': title,
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Verdana', color='#2e7d32')
        },
        xaxis_title='Age Groups',
        yaxis_title='Number of Reviews',
        barmode='relative',
        width=900,
        height=500,
        plot_bgcolor='rgba(242,245,233,0.8)',
        paper_bgcolor='rgba(242,245,233,0.8)',
        font=dict(family='Verdana', color='#33691e'),
        showlegend=True,
        legend=dict(
            bgcolor='rgba(242,245,233,0.8)'
        ),
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(76,175,80,0.2)',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='rgba(76,175,80,0.5)'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(76,175,80,0.2)',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='rgba(76,175,80,0.5)'
        )
    )
    
    fig.write_image("双向柱图_style_3.png")
    return fig

def plot_4(data, title='Age Group Product Reviews - Minimalist Style'):
    """极简风格"""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Positive Reviews',
        x=data['age_group'],
        y=data['positive'],
        marker_color='#212121',
        opacity=0.9,
        marker_line_width=0
    ))
    
    fig.add_trace(go.Bar(
        name='Negative Reviews',
        x=data['age_group'],
        y=data['negative'],
        marker_color='#757575',
        opacity=0.9,
        marker_line_width=0
    ))
    
    fig.update_layout(
        title={
            'text': title,
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Helvetica Neue')
        },
        xaxis_title='Age Groups',
        yaxis_title='Number of Reviews',
        barmode='relative',
        width=900,
        height=500,
        plot_bgcolor='white',
        font=dict(family='Helvetica Neue'),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=True,
            zerolinewidth=1,
            zerolinecolor='black'
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=True,
            zerolinewidth=1,
            zerolinecolor='black'
        )
    )
    
    fig.write_image("双向柱图_style_4.png")
    return fig

def plot_5(data, title='Age Group Product Reviews - Pastel Style'):
    """柔和清新风格"""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Positive Reviews',
        x=data['age_group'],
        y=data['positive'],
        marker_color='#ffcdd2',
        opacity=0.9,
        marker_line_width=1,
        marker_line_color='#ef9a9a'
    ))
    
    fig.add_trace(go.Bar(
        name='Negative Reviews',
        x=data['age_group'],
        y=data['negative'],
        marker_color='#b2dfdb',
        opacity=0.9,
        marker_line_width=1,
        marker_line_color='#80cbc4'
    ))
    
    fig.update_layout(
        title={
            'text': title,
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Comic Sans MS', color='#f06292')
        },
        xaxis_title='Age Groups',
        yaxis_title='Number of Reviews',
        barmode='relative',
        width=900,
        height=500,
        plot_bgcolor='#fafafa',
        paper_bgcolor='#fafafa',
        font=dict(family='Comic Sans MS', color='#4db6ac'),
        showlegend=True,
        legend=dict(
            bgcolor='#fafafa'
        ),
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(189,189,189,0.2)',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='rgba(189,189,189,0.5)'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(189,189,189,0.2)',
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='rgba(189,189,189,0.5)'
        )
    )
    
    fig.write_image("双向柱图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
