import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
import plotly.io as pio

def preprocess(data=None):
    # Generate quarterly dates for 2 years
    dates = pd.date_range(start='2022-01-01', end='2023-12-31', freq='Q')
    
    # Generate realistic looking sales data for 3 product categories
    electronics = [250, 220, 280, 310, 290, 260, 320, 350]
    clothing = [180, 210, 190, 240, 200, 230, 210, 260] 
    furniture = [150, 140, 160, 190, 170, 160, 180, 210]
    
    # Create dataframe
    df = pd.DataFrame({
        'Date': dates,
        'Electronics': electronics,
        'Clothing': clothing,
        'Furniture': furniture
    })
    
    # Save to CSV
    df.to_csv('多列面积图.csv', index=False)
    return df

def plot(data):
    # Create figure
    fig = go.Figure()
    
    # Add traces for each category
    categories = ['Electronics', 'Clothing', 'Furniture']
    colors = ['rgba(67, 147, 195, 0.6)', 'rgba(178, 24, 43, 0.6)', 'rgba(77, 175, 74, 0.6)']
    
    for cat, color in zip(categories, colors):
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[cat],
                name=cat,
                fill='tonexty',
                mode='lines+markers',
                line=dict(width=2),
                marker=dict(size=8),
                fillcolor=color
            )
        )
    
    # Update layout
    fig.update_layout(
        title={
            'text': 'Quarterly Sales by Product Category',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24)
        },
        xaxis_title="Quarter",
        yaxis_title="Sales ($ thousands)",
        legend=dict(
            yanchor="bottom",
            y=0.99,
            xanchor="right",
            x=0.99
        ),
        showlegend=True,
        hovermode='x unified',
        plot_bgcolor='white',
        width=1000,
        height=600
    )
    
        # Add grid
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        title_font=dict(size=14)
    )
    
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)', 
        title_font=dict(size=14)
    )
    
    # Save static image
    fig.write_image("多列面积图.png")
    fig.write_html("data.html")
    
    return fig


def plot_1(data):
    # 商务风格 - 蓝色渐变主题
    fig = go.Figure()
    colors = ['rgba(8,48,107,0.6)', 'rgba(66,146,198,0.6)', 'rgba(158,202,225,0.6)']
    categories = ['Electronics', 'Clothing', 'Furniture']
    
    for cat, color in zip(categories, colors):
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[cat],
                name=cat,
                fill='tonexty',
                mode='lines',
                line=dict(width=1.5),
                fillcolor=color
            )
        )
    
    fig.update_layout(
        template='plotly_white',
        title={
            'text': 'Quarterly Sales Analysis',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=22, color='#2F4F4F')
        },
        xaxis_title="Quarter",
        yaxis_title="Sales ($ thousands)",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(255,255,255,0.8)'
        ),
        width=1000,
        height=600
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='rgba(128,128,128,0.1)')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='rgba(128,128,128,0.1)')
    
    fig.write_image("多列面积图_style_1.png")
    return fig

def plot_2(data):
    # 活泼风格 - 彩虹色系
    fig = go.Figure()
    colors = ['rgba(255,90,95,0.5)', 'rgba(86,192,146,0.5)', 'rgba(255,173,27,0.5)']
    categories = ['Electronics', 'Clothing', 'Furniture']
    
    for cat, color in zip(categories, colors):
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[cat],
                name=cat,
                fill='tonexty',
                mode='lines+markers',
                line=dict(width=2),
                marker=dict(size=10, symbol='circle'),
                fillcolor=color
            )
        )
    
    fig.update_layout(
        template='plotly_white',
        title={
            'text': '📊 Product Sales Trends',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Arial', color='#484848')
        },
        xaxis_title="Quarter",
        yaxis_title="Sales ($ thousands)",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bordercolor='#E5E5E5',
            borderwidth=1
        ),
        width=1000,
        height=600
    )
    
    fig.write_image("多列面积图_style_2.png")
    return fig

def plot_3(data):
    # 极简风格 - 灰度主题
    fig = go.Figure()
    colors = ['rgba(0,0,0,0.7)', 'rgba(80,80,80,0.5)', 'rgba(160,160,160,0.3)']
    categories = ['Electronics', 'Clothing', 'Furniture']
    
    for cat, color in zip(categories, colors):
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[cat],
                name=cat,
                fill='tonexty',
                mode='lines',
                line=dict(width=1),
                fillcolor=color
            )
        )
    
    fig.update_layout(
        template='plotly_white',
        title={
            'text': 'Sales Performance',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, family='Helvetica')
        },
        xaxis_title="Quarter",
        yaxis_title="Sales ($ thousands)",
        legend=dict(
            yanchor="bottom",
            y=0.01,
            xanchor="right",
            x=0.99
        ),
        showlegend=True,
        width=1000,
        height=600
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    
    fig.write_image("多列面积图_style_3.png")
    return fig

def plot_4(data):
    # 自然风格 - 绿色主题
    fig = go.Figure()
    colors = ['rgba(27,120,55,0.6)', 'rgba(127,191,123,0.6)', 'rgba(217,240,211,0.6)']
    categories = ['Electronics', 'Clothing', 'Furniture']
    
    for cat, color in zip(categories, colors):
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[cat],
                name=cat,
                fill='tonexty',
                mode='lines+markers',
                line=dict(width=1.5),
                marker=dict(size=8, symbol='diamond'),
                fillcolor=color
            )
        )
    
    fig.update_layout(
        template='plotly_white',
        title={
            'text': 'Eco-friendly Sales Report',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=22, color='#1b7837')
        },
        xaxis_title="Quarter",
        yaxis_title="Sales ($ thousands)",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(255,255,255,0.8)'
        ),
        width=1000,
        height=600,
        plot_bgcolor='rgba(240,248,240,0.5)'
    )
    
    fig.write_image("多列面积图_style_4.png")
    return fig

def plot_5(data):
    # 科技风格 - 深色主题
    fig = go.Figure()
    colors = ['rgba(0,147,255,0.6)', 'rgba(0,255,198,0.6)', 'rgba(172,240,242,0.6)']
    categories = ['Electronics', 'Clothing', 'Furniture']
    
    for cat, color in zip(categories, colors):
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[cat],
                name=cat,
                fill='tonexty',
                mode='lines',
                line=dict(width=2),
                fillcolor=color
            )
        )
    
    fig.update_layout(
        template='plotly_dark',
        title={
            'text': 'Sales Analytics Dashboard',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#00ffff')
        },
        xaxis_title="Quarter",
        yaxis_title="Sales ($ thousands)",
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            font=dict(color='#ffffff')
        ),
        width=1000,
        height=600,
        paper_bgcolor='rgb(17,17,17)',
        plot_bgcolor='rgb(17,17,17)'
    )
    
    fig.update_xaxes(gridcolor='rgba(128,128,128,0.2)', gridwidth=0.5)
    fig.update_yaxes(gridcolor='rgba(128,128,128,0.2)', gridwidth=0.5)
    
    fig.write_image("多列面积图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
