import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    # Create hierarchical data for renewable energy production
    data = {
        'id': [
            'Renewable Energy',
            'Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal',
            'Solar PV', 'Solar Thermal', 'CSP',
            'Onshore Wind', 'Offshore Wind',
            'Large Hydro', 'Small Hydro',
            'Wood', 'Waste', 'Biogas',
            'Binary Plant', 'Flash Plant', 'Dry Steam'
        ],
        'parent': [
            '',
            'Renewable Energy', 'Renewable Energy', 'Renewable Energy', 'Renewable Energy', 'Renewable Energy',
            'Solar', 'Solar', 'Solar',
            'Wind', 'Wind',
            'Hydro', 'Hydro',
            'Biomass', 'Biomass', 'Biomass',
            'Geothermal', 'Geothermal', 'Geothermal'
        ],
        'value': [
            1000,
            300, 250, 200, 150, 100,
            150, 100, 50,
            150, 100,
            150, 50,
            70, 50, 30,
            40, 35, 25
        ]
    }
    
    df = pd.DataFrame(data)
    df.to_csv('旭日图.csv', index=False)
    return df

def plot(data):
    # Create sunburst chart
    fig = go.Figure(go.Sunburst(
        labels=data['id'],
        parents=data['parent'],
        values=data['value'],
        branchvalues="total",
        textfont=dict(size=14),
        insidetextorientation='radial'
    ))

    # Update layout for professional appearance
    fig.update_layout(
        title={
            'text': "Global Renewable Energy Production Breakdown",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24)
        },
        width=1000,
        height=1000,
        showlegend=False,
        template='plotly_white'
    )

    # Save figure
    fig.write_image("旭日图.png")


def plot_1(data):
    # 商务风格：深蓝色调
    fig = go.Figure(go.Sunburst(
        labels=data['id'],
        parents=data['parent'],
        values=data['value'],
        branchvalues="total",
        textfont=dict(size=14, color='white'),
        insidetextorientation='radial',
        marker=dict(
            colors=['#1f77b4', '#2c3e50', '#34495e', '#487eb0', '#40739e',
                   '#273c75', '#192a56', '#0097e6', '#00a8ff', '#25CCF7',
                   '#1B9CFC', '#1B9CFC', '#1B9CFC', '#1B9CFC', '#1B9CFC']
        )
    ))
    
    fig.update_layout(
        title={
            'text': "Renewable Energy Production (Business Style)",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#2c3e50')
        },
        width=1000,
        height=1000,
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    fig.write_image("旭日图_style_1.png")

def plot_2(data):
    # 环保风格：绿色系
    fig = go.Figure(go.Sunburst(
        labels=data['id'],
        parents=data['parent'],
        values=data['value'],
        branchvalues="total",
        textfont=dict(size=14),
        insidetextorientation='radial',
        marker=dict(
            colors=['#2ecc71', '#27ae60', '#219653', '#1e8449', '#196f3d',
                   '#145a32', '#0b5345', '#186a3b', '#239b56', '#28b463',
                   '#2ecc71', '#48c9b0', '#45b39d', '#52be80', '#58d68d']
        )
    ))
    
    fig.update_layout(
        title={
            'text': "Renewable Energy Production (Eco Style)",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#27ae60')
        },
        width=1000,
        height=1000,
        showlegend=False,
        template='plotly_white'
    )
    
    fig.write_image("旭日图_style_2.png")

def plot_3(data):
    # 现代科技风格：深色背景
    fig = go.Figure(go.Sunburst(
        labels=data['id'],
        parents=data['parent'],
        values=data['value'],
        branchvalues="total",
        textfont=dict(size=14, color='white'),
        insidetextorientation='radial',
        marker=dict(
            colors=['#00ffff', '#00bfff', '#007fff', '#0040ff', '#0000ff',
                   '#4000ff', '#8000ff', '#bf00ff', '#ff00ff', '#ff00bf',
                   '#ff0080', '#ff0040', '#ff0000', '#ff4000', '#ff8000']
        )
    ))
    
    fig.update_layout(
        title={
            'text': "Renewable Energy Production (Tech Style)",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='white')
        },
        width=1000,
        height=1000,
        showlegend=False,
        paper_bgcolor='rgb(17,17,17)',
        plot_bgcolor='rgb(17,17,17)'
    )
    
    fig.write_image("旭日图_style_3.png")

def plot_4(data):
    # 活泼风格：彩虹色
    fig = go.Figure(go.Sunburst(
        labels=data['id'],
        parents=data['parent'],
        values=data['value'],
        branchvalues="total",
        textfont=dict(size=14),
        insidetextorientation='radial',
        marker=dict(
            colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD',
                   '#D4A5A5', '#9B59B6', '#3498DB', '#1ABC9C', '#F1C40F',
                   '#E74C3C', '#2ECC71', '#E67E22', '#95A5A6', '#34495E']
        )
    ))
    
    fig.update_layout(
        title={
            'text': "Renewable Energy Production (Vibrant Style)",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#FF6B6B')
        },
        width=1000,
        height=1000,
        showlegend=False,
        template='plotly_white'
    )
    
    fig.write_image("旭日图_style_4.png")

def plot_5(data):
    # 极简风格：黑白灰
    fig = go.Figure(go.Sunburst(
        labels=data['id'],
        parents=data['parent'],
        values=data['value'],
        branchvalues="total",
        textfont=dict(size=14),
        insidetextorientation='radial',
        marker=dict(
            colors=['#000000', '#1a1a1a', '#333333', '#4d4d4d', '#666666',
                   '#808080', '#999999', '#b3b3b3', '#cccccc', '#e6e6e6',
                   '#ffffff', '#f2f2f2', '#e6e6e6', '#d9d9d9', '#cccccc']
        )
    ))
    
    fig.update_layout(
        title={
            'text': "Renewable Energy Production (Minimalist Style)",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#333333')
        },
        width=1000,
        height=1000,
        showlegend=False,
        template='plotly_white'
    )
    
    fig.write_image("旭日图_style_5.png")

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
