import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import random

def preprocess(data=None):
    # Generate sample temperature data if none provided
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Create realistic temperature ranges with seasonal pattern
    np.random.seed(42)
    temp_min = [random.uniform(-5, 5), random.uniform(-3, 7), random.uniform(2, 10),
                random.uniform(8, 15), random.uniform(12, 20), random.uniform(15, 25),
                random.uniform(18, 28), random.uniform(17, 27), random.uniform(14, 24),
                random.uniform(8, 18), random.uniform(2, 12), random.uniform(-2, 8)]
    
    temp_max = [min + random.uniform(5, 10) for min in temp_min]
    
    # Create DataFrame
    df = pd.DataFrame({
        'Month': months,
        'Min_Temp': temp_min,
        'Max_Temp': temp_max
    })
    
    # Save to CSV
    df.to_csv('区间柱状图.csv', index=False)
    return df

def plot(data):
    # Create range bar chart
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Temperature Range',
        x=data['Month'],
        y=data['Max_Temp'] - data['Min_Temp'],  # Height of bars
        base=data['Min_Temp'],                  # Starting point of bars
        marker_color='rgb(158,202,225)',
        marker_line_color='rgb(8,48,107)',
        marker_line_width=1.5,
        hovertemplate='Month: %{x}<br>' +
                      'Min Temp: %{base:.1f}°C<br>' +
                      'Max Temp: %{base+y:.1f}°C<br>' +
                      '<extra></extra>'
    ))

    # Customize layout
    fig.update_layout(
        title={
            'text': 'Monthly Temperature Ranges',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24)
        },
        xaxis_title="Month",
        yaxis_title="Temperature (°C)",
        font=dict(size=14),
        showlegend=False,
        plot_bgcolor='white',
        width=900,
        height=600,
        margin=dict(l=80, r=80, t=100, b=80)
    )
    
    # Customize axes
    fig.update_xaxes(
        tickangle=0,
        gridcolor='lightgray',
        gridwidth=0.5,
        zeroline=True,
        zerolinecolor='gray',
        zerolinewidth=1
    )
    
    fig.update_yaxes(
        gridcolor='lightgray',
        gridwidth=0.5,
        zeroline=True,
        zerolinecolor='gray',
        zerolinewidth=1
    )

    # Add value annotations
    for i in range(len(data)):
        fig.add_annotation(
            x=data['Month'][i],
            y=data['Max_Temp'][i],
            text=f"{data['Max_Temp'][i]:.1f}°C",
            yshift=10,
            showarrow=False,
            font=dict(size=12)
        )
        fig.add_annotation(
            x=data['Month'][i],
            y=data['Min_Temp'][i],
            text=f"{data['Min_Temp'][i]:.1f}°C",
            yshift=-20,
            showarrow=False,
            font=dict(size=12)
        )

    # Save plot
    fig.write_image("区间柱状图.png")
    return fig


def plot_1(data):
    # 商务蓝灰风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['Month'],
        y=data['Max_Temp'] - data['Min_Temp'],
        base=data['Min_Temp'],
        marker_color='rgba(65, 105, 225, 0.7)',
        marker_line_color='rgba(25, 25, 112, 1)',
        marker_line_width=1.5
    ))

    fig.update_layout(
        title={
            'text': 'Monthly Temperature Ranges',
            'font': dict(family='Arial', size=24, color='#2F4F4F')
        },
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Arial', size=12),
        width=900, height=600,
        margin=dict(l=80, r=80, t=100, b=80)
    )

    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgrey')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgrey')

    for i in range(len(data)):
        fig.add_annotation(
            x=data['Month'][i],
            y=data['Max_Temp'][i],
            text=f"{data['Max_Temp'][i]:.1f}°C",
            font=dict(family='Arial', size=10),
            yshift=10,
            showarrow=False
        )
    
    fig.write_image("区间柱状图_style_1.png")
    return fig

def plot_2(data):
    # 自然渐变风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['Month'],
        y=data['Max_Temp'] - data['Min_Temp'],
        base=data['Min_Temp'],
        marker=dict(
            color='rgb(102, 197, 204)',
            # gradient=dict(
            #     type='vertical',
            #     color='rgb(246, 207, 113)'
            # )
        ),
        marker_line_color='white',
        marker_line_width=0.5
    ))

    fig.update_layout(
        title={
            'text': 'Temperature Variations',
            'font': dict(family='Verdana', size=24, color='#445566')
        },
        plot_bgcolor='rgba(240,240,240,0.3)',
        paper_bgcolor='white',
        font=dict(family='Verdana'),
        width=900, height=600
    )

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='white', gridwidth=2)

    fig.write_image("区间柱状图_style_2.png")
    return fig

def plot_3(data):
    # 科技暗色风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['Month'],
        y=data['Max_Temp'] - data['Min_Temp'],
        base=data['Min_Temp'],
        marker_color='rgba(0, 255, 255, 0.6)',
        marker_line_color='rgb(0, 255, 255)',
        marker_line_width=1
    ))

    fig.update_layout(
        title={
            'text': 'Temperature Analysis',
            'font': dict(family='Roboto', size=24, color='white')
        },
        plot_bgcolor='rgb(17,17,17)',
        paper_bgcolor='rgb(17,17,17)',
        font=dict(color='white'),
        width=900, height=600
    )

    fig.update_xaxes(showgrid=True, gridcolor='rgba(128,128,128,0.2)')
    fig.update_yaxes(showgrid=True, gridcolor='rgba(128,128,128,0.2)')

    fig.write_image("区间柱状图_style_3.png")
    return fig

def plot_4(data):
    # 活泼彩色风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['Month'],
        y=data['Max_Temp'] - data['Min_Temp'],
        base=data['Min_Temp'],
        marker_color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', 
                     '#FF99CC', '#99FFCC', '#FFB366', '#99FF99', 
                     '#FF99FF', '#99CCFF', '#FFB366', '#99FF99'],
        marker_line_color='white',
        marker_line_width=1.5
    ))

    fig.update_layout(
        title={
            'text': '🌡️ Temperature Range Chart 🌡️',
            'font': dict(family='Comic Sans MS', size=24)
        },
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Comic Sans MS'),
        width=900, height=600
    )

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='rgba(200,200,200,0.2)')

    fig.write_image("区间柱状图_style_4.png")
    return fig

def plot_5(data):
    # 极简风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=data['Month'],
        y=data['Max_Temp'] - data['Min_Temp'],
        base=data['Min_Temp'],
        marker_color='rgb(200,200,200)',
        marker_line_color='rgb(100,100,100)',
        marker_line_width=0.5
    ))

    fig.update_layout(
        title={
            'text': 'Temperature Range',
            'font': dict(family='Helvetica', size=24, color='black')
        },
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Helvetica'),
        showlegend=False,
        width=900, height=600,
        margin=dict(l=40, r=40, t=80, b=40)
    )

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    fig.write_image("区间柱状图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
