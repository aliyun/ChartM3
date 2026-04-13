import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import random

def preprocess(data=None):
    # Set random seed for reproducibility
    random.seed(42)
    
    # Generate monthly temperature deviations
    months = pd.date_range(start='2023-01-01', periods=12, freq='M')
    deviations = [round(random.uniform(-5, 5), 1) for _ in range(12)]
    
    # Create DataFrame
    df = pd.DataFrame({
        'Month': months.strftime('%B'),
        'Temperature_Deviation': deviations
    })
    
    # Save to CSV
    df.to_csv('正负条形图.csv', index=False)
    return df

def plot(data):
    # Create figure
    fig = go.Figure()
    
    # Add bars
    fig.add_trace(go.Bar(
        x=data['Month'],
        y=data['Temperature_Deviation'],
        text=data['Temperature_Deviation'].apply(lambda x: f"{x:+.1f}°C"),
        textposition='outside',
        marker_color=['red' if x >= 0 else 'blue' for x in data['Temperature_Deviation']],
        name='Temperature Deviation'
    ))
    
    # Update layout
    fig.update_layout(
        title={
            'text': 'Monthly Temperature Deviations from Average (2023)',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Month",
        yaxis_title="Temperature Deviation (°C)",
        plot_bgcolor='rgba(240,240,240,0.3)',
        yaxis=dict(
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='black',
            gridcolor='rgba(0,0,0,0.1)'
        ),
        showlegend=False
    )
    
    # Save static image
    fig.write_image("正负条形图.png")
    
    return fig

# Generate and plot data
data = preprocess()
fig = plot(data)

def plot_1(data):
    # 现代简约风格
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=data['Month'],
        y=data['Temperature_Deviation'],
        text=data['Temperature_Deviation'].apply(lambda x: f"{x:+.1f}°C"),
        textposition='inside',
        marker_color=['#FF6B6B' if x >= 0 else '#4ECDC4' for x in data['Temperature_Deviation']],
        marker_line_width=0
    ))
    
    fig.update_layout(
        title={
            'text': 'Monthly Temperature Deviations',
            'y':0.95,
            'x':0.02,
            'xanchor': 'left',
            'yanchor': 'top'
        },
        xaxis_title=None,
        yaxis_title="Temperature Deviation (°C)",
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family="Arial", size=12),
        yaxis=dict(
            zeroline=True,
            zerolinewidth=1.5,
            zerolinecolor='#2C3E50',
            gridcolor='rgba(189,189,189,0.2)',
            gridwidth=0.5
        ),
        showlegend=False,
        margin=dict(l=50, r=50, t=80, b=50)
    )
    
    fig.write_image("正负条形图_style_1.png")
    return fig

def plot_2(data):
    # 商务专业风格
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=data['Month'],
        y=data['Temperature_Deviation'],
        text=data['Temperature_Deviation'].apply(lambda x: f"{x:+.1f}°C"),
        textposition='outside',
        marker_color=['#1f77b4' if x >= 0 else '#ff7f0e' for x in data['Temperature_Deviation']],
        marker_line_width=1,
        marker_line_color='#333333',
        width=0.6
    ))
    
    fig.update_layout(
        title={
            'text': 'Temperature Deviation Analysis - 2023',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Month",
        yaxis_title="Temperature Deviation (°C)",
        plot_bgcolor='rgba(240,240,240,0.3)',
        font=dict(family="Times New Roman", size=12),
        yaxis=dict(
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='#333333',
            gridcolor='rgba(51,51,51,0.2)',
            gridwidth=1
        ),
        showlegend=False
    )
    
    fig.write_image("正负条形图_style_2.png")
    return fig

def plot_3(data):
    # 深色科技风格
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=data['Month'],
        y=data['Temperature_Deviation'],
        text=data['Temperature_Deviation'].apply(lambda x: f"{x:+.1f}°C"),
        textposition='outside',
        marker_color=['#00ff00' if x >= 0 else '#00ffff' for x in data['Temperature_Deviation']],
        marker_line_width=0,
        opacity=0.7
    ))
    
    fig.update_layout(
        title={
            'text': 'Temperature Deviation Monitor',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Time Period",
        yaxis_title="Δ Temperature (°C)",
        plot_bgcolor='rgb(17,17,17)',
        paper_bgcolor='rgb(17,17,17)',
        font=dict(color='#ffffff', family="Courier New", size=12),
        yaxis=dict(
            zeroline=True,
            zerolinewidth=1,
            zerolinecolor='#ffffff',
            gridcolor='rgba(255,255,255,0.1)',
            gridwidth=0.5
        ),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        showlegend=False
    )
    
    fig.write_image("正负条形图_style_3.png")
    return fig

def plot_4(data):
    # 渐变色风格
    colors = ['#d73027', '#f46d43', '#fdae61', '#fee090', '#e0f3f8', '#abd9e9', '#74add1', '#4575b4']
    norm = (data['Temperature_Deviation'] - data['Temperature_Deviation'].min()) / \
           (data['Temperature_Deviation'].max() - data['Temperature_Deviation'].min())
    color_indices = (norm * (len(colors)-1)).round().astype(int)
    bar_colors = [colors[i] for i in color_indices]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=data['Month'],
        y=data['Temperature_Deviation'],
        text=data['Temperature_Deviation'].apply(lambda x: f"{x:+.1f}°C"),
        textposition='outside',
        marker_color=bar_colors,
        marker_line_width=0.5,
        marker_line_color='#ffffff'
    ))
    
    fig.update_layout(
        title={
            'text': 'Temperature Variation Spectrum',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title=None,
        yaxis_title="Temperature Deviation (°C)",
        plot_bgcolor='rgba(250,250,250,0.9)',
        font=dict(family="Helvetica", size=12),
        yaxis=dict(
            zeroline=True,
            zerolinewidth=1.5,
            zerolinecolor='#666666',
            gridcolor='rgba(189,189,189,0.2)'
        ),
        showlegend=False
    )
    
    fig.write_image("正负条形图_style_4.png")
    return fig

def plot_5(data):
    # 活泼清新风格
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=data['Month'],
        y=data['Temperature_Deviation'],
        text=data['Temperature_Deviation'].apply(lambda x: f"{x:+.1f}°C"),
        textposition='outside',
        marker_color=['#FF9999' if x >= 0 else '#99CCFF' for x in data['Temperature_Deviation']],
        marker_line_width=2,
        marker_line_color=['#FF6666' if x >= 0 else '#6699FF' for x in data['Temperature_Deviation']],
        width=0.7
    ))
    
    fig.update_layout(
        title={
            'text': '2023年月度温度变化',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="月份",
        yaxis_title="温度偏差 (°C)",
        plot_bgcolor='rgba(240,240,240,0.3)',
        font=dict(family="Arial", size=12),
        yaxis=dict(
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='#666666',
            gridcolor='rgba(189,189,189,0.3)',
            gridwidth=1
        ),
        showlegend=False,
        shapes=[
            dict(
                type='rect',
                xref='paper',
                yref='paper',
                x0=0,
                y0=0,
                x1=1,
                y1=1,
                line=dict(
                    color="#E8E8E8",
                    width=2,
                )
            )
        ]
    )
    
    fig.write_image("正负条形图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
