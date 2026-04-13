import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    """Generate sample data for linear ring gap chart"""
    # Create sample data if none provided
    if data is None:
        data = pd.DataFrame({
            'metric': ['Project Progress'],
            'actual': [67],  # 67% complete
            'target': [100]  # 100% target
        })
    
    # Save to CSV
    data.to_csv('线形玉玦图.csv', index=False)
    return data

def plot(data):
    """Create linear ring gap chart"""
    # Extract values
    actual = data['actual'].values[0]
    target = data['target'].values[0]
    
    # Generate curve coordinates
    theta = np.linspace(-np.pi/2, 3*np.pi/2, 200)
    r = np.ones_like(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Create color gradient
    colors = [f'rgba(55, 135, 192, {i/100})' for i in range(50, 100)]
    
    # Create figure
    fig = go.Figure()
    
    # Add base curve (background)
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(color='rgba(200,200,200,0.2)', width=15),
        hoverinfo='skip'
    ))
    
    # Add progress curve
    progress_theta = np.linspace(-np.pi/2, -np.pi/2 + 2*np.pi*actual/100, 200)
    progress_x = np.cos(progress_theta)
    progress_y = np.sin(progress_theta)
    
    fig.add_trace(go.Scatter(
        x=progress_x, y=progress_y,
        mode='lines',
        line=dict(
            color='rgb(55, 135, 192)',
            width=15
        ),
        fill='tonexty',
        fillcolor='rgba(55, 135, 192, 0.2)'
    ))
    
    # Add annotations
    fig.add_annotation(
        text=f"{actual}%",
        x=progress_x[-1], y=progress_y[-1],
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor='rgb(55, 135, 192)',
        font=dict(size=16, color='rgb(55, 135, 192)'),
        ax=40,
        ay=-40
    )
    
    # Update layout
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-1.5, 1.5]
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-1.5, 1.5],
            scaleanchor="x",
            scaleratio=1
        ),
        title=dict(
            text='Project Completion Progress',
            x=0.5,
            y=0.95,
            font=dict(size=20)
        ),
        annotations=[
            dict(
                text=f"Target: {target}%",
                x=0.85,
                y=-0.3,
                showarrow=False,
                font=dict(size=14, color='gray')
            )
        ]
    )
    
    # Save figure
    fig.write_image("线形玉玦图.png", width=800, height=600)
    return fig

def plot_1(data):
    """商务风格 - 深蓝灰配色"""
    actual = data['actual'].values[0] 
    target = data['target'].values[0]
    
    theta = np.linspace(-np.pi/2, 3*np.pi/2, 200)
    r = np.ones_like(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(color='rgba(220,220,220,0.3)', width=12, dash='dot'),
        hoverinfo='skip'
    ))
    
    progress_theta = np.linspace(-np.pi/2, -np.pi/2 + 2*np.pi*actual/100, 200)
    progress_x = np.cos(progress_theta)
    progress_y = np.sin(progress_theta)
    
    fig.add_trace(go.Scatter(
        x=progress_x, y=progress_y,
        mode='lines',
        line=dict(
            color='rgb(28,66,107)',
            width=12
        ),
        fill='tonexty',
        fillcolor='rgba(28,66,107,0.1)'
    ))
    
    fig.add_annotation(
        text=f"{actual}%",
        x=progress_x[-1], y=progress_y[-1],
        showarrow=True,
        arrowhead=1,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor='rgb(28,66,107)',
        font=dict(size=18, color='rgb(28,66,107)', family='Arial'),
        ax=40,
        ay=-40
    )
    
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 1.5]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 1.5], 
                  scaleanchor="x", scaleratio=1),
        title=dict(
            text='Project Progress',
            x=0.5,
            y=0.95,
            font=dict(size=22, color='rgb(28,66,107)', family='Arial Black')
        ),
        annotations=[
            dict(
                text=f"Target {target}%",
                x=0.85,
                y=-0.3,
                showarrow=False,
                font=dict(size=14, color='rgb(100,100,100)', family='Arial')
            )
        ]
    )
    
    fig.write_image("线形玉玦图_style_1.png", width=800, height=600)
    return fig

def plot_2(data):
    """活力风格 - 橙色系"""
    actual = data['actual'].values[0]
    target = data['target'].values[0]
    
    theta = np.linspace(-np.pi/2, 3*np.pi/2, 200)
    r = np.ones_like(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(color='rgba(255,236,217,0.8)', width=15),
        hoverinfo='skip'
    ))
    
    progress_theta = np.linspace(-np.pi/2, -np.pi/2 + 2*np.pi*actual/100, 200)
    progress_x = np.cos(progress_theta)
    progress_y = np.sin(progress_theta)
    
    fig.add_trace(go.Scatter(
        x=progress_x, y=progress_y,
        mode='lines',
        line=dict(
            color='rgb(255,140,0)',
            width=15
        ),
        fill='tonexty',
        fillcolor='rgba(255,140,0,0.2)'
    ))
    
    fig.add_annotation(
        text=f"{actual}%",
        x=progress_x[-1], y=progress_y[-1],
        showarrow=True,
        arrowhead=3,
        arrowsize=1.5,
        arrowwidth=3,
        arrowcolor='rgb(255,140,0)',
        font=dict(size=20, color='rgb(255,140,0)', family='Verdana'),
        ax=50,
        ay=-50
    )
    
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgb(255,250,245)',
        paper_bgcolor='rgb(255,250,245)',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 1.5]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 1.5],
                  scaleanchor="x", scaleratio=1),
        title=dict(
            text='Progress Tracker',
            x=0.5,
            y=0.95,
            font=dict(size=24, color='rgb(255,140,0)', family='Verdana')
        ),
        annotations=[
            dict(
                text=f"Goal: {target}%",
                x=0.85,
                y=-0.3,
                showarrow=False,
                font=dict(size=16, color='rgb(255,160,40)', family='Verdana')
            )
        ]
    )
    
    fig.write_image("线形玉玦图_style_2.png", width=800, height=600)
    return fig

def plot_3(data):
    """环保风格 - 绿色渐变"""
    actual = data['actual'].values[0]
    target = data['target'].values[0]
    
    theta = np.linspace(-np.pi/2, 3*np.pi/2, 200)
    r = np.ones_like(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(color='rgba(230,240,230,0.5)', width=18),
        hoverinfo='skip'
    ))
    
    progress_theta = np.linspace(-np.pi/2, -np.pi/2 + 2*np.pi*actual/100, 200)
    progress_x = np.cos(progress_theta)
    progress_y = np.sin(progress_theta)
    
    fig.add_trace(go.Scatter(
        x=progress_x, y=progress_y,
        mode='lines',
        line=dict(
            color='rgb(76,175,80)',
            width=18
        ),
        fill='tonexty',
        fillcolor='rgba(76,175,80,0.15)'
    ))
    
    fig.add_annotation(
        text=f"{actual}%",
        x=progress_x[-1], y=progress_y[-1],
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor='rgb(76,175,80)',
        font=dict(size=18, color='rgb(76,175,80)', family='Roboto'),
        ax=45,
        ay=-45
    )
    
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgb(250,255,250)',
        paper_bgcolor='rgb(250,255,250)',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 1.5]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 1.5],
                  scaleanchor="x", scaleratio=1),
        title=dict(
            text='Sustainability Progress',
            x=0.5,
            y=0.95,
            font=dict(size=22, color='rgb(56,142,60)', family='Roboto')
        ),
        annotations=[
            dict(
                text=f"Target: {target}%",
                x=0.85,
                y=-0.3,
                showarrow=False,
                font=dict(size=14, color='rgb(129,199,132)', family='Roboto')
            )
        ]
    )
    
    fig.write_image("线形玉玦图_style_3.png", width=800, height=600)
    return fig

def plot_4(data):
    """科技风格 - 紫蓝渐变"""
    actual = data['actual'].values[0]
    target = data['target'].values[0]
    
    theta = np.linspace(-np.pi/2, 3*np.pi/2, 200)
    r = np.ones_like(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(color='rgba(200,200,255,0.2)', width=16, dash='dash'),
        hoverinfo='skip'
    ))
    
    progress_theta = np.linspace(-np.pi/2, -np.pi/2 + 2*np.pi*actual/100, 200)
    progress_x = np.cos(progress_theta)
    progress_y = np.sin(progress_theta)
    
    fig.add_trace(go.Scatter(
        x=progress_x, y=progress_y,
        mode='lines',
        line=dict(
            color='rgb(103,58,183)',
            width=16
        ),
        fill='tonexty',
        fillcolor='rgba(103,58,183,0.1)'
    ))
    
    fig.add_annotation(
        text=f"{actual}%",
        x=progress_x[-1], y=progress_y[-1],
        showarrow=True,
        arrowhead=4,
        arrowsize=1.2,
        arrowwidth=2.5,
        arrowcolor='rgb(103,58,183)',
        font=dict(size=20, color='rgb(103,58,183)', family='Courier New'),
        ax=40,
        ay=-40
    )
    
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgb(245,245,255)',
        paper_bgcolor='rgb(245,245,255)',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 1.5]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 1.5],
                  scaleanchor="x", scaleratio=1),
        title=dict(
            text='System Progress Monitor',
            x=0.5,
            y=0.95,
            font=dict(size=24, color='rgb(103,58,183)', family='Courier New')
        ),
        annotations=[
            dict(
                text=f"TARGET {target}%",
                x=0.85,
                y=-0.3,
                showarrow=False,
                font=dict(size=14, color='rgb(149,117,205)', family='Courier New')
            )
        ]
    )
    
    fig.write_image("线形玉玦图_style_4.png", width=800, height=600)
    return fig

def plot_5(data):
    """优雅风格 - 红粉系"""
    actual = data['actual'].values[0]
    target = data['target'].values[0]
    
    theta = np.linspace(-np.pi/2, 3*np.pi/2, 200)
    r = np.ones_like(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(color='rgba(255,220,220,0.6)', width=14),
        hoverinfo='skip'
    ))
    
    progress_theta = np.linspace(-np.pi/2, -np.pi/2 + 2*np.pi*actual/100, 200)
    progress_x = np.cos(progress_theta)
    progress_y = np.sin(progress_theta)
    
    fig.add_trace(go.Scatter(
        x=progress_x, y=progress_y,
        mode='lines',
        line=dict(
            color='rgb(233,30,99)',
            width=14
        ),
        fill='tonexty',
        fillcolor='rgba(233,30,99,0.1)'
    ))
    
    fig.add_annotation(
        text=f"{actual}%",
        x=progress_x[-1], y=progress_y[-1],
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor='rgb(233,30,99)',
        font=dict(size=18, color='rgb(233,30,99)', family='Georgia'),
        ax=40,
        ay=-40
    )
    
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgb(255,248,248)',
        paper_bgcolor='rgb(255,248,248)',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 1.5]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.5, 1.5],
                  scaleanchor="x", scaleratio=1),
        title=dict(
            text='Milestone Progress',
            x=0.5,
            y=0.95,
            font=dict(size=22, color='rgb(233,30,99)', family='Georgia')
        ),
        annotations=[
            dict(
                text=f"Target · {target}%",
                x=0.85,
                y=-0.3,
                showarrow=False,
                font=dict(size=14, color='rgb(240,98,146)', family='Georgia')
            )
        ]
    )
    
    fig.write_image("线形玉玦图_style_5.png", width=800, height=600)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
