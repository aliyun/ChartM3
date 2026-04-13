import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

def preprocess(data=None):
    # Generate sample data if none provided
    dates = pd.date_range(start='2023-01-01', end='2023-01-15', freq='D')
    inventory = [100, 100, 100, 85, 85, 85, 150, 150, 120, 120, 120, 180, 180, 160, 160]
    events = ['', '', 'Shipment out', '', '', 'Restock', '', 'Shipment out', '', '', 'Restock', '', 'Shipment out', '', '']
    
    # Create DataFrame
    df = pd.DataFrame({
        'date': dates,
        'inventory': inventory,
        'event': events
    })
    
    # Save to CSV
    df.to_csv('阶梯线图.csv', index=False)
    return df

def plot(data):
    # Create figure
    fig = go.Figure()
    
    # Add step line
    fig.add_trace(
        go.Scatter(
            x=data['date'],
            y=data['inventory'],
            mode='lines',
            line=dict(shape='hv', width=3, color='#2E86C1'),
            name='Inventory Level',
            hovertemplate='Date: %{x}<br>Inventory: %{y}<extra></extra>'
        )
    )
    
    # Add event annotations
    for idx, row in data.iterrows():
        if row['event']:
            fig.add_annotation(
                x=row['date'],
                y=row['inventory'],
                text=row['event'],
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="#636363",
                ax=0,
                ay=-40
            )
    
    # Update layout
    fig.update_layout(
        title={
            'text': 'Warehouse Inventory Levels',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Date",
        yaxis_title="Inventory Units",
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        plot_bgcolor='white',
        width=1000,
        height=600,
    )
    
    # Add grid
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
    
    # Save figure
    fig.write_image("阶梯线图.png")
    
    return fig

# Execute the functions

def plot_1(data):
    # 商务蓝风格
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(
            x=data['date'],
            y=data['inventory'],
            mode='lines+markers',
            line=dict(shape='hv', width=2, color='#1f77b4'),
            marker=dict(size=8, symbol='circle', color='#1f77b4'),
            name='Inventory Level',
            hovertemplate='Date: %{x}<br>Inventory: %{y}<extra></extra>'
        )
    )
    
    for idx, row in data.iterrows():
        if row['event']:
            fig.add_annotation(
                x=row['date'],
                y=row['inventory'],
                text=row['event'],
                showarrow=True,
                arrowhead=1,
                arrowsize=1,
                arrowwidth=1.5,
                arrowcolor="#404040",
                ax=0,
                ay=-30,
                font=dict(size=10, color="#404040")
            )
    
    fig.update_layout(
        title={
            'text': 'Warehouse Inventory Levels',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#2c3e50')
        },
        xaxis_title="Date",
        yaxis_title="Inventory Units",
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ),
        plot_bgcolor='white',
        width=1000,
        height=600,
        font=dict(family="Arial", size=12)
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='#e6e6e6')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#e6e6e6')
    
    fig.write_image("阶梯线图_style_1.png")
    return fig

def plot_2(data):
    # 活泼多彩风格
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(
            x=data['date'],
            y=data['inventory'],
            mode='lines+markers',
            line=dict(shape='hv', width=3, color='#FF6B6B'),
            marker=dict(size=10, symbol='star', color='#4ECDC4'),
            name='Inventory Level',
            hovertemplate='Date: %{x}<br>Inventory: %{y}<extra></extra>'
        )
    )
    
    for idx, row in data.iterrows():
        if row['event']:
            fig.add_annotation(
                x=row['date'],
                y=row['inventory'],
                text=row['event'],
                showarrow=True,
                arrowhead=2,
                arrowsize=1.5,
                arrowwidth=2,
                arrowcolor="#FFB347",
                ax=0,
                ay=-40,
                font=dict(size=11, color="#FF6B6B")
            )
    
    fig.update_layout(
        title={
            'text': 'Warehouse Inventory Levels',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#45B7AF')
        },
        xaxis_title="Date",
        yaxis_title="Inventory Units",
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor="rgba(255, 255, 255, 0.8)"
        ),
        plot_bgcolor='#f8f9fa',
        width=1000,
        height=600,
        font=dict(family="Comic Sans MS", size=12)
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='white')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white')
    
    fig.write_image("阶梯线图_style_2.png")
    return fig

def plot_3(data):
    # 暗黑科技风格
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(
            x=data['date'],
            y=data['inventory'],
            mode='lines+markers',
            line=dict(shape='hv', width=2, color='#00ff00'),
            marker=dict(size=8, symbol='diamond', color='#00ff00'),
            name='Inventory Level',
            hovertemplate='Date: %{x}<br>Inventory: %{y}<extra></extra>'
        )
    )
    
    for idx, row in data.iterrows():
        if row['event']:
            fig.add_annotation(
                x=row['date'],
                y=row['inventory'],
                text=row['event'],
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="#00ff00",
                ax=0,
                ay=-40,
                font=dict(size=10, color="#00ff00")
            )
    
    fig.update_layout(
        title={
            'text': 'Warehouse Inventory Levels',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#00ff00')
        },
        xaxis_title="Date",
        yaxis_title="Inventory Units",
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            font=dict(color='#00ff00')
        ),
        plot_bgcolor='black',
        paper_bgcolor='black',
        width=1000,
        height=600,
        font=dict(family="Courier New", size=12, color='#00ff00')
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='#333333', color='#00ff00')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#333333', color='#00ff00')
    
    fig.write_image("阶梯线图_style_3.png")
    return fig

def plot_4(data):
    # 渐变极简风格
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(
            x=data['date'],
            y=data['inventory'],
            mode='lines',
            line=dict(shape='hv', width=3, color='#8E44AD'),
            fill='tonexty',
            fillcolor='rgba(142, 68, 173, 0.1)',
            name='Inventory Level',
            hovertemplate='Date: %{x}<br>Inventory: %{y}<extra></extra>'
        )
    )
    
    for idx, row in data.iterrows():
        if row['event']:
            fig.add_annotation(
                x=row['date'],
                y=row['inventory'],
                text=row['event'],
                showarrow=True,
                arrowhead=1,
                arrowsize=1,
                arrowwidth=1,
                arrowcolor="#8E44AD",
                ax=0,
                ay=-30,
                font=dict(size=10, color="#8E44AD")
            )
    
    fig.update_layout(
        title={
            'text': 'Warehouse Inventory Levels',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#8E44AD')
        },
        xaxis_title="Date",
        yaxis_title="Inventory Units",
        showlegend=False,
        plot_bgcolor='white',
        width=1000,
        height=600,
        font=dict(family="Helvetica", size=12)
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    
    fig.write_image("阶梯线图_style_4.png")
    return fig

def plot_5(data):
    # Material Design风格
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(
            x=data['date'],
            y=data['inventory'],
            mode='lines+markers',
            line=dict(shape='hv', width=2.5, color='#2196F3'),
            marker=dict(size=9, symbol='circle', color='#2196F3',
                       line=dict(color='#ffffff', width=2)),
            name='Inventory Level',
            hovertemplate='Date: %{x}<br>Inventory: %{y}<extra></extra>'
        )
    )
    
    for idx, row in data.iterrows():
        if row['event']:
            fig.add_annotation(
                x=row['date'],
                y=row['inventory'],
                text=row['event'],
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="#757575",
                ax=0,
                ay=-35,
                font=dict(size=11, color="#757575")
            )
    
    fig.update_layout(
        title={
            'text': 'Warehouse Inventory Levels',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#212121')
        },
        xaxis_title="Date",
        yaxis_title="Inventory Units",
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor="rgba(255, 255, 255, 0.9)"
        ),
        plot_bgcolor='#FAFAFA',
        width=1000,
        height=600,
        font=dict(family="Roboto", size=12)
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='#E0E0E0')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#E0E0E0')
    
    fig.write_image("阶梯线图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
