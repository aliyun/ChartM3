import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

def preprocess(data=None):
    # Generate 30 days of sample OHLC data
    np.random.seed(42)
    
    # Generate dates (excluding weekends)
    dates = []
    start_date = datetime(2023, 1, 1)
    while len(dates) < 30:
        if start_date.weekday() < 5:  # Monday = 0, Friday = 4
            dates.append(start_date)
        start_date += timedelta(days=1)
    
    # Generate price data
    base_price = 100
    volatility = 0.02
    
    opens = [base_price]
    highs = []
    lows = []
    closes = []
    
    # Generate realistic price movements
    for i in range(30):
        if i > 0:
            opens.append(closes[-1])
        
        close = opens[i] * (1 + np.random.normal(0, volatility))
        high = max(opens[i], close) * (1 + abs(np.random.normal(0, volatility/2)))
        low = min(opens[i], close) * (1 - abs(np.random.normal(0, volatility/2)))
        
        highs.append(high)
        lows.append(low)
        closes.append(close)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Open': opens,
        'High': highs,
        'Low': lows,
        'Close': closes
    })
    
    # Save to CSV
    df.to_csv('蜡烛图.csv', index=False)
    return df

def plot(data):
    # Create candlestick chart
    fig = go.Figure()
    
    # Add candlestick trace
    fig.add_trace(go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='OHLC',
        increasing_line_color='#26A69A',
        decreasing_line_color='#EF5350',
        showlegend=True
    ))
    
    # Update layout
    fig.update_layout(
        title={
            'text': 'Stock Price Movement',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        yaxis_title='Price ($)',
        xaxis_title='Date',
        template='plotly_white',
        height=600,
        width=1000,
        yaxis={
            'gridcolor': '#eee',
            'zerolinecolor': '#666',
            'tickformat': '.2f',
            'tickprefix': '$'
        },
        xaxis={
            'gridcolor': '#eee',
            'rangeslider': {'visible': False}
        },
        hoverlabel={
            'bgcolor': 'white',
            'font_size': 12
        },
        margin=dict(l=50, r=50, t=50, b=50),
        # 设置hover模板
        hovermode='x',
        hoverdistance=100,
    )

    # Save figure
    fig.write_image("蜡烛图.png")
    fig.write_html("data.html")
    return fig

# Example usage

def plot_1(data):
    # 专业金融风格
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        increasing_line_color='#1f77b4',
        decreasing_line_color='#ff7f0e',
        showlegend=True
    ))
    
    fig.update_layout(
        title={
            'text': 'Professional Trading View',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#2c3e50')
        },
        yaxis_title='Price ($)',
        xaxis_title='Date',
        template='none',
        height=600,
        width=1000,
        plot_bgcolor='white',
        paper_bgcolor='white',
        yaxis={
            'gridcolor': '#ecf0f1',
            'zerolinecolor': '#2c3e50',
            'tickformat': '.2f',
            'tickprefix': '$',
            'linewidth': 2,
            'linecolor': '#2c3e50'
        },
        xaxis={
            'gridcolor': '#ecf0f1',
            'rangeslider': {'visible': False},
            'linewidth': 2,
            'linecolor': '#2c3e50'
        },
        hoverlabel={'bgcolor': 'white', 'font_size': 12},
        margin=dict(l=50, r=50, t=50, b=50)
    )
    fig.write_image("蜡烛图_style_1.png")
    return fig

def plot_2(data):
    # 环保主题风格
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        increasing_line_color='#2ecc71',
        decreasing_line_color='#e74c3c',
        showlegend=True
    ))
    
    fig.update_layout(
        title={
            'text': 'Eco-Friendly Trading View',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#27ae60')
        },
        yaxis_title='Price ($)',
        xaxis_title='Date',
        template='none',
        height=600,
        width=1000,
        plot_bgcolor='#f9fefe',
        paper_bgcolor='#f9fefe',
        yaxis={
            'gridcolor': '#d5f5e3',
            'zerolinecolor': '#27ae60',
            'tickformat': '.2f',
            'tickprefix': '$'
        },
        xaxis={
            'gridcolor': '#d5f5e3',
            'rangeslider': {'visible': False}
        },
        hoverlabel={'bgcolor': '#f9fefe', 'font_size': 12}
    )
    fig.write_image("蜡烛图_style_2.png")
    return fig

def plot_3(data):
    # 科技风格
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        increasing_line_color='#9b59b6',
        decreasing_line_color='#3498db',
        showlegend=True
    ))
    
    fig.update_layout(
        title={
            'text': 'Tech Trading View',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#8e44ad')
        },
        yaxis_title='Price ($)',
        xaxis_title='Date',
        template='none',
        height=600,
        width=1000,
        plot_bgcolor='#f0f3f6',
        paper_bgcolor='#f0f3f6',
        yaxis={
            'gridcolor': '#dfe4ea',
            'zerolinecolor': '#8e44ad',
            'tickformat': '.2f',
            'tickprefix': '$'
        },
        xaxis={
            'gridcolor': '#dfe4ea',
            'rangeslider': {'visible': False}
        },
        hoverlabel={'bgcolor': '#f0f3f6', 'font_size': 12}
    )
    fig.write_image("蜡烛图_style_3.png")
    return fig

def plot_4(data):
    # 温暖风格
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        increasing_line_color='#e67e22',
        decreasing_line_color='#d35400',
        showlegend=True
    ))
    
    fig.update_layout(
        title={
            'text': 'Warm Trading View',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#d35400')
        },
        yaxis_title='Price ($)',
        xaxis_title='Date',
        template='none',
        height=600,
        width=1000,
        plot_bgcolor='#fff5eb',
        paper_bgcolor='#fff5eb',
        yaxis={
            'gridcolor': '#fae5d3',
            'zerolinecolor': '#d35400',
            'tickformat': '.2f',
            'tickprefix': '$'
        },
        xaxis={
            'gridcolor': '#fae5d3',
            'rangeslider': {'visible': False}
        },
        hoverlabel={'bgcolor': '#fff5eb', 'font_size': 12}
    )
    fig.write_image("蜡烛图_style_4.png")
    return fig

def plot_5(data):
    # 现代简约风格
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        increasing_line_color='#2c3e50',
        decreasing_line_color='#7f8c8d',
        showlegend=True
    ))
    
    fig.update_layout(
        title={
            'text': 'Minimalist Trading View',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#2c3e50')
        },
        yaxis_title='Price ($)',
        xaxis_title='Date',
        template='none',
        height=600,
        width=1000,
        plot_bgcolor='white',
        paper_bgcolor='white',
        yaxis={
            'gridcolor': '#f8f9f9',
            'zerolinecolor': '#2c3e50',
            'tickformat': '.2f',
            'tickprefix': '$',
            'showgrid': False
        },
        xaxis={
            'gridcolor': '#f8f9f9',
            'rangeslider': {'visible': False},
            'showgrid': False
        },
        hoverlabel={'bgcolor': 'white', 'font_size': 12}
    )
    fig.write_image("蜡烛图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
