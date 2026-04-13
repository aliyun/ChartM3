import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    # Generate sample data for energy consumption by source
    years = list(range(2010, 2021))
    
    # Create sample data for different energy sources
    data = {
        'Coal': [40, 37, 34, 31, 28, 25, 22, 20, 18, 16, 15],
        'Natural Gas': [25, 26, 27, 28, 29, 28, 27, 26, 25, 24, 25],
        'Nuclear': [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
        'Renewables': [20, 22, 24, 26, 28, 32, 36, 39, 42, 45, 45]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data, index=years)
    
    # Save to CSV
    df.to_csv('堆叠面积图.csv')
    return df

def plot(data):
    # Color scheme
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    
    # Create figure
    fig = go.Figure()
    
    # Add traces for each energy source
    for idx, column in enumerate(data.columns):
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data[column],
            name=column,
            mode='lines',
            stackgroup='one',
            line=dict(width=0.5),
            fillcolor=colors[idx],
            hovertemplate='%{y:.0f}%<extra></extra>'
        ))
    
    # Update layout
    fig.update_layout(
        title={
            'text': 'Energy Consumption by Source (2010-2020)',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title='Year',
        yaxis_title='Percentage of Total Energy Consumption',
        hovermode='x unified',
        showlegend=True,
        legend={
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': 1.02,
            'xanchor': 'right',
            'x': 1
        },
        # Add grid
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='LightGrey'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='LightGrey',
            ticksuffix='%'
        ),
        # Set plot background
        paper_bgcolor='white',
        # Add margin
        margin=dict(l=80, r=80, t=100, b=80)
    )
    
    # Save plot
    fig.write_image("堆叠面积图.png", width=1200, height=800)
    return fig

# Execute functions

def plot_1(data):
    # Modern Minimalist Style
    colors = ['#E63946', '#F1FAEE', '#A8DADC', '#457B9D']
    
    fig = go.Figure()
    
    for idx, column in enumerate(data.columns):
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data[column],
            name=column,
            mode='lines',
            stackgroup='one',
            line=dict(width=0.8),
            fillcolor=colors[idx],
            hovertemplate='%{y:.0f}%<extra></extra>'
        ))
    
    fig.update_layout(
        template='plotly_white',
        title={
            'text': 'Energy Sources Distribution',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#1D3557')
        },
        xaxis_title='Year',
        yaxis_title='Percentage',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        xaxis=dict(showgrid=False),
        yaxis=dict(
            showgrid=True,
            gridwidth=0.5,
            gridcolor='rgba(0,0,0,0.1)',
            ticksuffix='%'
        ),
        paper_bgcolor='white',
        margin=dict(l=60, r=60, t=100, b=60)
    )
    
    fig.write_image("堆叠面积图_style_1.png", width=1200, height=800)
    return fig

def plot_2(data):
    # Corporate Professional Style
    colors = ['#003f5c', '#58508d', '#bc5090', '#ff6361']
    
    fig = go.Figure()
    
    for idx, column in enumerate(data.columns):
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data[column],
            name=column,
            mode='lines',
            stackgroup='one',
            line=dict(width=1),
            fillcolor=colors[idx],
            opacity=0.8,
            hovertemplate='%{y:.0f}%<extra></extra>'
        ))
    
    fig.update_layout(
        template='none',
        title={
            'text': 'Energy Consumption Analysis (2010-2020)',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, family='Arial', color='#333333')
        },
        xaxis_title='Year',
        yaxis_title='Percentage of Total Energy',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            orientation='v',
            yanchor='top',
            y=0.95,
            xanchor='left',
            x=1.05
        ),
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(0,0,0,0.1)'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(0,0,0,0.1)',
            ticksuffix='%'
        ),
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(l=80, r=120, t=100, b=80)
    )
    
    fig.write_image("堆叠面积图_style_2.png", width=1200, height=800)
    return fig

def plot_3(data):
    # Eco-Friendly Style
    colors = ['#2d6a4f', '#40916c', '#52b788', '#74c69d']
    
    fig = go.Figure()
    
    for idx, column in enumerate(data.columns):
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data[column],
            name=column,
            mode='lines',
            stackgroup='one',
            line=dict(width=0),
            fillcolor=colors[idx],
            opacity=0.9,
            hovertemplate='%{y:.0f}%<extra></extra>'
        ))
    
    fig.update_layout(
        template='simple_white',
        title={
            'text': 'Sustainable Energy Distribution',
            'y':0.98,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=22, color='#1b4332')
        },
        xaxis_title='Year',
        yaxis_title='Share of Energy Sources (%)',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='center',
            x=0.5
        ),
        xaxis=dict(
            showgrid=True,
            gridwidth=0.5,
            gridcolor='rgba(0,0,0,0.05)'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=0.5,
            gridcolor='rgba(0,0,0,0.05)',
            ticksuffix='%'
        ),
        paper_bgcolor='white',
        margin=dict(l=60, r=60, t=100, b=60)
    )
    
    fig.write_image("堆叠面积图_style_3.png", width=1200, height=800)
    return fig

def plot_4(data):
    # High-Tech Style
    colors = ['#00b4d8', '#0096c7', '#0077b6', '#023e8a']
    
    fig = go.Figure()
    
    for idx, column in enumerate(data.columns):
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data[column],
            name=column,
            mode='lines',
            stackgroup='one',
            line=dict(width=1),
            fillcolor=colors[idx],
            opacity=0.85,
            hovertemplate='%{y:.0f}%<extra></extra>'
        ))
    
    fig.update_layout(
        template='plotly_dark',
        title={
            'text': 'Energy Distribution Matrix',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#caf0f8')
        },
        xaxis_title='Year',
        yaxis_title='Energy Share (%)',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            orientation='v',
            yanchor='top',
            y=1,
            xanchor='left',
            x=1.05,
            font=dict(color='#caf0f8')
        ),
        xaxis=dict(
            showgrid=True,
            gridwidth=0.5,
            gridcolor='rgba(255,255,255,0.1)',
            color='#caf0f8'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=0.5,
            gridcolor='rgba(255,255,255,0.1)',
            ticksuffix='%',
            color='#caf0f8'
        ),
        paper_bgcolor='#111111',
        plot_bgcolor='#111111',
        margin=dict(l=80, r=120, t=100, b=80)
    )
    
    fig.write_image("堆叠面积图_style_4.png", width=1200, height=800)
    return fig

def plot_5(data):
    # Vintage Style
    colors = ['#8b4513', '#deb887', '#d2691e', '#cd853f']
    
    fig = go.Figure()
    
    for idx, column in enumerate(data.columns):
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data[column],
            name=column,
            mode='lines',
            stackgroup='one',
            line=dict(width=0.5),
            fillcolor=colors[idx],
            opacity=0.7,
            hovertemplate='%{y:.0f}%<extra></extra>'
        ))
    
    fig.update_layout(
        template='simple_white',
        title={
            'text': 'Historical Energy Composition',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=22, family='Garamond', color='#8b4513')
        },
        xaxis_title='Year',
        yaxis_title='Percentage Distribution',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1,
            bgcolor='rgba(255,255,255,0.8)'
        ),
        xaxis=dict(
            showgrid=True,
            gridwidth=0.5,
            gridcolor='rgba(139,69,19,0.1)'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=0.5,
            gridcolor='rgba(139,69,19,0.1)',
            ticksuffix='%'
        ),
        paper_bgcolor='#fff8dc',
        plot_bgcolor='#fff8dc',
        margin=dict(l=80, r=80, t=100, b=80)
    )
    
    fig.write_image("堆叠面积图_style_5.png", width=1200, height=800)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
