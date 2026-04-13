import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    # Create sample data
    years = range(2019, 2024)
    
    # Generate realistic market share percentages
    apple = [20, 22, 24, 25, 27]
    samsung = [30, 29, 28, 27, 26] 
    xiaomi = [10, 12, 15, 17, 18]
    others = [40, 37, 33, 31, 29]
    
    # Create dataframe
    df = pd.DataFrame({
        'Year': years,
        'Apple': apple,
        'Samsung': samsung,
        'Xiaomi': xiaomi,
        'Others': others
    })
    
    # Save to CSV
    df.to_csv('堆叠折线图.csv', index=False)
    return df

def plot(data):
    # Create figure
    fig = go.Figure()
    
    # Add traces
    manufacturers = ['Apple', 'Samsung', 'Xiaomi', 'Others']
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96C7C1']
    
    for manufacturer, color in zip(manufacturers, colors):
        fig.add_trace(go.Scatter(
            x=data['Year'],
            y=data[manufacturer],
            name=manufacturer,
            mode='lines',
            stackgroup='one',
            line=dict(width=2, color=color),
            hovertemplate='%{y}%<extra></extra>'
        ))
    
    # Update layout
    fig.update_layout(
        title='Global Smartphone Market Share (2019-2023)',
        xaxis_title='Year',
        yaxis_title='Market Share (%)',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        plot_bgcolor='white',
        yaxis=dict(
            gridcolor='lightgray',
            range=[0,100]
        )
    )
    
    # Save
    fig.write_image("堆叠折线图.png")
    fig.write_html("data.html")
    return fig


def plot_1(data):
    # 商务风格，深色主题
    fig = go.Figure()
    manufacturers = ['Apple', 'Samsung', 'Xiaomi', 'Others']
    colors = ['#2C3E50', '#E74C3C', '#3498DB', '#95A5A6']
    
    for manufacturer, color in zip(manufacturers, colors):
        fig.add_trace(go.Scatter(
            x=data['Year'],
            y=data[manufacturer],
            name=manufacturer,
            mode='lines',
            stackgroup='one',
            line=dict(width=1.5, color=color),
            hovertemplate='%{y}%<extra></extra>'
        ))
    
    fig.update_layout(
        title='Global Smartphone Market Share (2019-2023)',
        paper_bgcolor='#1a1a1a',
        plot_bgcolor='#1a1a1a',
        font=dict(color='white'),
        xaxis=dict(showgrid=False, gridcolor='#333333'),
        yaxis=dict(showgrid=True, gridcolor='#333333', range=[0,100]),
        legend=dict(
            bgcolor='rgba(0,0,0,0)',
            bordercolor='rgba(0,0,0,0)',
            x=0.01,
            y=0.99
        )
    )
    
    fig.write_image("堆叠折线图_style_1.png")
    return fig

def plot_2(data):
    # 极简风格
    fig = go.Figure()
    manufacturers = ['Apple', 'Samsung', 'Xiaomi', 'Others']
    colors = ['#000000', '#404040', '#808080', '#c0c0c0']
    
    for manufacturer, color in zip(manufacturers, colors):
        fig.add_trace(go.Scatter(
            x=data['Year'],
            y=data[manufacturer],
            name=manufacturer,
            mode='lines',
            stackgroup='one',
            line=dict(width=0.8, color=color),
            hovertemplate='%{y}%<extra></extra>'
        ))
    
    fig.update_layout(
        title=None,
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False, range=[0,100]),
        legend=dict(
            x=1.02,
            y=1,
            bordercolor='white'
        ),
        margin=dict(t=30)
    )
    
    fig.write_image("堆叠折线图_style_2.png")
    return fig

def plot_3(data):
    # 活泼风格，渐变色
    fig = go.Figure()
    manufacturers = ['Apple', 'Samsung', 'Xiaomi', 'Others']
    colors = ['#FF6B6B', '#4ECDC4', '#FFE66D', '#6C5B7B']
    
    for manufacturer, color in zip(manufacturers, colors):
        fig.add_trace(go.Scatter(
            x=data['Year'],
            y=data[manufacturer],
            name=manufacturer,
            mode='lines+markers',
            stackgroup='one',
            line=dict(width=2, color=color),
            marker=dict(size=8, symbol='circle'),
            hovertemplate='%{y}%<extra></extra>'
        ))
    
    fig.update_layout(
        title='Smartphone Market Share Trends',
        plot_bgcolor='rgba(245,245,245,1)',
        paper_bgcolor='white',
        font=dict(family="Arial", size=12),
        xaxis=dict(showgrid=True, gridcolor='white', gridwidth=2),
        yaxis=dict(showgrid=True, gridcolor='white', gridwidth=2, range=[0,100]),
        legend=dict(
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='white',
            borderwidth=1
        )
    )
    
    fig.write_image("堆叠折线图_style_3.png")
    return fig

def plot_4(data):
    # 科技风格
    fig = go.Figure()
    manufacturers = ['Apple', 'Samsung', 'Xiaomi', 'Others']
    colors = ['#00ff00', '#00ffff', '#ff00ff', '#ffff00']
    
    for manufacturer, color in zip(manufacturers, colors):
        fig.add_trace(go.Scatter(
            x=data['Year'],
            y=data[manufacturer],
            name=manufacturer,
            mode='lines',
            stackgroup='one',
            line=dict(width=2, color=color),
            hovertemplate='%{y}%<extra></extra>'
        ))
    
    fig.update_layout(
        title='Market Share Analysis',
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='#00ff00', family='Courier New'),
        xaxis=dict(showgrid=True, gridcolor='#333333', color='#00ff00'),
        yaxis=dict(showgrid=True, gridcolor='#333333', color='#00ff00', range=[0,100]),
        legend=dict(
            font=dict(color='#00ff00'),
            bgcolor='rgba(0,0,0,0.5)'
        )
    )
    
    fig.write_image("堆叠折线图_style_4.png")
    return fig

def plot_5(data):
    # 复古风格
    fig = go.Figure()
    manufacturers = ['Apple', 'Samsung', 'Xiaomi', 'Others']
    colors = ['#8B4513', '#A0522D', '#CD853F', '#DEB887']
    
    for manufacturer, color in zip(manufacturers, colors):
        fig.add_trace(go.Scatter(
            x=data['Year'],
            y=data[manufacturer],
            name=manufacturer,
            mode='lines',
            stackgroup='one',
            line=dict(width=1.5, color=color, dash='dot'),
            hovertemplate='%{y}%<extra></extra>'
        ))
    
    fig.update_layout(
        title='Historical Market Share Overview',
        plot_bgcolor='#FFF8DC',
        paper_bgcolor='#FFF8DC',
        font=dict(family='Times New Roman', color='#8B4513'),
        xaxis=dict(showgrid=True, gridcolor='#DEB887'),
        yaxis=dict(showgrid=True, gridcolor='#DEB887', range=[0,100]),
        legend=dict(
            bgcolor='#FFF8DC',
            bordercolor='#8B4513'
        )
    )
    
    fig.write_image("堆叠折线图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
