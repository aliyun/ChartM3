import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    """
    Generate or process data for ring gap chart
    Returns a dataframe with percentage value
    """
    # If no data provided, generate sample data
    if data is None:
        data = pd.DataFrame({
            'metric': ['Completion Rate'],
            'value': [75.5]  # Sample percentage
        })
    
    # Validate percentage is between 0-100
    if not all(0 <= x <= 100 for x in data['value']):
        raise ValueError("Values must be percentages between 0 and 100")
    
    # Save to CSV
    data.to_csv('玉玦图.csv', index=False)
    return data

def plot(data):
    """
    Create a ring gap chart showing percentage completion
    Args:
        data: DataFrame with columns 'metric' and 'value'
    """
    value = data['value'].iloc[0]
    
    # Chart configuration
    config = {
        'gap_size': 60,  # Size of gap in degrees
        'start_angle': 90,  # Position of gap (90 = top)
        'hole_size': 0.75,  # Size of center hole (0-1)
        'main_color': '#1E88E5',  # 主要部分颜色加深
        'bg_color': 'white',  # 未填充部分改为白色
        'width': 800,
        'height': 500
    }
    
    # Create figure
    fig = go.Figure()
    
    # Add main value segment
    fig.add_trace(go.Pie(
        values=[value, 100-value],
        rotation=config['start_angle'],
        hole=config['hole_size'],
        direction='clockwise',
        showlegend=False,
        textinfo='none',
        marker_colors=[config['main_color'], config['bg_color']],
        sort=False
    ))
    
    # Add center text
    fig.add_annotation(
        text=f"{value:.1f}%",
        x=0.5, y=0.5,
        font=dict(size=40, color='#2E4053'),
        showarrow=False
    )
    
    # Update layout
    fig.update_layout(
        width=config['width'],
        height=config['height'],
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(t=80, b=80, l=80, r=80),
        title=dict(
            text="Completion Progress",
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top',
            font=dict(size=24, color='#2E4053')
        ),
        shapes=[dict(
            type="rect",
            xref="paper",
            yref="paper",
            x0=0,
            y0=0,
            x1=1,
            y1=1,
            line=dict(width=2, color="white"),
            fillcolor='white',
            layer='below'
        )]
    )
    
    # Add subtle shadow effect
    fig.update_traces(marker=dict(
        line=dict(color='white', width=1.5)
    ))

    # Save figure
    fig.write_image("玉玦图.png", scale=2)
    return fig


def plot_1(data):
    """商务风格"""
    value = data['value'].iloc[0]
    config = {
        'gap_size': 60,
        'start_angle': 90,
        'hole_size': 0.8,
        'main_color': ['#2E4053', '#5D6D7E'],
        'bg_color': '#EBF5FB',
        'width': 800,
        'height': 500
    }
    
    fig = go.Figure()
    fig.add_trace(go.Pie(
        values=[value, 100-value],
        rotation=config['start_angle'],
        hole=config['hole_size'],
        direction='clockwise',
        showlegend=False,
        textinfo='none',
        marker_colors=[config['main_color'][0], config['bg_color']],
        marker=dict(
            line=dict(color='white', width=2)
        ),
        sort=False
    ))
    
    fig.add_annotation(
        text=f"{value:.1f}%",
        x=0.5, y=0.5,
        font=dict(size=45, color=config['main_color'][1], family='Arial Black'),
        showarrow=False
    )
    
    fig.update_layout(
        width=config['width'],
        height=config['height'],
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(t=100, b=80, l=80, r=80),
        title=dict(
            text="Business Progress",
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top',
            font=dict(size=24, color=config['main_color'][1], family='Arial')
        )
    )
    
    fig.write_image("玉玦图_style_1.png", scale=2)
    return fig

def plot_2(data):
    """活力风格"""
    value = data['value'].iloc[0]
    config = {
        'gap_size': 45,
        'start_angle': 90,
        'hole_size': 0.75,
        'main_color': '#FF6B6B',
        'bg_color': '#FFE066',
        'width': 800,
        'height': 500
    }
    
    fig = go.Figure()
    fig.add_trace(go.Pie(
        values=[value, 100-value],
        rotation=config['start_angle'],
        hole=config['hole_size'],
        direction='clockwise',
        showlegend=False,
        textinfo='none',
        marker_colors=[config['main_color'], config['bg_color']],
        sort=False
    ))
    
    fig.add_annotation(
        text=f"{value:.1f}%",
        x=0.5, y=0.5,
        font=dict(size=50, color='#FF6B6B', family='Comic Sans MS'),
        showarrow=False
    )
    
    fig.update_layout(
        width=config['width'],
        height=config['height'],
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(t=80, b=80, l=80, r=80),
        title=dict(
            text="Energy Level",
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top',
            font=dict(size=28, color='#FF6B6B', family='Comic Sans MS')
        )
    )
    
    fig.write_image("玉玦图_style_2.png", scale=2)
    return fig

def plot_3(data):
    """环保风格"""
    value = data['value'].iloc[0]
    config = {
        'gap_size': 50,
        'start_angle': 90,
        'hole_size': 0.7,
        'main_color': '#4CAF50',
        'bg_color': '#C8E6C9',
        'width': 800,
        'height': 500
    }
    
    fig = go.Figure()
    fig.add_trace(go.Pie(
        values=[value, 100-value],
        rotation=config['start_angle'],
        hole=config['hole_size'],
        direction='clockwise',
        showlegend=False,
        textinfo='none',
        marker_colors=[config['main_color'], config['bg_color']],
        opacity=0.9,
        sort=False
    ))
    
    fig.add_annotation(
        text=f"{value:.1f}%",
        x=0.5, y=0.5,
        font=dict(size=40, color='#2E7D32', family='Verdana'),
        showarrow=False
    )
    
    fig.update_layout(
        width=config['width'],
        height=config['height'],
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(t=80, b=80, l=80, r=80),
        title=dict(
            text="Sustainability Index",
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top',
            font=dict(size=24, color='#2E7D32', family='Verdana')
        )
    )
    
    fig.write_image("玉玦图_style_3.png", scale=2)
    return fig

def plot_4(data):
    """科技风格"""
    value = data['value'].iloc[0]
    config = {
        'gap_size': 30,
        'start_angle': 90,
        'hole_size': 0.85,
        'main_color': '#3F51B5',
        'bg_color': '#E8EAF6',
        'width': 800,
        'height': 500
    }
    
    fig = go.Figure()
    fig.add_trace(go.Pie(
        values=[value, 100-value],
        rotation=config['start_angle'],
        hole=config['hole_size'],
        direction='clockwise',
        showlegend=False,
        textinfo='none',
        marker_colors=[config['main_color'], config['bg_color']],
        sort=False
    ))
    
    fig.add_annotation(
        text=f"{value:.1f}%",
        x=0.5, y=0.5,
        font=dict(size=35, color='#303F9F', family='Roboto'),
        showarrow=False
    )
    
    fig.update_layout(
        width=config['width'],
        height=config['height'],
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(t=80, b=80, l=80, r=80),
        title=dict(
            text="System Status",
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top',
            font=dict(size=24, color='#303F9F', family='Roboto')
        )
    )
    
    fig.write_image("玉玦图_style_4.png", scale=2)
    return fig

def plot_5(data):
    """优雅风格"""
    value = data['value'].iloc[0]
    config = {
        'gap_size': 40,
        'start_angle': 90,
        'hole_size': 0.78,
        'main_color': '#E91E63',
        'bg_color': '#FCE4EC',
        'width': 800,
        'height': 500
    }
    
    fig = go.Figure()
    fig.add_trace(go.Pie(
        values=[value, 100-value],
        rotation=config['start_angle'],
        hole=config['hole_size'],
        direction='clockwise',
        showlegend=False,
        textinfo='none',
        marker_colors=[config['main_color'], config['bg_color']],
        sort=False
    ))
    
    fig.add_annotation(
        text=f"{value:.1f}%",
        x=0.5, y=0.5,
        font=dict(size=42, color='#C2185B', family='Playfair Display'),
        showarrow=False
    )
    
    fig.update_layout(
        width=config['width'],
        height=config['height'],
        paper_bgcolor='white',
        plot_bgcolor='white',
        margin=dict(t=80, b=80, l=80, r=80),
        title=dict(
            text="Elegance Meter",
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top',
            font=dict(size=26, color='#C2185B', family='Playfair Display')
        )
    )
    
    fig.write_image("玉玦图_style_5.png", scale=2)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
