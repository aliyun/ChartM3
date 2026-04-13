import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    """
    生成或处理用于杠铃图的数据
    """
    # 生成示例数据
    countries = ['China', 'India', 'Brazil', 'Russia', 'South Africa', 'Indonesia', 'Mexico', 'Turkey']
    
    # 生成2010和2020年的GDP per capita数据(简化数值)
    np.random.seed(42)
    gdp_2010 = np.random.randint(1000, 5000, len(countries))
    growth_factors = np.random.uniform(1.2, 2.5, len(countries))
    gdp_2020 = (gdp_2010 * growth_factors).astype(int)
    
    # 创建DataFrame
    df = pd.DataFrame({
        'Country': countries,
        'GDP_2010': gdp_2010,
        'GDP_2020': gdp_2020
    })
    
    # 计算变化值用于排序
    df['Change'] = df['GDP_2020'] - df['GDP_2010']
    df = df.sort_values('Change', ascending=True)
    
    # 保存数据
    df.to_csv('杠铃图.csv', index=False)
    return df

def plot(data):
    """
    绘制杠铃图
    """
    # 创建图表
    fig = go.Figure()
    
    # 添加连接线
    fig.add_trace(go.Scatter(
        x=data['GDP_2010'],
        y=data['Country'],
        mode='markers+text',
        marker=dict(size=12, color='#1f77b4'),
        text=data['GDP_2010'],
        textposition='middle left',
        name='2010',
        hovertemplate='%{y}: $%{x:,.0f}<extra>2010</extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=data['GDP_2020'],
        y=data['Country'],
        mode='markers+text',
        marker=dict(size=12, color='#ff7f0e'),
        text=data['GDP_2020'],
        textposition='middle right',
        name='2020',
        hovertemplate='%{y}: $%{x:,.0f}<extra>2020</extra>'
    ))
    
    # 添加连接线
    for i in range(len(data)):
        fig.add_shape(
            type='line',
            x0=data['GDP_2010'].iloc[i],
            y0=data['Country'].iloc[i],
            x1=data['GDP_2020'].iloc[i],
            y1=data['Country'].iloc[i],
            line=dict(color='#dedede', width=2)
        )
    
    # 更新布局
    fig.update_layout(
        title=dict(
            text='GDP per Capita Change (2010-2020)',
            x=0.5,
            font=dict(size=20)
        ),
        xaxis=dict(
            title='GDP per Capita (USD)',
            showgrid=True,
            gridwidth=1,
            gridcolor='#f0f0f0',
            zeroline=False
        ),
        yaxis=dict(
            title='Country',
            showgrid=False,
            zeroline=False
        ),
        plot_bgcolor='white',
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        margin=dict(l=100, r=50, t=80, b=50),
        height=500
    )
    
    # 保存图表
    fig.write_image("杠铃图.png")
    return fig


def plot_1(data):
    """商务风格：深蓝配色方案"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['GDP_2010'],
        y=data['Country'],
        mode='markers+text',
        marker=dict(size=10, color='#1f3d7a'),
        text=data['GDP_2010'],
        textposition='middle left',
        name='2010',
        hovertemplate='%{y}: $%{x:,.0f}<extra>2010</extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=data['GDP_2020'],
        y=data['Country'],
        mode='markers+text',
        marker=dict(size=10, color='#3c78d8'),
        text=data['GDP_2020'],
        textposition='middle right',
        name='2020',
        hovertemplate='%{y}: $%{x:,.0f}<extra>2020</extra>'
    ))
    
    for i in range(len(data)):
        fig.add_shape(
            type='line',
            x0=data['GDP_2010'].iloc[i],
            y0=data['Country'].iloc[i],
            x1=data['GDP_2020'].iloc[i],
            y1=data['Country'].iloc[i],
            line=dict(color='#c9daf8', width=1.5)
        )
    
    fig.update_layout(
        title=dict(
            text='GDP per Capita Change (2010-2020)',
            x=0.5,
            font=dict(size=20, color='#1f3d7a')
        ),
        xaxis=dict(
            title='GDP per Capita (USD)',
            showgrid=True,
            gridwidth=1,
            gridcolor='#f0f0f0',
            zeroline=False
        ),
        yaxis=dict(
            title='Country',
            showgrid=False,
            zeroline=False
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        margin=dict(l=100, r=50, t=80, b=50),
        height=500,
        font=dict(family='Arial')
    )
    
    fig.write_image("杠铃图_style_1.png")
    return fig

def plot_2(data):
    """极简风格：灰度方案"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['GDP_2010'],
        y=data['Country'],
        mode='markers+text',
        marker=dict(size=8, color='#404040', symbol='square'),
        text=data['GDP_2010'],
        textposition='middle left',
        name='2010',
        hovertemplate='%{y}: $%{x:,.0f}<extra>2010</extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=data['GDP_2020'],
        y=data['Country'],
        mode='markers+text',
        marker=dict(size=8, color='#808080', symbol='square'),
        text=data['GDP_2020'],
        textposition='middle right',
        name='2020',
        hovertemplate='%{y}: $%{x:,.0f}<extra>2020</extra>'
    ))
    
    for i in range(len(data)):
        fig.add_shape(
            type='line',
            x0=data['GDP_2010'].iloc[i],
            y0=data['Country'].iloc[i],
            x1=data['GDP_2020'].iloc[i],
            y1=data['Country'].iloc[i],
            line=dict(color='#e0e0e0', width=1, dash='dash')
        )
    
    fig.update_layout(
        title=dict(
            text='GDP per Capita Change (2010-2020)',
            x=0.5,
            font=dict(size=16, color='#404040')
        ),
        xaxis=dict(
            title='GDP per Capita (USD)',
            showgrid=False,
            zeroline=False
        ),
        yaxis=dict(
            title='Country',
            showgrid=False,
            zeroline=False
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        margin=dict(l=100, r=50, t=80, b=50),
        height=500,
        font=dict(family='Helvetica')
    )
    
    fig.write_image("杠铃图_style_2.png")
    return fig

def plot_3(data):
    """科技风格：深色背景"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['GDP_2010'],
        y=data['Country'],
        mode='markers+text',
        marker=dict(size=12, color='#00ff00', symbol='diamond'),
        text=data['GDP_2010'],
        textposition='middle left',
        textfont=dict(color='white'),
        name='2010',
        hovertemplate='%{y}: $%{x:,.0f}<extra>2010</extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=data['GDP_2020'],
        y=data['Country'],
        mode='markers+text',
        marker=dict(size=12, color='#00ffff', symbol='diamond'),
        text=data['GDP_2020'],
        textposition='middle right',
        textfont=dict(color='white'),
        name='2020',
        hovertemplate='%{y}: $%{x:,.0f}<extra>2020</extra>'
    ))
    
    for i in range(len(data)):
        fig.add_shape(
            type='line',
            x0=data['GDP_2010'].iloc[i],
            y0=data['Country'].iloc[i],
            x1=data['GDP_2020'].iloc[i],
            y1=data['Country'].iloc[i],
            line=dict(color='rgba(0, 255, 0, 0.3)', width=2)
        )
    
    fig.update_layout(
        title=dict(
            text='GDP per Capita Change (2010-2020)',
            x=0.5,
            font=dict(size=20, color='white')
        ),
        xaxis=dict(
            title='GDP per Capita (USD)',
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(255, 255, 255, 0.1)',
            zeroline=False,
            color='white'
        ),
        yaxis=dict(
            title='Country',
            showgrid=False,
            zeroline=False,
            color='white'
        ),
        plot_bgcolor='rgb(17, 17, 17)',
        paper_bgcolor='rgb(17, 17, 17)',
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1,
            font=dict(color='white')
        ),
        margin=dict(l=100, r=50, t=80, b=50),
        height=500,
        font=dict(color='white')
    )
    
    fig.write_image("杠铃图_style_3.png")
    return fig

def plot_4(data):
    """活泼风格：渐变彩虹色"""
    fig = go.Figure()
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD', '#D4A5A5', '#9B59B6', '#3498DB']
    
    fig.add_trace(go.Scatter(
        x=data['GDP_2010'],
        y=data['Country'],
        mode='markers+text',
        marker=dict(size=15, color=colors, line=dict(color='white', width=2)),
        text=data['GDP_2010'],
        textposition='middle left',
        name='2010',
        hovertemplate='%{y}: $%{x:,.0f}<extra>2010</extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=data['GDP_2020'],
        y=data['Country'],
        mode='markers+text',
        marker=dict(size=15, color=colors, line=dict(color='white', width=2)),
        text=data['GDP_2020'],
        textposition='middle right',
        name='2020',
        hovertemplate='%{y}: $%{x:,.0f}<extra>2020</extra>'
    ))
    
    for i in range(len(data)):
        fig.add_shape(
            type='line',
            x0=data['GDP_2010'].iloc[i],
            y0=data['Country'].iloc[i],
            x1=data['GDP_2020'].iloc[i],
            y1=data['Country'].iloc[i],
            line=dict(color=colors[i], width=3)
        )
    
    fig.update_layout(
        title=dict(
            text='GDP per Capita Change (2010-2020)',
            x=0.5,
            font=dict(size=24, family='Comic Sans MS')
        ),
        xaxis=dict(
            title='GDP per Capita (USD)',
            showgrid=True,
            gridwidth=1,
            gridcolor='#f0f0f0',
            zeroline=False
        ),
        yaxis=dict(
            title='Country',
            showgrid=False,
            zeroline=False
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        margin=dict(l=100, r=50, t=80, b=50),
        height=500
    )
    
    fig.write_image("杠铃图_style_4.png")
    return fig

def plot_5(data):
    """渐变风格：单色渐变"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['GDP_2010'],
        y=data['Country'],
        mode='markers+text',
        marker=dict(
            size=12,
            color=data['GDP_2010'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title='GDP Value')
        ),
        text=data['GDP_2010'],
        textposition='middle left',
        name='2010',
        hovertemplate='%{y}: $%{x:,.0f}<extra>2010</extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=data['GDP_2020'],
        y=data['Country'],
        mode='markers+text',
        marker=dict(
            size=12,
            color=data['GDP_2020'],
            colorscale='Viridis',
            showscale=False
        ),
        text=data['GDP_2020'],
        textposition='middle right',
        name='2020',
        hovertemplate='%{y}: $%{x:,.0f}<extra>2020</extra>'
    ))
    
    for i in range(len(data)):
        fig.add_shape(
            type='line',
            x0=data['GDP_2010'].iloc[i],
            y0=data['Country'].iloc[i],
            x1=data['GDP_2020'].iloc[i],
            y1=data['Country'].iloc[i],
            line=dict(
                color='rgba(0,0,0,0.2)',
                width=2
            )
        )
    
    fig.update_layout(
        title=dict(
            text='GDP per Capita Change (2010-2020)',
            x=0.5,
            font=dict(size=20)
        ),
        xaxis=dict(
            title='GDP per Capita (USD)',
            showgrid=True,
            gridwidth=1,
            gridcolor='#f0f0f0',
            zeroline=False
        ),
        yaxis=dict(
            title='Country',
            showgrid=False,
            zeroline=False
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        margin=dict(l=100, r=50, t=80, b=50),
        height=500
    )
    
    fig.write_image("杠铃图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
