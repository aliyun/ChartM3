import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    # Generate sample data if none provided
    if data is None:
        products = ['Product A', 'Product B', 'Product C', 'Product D']
        targets = [1000, 800, 1200, 950]
        actuals = [850, 720, 980, 500]
        
        data = pd.DataFrame({
            'Product': products,
            'Target': targets,
            'Actual': actuals
        })
    
    # Calculate completion percentage
    data['Completion'] = (data['Actual'] / data['Target'] * 100).round(1)
    
    # Save to CSV
    data.to_csv('条形进度图.csv', index=False)
    return data

def plot(data):
    # Create figure
    fig = go.Figure()
    
    # Add bars for total target (background)
    fig.add_trace(go.Bar(
        x=data['Target'],
        y=data['Product'],
        orientation='h',
        name='Target',
        marker_color='rgb(220,220,220)',
        width=0.6
    ))
    
    # Add bars for actual progress
    fig.add_trace(go.Bar(
        x=data['Actual'],
        y=data['Product'],
        orientation='h',
        name='Actual',
        marker_color='rgb(55,126,184)',
        width=0.6
    ))
    
    # Customize layout
    fig.update_layout(
        title={
            'text': 'Sales Progress by Product Line',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20}
        },
        barmode='overlay',
        plot_bgcolor='white',
        font=dict(size=12),
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    # Add percentage labels
    for i, row in data.iterrows():
        fig.add_annotation(
            x=row['Target'],
            y=row['Product'],
            text=f"{row['Completion']}%",
            showarrow=False,
            xshift=10,
            font=dict(size=12)
        )
    
    # Update axes
    fig.update_xaxes(
        title_text='Sales Amount',
        showgrid=True,
        gridwidth=1,
        gridcolor='rgb(240,240,240)'
    )
        # Update y axis
    fig.update_yaxes(
        title_text='Product Line',
        showgrid=False
    )
    
    # Save figure
    fig.write_image("条形进度图.png", scale=2)
    return fig


def plot_1(data):
    # 现代简约风格：单色渐变
    blues = ['rgb(215,233,247)', 'rgb(66,146,198)']
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['Target'],
        y=data['Product'],
        orientation='h',
        name='Target',
        marker_color=blues[0],
        width=0.7
    ))
    
    fig.add_trace(go.Bar(
        x=data['Actual'],
        y=data['Product'],
        orientation='h',
        name='Actual',
        marker_color=blues[1],
        width=0.7
    ))
    
    fig.update_layout(
        title={
            'text': 'Sales Progress by Product Line',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20, 'family': 'Arial'}
        },
        barmode='overlay',
        plot_bgcolor='white',
        font=dict(family="Arial", size=12),
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    for i, row in data.iterrows():
        fig.add_annotation(
            x=row['Target'],
            y=row['Product'],
            text=f"{row['Completion']}%",
            showarrow=False,
            xshift=10,
            font=dict(size=12, family="Arial")
        )
    
    fig.update_xaxes(
        title_text='Sales Amount',
        showgrid=True,
        gridwidth=1,
        gridcolor='rgb(240,240,240)'
    )
    
    fig.update_yaxes(
        title_text='Product Line',
        showgrid=False
    )
    
    fig.write_image("条形进度图_style_1.png", scale=2)
    return fig

def plot_2(data):
    # 对比色商务风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['Target'],
        y=data['Product'],
        orientation='h',
        name='Target',
        marker_color='rgba(189,189,189,0.5)',
        width=0.65
    ))
    
    fig.add_trace(go.Bar(
        x=data['Actual'],
        y=data['Product'],
        orientation='h',
        name='Actual',
        marker_color='rgba(255,127,14,0.8)',
        width=0.65
    ))
    
    fig.update_layout(
        title={
            'text': 'Sales Progress by Product Line',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20, 'family': 'Helvetica'}
        },
        barmode='overlay',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family="Helvetica", size=12),
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="right",
            x=1.1
        )
    )
    
    for i, row in data.iterrows():
        fig.add_annotation(
            x=row['Actual'],
            y=row['Product'],
            text=f"{row['Completion']}%",
            showarrow=False,
            xshift=-20,
            font=dict(size=12, color='white', family="Helvetica")
        )
    
    fig.update_xaxes(
        title_text='Sales Amount',
        showgrid=True,
        gridwidth=1,
        gridcolor='rgb(240,240,240)'
    )
    
    fig.update_yaxes(
        title_text='Product Line',
        showgrid=False
    )
    
    fig.write_image("条形进度图_style_2.png", scale=2)
    return fig

def plot_3(data):
    # 科技暗色风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['Target'],
        y=data['Product'],
        orientation='h',
        name='Target',
        marker_color='rgba(71,71,71,0.6)',
        width=0.6
    ))
    
    fig.add_trace(go.Bar(
        x=data['Actual'],
        y=data['Product'],
        orientation='h',
        name='Actual',
        marker_color='rgba(0,255,255,0.7)',
        width=0.6
    ))
    
    fig.update_layout(
        title={
            'text': 'Sales Progress by Product Line',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20, 'color': 'white'}
        },
        barmode='overlay',
        plot_bgcolor='rgb(17,17,17)',
        paper_bgcolor='rgb(17,17,17)',
        font=dict(color='white', size=12),
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    for i, row in data.iterrows():
        fig.add_annotation(
            x=row['Target'],
            y=row['Product'],
            text=f"{row['Completion']}%",
            showarrow=False,
            xshift=10,
            font=dict(size=12, color='white')
        )
    
    fig.update_xaxes(
        title_text='Sales Amount',
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        color='white'
    )
    
    fig.update_yaxes(
        title_text='Product Line',
        showgrid=False,
        color='white'
    )
    
    fig.write_image("条形进度图_style_3.png", scale=2)
    return fig

def plot_4(data):
    # 活泼彩色风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['Target'],
        y=data['Product'],
        orientation='h',
        name='Target',
        marker_color='rgba(240,240,240,0.8)',
        width=0.75
    ))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    fig.add_trace(go.Bar(
        x=data['Actual'],
        y=data['Product'],
        orientation='h',
        name='Actual',
        marker_color=colors,
        width=0.75
    ))
    
    fig.update_layout(
        title={
            'text': 'Sales Progress by Product Line',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 22, 'family': 'Arial', 'color': '#2C3E50'}
        },
        barmode='overlay',
        plot_bgcolor='white',
        font=dict(family="Arial", size=12),
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    for i, row in data.iterrows():
        fig.add_annotation(
            x=row['Target'],
            y=row['Product'],
            text=f"{row['Completion']}%",
            showarrow=False,
            xshift=10,
            font=dict(size=13, color='#2C3E50', family="Arial")
        )
    
    fig.update_xaxes(
        title_text='Sales Amount',
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(220,220,220,0.5)'
    )
    
    fig.update_yaxes(
        title_text='Product Line',
        showgrid=False
    )
    
    fig.write_image("条形进度图_style_4.png", scale=2)
    return fig

def plot_5(data):
    # 典雅柔和风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['Target'],
        y=data['Product'],
        orientation='h',
        name='Target',
        marker_color='rgba(230,230,230,0.7)',
        width=0.55
    ))
    
    fig.add_trace(go.Bar(
        x=data['Actual'],
        y=data['Product'],
        orientation='h',
        name='Actual',
        marker_color='rgba(142,156,173,0.8)',
        width=0.55
    ))
    
    fig.update_layout(
        title={
            'text': 'Sales Progress by Product Line',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20, 'family': 'Georgia', 'color': '#555555'}
        },
        barmode='overlay',
        plot_bgcolor='rgba(250,250,250,0.9)',
        paper_bgcolor='rgba(250,250,250,0.9)',
        font=dict(family="Georgia", size=12, color='#555555'),
        height=400,
        margin=dict(l=20, r=20, t=60, b=20),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    for i, row in data.iterrows():
        fig.add_annotation(
            x=row['Target'],
            y=row['Product'],
            text=f"{row['Completion']}%",
            showarrow=False,
            xshift=10,
            font=dict(size=12, family="Georgia", color='#555555')
        )
    
    fig.update_xaxes(
        title_text='Sales Amount',
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(200,200,200,0.2)'
    )
    
    fig.update_yaxes(
        title_text='Product Line',
        showgrid=False
    )
    
    fig.write_image("条形进度图_style_5.png", scale=2)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
