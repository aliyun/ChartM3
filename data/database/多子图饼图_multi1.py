import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

def preprocess(data=None):
    # Create sample smartphone market share data
    regions = ['North America', 'Europe', 'Asia', 'Global']
    brands = ['Apple', 'Samsung', 'Xiaomi', 'Huawei', 'Others']
    
    data = {
        'North America': [45, 25, 5, 5, 20],
        'Europe': [35, 30, 15, 10, 10],
        'Asia': [20, 25, 25, 20, 10],
        'Global': [30, 28, 15, 12, 15]
    }
    
    # Create DataFrame
    rows = []
    for region in regions:
        for brand, share in zip(brands, data[region]):
            rows.append({
                'Region': region,
                'Brand': brand,
                'Market_Share': share
            })
    
    df = pd.DataFrame(rows)
    df.to_csv('多子图饼图.csv', index=False)
    return df

def plot(data):
    if isinstance(data, str):
        data = pd.read_csv(data)
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('North America', 'Europe', 'Asia', 'Global'),
        specs=[[{'type':'pie'}, {'type':'pie'}],
               [{'type':'pie'}, {'type':'pie'}]]
    )
    
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF99CC']
    regions = ['North America', 'Europe', 'Asia', 'Global']
    row_positions = [1, 1, 2, 2]
    col_positions = [1, 2, 1, 2]
    
    for region, row, col in zip(regions, row_positions, col_positions):
        region_data = data[data['Region'] == region]
        
        # Create custom text for labels
        custom_text = [
            f"{brand}<br>{share}%" 
            for brand, share in zip(region_data['Brand'], region_data['Market_Share'])
        ]
        
        fig.add_trace(
            go.Pie(
                labels=region_data['Brand'],
                values=region_data['Market_Share'],
                name=region,
                marker_colors=colors,
                # Enhanced text information
                text=custom_text,
                textinfo='text',
                textposition='outside',
                texttemplate='%{label}<br>%{percent:.1f}%',
                hovertemplate="<b>%{label}</b><br>" +
                            "Market Share: %{percent:.1f}%<br>" +
                            "<extra></extra>",
                hole=0.3,
                showlegend=True if (row==1 and col==1) else False,
                pull=[0.05] * len(region_data),  # Slight separation for better visibility
                rotation=90  # Rotate to optimize label placement
            ),
            row=row, col=col
        )
    
    # Update layout
    fig.update_layout(
        title_text='Smartphone Market Share by Region',
                title_x=0.5,
                height=800,
                width=1000,
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=-0.2,
                    xanchor="center",
                    x=0.5
                ),
                annotations=[
                    dict(
                        text=region,
                        x=0.5 if col==1 else 1.5,
                        y=1.2 if row==1 else 0.5,
                        showarrow=False,
                        font_size=16
                    )
                    for region, row, col in zip(regions, row_positions, col_positions)
                ]
            )
    
    # Update font sizes and spacing
    fig.update_traces(
        textfont_size=12,
        textposition='outside',
        insidetextorientation='radial'
    )
    
    # Adjust layout margins
    fig.update_layout(
        margin=dict(t=150, b=150, l=50, r=50)
    )
    
    # Save plot
    pio.write_image(fig, '多子图饼图.png', scale=2)
    return fig


def plot_1(data):
    """现代简约风格：黑白灰配色，极简设计"""
    if isinstance(data, str):
        data = pd.read_csv(data)
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('North America', 'Europe', 'Asia', 'Global'),
        specs=[[{'type':'pie'}, {'type':'pie'}],
               [{'type':'pie'}, {'type':'pie'}]]
    )
    
    colors = ['#2C3E50', '#95A5A6', '#BDC3C7', '#E74C3C', '#ECF0F1']
    regions = ['North America', 'Europe', 'Asia', 'Global']
    row_positions = [1, 1, 2, 2]
    col_positions = [1, 2, 1, 2]
    
    for region, row, col in zip(regions, row_positions, col_positions):
        region_data = data[data['Region'] == region]
        
        fig.add_trace(
            go.Pie(
                labels=region_data['Brand'],
                values=region_data['Market_Share'],
                name=region,
                marker_colors=colors,
                textinfo='label+percent',
                textposition='outside',
                hole=0.4,
                showlegend=True if (row==1 and col==1) else False,
                pull=[0.03] * len(region_data)
            ),
            row=row, col=col
        )
    
    fig.update_layout(
        title_text='Smartphone Market Share by Region',
        title_x=0.5,
        height=800,
        width=1000,
        paper_bgcolor='white',
        plot_bgcolor='white',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
        font=dict(
            family="Arial",
            size=12,
            color="#2C3E50"
        )
    )
    
    pio.write_image(fig, '多子图饼图_style_1.png', scale=2)
    return fig

def plot_2(data):
    """商务蓝风格：蓝色渐变，专业大气"""
    if isinstance(data, str):
        data = pd.read_csv(data)
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('North America', 'Europe', 'Asia', 'Global'),
        specs=[[{'type':'pie'}, {'type':'pie'}],
               [{'type':'pie'}, {'type':'pie'}]]
    )
    
    colors = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087']
    regions = ['North America', 'Europe', 'Asia', 'Global']
    row_positions = [1, 1, 2, 2]
    col_positions = [1, 2, 1, 2]
    
    for region, row, col in zip(regions, row_positions, col_positions):
        region_data = data[data['Region'] == region]
        
        fig.add_trace(
            go.Pie(
                labels=region_data['Brand'],
                values=region_data['Market_Share'],
                name=region,
                marker_colors=colors,
                textinfo='percent',
                textposition='inside',
                hole=0.5,
                showlegend=True if (row==1 and col==1) else False,
                pull=[0]* len(region_data)
            ),
            row=row, col=col
        )
    
    fig.update_layout(
        title_text='Smartphone Market Share by Region',
        title_x=0.5,
        height=800,
        width=1000,
        paper_bgcolor='#f8f9fa',
        plot_bgcolor='#f8f9fa',
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="right",
            x=1.1
        ),
        font=dict(
            family="Arial",
            size=12,
            color="#003f5c"
        )
    )
    
    pio.write_image(fig, '多子图饼图_style_2.png', scale=2)
    return fig

def plot_3(data):
    """活力彩虹风格：明亮色彩，充满活力"""
    if isinstance(data, str):
        data = pd.read_csv(data)
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('North America', 'Europe', 'Asia', 'Global'),
        specs=[[{'type':'pie'}, {'type':'pie'}],
               [{'type':'pie'}, {'type':'pie'}]]
    )
    
    colors = ['#FF595E', '#FFCA3A', '#8AC926', '#1982C4', '#6A4C93']
    regions = ['North America', 'Europe', 'Asia', 'Global']
    row_positions = [1, 1, 2, 2]
    col_positions = [1, 2, 1, 2]
    
    for region, row, col in zip(regions, row_positions, col_positions):
        region_data = data[data['Region'] == region]
        
        fig.add_trace(
            go.Pie(
                labels=region_data['Brand'],
                values=region_data['Market_Share'],
                name=region,
                marker_colors=colors,
                textinfo='label+percent',
                textposition='outside',
                hole=0.2,
                showlegend=True if (row==1 and col==1) else False,
                pull=[0.1] * len(region_data)
            ),
            row=row, col=col
        )
    
    fig.update_layout(
        title_text='Smartphone Market Share by Region',
        title_x=0.5,
        height=800,
        width=1000,
        paper_bgcolor='white',
        plot_bgcolor='white',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
        font=dict(
            family="Arial",
            size=12,
            color="#333333"
        )
    )
    
    pio.write_image(fig, '多子图饼图_style_3.png', scale=2)
    return fig

def plot_4(data):
    """深色科技风格：深色背景，高对比度"""
    if isinstance(data, str):
        data = pd.read_csv(data)
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('North America', 'Europe', 'Asia', 'Global'),
        specs=[[{'type':'pie'}, {'type':'pie'}],
               [{'type':'pie'}, {'type':'pie'}]]
    )
    
    colors = ['#00ff00', '#00cc00', '#009900', '#006600', '#003300']
    regions = ['North America', 'Europe', 'Asia', 'Global']
    row_positions = [1, 1, 2, 2]
    col_positions = [1, 2, 1, 2]
    
    for region, row, col in zip(regions, row_positions, col_positions):
        region_data = data[data['Region'] == region]
        
        fig.add_trace(
            go.Pie(
                labels=region_data['Brand'],
                values=region_data['Market_Share'],
                name=region,
                marker_colors=colors,
                textinfo='percent',
                textposition='inside',
                hole=0.6,
                showlegend=True if (row==1 and col==1) else False,
                pull=[0] * len(region_data)
            ),
            row=row, col=col
        )
    
    fig.update_layout(
        title_text='Smartphone Market Share by Region',
        title_x=0.5,
        height=800,
        width=1000,
        paper_bgcolor='#1a1a1a',
        plot_bgcolor='#1a1a1a',
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=-0.1,
            font=dict(color='#ffffff')
        ),
        font=dict(
            family="Arial",
            size=12,
            color="#ffffff"
        )
    )
    
    fig.update_annotations(font_color="#ffffff")
    
    pio.write_image(fig, '多子图饼图_style_4.png', scale=2)
    return fig

def plot_5(data):
    """自然柔和风格：地球色调"""
    if isinstance(data, str):
        data = pd.read_csv(data)
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('North America', 'Europe', 'Asia', 'Global'),
        specs=[[{'type':'pie'}, {'type':'pie'}],
               [{'type':'pie'}, {'type':'pie'}]]
    )
    
    colors = ['#8B4513', '#DEB887', '#D2691E', '#F4A460', '#A0522D']
    regions = ['North America', 'Europe', 'Asia', 'Global']
    row_positions = [1, 1, 2, 2]
    col_positions = [1, 2, 1, 2]
    
    for region, row, col in zip(regions, row_positions, col_positions):
        region_data = data[data['Region'] == region]
        
        fig.add_trace(
            go.Pie(
                labels=region_data['Brand'],
                values=region_data['Market_Share'],
                name=region,
                marker_colors=colors,
                textinfo='label+percent',
                textposition='inside',
                hole=0.3,
                showlegend=True if (row==1 and col==1) else False,
                pull=[0.05] * len(region_data)
            ),
            row=row, col=col
        )
    
    fig.update_layout(
        title_text='Smartphone Market Share by Region',
        title_x=0.5,
        height=800,
        width=1000,
        paper_bgcolor='#FFF8DC',
        plot_bgcolor='#FFF8DC',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            bgcolor='#FFF8DC'
        ),
        font=dict(
            family="Arial",
            size=12,
            color="#8B4513"
        )
    )
    
    pio.write_image(fig, '多子图饼图_style_5.png', scale=2)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
