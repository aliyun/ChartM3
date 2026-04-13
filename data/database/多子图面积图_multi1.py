import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

def preprocess(data=None):
    # Generate synthetic quarterly data for 3 years
    np.random.seed(42)
    dates = pd.date_range(start='2020-01-01', end='2022-12-31', freq='Q')
    
    # Create base metrics with different scales and patterns
    revenue = 1000 + np.random.normal(50, 10, len(dates)) + np.linspace(0, 200, len(dates))
    costs = 600 + np.random.normal(30, 5, len(dates)) + np.linspace(0, 100, len(dates))
    margin = 25 + np.random.normal(2, 1, len(dates)) - np.linspace(0, 5, len(dates))
    market_share = 35 + np.random.normal(3, 1, len(dates)) + np.sin(np.linspace(0, 4*np.pi, len(dates)))
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Revenue': revenue.round(0),
        'Costs': costs.round(0),
        'Profit_Margin': margin.round(1),
        'Market_Share': market_share.round(1)
    })
    
    # Save to CSV
    df.to_csv('多子图面积图.csv', index=False)
    return df

def plot(data):
    # Create figure with secondary y-axis
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Quarterly Revenue', 'Quarterly Costs', 
                       'Profit Margin', 'Market Share'),
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )

    # Color scheme
    colors = ['rgba(67, 133, 215, 0.7)', 'rgba(241, 90, 96, 0.7)', 
              'rgba(123, 192, 67, 0.7)', 'rgba(186, 104, 200, 0.7)']
    
    # Add traces
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Revenue'],
            fill='tozeroy',
            name='Revenue',
            line=dict(color=colors[0].replace('0.7', '1')),
            fillcolor=colors[0],
            hovertemplate='Date: %{x}<br>Revenue: $%{y:,.0f}K<extra></extra>'
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Costs'],
            fill='tozeroy',
            name='Costs',
            line=dict(color=colors[1].replace('0.7', '1')),
            fillcolor=colors[1],
                        hovertemplate='Date: %{x}<br>Costs: $%{y:,.0f}K<extra></extra>'
        ),
        row=1, col=2
    )

    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Profit_Margin'],
            fill='tozeroy',
            name='Profit Margin',
            line=dict(color=colors[2].replace('0.7', '1')),
            fillcolor=colors[2],
            hovertemplate='Date: %{x}<br>Margin: %{y:.1f}%<extra></extra>'
        ),
        row=2, col=1
    )

    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Market_Share'],
            fill='tozeroy',
            name='Market Share',
            line=dict(color=colors[3].replace('0.7', '1')),
            fillcolor=colors[3],
            hovertemplate='Date: %{x}<br>Share: %{y:.1f}%<extra></extra>'
        ),
        row=2, col=2
    )

    # Update layout
    fig.update_layout(
        height=800,
        showlegend=True,
        title_text="Company Performance Metrics",
        title_x=0.5,
        title_font_size=20,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        ),
        template='plotly_white'
    )

    # Update axes
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        tickangle=45,
        title_text='Date',
    )

    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        title_text='Revenue ($K)',
        row=1, col=1
    )
    fig.update_yaxes(
        title_text='Costs ($K)',
        row=1, col=2
    )
    fig.update_yaxes(
        title_text='Margin (%)',
        row=2, col=1
    )
    fig.update_yaxes(
        title_text='Share (%)',
        row=2, col=2
    )

    # Save to HTML
    fig.write_html('data.html')
    # Save to static image
    fig.write_image('多子图面积图.png', width=1200, height=800)


def plot_1(data):
    # 商务蓝风格
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Quarterly Revenue', 'Quarterly Costs', 
                       'Profit Margin', 'Market Share'),
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )

    colors = ['rgba(28, 69, 135, 0.7)', 'rgba(47, 109, 182, 0.7)', 
              'rgba(86, 152, 214, 0.7)', 'rgba(157, 195, 230, 0.7)']
    
    for idx, (col, title) in enumerate([('Revenue', 'Revenue ($K)'), 
                                      ('Costs', 'Costs ($K)'),
                                      ('Profit_Margin', 'Margin (%)'),
                                      ('Market_Share', 'Share (%)')]):
        row = idx // 2 + 1
        col_idx = idx % 2 + 1
        
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[col],
                fill='tozeroy',
                name=col.replace('_', ' '),
                line=dict(color=colors[idx].replace('0.7', '1'), width=2),
                fillcolor=colors[idx]
            ),
            row=row, col=col_idx
        )

    fig.update_layout(
        height=800,
        showlegend=True,
        title_text="Company Performance Metrics",
        title_x=0.5,
        title_font=dict(size=24, color='#1C4587'),
        paper_bgcolor='white',
        plot_bgcolor='white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                   xanchor="center", x=0.5),
        font=dict(family="Arial", size=12)
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, 
                     gridcolor='rgba(128,128,128,0.2)',
                     tickangle=45)
    fig.update_yaxes(showgrid=True, gridwidth=1, 
                     gridcolor='rgba(128,128,128,0.2)')

    fig.write_image('多子图面积图_style_1.png', width=1200, height=800)

def plot_2(data):
    # 活力多彩风格
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Quarterly Revenue', 'Quarterly Costs', 
                       'Profit Margin', 'Market Share'),
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )

    colors = ['rgba(255, 89, 94, 0.7)', 'rgba(255, 202, 58, 0.7)', 
              'rgba(138, 201, 38, 0.7)', 'rgba(25, 130, 196, 0.7)']

    for idx, (col, title) in enumerate([('Revenue', 'Revenue ($K)'), 
                                      ('Costs', 'Costs ($K)'),
                                      ('Profit_Margin', 'Margin (%)'),
                                      ('Market_Share', 'Share (%)')]):
        row = idx // 2 + 1
        col_idx = idx % 2 + 1
        
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[col],
                fill='tozeroy',
                name=col.replace('_', ' '),
                line=dict(color=colors[idx].replace('0.7', '1'), width=3),
                fillcolor=colors[idx],
                mode='lines+markers',
                marker=dict(size=8)
            ),
            row=row, col=col_idx
        )

    fig.update_layout(
        height=800,
        showlegend=True,
        title_text="Company Performance Metrics",
        title_x=0.5,
        title_font=dict(size=24, color='#FF595E'),
        paper_bgcolor='white',
        plot_bgcolor='rgba(240,240,240,0.3)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                   xanchor="center", x=0.5),
        font=dict(family="Roboto", size=12)
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, 
                     gridcolor='white',
                     tickangle=45)
    fig.update_yaxes(showgrid=True, gridwidth=1, 
                     gridcolor='white')

    fig.write_image('多子图面积图_style_2.png', width=1200, height=800)

def plot_3(data):
    # 极简黑白风格
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Quarterly Revenue', 'Quarterly Costs', 
                       'Profit Margin', 'Market Share'),
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )

    colors = ['rgba(0, 0, 0, 0.7)', 'rgba(70, 70, 70, 0.7)', 
              'rgba(140, 140, 140, 0.7)', 'rgba(200, 200, 200, 0.7)']

    for idx, (col, title) in enumerate([('Revenue', 'Revenue ($K)'), 
                                      ('Costs', 'Costs ($K)'),
                                      ('Profit_Margin', 'Margin (%)'),
                                      ('Market_Share', 'Share (%)')]):
        row = idx // 2 + 1
        col_idx = idx % 2 + 1
        
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[col],
                fill='tozeroy',
                name=col.replace('_', ' '),
                line=dict(color=colors[idx].replace('0.7', '1'), width=1),
                fillcolor=colors[idx]
            ),
            row=row, col=col_idx
        )

    fig.update_layout(
        height=800,
        showlegend=True,
        title_text="Company Performance Metrics",
        title_x=0.5,
        title_font=dict(size=24, color='black'),
        paper_bgcolor='white',
        plot_bgcolor='white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                   xanchor="center", x=0.5),
        font=dict(family="Helvetica", size=12)
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, 
                     gridcolor='rgba(0,0,0,0.1)',
                     tickangle=45)
    fig.update_yaxes(showgrid=True, gridwidth=1, 
                     gridcolor='rgba(0,0,0,0.1)')

    fig.write_image('多子图面积图_style_3.png', width=1200, height=800)

def plot_4(data):
    # 柔和暖色风格
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Quarterly Revenue', 'Quarterly Costs', 
                       'Profit Margin', 'Market Share'),
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )

    colors = ['rgba(255, 166, 158, 0.7)', 'rgba(250, 208, 196, 0.7)', 
              'rgba(255, 219, 172, 0.7)', 'rgba(255, 231, 205, 0.7)']

    for idx, (col, title) in enumerate([('Revenue', 'Revenue ($K)'), 
                                      ('Costs', 'Costs ($K)'),
                                      ('Profit_Margin', 'Margin (%)'),
                                      ('Market_Share', 'Share (%)')]):
        row = idx // 2 + 1
        col_idx = idx % 2 + 1
        
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[col],
                fill='tozeroy',
                name=col.replace('_', ' '),
                line=dict(color=colors[idx].replace('0.7', '1'), width=2),
                fillcolor=colors[idx]
            ),
            row=row, col=col_idx
        )

    fig.update_layout(
        height=800,
        showlegend=True,
        title_text="Company Performance Metrics",
        title_x=0.5,
        title_font=dict(size=24, color='#FF6B6B'),
        paper_bgcolor='#FFF5F5',
        plot_bgcolor='#FFF5F5',
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                   xanchor="center", x=0.5),
        font=dict(family="Comic Sans MS", size=12)
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, 
                     gridcolor='rgba(255,255,255,0.9)',
                     tickangle=45)
    fig.update_yaxes(showgrid=True, gridwidth=1, 
                     gridcolor='rgba(255,255,255,0.9)')

    fig.write_image('多子图面积图_style_4.png', width=1200, height=800)

def plot_5(data):
    # 科技感风格
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Quarterly Revenue', 'Quarterly Costs', 
                       'Profit Margin', 'Market Share'),
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )

    colors = ['rgba(0, 255, 255, 0.7)', 'rgba(0, 255, 128, 0.7)', 
              'rgba(128, 255, 0, 0.7)', 'rgba(255, 128, 255, 0.7)']

    for idx, (col, title) in enumerate([('Revenue', 'Revenue ($K)'), 
                                      ('Costs', 'Costs ($K)'),
                                      ('Profit_Margin', 'Margin (%)'),
                                      ('Market_Share', 'Share (%)')]):
        row = idx // 2 + 1
        col_idx = idx % 2 + 1
        
        fig.add_trace(
            go.Scatter(
                x=data['Date'],
                y=data[col],
                fill='tozeroy',
                name=col.replace('_', ' '),
                line=dict(color=colors[idx].replace('0.7', '1'), width=2),
                fillcolor=colors[idx]
            ),
            row=row, col=col_idx
        )

    fig.update_layout(
        height=800,
        showlegend=True,
        title_text="Company Performance Metrics",
        title_x=0.5,
        title_font=dict(size=24, color='#00FFFF'),
        paper_bgcolor='#1A1A1A',
        plot_bgcolor='#1A1A1A',
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                   xanchor="center", x=0.5,
                   font=dict(color='white')),
        font=dict(family="Arial Black", size=12, color='white')
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, 
                     gridcolor='rgba(255,255,255,0.1)',
                     tickangle=45, tickfont=dict(color='white'))
    fig.update_yaxes(showgrid=True, gridwidth=1, 
                     gridcolor='rgba(255,255,255,0.1)',
                     tickfont=dict(color='white'))

    fig.write_image('多子图面积图_style_5.png', width=1200, height=800)

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
