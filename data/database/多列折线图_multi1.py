import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

def preprocess(data=None):
    # Generate 12 months of data
    dates = pd.date_range(start='2023-01-01', periods=12, freq='M')
    
    # Create synthetic data for 3 product categories
    np.random.seed(42)
    base = np.linspace(100, 150, 12)  # Underlying trend
    seasonal = 20 * np.sin(np.linspace(0, 2*np.pi, 12))  # Seasonal pattern
    
    products = {
        'Electronics': base + seasonal + np.random.normal(0, 5, 12),
        'Clothing': base*0.7 + seasonal + np.random.normal(0, 4, 12),
        'Home Goods': base*0.5 + seasonal + np.random.normal(0, 3, 12)
    }
    
    # Create DataFrame
    df = pd.DataFrame(products, index=dates)
    df.index.name = 'Date'
    
    # Save to CSV
    df.to_csv('多列折线图.csv')
    return df

def plot(data):
    # Create figure
    fig = go.Figure()
    
    colors = ['#1f77b4', '#2ca02c', '#ff7f0e']  # Professional color scheme
    
    # Add traces for each product
    for i, col in enumerate(data.columns):
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data[col],
                name=col,
                line=dict(color=colors[i], width=2),
                mode='lines+markers',
                marker=dict(size=8)
            )
        )
    
    # Update layout
    fig.update_layout(
        title='Monthly Sales by Product Category',
        xaxis_title='Month',
        yaxis_title='Sales (thousands $)',
        template='plotly_white',
        hovermode='x unified',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )
    
    # Add gridlines
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    
    # Save as png
    fig.write_image("多列折线图.png")
    return fig

# Generate and plot data
data = preprocess()
fig = plot(data)

def plot_1(data):
    # 商务简约风格
    fig = go.Figure()
    colors = ['#2C3E50', '#34495E', '#587498']  # 深蓝色系
    
    for i, col in enumerate(data.columns):
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data[col],
                name=col,
                line=dict(color=colors[i], width=1.5),
                mode='lines',
            )
        )
    
    fig.update_layout(
        title='Sales Trends Analysis',
        template='plotly_white',
        font=dict(family='Arial', size=12),
        showlegend=True,
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        margin=dict(l=40, r=40, t=60, b=40),
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#E5E5E5')
    
    fig.write_image("多列折线图_style_1.png")
    return fig

def plot_2(data):
    # 科技感风格
    fig = go.Figure()
    colors = ['#00BCD4', '#03A9F4', '#3F51B5']  # Material Design色板
    
    for i, col in enumerate(data.columns):
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data[col],
                name=col,
                line=dict(color=colors[i], width=2),
                mode='lines+markers',
                marker=dict(size=8, symbol='diamond')
            )
        )
    
    fig.update_layout(
        title='Sales Performance Dashboard',
        template='plotly_dark',
        paper_bgcolor='rgb(17,17,17)',
        plot_bgcolor='rgb(17,17,17)',
        font=dict(color='white'),
        legend=dict(
            bgcolor='rgba(0,0,0,0.5)',
            bordercolor='rgba(255,255,255,0.2)',
            borderwidth=1
        )
    )
    
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)', zeroline=False)
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.1)', zeroline=False)
    
    fig.write_image("多列折线图_style_2.png")
    return fig

def plot_3(data):
    # 柔和渐变风格
    fig = go.Figure()
    colors = ['#FF9AA2', '#FFB7B2', '#FFDAC1']  # 柔和色系
    
    for i, col in enumerate(data.columns):
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data[col],
                name=col,
                line=dict(color=colors[i], width=3),
                mode='lines',
                fill='tonexty',
                fillcolor=f'rgba{tuple(list(px.colors.hex_to_rgb(colors[i])) + [0.1])}',
            )
        )
    
    fig.update_layout(
        title='Monthly Sales Overview',
        template='simple_white',
        font=dict(family='Helvetica'),
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        )
    )
    
    fig.write_image("多列折线图_style_3.png")
    return fig

def plot_4(data):
    # 极简黑白风格
    fig = go.Figure()
    colors = ['#000000', '#404040', '#808080']  # 黑白灰
    
    for i, col in enumerate(data.columns):
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data[col],
                name=col,
                line=dict(color=colors[i], width=1, dash=['solid', 'dash', 'dot'][i]),
                mode='lines+markers',
                marker=dict(size=6, symbol=['circle', 'square', 'triangle-up'][i])
            )
        )
    
    fig.update_layout(
        title=None,
        template='simple_white',
        font=dict(family='Helvetica', color='black'),
        showlegend=True,
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    
    fig.write_image("多列折线图_style_4.png")
    return fig

def plot_5(data):
    # 活泼明亮风格
    fig = go.Figure()
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']  # 明亮对比色
    
    for i, col in enumerate(data.columns):
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data[col],
                name=col,
                line=dict(color=colors[i], width=2.5),
                mode='lines+markers',
                marker=dict(
                    size=10,
                    symbol='circle',
                    line=dict(color='white', width=2)
                )
            )
        )
    
    fig.update_layout(
        title='Product Category Sales',
        template='plotly_white',
        font=dict(family='Roboto', size=12),
        showlegend=True,
        legend=dict(
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#CCCCCC',
            borderwidth=1
        ),
        plot_bgcolor='white'
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#F0F0F0')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#F0F0F0')
    
    fig.write_image("多列折线图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
