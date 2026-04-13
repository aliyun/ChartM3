import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

def preprocess(data=None):
    """Generate and preprocess sample temperature range data"""
    # Generate 30 days of sample temperature data
    dates = [datetime(2024, 1, 1) + timedelta(days=x) for x in range(10)]
    
    # Create realistic temperature ranges with some randomness
    np.random.seed(42)  # For reproducibility
    max_temps = [25 + np.random.normal(0, 2) for _ in range(10)]
    min_temps = [15 + np.random.normal(0, 2) for _ in range(10)]
    
    # Create dataframe
    df = pd.DataFrame({
        'Date': dates,
        'Max_Temp': np.round(max_temps, 1),
        'Min_Temp': np.round(min_temps, 1)
    })
    
    # Save to CSV
    df.to_csv('区间面积图.csv', index=False)
    return df

def plot(data):
    """Create range area chart using Plotly"""
    fig = go.Figure()
    
    # Add traces
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Max_Temp'],
        name='Maximum Temperature',
        mode='lines+text+markers', 
        line=dict(color='rgb(239, 85, 59)', width=2),
        marker=dict(size=6),
        text=[f'{temp:.1f}°C' for temp in data['Max_Temp']],
        textposition='top center',
        textfont=dict(
            size=10,
            color='rgb(239, 85, 59)'
        ),
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Min_Temp'],
        name='Minimum Temperature',
        mode='lines+text+markers',
        line=dict(color='rgb(99, 110, 250)', width=2),
        marker=dict(size=6),
        fill='tonexty',
        fillcolor='rgba(99, 110, 250, 0.2)',
        text=[f'{temp:.1f}°C' for temp in data['Min_Temp']],
        textposition='bottom center',
        textfont=dict(
            size=10,
            color='rgb(99, 110, 250)'
        ),
    ))
    
    # Update layout
    fig.update_layout(
        title={
            'text': 'Daily Temperature Range - January 2024',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title='Date',
        yaxis_title='Temperature (°C)',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            yanchor="bottom",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        plot_bgcolor='white',
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='lightgray'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='lightgray',
            zeroline=False
        )
    )
    
    # Save figure
    fig.write_image("区间面积图.png")
    return fig

# Generate and plot data
data = preprocess()
fig = plot(data)

def plot_1(data):
    """现代商务风格"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Max_Temp'],
        name='Maximum Temperature',
        mode='lines',
        line=dict(color='#2C3E50', width=2),
        marker=dict(size=8, symbol='circle'),
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Min_Temp'],
        name='Minimum Temperature',
        mode='lines',
        line=dict(color='#E74C3C', width=2),
        fill='tonexty',
        fillcolor='rgba(231, 76, 60, 0.1)',
    ))
    
    fig.update_layout(
        title={
            'text': 'Temperature Range Analysis',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#2C3E50')
        },
        xaxis_title='Date',
        yaxis_title='Temperature (°C)',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#2C3E50'),
        showlegend=True,
        legend=dict(
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#2C3E50',
            borderwidth=1
        ),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#ECF0F1')
    )
    
    fig.write_image("区间面积图_style_1.png")
    return fig

def plot_2(data):
    """柔和渐变风格"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Max_Temp'],
        name='Maximum Temperature',
        mode='lines+markers',
        line=dict(color='#A8E6CF', width=3),
        marker=dict(size=8, symbol='circle', color='#A8E6CF'),
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Min_Temp'],
        name='Minimum Temperature',
        mode='lines+markers',
        line=dict(color='#FFB7B2', width=3),
        marker=dict(size=8, symbol='circle', color='#FFB7B2'),
        fill='tonexty',
        fillcolor='rgba(255, 183, 178, 0.2)',
    ))
    
    fig.update_layout(
        title={
            'text': 'Temperature Variations',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Arial', color='#3D3D3D')
        },
        xaxis_title='Date',
        yaxis_title='Temperature (°C)',
        plot_bgcolor='rgba(240,240,240,0.3)',
        paper_bgcolor='white',
        font=dict(family='Arial'),
        showlegend=True,
        legend=dict(
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#DCDCDC'
        ),
        xaxis=dict(showgrid=True, gridcolor='white'),
        yaxis=dict(showgrid=True, gridcolor='white')
    )
    
    fig.write_image("区间面积图_style_2.png")
    return fig

def plot_3(data):
    """科技暗黑风格"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Max_Temp'],
        name='Maximum Temperature',
        mode='lines+markers',
        line=dict(color='#00FF00', width=2),
        marker=dict(size=6, symbol='diamond'),
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Min_Temp'],
        name='Minimum Temperature',
        mode='lines+markers',
        line=dict(color='#00FFFF', width=2),
        marker=dict(size=6, symbol='diamond'),
        fill='tonexty',
        fillcolor='rgba(0, 255, 255, 0.1)',
    ))
    
    fig.update_layout(
        title={
            'text': 'Temperature Monitor',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#00FF00')
        },
        xaxis_title='Date',
        yaxis_title='Temperature (°C)',
        plot_bgcolor='rgb(8,8,8)',
        paper_bgcolor='rgb(8,8,8)',
        font=dict(color='#FFFFFF'),
        showlegend=True,
        legend=dict(
            bgcolor='rgba(8,8,8,0.9)',
            bordercolor='#00FF00'
        ),
        xaxis=dict(showgrid=True, gridcolor='rgba(0,255,0,0.1)'),
        yaxis=dict(showgrid=True, gridcolor='rgba(0,255,0,0.1)')
    )
    
    fig.write_image("区间面积图_style_3.png")
    return fig

def plot_4(data):
    """极简风格"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Max_Temp'],
        name='Maximum Temperature',
        mode='lines',
        line=dict(color='#000000', width=1.5),
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Min_Temp'],
        name='Minimum Temperature',
        mode='lines',
        line=dict(color='#666666', width=1.5),
        fill='tonexty',
        fillcolor='rgba(200,200,200,0.2)',
    ))
    
    fig.update_layout(
        title={
            'text': 'Temperature Range',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, color='black')
        },
        xaxis_title='Date',
        yaxis_title='Temperature (°C)',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='black'),
        showlegend=False,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
    
    fig.write_image("区间面积图_style_4.png")
    return fig

def plot_5(data):
    """活泼彩虹风格"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Max_Temp'],
        name='Maximum Temperature',
        mode='lines+markers',
        line=dict(color='#FF6B6B', width=4),
        marker=dict(size=10, symbol='star', color='#FF6B6B'),
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Min_Temp'],
        name='Minimum Temperature',
        mode='lines+markers',
        line=dict(color='#4ECDC4', width=4),
        marker=dict(size=10, symbol='star', color='#4ECDC4'),
        fill='tonexty',
        fillcolor='rgba(78, 205, 196, 0.3)',
    ))
    
    fig.update_layout(
        title={
            'text': '🌡️ Fun Temperature Chart! 🌡️',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, family='Arial', color='#FF6B6B')
        },
        xaxis_title='Date',
        yaxis_title='Temperature (°C)',
        plot_bgcolor='#FFFDF9',
        paper_bgcolor='#FFFDF9',
        font=dict(family='Arial', color='#45B7AF'),
        showlegend=True,
        legend=dict(
            bgcolor='rgba(255,253,249,0.9)',
            bordercolor='#FF6B6B',
            borderwidth=2
        ),
        xaxis=dict(showgrid=True, gridcolor='rgba(255,107,107,0.1)'),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,107,107,0.1)')
    )
    
    fig.write_image("区间面积图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
