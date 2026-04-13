import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def preprocess(data=None):
    # Generate sample data if none provided
    if data is None:
        np.random.seed(42)
        dates = pd.date_range(start='2023-01-01', periods=12, freq='M')
        
        # Generate realistic revenue data (millions) with slight upward trend
        revenue = np.linspace(1, 1.3, 12) * (1 + 0.1 * np.random.randn(12))
        revenue = np.round(revenue * 1e3, -1)  # Round to thousands
        
        # Generate profit margin data (percentage) with some correlation to revenue
        margin = 20 + 5 * np.random.randn(12) + np.linspace(0, 2, 12)
        margin = np.round(margin, 1)  # Round to 1 decimal place
        
        data = pd.DataFrame({
            'Date': dates,
            'Revenue': revenue,
            'Profit_Margin': margin
        })
    
    # Save to CSV
    data.to_csv('双Y轴折线图.csv', index=False)
    return data

def plot(data):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add revenue line
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Revenue'],
            name="Revenue",
            line=dict(color="#1f77b4", width=3),
            mode='lines+markers',
            marker=dict(size=8)
        ),
        secondary_y=False
    )
    
    # Add profit margin line
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Profit_Margin'],
            name="Profit Margin",
            line=dict(color="#ff7f0e", width=3),
            mode='lines+markers',
            marker=dict(size=8)
        ),
        secondary_y=True
    )
    
    # Update layout with titles and formatting
    fig.update_layout(
        title={
            'text': "Monthly Revenue and Profit Margin",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20)
        },
        template='plotly_white',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
                        x=0.99,
            orientation="h"
        ),
        hovermode='x unified',
        margin=dict(l=60, r=60, t=80, b=60)
    )
    
    # Configure axes
    fig.update_xaxes(
        title_text="Date",
        gridcolor='lightgray',
        tickformat="%b %Y"
    )
    
    fig.update_yaxes(
        title_text="Revenue ($)",
        secondary_y=False,
        gridcolor='lightgray',
        tickprefix="$"
    )
    
    fig.update_yaxes(
        title_text="Profit Margin (%)",
        secondary_y=True,
        gridcolor='lightgray',
        ticksuffix="%"
    )
    
    # Add custom hover template
    fig.update_traces(
        hovertemplate="<b>Date</b>: %{x|%b %Y}<br>" +
                      "<b>%{data.name}</b>: %{y:,.1f}" +
                      "<extra></extra>"
    )
    
    # Save plot
    fig.write_image("双Y轴折线图.png", width=1000, height=600)
    return fig

# Generate and plot data
data = preprocess()
fig = plot(data)

def plot_1(data):  # 商务简约风
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Revenue'],
            name="Revenue",
            line=dict(color="#234B6E", width=2.5),
            mode='lines+markers',
            marker=dict(size=7, symbol="circle")
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Profit_Margin'],
            name="Profit Margin",
            line=dict(color="#9B2335", width=2.5),
            mode='lines+markers',
            marker=dict(size=7, symbol="circle")
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title={
            'text': "Monthly Revenue and Profit Margin",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, family="Arial")
        },
        template='none',
        plot_bgcolor='white',
        paper_bgcolor='white',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            orientation="h"
        ),
        hovermode='x unified',
        margin=dict(l=60, r=60, t=80, b=60)
    )
    
    fig.update_xaxes(
        title_text="Date",
        gridcolor='#E5E5E5',
        tickformat="%b %Y",
        showgrid=True
    )
    
    fig.update_yaxes(
        title_text="Revenue ($)",
        secondary_y=False,
        gridcolor='#E5E5E5',
        tickprefix="$",
        showgrid=True
    )
    
    fig.update_yaxes(
        title_text="Profit Margin (%)",
        secondary_y=True,
        ticksuffix="%",
        showgrid=False
    )
    
    fig.update_traces(
        hovertemplate="<b>Date</b>: %{x|%b %Y}<br><b>%{data.name}</b>: %{y:,.1f}<extra></extra>"
    )
    
    fig.write_image("双Y轴折线图_style_1.png", width=1000, height=600)
    return fig

def plot_2(data):  # 科技感风格
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Revenue'],
            name="Revenue",
            line=dict(color="#4A90E2", width=3),
            mode='lines+markers',
            marker=dict(size=8, symbol="diamond")
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Profit_Margin'],
            name="Profit Margin",
            line=dict(color="#9013FE", width=3),
            mode='lines+markers',
            marker=dict(size=8, symbol="diamond")
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title={
            'text': "Monthly Revenue and Profit Margin",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, family="Roboto")
        },
        template='plotly_dark',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            orientation="h",
            bgcolor="rgba(0,0,0,0.5)"
        ),
        hovermode='x unified',
        margin=dict(l=60, r=60, t=80, b=60)
    )
    
    fig.update_xaxes(
        title_text="Date",
        gridcolor='rgba(255,255,255,0.1)',
        tickformat="%b %Y"
    )
    
    fig.update_yaxes(
        title_text="Revenue ($)",
        secondary_y=False,
        gridcolor='rgba(255,255,255,0.1)',
        tickprefix="$"
    )
    
    fig.update_yaxes(
        title_text="Profit Margin (%)",
        secondary_y=True,
        ticksuffix="%"
    )
    
    fig.update_traces(
        hovertemplate="<b>Date</b>: %{x|%b %Y}<br><b>%{data.name}</b>: %{y:,.1f}<extra></extra>"
    )
    
    fig.write_image("双Y轴折线图_style_2.png", width=1000, height=600)
    return fig

def plot_3(data):  # 清新自然风
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Revenue'],
            name="Revenue",
            line=dict(color="#2E8B57", width=2),
            mode='lines+markers',
            marker=dict(size=9, symbol="circle-open")
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Profit_Margin'],
            name="Profit Margin",
            line=dict(color="#8FBC8F", width=2),
            mode='lines+markers',
            marker=dict(size=9, symbol="circle-open")
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title={
            'text': "Monthly Revenue and Profit Margin",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, family="Georgia")
        },
        template='simple_white',
        plot_bgcolor='rgba(240,255,240,0.5)',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="center",
            x=0.5,
            orientation="h"
        ),
        hovermode='x unified',
        margin=dict(l=60, r=60, t=80, b=60)
    )
    
    fig.update_xaxes(
        title_text="Date",
        gridcolor='rgba(46,139,87,0.2)',
        tickformat="%b %Y"
    )
    
    fig.update_yaxes(
        title_text="Revenue ($)",
        secondary_y=False,
        gridcolor='rgba(46,139,87,0.2)',
        tickprefix="$"
    )
    
    fig.update_yaxes(
        title_text="Profit Margin (%)",
        secondary_y=True,
        ticksuffix="%"
    )
    
    fig.update_traces(
        hovertemplate="<b>Date</b>: %{x|%b %Y}<br><b>%{data.name}</b>: %{y:,.1f}<extra></extra>"
    )
    
    fig.write_image("双Y轴折线图_style_3.png", width=1000, height=600)
    return fig

def plot_4(data):  # 现代简约风
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Revenue'],
            name="Revenue",
            line=dict(color="#000000", width=1.5),
            mode='lines+markers',
            marker=dict(size=6, symbol="square")
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Profit_Margin'],
            name="Profit Margin",
            line=dict(color="#FF4500", width=1.5),
            mode='lines+markers',
            marker=dict(size=6, symbol="square")
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title={
            'text': "Monthly Revenue and Profit Margin",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, family="Helvetica")
        },
        template='simple_white',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            orientation="h"
        ),
        hovermode='x unified',
        margin=dict(l=60, r=60, t=80, b=60)
    )
    
    fig.update_xaxes(
        title_text="Date",
        gridcolor='#E5E5E5',
        tickformat="%b %Y"
    )
    
    fig.update_yaxes(
        title_text="Revenue ($)",
        secondary_y=False,
        gridcolor='#E5E5E5',
        tickprefix="$"
    )
    
    fig.update_yaxes(
        title_text="Profit Margin (%)",
        secondary_y=True,
        ticksuffix="%"
    )
    
    fig.update_traces(
        hovertemplate="<b>Date</b>: %{x|%b %Y}<br><b>%{data.name}</b>: %{y:,.1f}<extra></extra>"
    )
    
    fig.write_image("双Y轴折线图_style_4.png", width=1000, height=600)
    return fig

def plot_5(data):  # 典雅复古风
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Revenue'],
            name="Revenue",
            line=dict(color="#8B4513", width=2.5, dash='dot'),
            mode='lines+markers',
            marker=dict(size=8, symbol="star")
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Profit_Margin'],
            name="Profit Margin",
            line=dict(color="#CD853F", width=2.5, dash='dot'),
            mode='lines+markers',
            marker=dict(size=8, symbol="star")
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title={
            'text': "Monthly Revenue and Profit Margin",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, family="Times New Roman")
        },
        template='simple_white',
        plot_bgcolor='rgba(255,248,220,0.5)',
        paper_bgcolor='rgba(255,248,220,0.5)',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            orientation="h",
            bgcolor="rgba(255,248,220,0.8)"
        ),
        hovermode='x unified',
        margin=dict(l=60, r=60, t=80, b=60)
    )
    
    fig.update_xaxes(
        title_text="Date",
        gridcolor='rgba(139,69,19,0.2)',
        tickformat="%b %Y"
    )
    
    fig.update_yaxes(
        title_text="Revenue ($)",
        secondary_y=False,
        gridcolor='rgba(139,69,19,0.2)',
        tickprefix="$"
    )
    
    fig.update_yaxes(
        title_text="Profit Margin (%)",
        secondary_y=True,
        ticksuffix="%"
    )
    
    fig.update_traces(
        hovertemplate="<b>Date</b>: %{x|%b %Y}<br><b>%{data.name}</b>: %{y:,.1f}<extra></extra>"
    )
    
    fig.write_image("双Y轴折线图_style_5.png", width=1000, height=600)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
