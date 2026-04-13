import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def preprocess(data=None):
    # Generate sample data if none provided
    if data is None:
        np.random.seed(42)
        months = pd.date_range('2023-01-01', '2023-12-31', freq='M')
        
        # Generate revenue with seasonal pattern
        base_revenue = 1000000  # Base revenue of 1M
        seasonal_factor = np.sin(np.linspace(0, 2*np.pi, 12)) * 200000
        noise = np.random.normal(0, 50000, 12)
        revenue = base_revenue + seasonal_factor + noise
        
        # Generate correlated profit margins
        base_margin = 10  # Base margin of 10%
        margin_noise = np.random.normal(0, 1, 12)
        margin = base_margin + (revenue - base_revenue) / 500000 + margin_noise
        
        data = pd.DataFrame({
            'Month': months,
            'Revenue': revenue,
            'Profit_Margin': margin
        })
        
    # Format the data
    data['Month'] = data['Month'].dt.strftime('%Y-%m')
    data['Revenue'] = data['Revenue'].round(0)
    data['Profit_Margin'] = data['Profit_Margin'].round(1)
    
    # Save to CSV
    data.to_csv('折线-柱状图.csv', index=False)
    return data

def plot(data=None):
    if data is None:
        data = pd.read_csv('折线-柱状图.csv')
    
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add revenue bars
    fig.add_trace(
        go.Bar(
            x=data['Month'],
            y=data['Revenue'],
            name="Revenue",
            marker_color='#2E86C1',
            text=data['Revenue'].apply(lambda x: f'${x:,.0f}'),
            textposition='outside',
        ),
        secondary_y=False
    )
    
    # Add profit margin line
    fig.add_trace(
        go.Scatter(
            x=data['Month'],
            y=data['Profit_Margin'],
            name="Profit Margin",
            line=dict(color='#E74C3C', width=3),
            mode='lines+markers+text',
            text=data['Profit_Margin'].apply(lambda x: f'{x:.1f}%'),
            textposition='top center',
            marker=dict(size=8)
        ),
        secondary_y=True
    )
    
    # Update layout
    fig.update_layout(
        title={
            'text': 'Monthly Revenue and Profit Margin',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20)
        },
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        ),
        barmode='group',
        template='plotly_white',
        height=600,
        showlegend=True
    )

    # Update y-axes
    fig.update_yaxes(
        title_text="Revenue ($)", 
        secondary_y=False,
        tickformat="$,.0f",
        gridcolor='lightgray'
    )
    fig.update_yaxes(
        title_text="Profit Margin (%)", 
        secondary_y=True,
        ticksuffix="%",
        gridcolor='lightgray'
    )
    
    # Update x-axis
    fig.update_xaxes(
        title_text="Month",
        tickangle=45,
        gridcolor='lightgray'
    )
    
    # Save figure
    fig.write_image("折线-柱状图.png", width=1000, height=600)
    return fig


def plot_1(data=None):
    """商务专业风格：深蓝色系"""
    if data is None:
        data = pd.read_csv('data.csv')
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            x=data['Month'],
            y=data['Revenue'],
            name="Revenue",
            marker_color='rgba(41, 128, 185, 0.7)',
            text=data['Revenue'].apply(lambda x: f'${x:,.0f}'),
            textposition='outside',
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Month'],
            y=data['Profit_Margin'],
            name="Profit Margin",
            line=dict(color='#1A5276', width=2),
            mode='lines+markers',
            marker=dict(size=8, symbol='diamond')
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title={
            'text': 'Monthly Revenue and Profit Margin',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(family="Arial", size=20, color="#2C3E50")
        },
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(255, 255, 255, 0.8)',
            bordercolor='#CCCCCC'
        ),
        template='plotly_white',
        height=600,
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    fig.update_yaxes(title_text="Revenue ($)", secondary_y=False, tickformat="$,.0f", gridcolor='#E5E7E9')
    fig.update_yaxes(title_text="Profit Margin (%)", secondary_y=True, ticksuffix="%", gridcolor='#E5E7E9')
    fig.update_xaxes(title_text="Month", tickangle=45, gridcolor='#E5E7E9')
    
    fig.write_image("折线-柱状图_style_1.png", width=1000, height=600)
    return fig

def plot_2(data=None):
    """现代简约风格：黑白主色调"""
    if data is None:
        data = pd.read_csv('data.csv')
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            x=data['Month'],
            y=data['Revenue'],
            name="Revenue",
            marker_color='rgba(0, 0, 0, 0.6)',
            text=data['Revenue'].apply(lambda x: f'${x:,.0f}'),
            textposition='outside',
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Month'],
            y=data['Profit_Margin'],
            name="Profit Margin",
            line=dict(color='#FF5252', width=3),
            mode='lines+markers',
            marker=dict(size=10, symbol='circle')
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title={
            'text': 'Monthly Revenue and Profit Margin',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(family="Helvetica", size=20, color="#333333")
        },
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        ),
        template='simple_white',
        height=600
    )
    
    fig.update_yaxes(title_text="Revenue ($)", secondary_y=False, tickformat="$,.0f", gridcolor='#EEEEEE')
    fig.update_yaxes(title_text="Profit Margin (%)", secondary_y=True, ticksuffix="%", gridcolor='#EEEEEE')
    fig.update_xaxes(title_text="Month", tickangle=45, gridcolor='#EEEEEE')
    
    fig.write_image("折线-柱状图_style_2.png", width=1000, height=600)
    return fig

def plot_3(data=None):
    """活泼渐变风格"""
    if data is None:
        data = pd.read_csv('data.csv')
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            x=data['Month'],
            y=data['Revenue'],
            name="Revenue",
            marker=dict(
                color='rgb(158,202,225)'
            ),
            text=data['Revenue'].apply(lambda x: f'${x:,.0f}'),
            textposition='outside',
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Month'],
            y=data['Profit_Margin'],
            name="Profit Margin",
            line=dict(color='#FF6B6B', width=4),
            mode='lines+markers',
            marker=dict(
                size=12,
                symbol='star',
                line=dict(color='#FF6B6B', width=2)
            )
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title={
            'text': 'Monthly Revenue and Profit Margin',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(family="Comic Sans MS", size=20, color="#4A90E2")
        },
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(255, 255, 255, 0.8)',
        ),
        template='plotly_white',
        height=600,
        paper_bgcolor='white'
    )
    
    fig.update_yaxes(title_text="Revenue ($)", secondary_y=False, tickformat="$,.0f", gridcolor='#E5E7E9')
    fig.update_yaxes(title_text="Profit Margin (%)", secondary_y=True, ticksuffix="%", gridcolor='#E5E7E9')
    fig.update_xaxes(title_text="Month", tickangle=45, gridcolor='#E5E7E9')
    
    fig.write_image("折线-柱状图_style_3.png", width=1000, height=600)
    return fig

def plot_4(data=None):
    """暗色主题风格"""
    if data is None:
        data = pd.read_csv('data.csv')
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            x=data['Month'],
            y=data['Revenue'],
            name="Revenue",
            marker_color='rgba(46, 204, 113, 0.7)',
            text=data['Revenue'].apply(lambda x: f'${x:,.0f}'),
            textposition='outside',
            textfont=dict(color='white')
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Month'],
            y=data['Profit_Margin'],
            name="Profit Margin",
            line=dict(color='#F1C40F', width=3),
            mode='lines+markers',
            marker=dict(size=10, symbol='circle')
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title={
            'text': 'Monthly Revenue and Profit Margin',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(family="Arial", size=20, color="white")
        },
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(color='white')
        ),
        template='plotly_dark',
        height=600,
        paper_bgcolor='rgb(50, 50, 50)',
        plot_bgcolor='rgb(50, 50, 50)'
    )
    
    fig.update_yaxes(
        title_text="Revenue ($)", 
        secondary_y=False, 
        tickformat="$,.0f",
        gridcolor='rgba(255, 255, 255, 0.1)',
        tickfont=dict(color='white'),
        title_font=dict(color='white')
    )
    fig.update_yaxes(
        title_text="Profit Margin (%)", 
        secondary_y=True,
        ticksuffix="%",
        gridcolor='rgba(255, 255, 255, 0.1)',
        tickfont=dict(color='white'),
        title_font=dict(color='white')
    )
    fig.update_xaxes(
        title_text="Month",
        tickangle=45,
        gridcolor='rgba(255, 255, 255, 0.1)',
        tickfont=dict(color='white'),
        title_font=dict(color='white')
    )
    
    fig.write_image("折线-柱状图_style_4.png", width=1000, height=600)
    return fig

def plot_5(data=None):
    """柔和暖色风格"""
    if data is None:
        data = pd.read_csv('data.csv')
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            x=data['Month'],
            y=data['Revenue'],
            name="Revenue",
            marker_color='rgba(255, 164, 127, 0.7)',
            text=data['Revenue'].apply(lambda x: f'${x:,.0f}'),
            textposition='outside',
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Month'],
            y=data['Profit_Margin'],
            name="Profit Margin",
            line=dict(color='#FF7675', width=2.5),
            mode='lines+markers',
            marker=dict(
                size=9,
                symbol='circle',
                line=dict(color='#FF7675', width=2)
            )
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title={
            'text': 'Monthly Revenue and Profit Margin',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(family="Georgia", size=20, color="#6B4423")
        },
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(255, 248, 240, 0.8)',
        ),
        template='simple_white',
        height=600,
        paper_bgcolor='#FFF8F0',
        plot_bgcolor='#FFF8F0'
    )
    
    fig.update_yaxes(title_text="Revenue ($)", secondary_y=False, tickformat="$,.0f", gridcolor='#FFE4D6')
    fig.update_yaxes(title_text="Profit Margin (%)", secondary_y=True, ticksuffix="%", gridcolor='#FFE4D6')
    fig.update_xaxes(title_text="Month", tickangle=45, gridcolor='#FFE4D6')
    
    fig.write_image("折线-柱状图_style_5.png", width=1000, height=600)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
