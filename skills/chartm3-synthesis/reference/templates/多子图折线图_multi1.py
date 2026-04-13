import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import random

def preprocess(data=None):
    # Generate sample quarterly economic data
    dates = pd.date_range(start='2020-01-01', end='2022-12-31', freq='Q')
    
    # Create base trends with some random variation
    np.random.seed(42)
    gdp_growth = [3.5 + random.uniform(-0.5, 0.5) for _ in range(len(dates))]
    unemployment = [5.0 + np.cumsum(np.random.normal(0, 0.3, len(dates)))]
    inflation = [2.0 + np.cumsum(np.random.normal(0, 0.2, len(dates)))]
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'GDP_Growth': np.round(gdp_growth, 2),
        'Unemployment_Rate': np.round(unemployment[0], 2),
        'Inflation_Rate': np.round(inflation[0], 2)
    })
    
    # Save to CSV
    df.to_csv('多子图折线图.csv', index=False)
    return df

def plot(data=None):
    # Read data if not provided
    if data is None:
        data = pd.read_csv('多子图折线图.csv')
        data['Date'] = pd.to_datetime(data['Date'])
    
    # Create figure with subplots
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=('GDP Growth Rate (%)', 'Unemployment Rate (%)', 'Inflation Rate (%)'),
        vertical_spacing=0.12
    )
    
    # Add traces for each metric
    metrics = ['GDP_Growth', 'Unemployment_Rate', 'Inflation_Rate']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Blue, Orange, Green
    
    for i, (metric, color) in enumerate(zip(metrics, colors), 1):
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[metric],
                name=metric.replace('_', ' '),
                line=dict(color=color, width=2),
                hovertemplate=(
                    '%{x|%Q-%Y}<br>' +
                    metric.replace('_', ' ') + ': %{y:.2f}%<br>' +
                    '<extra></extra>'
                )
            ),
            row=i, col=1
        )

        # Add text annotations
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[metric],
                mode='text',
                text=[f'{val:.2f}%' for val in data[metric]],
                textposition='top center',
                textfont=dict(
                    size=10,
                    color=color
                ),
                showlegend=False,
                hoverinfo='skip'
            ),
            row=i, col=1
        )
    
        # Update layout
    fig.update_layout(
        height=800,
        width=1000,
        showlegend=True,
        title_text="Economic Indicators Over Time",
        title_x=0.5,
        title_font_size=20,
        legend=dict(
            yanchor="top",
            y=1.1,
            xanchor="center",
            x=0.5,
            orientation="h"
        ),
        hovermode='x unified',
        template='plotly_white'
    )

    # Update axes
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='LightGray',
        zeroline=False,
        dtick="M3"  # Show tick every 3 months
    )

    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='LightGray',
        zeroline=False,
        ticksuffix='%'
    )

    # Save figure
    fig.write_image("多子图折线图.png", scale=2)
    return fig


def plot_1(data=None):
    # 商务风格：单色系蓝色渐变
    if data is None:
        data = pd.read_csv('data.csv')
        data['Date'] = pd.to_datetime(data['Date'])
    
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=('GDP Growth Rate (%)', 'Unemployment Rate (%)', 'Inflation Rate (%)'),
        vertical_spacing=0.12
    )
    
    metrics = ['GDP_Growth', 'Unemployment_Rate', 'Inflation_Rate']
    colors = ['#1f77b4', '#4c96c9', '#7ab5de']  # 蓝色渐变
    
    for i, (metric, color) in enumerate(zip(metrics, colors), 1):
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[metric],
                name=metric.replace('_', ' '),
                line=dict(color=color, width=1.5),
                mode='lines+markers',
                marker=dict(size=6),
                hovertemplate='%{x|%Q-%Y}<br>' + metric.replace('_', ' ') + ': %{y:.2f}%<br><extra></extra>'
            ),
            row=i, col=1
        )
    
    fig.update_layout(
        height=800, width=1000,
        title_text="Economic Indicators Analysis",
        title_x=0.5,
        title_font=dict(size=24, color='#2f3640'),
        plot_bgcolor='white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
        template='none'
    )

    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='#f1f2f6')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#f1f2f6')

    fig.write_image("多子图折线图_style_1.png", scale=2)
    return fig

def plot_2(data=None):
    # 科技风格：深色背景+霓虹效果
    if data is None:
        data = pd.read_csv('data.csv')
        data['Date'] = pd.to_datetime(data['Date'])
    
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=('GDP Growth Rate (%)', 'Unemployment Rate (%)', 'Inflation Rate (%)'),
        vertical_spacing=0.12
    )
    
    metrics = ['GDP_Growth', 'Unemployment_Rate', 'Inflation_Rate']
    colors = ['#00ff00', '#ff00ff', '#00ffff']  # 霓虹色
    
    for i, (metric, color) in enumerate(zip(metrics, colors), 1):
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[metric],
                name=metric.replace('_', ' '),
                line=dict(color=color, width=2),
                mode='lines',
                hovertemplate='%{x|%Q-%Y}<br>' + metric.replace('_', ' ') + ': %{y:.2f}%<br><extra></extra>'
            ),
            row=i, col=1
        )
    
    fig.update_layout(
        height=800, width=1000,
        title_text="Economic Indicators Dashboard",
        title_x=0.5,
        title_font=dict(size=24, color='white'),
        paper_bgcolor='rgb(17,17,17)',
        plot_bgcolor='rgb(17,17,17)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5,
                   font=dict(color='white')),
        template='plotly_dark'
    )

    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='rgba(255,255,255,0.1)')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='rgba(255,255,255,0.1)')

    fig.write_image("多子图折线图_style_2.png", scale=2)
    return fig

def plot_3(data=None):
    # 极简风格：黑白灰
    if data is None:
        data = pd.read_csv('data.csv')
        data['Date'] = pd.to_datetime(data['Date'])
    
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=('GDP Growth Rate (%)', 'Unemployment Rate (%)', 'Inflation Rate (%)'),
        vertical_spacing=0.12
    )
    
    metrics = ['GDP_Growth', 'Unemployment_Rate', 'Inflation_Rate']
    colors = ['#000000', '#404040', '#808080']  # 黑白灰
    
    for i, (metric, color) in enumerate(zip(metrics, colors), 1):
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[metric],
                name=metric.replace('_', ' '),
                line=dict(color=color, width=1),
                mode='lines+markers',
                marker=dict(size=4),
                hovertemplate='%{x|%Q-%Y}<br>' + metric.replace('_', ' ') + ': %{y:.2f}%<br><extra></extra>'
            ),
            row=i, col=1
        )
    
    fig.update_layout(
        height=800, width=1000,
        title_text="Economic Indicators",
        title_x=0.5,
        title_font=dict(size=20),
        plot_bgcolor='white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
        template='simple_white'
    )

    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='#e0e0e0')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#e0e0e0')

    fig.write_image("多子图折线图_style_3.png", scale=2)
    return fig

def plot_4(data=None):
    # 活泼风格：明亮对比色
    if data is None:
        data = pd.read_csv('data.csv')
        data['Date'] = pd.to_datetime(data['Date'])
    
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=('GDP Growth Rate (%)', 'Unemployment Rate (%)', 'Inflation Rate (%)'),
        vertical_spacing=0.12
    )
    
    metrics = ['GDP_Growth', 'Unemployment_Rate', 'Inflation_Rate']
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']  # 明亮对比色
    
    for i, (metric, color) in enumerate(zip(metrics, colors), 1):
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[metric],
                name=metric.replace('_', ' '),
                line=dict(color=color, width=3),
                mode='lines+markers',
                marker=dict(size=8, symbol='circle'),
                hovertemplate='%{x|%Q-%Y}<br>' + metric.replace('_', ' ') + ': %{y:.2f}%<br><extra></extra>'
            ),
            row=i, col=1
        )
    
    fig.update_layout(
        height=800, width=1000,
        title_text="Economic Indicators Trends",
        title_x=0.5,
        title_font=dict(size=24, color='#2C3E50'),
        plot_bgcolor='rgba(240,240,240,0.3)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
        template='none'
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(189,195,199,0.5)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(189,195,199,0.5)')

    fig.write_image("多子图折线图_style_4.png", scale=2)
    return fig

def plot_5(data=None):
    # 专业分析风格：Color Brewer方案
    if data is None:
        data = pd.read_csv('data.csv')
        data['Date'] = pd.to_datetime(data['Date'])
    
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=('GDP Growth Rate (%)', 'Unemployment Rate (%)', 'Inflation Rate (%)'),
        vertical_spacing=0.12
    )
    
    metrics = ['GDP_Growth', 'Unemployment_Rate', 'Inflation_Rate']
    colors = ['#e41a1c', '#377eb8', '#4daf4a']  # Color Brewer Set1
    
    for i, (metric, color) in enumerate(zip(metrics, colors), 1):
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[metric],
                name=metric.replace('_', ' '),
                line=dict(color=color, width=2),
                mode='lines+markers',
                marker=dict(size=6, symbol=['circle', 'square', 'diamond'][i-1]),
                hovertemplate='%{x|%Q-%Y}<br>' + metric.replace('_', ' ') + ': %{y:.2f}%<br><extra></extra>'
            ),
            row=i, col=1
        )
    
    fig.update_layout(
        height=800, width=1000,
        title_text="Economic Indicators Analysis Report",
        title_x=0.5,
        title_font=dict(size=22),
        plot_bgcolor='white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
        template='plotly_white'
    )

    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='#E5E5E5')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#E5E5E5')

    fig.write_image("多子图折线图_style_5.png", scale=2)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
