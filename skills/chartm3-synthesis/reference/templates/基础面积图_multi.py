import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

def preprocess(data=None):
    # Generate sample monthly sales data
    np.random.seed(42)
    
    # Create date range for 2 years of monthly data
    dates = pd.date_range(start='2022-01-01', end='2023-12-31', freq='M')
    
    # Generate base sales with upward trend and seasonal variation
    base_trend = np.linspace(100, 140, len(dates))  # Gradual upward trend
    seasonal = 15 * np.sin(np.linspace(0, 4*np.pi, len(dates)))  # Seasonal pattern
    noise = np.random.normal(0, 5, len(dates))  # Random variation
    
    sales = base_trend + seasonal + noise
    sales = np.round(sales, 1)  # Round to 1 decimal place
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Sales': sales
    })
    
    # Save to CSV
    df.to_csv('基础面积图.csv', index=False)
    return df

def plot(data):
    # Create figure
    fig = go.Figure()
    
    # Add area trace
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Sales'],
        fill='tozeroy',  # Fill to x-axis
        fillcolor='rgba(65, 105, 225, 0.3)',  # Semi-transparent royal blue
        line=dict(color='rgb(65, 105, 225)', width=2),
        name='Monthly Sales',
        hovertemplate='Date: %{x|%B %Y}<br>Sales: $%{y:.1f}K<extra></extra>'
    ))
    
    # Update layout
    fig.update_layout(
        title=dict(
            text='Monthly Sales Performance',
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor='top',
            font=dict(size=20)
        ),
        xaxis=dict(
            title='Date',
            showgrid=True,
            gridcolor='rgba(211, 211, 211, 0.5)',
            gridwidth=1,
            tickangle=-45,  # Rotate labels for better readability
            tickformat='%Y-%m',  # Show as YYYY-MM
            dtick='M1',  # Show every month
            tickmode='linear'
        ),
        yaxis=dict(
            title='Sales (Thousands $)',
            showgrid=True,
            gridcolor='rgba(211, 211, 211, 0.5)',
            gridwidth=1,
            zeroline=True,
            zerolinecolor='rgba(211, 211, 211, 1)',
            zerolinewidth=1
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        margin=dict(l=80, r=50, t=100, b=80),
        width=1000,
        height=600,
        hovermode='x unified'
    )
    
    # Save figure
    fig.write_image("基础面积图.png")
    
    return fig


def plot_1(data):
    # 现代简约风格 - 深色主题
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Sales'],
        fill='tozeroy',
        fillcolor='rgba(50, 171, 96, 0.4)',
        line=dict(color='rgb(50, 171, 96)', width=2),
        name='Monthly Sales',
        hovertemplate='%{x|%B %Y}<br>Sales: $%{y:.1f}K<extra></extra>'
    ))
    
    fig.update_layout(
        template='plotly_dark',
        title=dict(
            text='Monthly Sales Performance',
            x=0.5,
            y=0.95,
            font=dict(size=24, family='Arial Black')
        ),
        xaxis=dict(
            title='Date',
            showgrid=True,
            gridcolor='rgba(211, 211, 211, 0.2)',
            tickangle=-45,
            tickformat='%Y-%m'
        ),
        yaxis=dict(
            title='Sales (Thousands $)',
            showgrid=True,
            gridcolor='rgba(211, 211, 211, 0.2)'
        ),
        width=1000,
        height=600,
        showlegend=False,
        hovermode='x unified'
    )
    
    # Save figure
    fig.write_image("基础面积图_style1.png")

    return fig

def plot_2(data):
    # 柔和暖色系风格
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Sales'],
        fill='tozeroy',
        fillcolor='rgba(255, 127, 80, 0.3)',
        line=dict(color='rgb(255, 127, 80)', width=3),
        name='Monthly Sales',
        hovertemplate='%{x|%B %Y}<br>Sales: $%{y:.1f}K<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(
            text='Monthly Sales Performance',
            x=0.5,
            y=0.95,
            font=dict(size=22, family='Verdana', color='#444444')
        ),
        xaxis=dict(
            title='Date',
            showgrid=False,
            tickangle=-45,
            tickformat='%Y-%m'
        ),
        yaxis=dict(
            title='Sales (Thousands $)',
            showgrid=True,
            gridcolor='rgba(244, 164, 96, 0.3)'
        ),
        plot_bgcolor='#fff9f5',
        paper_bgcolor='#fff9f5',
        width=1000,
        height=600,
        showlegend=False,
        hovermode='x unified'
    )

    # Save figure
    fig.write_image("基础面积图_style2.png")
    
    return fig

def plot_3(data):
    # 商务蓝风格
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Sales'],
        fill='tonexty',
        fillcolor='rgba(0, 123, 255, 0.1)',
        line=dict(color='rgb(0, 123, 255)', width=2),
        name='Monthly Sales',
        hovertemplate='%{x|%B %Y}<br>Sales: $%{y:.1f}K<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(
            text='Monthly Sales Performance',
            x=0.5,
            y=0.95,
            font=dict(size=20, family='Arial', color='#003366')
        ),
        xaxis=dict(
            title='Date',
            showgrid=True,
            gridcolor='rgba(233, 236, 239, 0.8)',
            tickangle=-45,
            tickformat='%Y-%m'
        ),
        yaxis=dict(
            title='Sales (Thousands $)',
            showgrid=True,
            gridcolor='rgba(233, 236, 239, 0.8)'
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        width=1000,
        height=600,
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ),
        hovermode='x unified'
    )

    # Save figure
    fig.write_image("基础面积图_style3.png")
    
    return fig

def plot_4(data):
    # 科技感风格
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Sales'],
        fill='tozeroy',
        fillcolor='rgba(45, 203, 167, 0.2)',
        line=dict(color='rgb(45, 203, 167)', width=2.5),
        name='Monthly Sales',
        hovertemplate='%{x|%B %Y}<br>Sales: $%{y:.1f}K<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(
            text='Monthly Sales Performance',
            x=0.5,
            y=0.95,
            font=dict(size=24, family='Roboto', color='#1a1a1a')
        ),
        xaxis=dict(
            title='Date',
            showgrid=True,
            gridcolor='rgba(230, 230, 230, 0.8)',
            tickangle=-45,
            tickformat='%Y-%m'
        ),
        yaxis=dict(
            title='Sales (Thousands $)',
            showgrid=True,
            gridcolor='rgba(230, 230, 230, 0.8)'
        ),
        plot_bgcolor='rgb(250, 250, 250)',
        paper_bgcolor='rgb(250, 250, 250)',
        width=1000,
        height=600,
        showlegend=False,
        hovermode='x unified'
    )

    # Save figure
    fig.write_image("基础面积图_style4.png")
    
    return fig

def plot_5(data):
    # 复古风格
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Sales'],
        fill='tozeroy',
        fillcolor='rgba(205, 133, 63, 0.3)',
        line=dict(color='rgb(139, 69, 19)', width=2),
        name='Monthly Sales',
        hovertemplate='%{x|%B %Y}<br>Sales: $%{y:.1f}K<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(
            text='Monthly Sales Performance',
            x=0.5,
            y=0.95,
            font=dict(size=22, family='Times New Roman', color='#8B4513')
        ),
        xaxis=dict(
            title='Date',
            showgrid=True,
            gridcolor='rgba(222, 184, 135, 0.3)',
            tickangle=-45,
            tickformat='%Y-%m'
        ),
        yaxis=dict(
            title='Sales (Thousands $)',
            showgrid=True,
            gridcolor='rgba(222, 184, 135, 0.3)'
        ),
        plot_bgcolor='rgba(255, 248, 220, 0.5)',
        paper_bgcolor='rgba(255, 248, 220, 0.5)',
        width=1000,
        height=600,
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(255, 248, 220, 0.8)'
        ),
        hovermode='x unified'
    )

    # Save figure
    fig.write_image("基础面积图_style5.png")
    
    return fig

if __name__ == "__main__":
    # Generate and process data
    data = preprocess()
    
    # Create and save plot
    fig = plot(data)
    fig = plot_1(data)
    fig = plot_2(data)
    fig = plot_3(data)
    fig = plot_4(data)
    fig = plot_5(data)
