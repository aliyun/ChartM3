import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def preprocess(data=None):
    # Generate sample data if none provided
    if data is None:
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        avg_bill = [35.5, 42.8, 38.2, 44.5, 48.2, 45.7]
        customers = [320, 380, 450, 410, 390, 485]
        
        data = pd.DataFrame({
            'Month': months,
            'Average Bill ($)': avg_bill,
            'Number of Customers': customers
        })
    
    # Validate data
    required_cols = ['Month', 'Average Bill ($)', 'Number of Customers']
    if not all(col in data.columns for col in required_cols):
        raise ValueError("Data must contain columns: " + ", ".join(required_cols))
    
    # Save to CSV
    data.to_csv('双Y轴柱状图.csv', index=False)
    return data

def plot(data):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add bars for average bill
    fig.add_trace(
        go.Bar(
            name="Average Bill",
            x=data['Month'],
            y=data['Average Bill ($)'],
            marker=dict(
                color='rgba(58,134,192,0.7)',
                line=dict(color='rgb(58,134,192)', width=2)
            ),
            text=data['Average Bill ($)'].round(1),
            textposition='outside',
            offsetgroup=0
        ),
        secondary_y=False
    )

    # Add bars for customer count
    fig.add_trace(
        go.Bar(
            name="Number of Customers",
            x=data['Month'],
            y=data['Number of Customers'],
            marker=dict(
                color='rgba(244,170,88,0.7)',
                line=dict(color='rgb(244,170,88)', width=2)
            ),
            text=data['Number of Customers'],
            textposition='outside',
            offsetgroup=1
        ),
        secondary_y=True
    )

    # Update layout
    fig.update_layout(
        title={
            'text': 'Restaurant Performance Metrics by Month',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20)
        },
        legend=dict(
            yanchor="top",
            y=1.1,
            xanchor="right",
            x=1,
            orientation="h"
        ),
        barmode='group',
        bargap=0.15,
        bargroupgap=0.1,
                plot_bgcolor='white',
        showlegend=True,
        height=600
    )

    # Update axes
    fig.update_xaxes(
        title_text="Month",
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray',
        showline=True,
        linewidth=1,
        linecolor='black'
    )

    fig.update_yaxes(
        title_text="Average Bill ($)",
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray',
        showline=True,
        linewidth=1,
        linecolor='black',
        secondary_y=False
    )

    fig.update_yaxes(
        title_text="Number of Customers",
        showgrid=False,
        showline=True,
        linewidth=1,
        linecolor='black',
        secondary_y=True
    )

    # Save plot
    fig.write_image("双Y轴柱状图.png")
    return fig

# Example usage

def plot_1(data):
    # 商务专业风格 - 蓝灰配色
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            name="Average Bill",
            x=data['Month'],
            y=data['Average Bill ($)'],
            marker_color='rgb(66, 133, 244)',
            text=data['Average Bill ($)'].round(1),
            textposition='outside',
            offsetgroup=0
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Bar(
            name="Number of Customers",
            x=data['Month'],
            y=data['Number of Customers'],
            marker_color='rgb(189, 189, 189)',
            text=data['Number of Customers'],
            textposition='outside',
            offsetgroup=1
        ),
        secondary_y=True
    )

    fig.update_layout(
        title={
            'text': 'Restaurant Performance Metrics',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, color='#444444')
        },
        legend=dict(
            yanchor="top",
            y=1.1,
            xanchor="right",
            x=1,
            orientation="h"
        ),
        barmode='group',
        plot_bgcolor='white',
        font=dict(family="Arial"),
        height=600
    )

    fig.update_xaxes(showgrid=False, showline=True, linecolor='black')
    fig.update_yaxes(showgrid=True, gridcolor='#E5E5E5', secondary_y=False)
    fig.update_yaxes(showgrid=False, secondary_y=True)

    fig.write_image("双Y轴柱状图_style_1.png")
    return fig

def plot_2(data):
    # 现代简约风格 - 渐变色
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            name="Average Bill",
            x=data['Month'],
            y=data['Average Bill ($)'],
            marker=dict(
                color=data['Average Bill ($)'],
                colorscale='Viridis'
            ),
            text=data['Average Bill ($)'].round(1),
            textposition='outside',
            offsetgroup=0
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Bar(
            name="Number of Customers",
            x=data['Month'],
            y=data['Number of Customers'],
            marker=dict(
                color=data['Number of Customers'],
                colorscale='Magma'
            ),
            text=data['Number of Customers'],
            textposition='outside',
            offsetgroup=1
        ),
        secondary_y=True
    )

    fig.update_layout(
        title={
            'text': 'Monthly Performance Analysis',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, color='#333333', family='Helvetica')
        },
        legend=dict(
            yanchor="top",
            y=1.1,
            xanchor="right",
            x=1,
            orientation="h"
        ),
        barmode='group',
        plot_bgcolor='white',
        height=600
    )

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='#f0f0f0', secondary_y=False)
    fig.update_yaxes(showgrid=False, secondary_y=True)

    fig.write_image("双Y轴柱状图_style_2.png")
    return fig

def plot_3(data):
    # 深色主题
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            name="Average Bill",
            x=data['Month'],
            y=data['Average Bill ($)'],
            marker_color='rgb(0, 255, 255)',
            text=data['Average Bill ($)'].round(1),
            textposition='outside',
            offsetgroup=0
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Bar(
            name="Number of Customers",
            x=data['Month'],
            y=data['Number of Customers'],
            marker_color='rgb(255, 128, 0)',
            text=data['Number of Customers'],
            textposition='outside',
            offsetgroup=1
        ),
        secondary_y=True
    )

    fig.update_layout(
        title={
            'text': 'Performance Dashboard',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, color='white')
        },
        paper_bgcolor='rgb(17,17,17)',
        plot_bgcolor='rgb(17,17,17)',
        font=dict(color='white'),
        legend=dict(
            yanchor="top",
            y=1.1,
            xanchor="right",
            x=1,
            orientation="h"
        ),
        barmode='group',
        height=600
    )

    fig.update_xaxes(showgrid=True, gridcolor='rgba(128,128,128,0.2)', linecolor='gray')
    fig.update_yaxes(showgrid=True, gridcolor='rgba(128,128,128,0.2)', linecolor='gray', secondary_y=False)
    fig.update_yaxes(showgrid=False, linecolor='gray', secondary_y=True)

    fig.write_image("双Y轴柱状图_style_3.png")
    return fig

def plot_4(data):
    # 活泼配色风格
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            name="Average Bill",
            x=data['Month'],
            y=data['Average Bill ($)'],
            marker=dict(
                color='rgb(255,105,180)',
                line=dict(color='rgb(255,20,147)', width=1.5)
            ),
            text=data['Average Bill ($)'].round(1),
            textposition='outside',
            offsetgroup=0
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Bar(
            name="Number of Customers",
            x=data['Month'],
            y=data['Number of Customers'],
            marker=dict(
                color='rgb(135,206,250)',
                line=dict(color='rgb(30,144,255)', width=1.5)
            ),
            text=data['Number of Customers'],
            textposition='outside',
            offsetgroup=1
        ),
        secondary_y=True
    )

    fig.update_layout(
        title={
            'text': 'Fun Performance Metrics',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, family='Comic Sans MS')
        },
        legend=dict(
            yanchor="top",
            y=1.1,
            xanchor="right",
            x=1,
            orientation="h"
        ),
        barmode='group',
        plot_bgcolor='rgb(255,250,250)',
        paper_bgcolor='rgb(255,250,250)',
        height=600
    )

    fig.update_xaxes(showgrid=True, gridcolor='rgba(255,192,203,0.3)')
    fig.update_yaxes(showgrid=True, gridcolor='rgba(255,192,203,0.3)', secondary_y=False)
    fig.update_yaxes(showgrid=False, secondary_y=True)

    fig.write_image("双Y轴柱状图_style_4.png")
    return fig

def plot_5(data):
    # 报告型风格
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(
            name="Average Bill",
            x=data['Month'],
            y=data['Average Bill ($)'],
            marker=dict(
                color='rgb(55,126,184)',
                line=dict(color='rgb(25,82,131)', width=1)
            ),
            text=data['Average Bill ($)'].round(1),
            textposition='outside',
            offsetgroup=0
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Bar(
            name="Number of Customers",
            x=data['Month'],
            y=data['Number of Customers'],
            marker=dict(
                color='rgb(228,26,28)',
                line=dict(color='rgb(178,0,0)', width=1)
            ),
            text=data['Number of Customers'],
            textposition='outside',
            offsetgroup=1
        ),
        secondary_y=True
    )

    fig.update_layout(
        title={
            'text': 'Monthly Business Report',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=20, family='Times New Roman')
        },
        legend=dict(
            yanchor="top",
            y=1.1,
            xanchor="right",
            x=1,
            orientation="h",
            bgcolor='rgba(255,255,255,0.9)'
        ),
        barmode='group',
        plot_bgcolor='white',
        height=600
    )

    fig.update_xaxes(showgrid=True, gridcolor='lightgray', zeroline=True, zerolinecolor='black')
    fig.update_yaxes(showgrid=True, gridcolor='lightgray', zeroline=True, zerolinecolor='black', secondary_y=False)
    fig.update_yaxes(showgrid=False, zeroline=True, zerolinecolor='black', secondary_y=True)

    fig.write_image("双Y轴柱状图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
