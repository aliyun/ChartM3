import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy import stats

def preprocess(data=None):
    # Generate synthetic test score data
    np.random.seed(42)
    
    # Create bimodal distribution
    scores1 = np.random.normal(loc=70, scale=10, size=300)
    scores2 = np.random.normal(loc=85, scale=5, size=200)
    scores = np.concatenate([scores1, scores2])
    
    # Clip scores to valid range
    scores = np.clip(scores, 0, 100)
    
    # Create dataframe
    df = pd.DataFrame({'score': scores})
    
    # Save to CSV
    df.to_csv('不等宽直方图.csv', index=False)
    return df

def plot(data):
    # Define variable width bins - narrower in the middle
    bins = [0, 40, 55, 65, 75, 80, 85, 90, 95, 100]
    
    # Calculate histogram
    hist, edges = np.histogram(data['score'], bins=bins, density=True)
    
    # Calculate bar widths and centers
    widths = np.diff(edges)
    centers = edges[:-1] + widths/2
    
    # Create figure
    fig = go.Figure()
    
    # Add bars
    fig.add_trace(go.Bar(
        x=centers,
        y=hist,
        width=widths,
        name='Frequency',
        text=np.round(hist*100, 1),
        textposition='auto',
        hovertemplate="Range: %{x}-" + 
                      np.array2string(edges[1:], precision=1) +
                      "<br>Density: %{y:.3f}<extra></extra>"
    ))
    
    # Update layout
    fig.update_layout(
        title={
            'text': 'Student Test Score Distribution',
            'x': 0.5,
            'y': 0.95
        },
        xaxis_title="Test Score",
        yaxis_title="Density",
        showlegend=False,
        plot_bgcolor='white',
        width=800,
        height=500
    )
    
    # Add grid
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    # Customize bar appearance
    fig.update_traces(
        marker_color='rgb(158,202,225)',
        marker_line_color='rgb(8,48,107)',
        marker_line_width=1.5,
        opacity=0.8
    )
    
    # Save figure
    fig.write_image("不等宽直方图.png", scale=2)
    return fig


def plot_1(data):
    # 商务蓝风格
    bins = [0, 40, 55, 65, 75, 80, 85, 90, 95, 100]
    hist, edges = np.histogram(data['score'], bins=bins, density=True)
    widths = np.diff(edges)
    centers = edges[:-1] + widths/2
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=centers,
        y=hist,
        width=widths,
        text=np.round(hist*100, 1),
        textposition='auto',
        hovertemplate="Range: %{x}-" + np.array2string(edges[1:], precision=1) +
                      "<br>Density: %{y:.3f}<extra></extra>"
    ))
    
    fig.update_layout(
        title={
            'text': 'Test Score Distribution - Business Style',
            'x': 0.5,
            'y': 0.95,
            'font': dict(family="Arial", size=24, color="#2E4053")
        },
        xaxis_title="Test Score",
        yaxis_title="Density",
        showlegend=False,
        plot_bgcolor='white',
        width=800,
        height=500,
        font=dict(family="Arial", size=12)
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#E5E8E8')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#E5E8E8')
    
    fig.update_traces(
        marker_color='#5DADE2',
        marker_line_color='#2874A6',
        marker_line_width=1,
        opacity=0.8
    )
    
    fig.write_image("不等宽直方图_style_1.png", scale=2)
    return fig

def plot_2(data):
    # 活泼彩虹风格
    bins = [0, 40, 55, 65, 75, 80, 85, 90, 95, 100]
    hist, edges = np.histogram(data['score'], bins=bins, density=True)
    widths = np.diff(edges)
    centers = edges[:-1] + widths/2
    
    colors = ['#FF9999', '#FF99CC', '#99FF99', '#99FFCC', '#9999FF', '#99CCFF', '#FFCC99', '#FF99FF', '#99FFFF']
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=centers,
        y=hist,
        width=widths,
        text=np.round(hist*100, 1),
        textposition='auto',
        marker_color=colors,
        hovertemplate="Range: %{x}-" + np.array2string(edges[1:], precision=1) +
                      "<br>Density: %{y:.3f}<extra></extra>"
    ))
    
    fig.update_layout(
        title={
            'text': 'Test Score Distribution - Playful Style',
            'x': 0.5,
            'y': 0.95,
            'font': dict(family="Comic Sans MS", size=24, color="#FF6B6B")
        },
        xaxis_title="Test Score",
        yaxis_title="Density",
        showlegend=False,
        plot_bgcolor='#FAFAFA',
        width=800,
        height=500,
        font=dict(family="Comic Sans MS", size=12)
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#F0F0F0')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#F0F0F0')
    
    fig.update_traces(
        marker_line_width=2,
        opacity=0.7
    )
    
    fig.write_image("不等宽直方图_style_2.png", scale=2)
    return fig

def plot_3(data):
    # 环保绿色风格
    bins = [0, 40, 55, 65, 75, 80, 85, 90, 95, 100]
    hist, edges = np.histogram(data['score'], bins=bins, density=True)
    widths = np.diff(edges)
    centers = edges[:-1] + widths/2
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=centers,
        y=hist,
        width=widths,
        text=np.round(hist*100, 1),
        textposition='auto',
        hovertemplate="Range: %{x}-" + np.array2string(edges[1:], precision=1) +
                      "<br>Density: %{y:.3f}<extra></extra>"
    ))
    
    fig.update_layout(
        title={
            'text': 'Test Score Distribution - Eco Style',
            'x': 0.5,
            'y': 0.95,
            'font': dict(family="Verdana", size=24, color="#2E7D32")
        },
        xaxis_title="Test Score",
        yaxis_title="Density",
        showlegend=False,
        plot_bgcolor='#F1F8E9',
        width=800,
        height=500,
        font=dict(family="Verdana", size=12)
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#C5E1A5')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#C5E1A5')
    
    fig.update_traces(
        marker_color='#81C784',
        marker_line_color='#388E3C',
        marker_line_width=1.5,
        opacity=0.85
    )
    
    fig.write_image("不等宽直方图_style_3.png", scale=2)
    return fig

def plot_4(data):
    # 科技暗黑风格
    bins = [0, 40, 55, 65, 75, 80, 85, 90, 95, 100]
    hist, edges = np.histogram(data['score'], bins=bins, density=True)
    widths = np.diff(edges)
    centers = edges[:-1] + widths/2
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=centers,
        y=hist,
        width=widths,
        text=np.round(hist*100, 1),
        textposition='auto',
        hovertemplate="Range: %{x}-" + np.array2string(edges[1:], precision=1) +
                      "<br>Density: %{y:.3f}<extra></extra>"
    ))
    
    fig.update_layout(
        title={
            'text': 'Test Score Distribution - Tech Style',
            'x': 0.5,
            'y': 0.95,
            'font': dict(family="Roboto Mono", size=24, color="#00FF00")
        },
        xaxis_title="Test Score",
        yaxis_title="Density",
        showlegend=False,
        plot_bgcolor='#1A1A1A',
        paper_bgcolor='#1A1A1A',
        width=800,
        height=500,
        font=dict(family="Roboto Mono", size=12, color='#FFFFFF')
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#333333', color='#FFFFFF')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#333333', color='#FFFFFF')
    
    fig.update_traces(
        marker_color='#00FF00',
        marker_line_color='#00CC00',
        marker_line_width=1,
        opacity=0.7
    )
    
    fig.write_image("不等宽直方图_style_4.png", scale=2)
    return fig

def plot_5(data):
    # 温暖橙色风格
    bins = [0, 40, 55, 65, 75, 80, 85, 90, 95, 100]
    hist, edges = np.histogram(data['score'], bins=bins, density=True)
    widths = np.diff(edges)
    centers = edges[:-1] + widths/2
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=centers,
        y=hist,
        width=widths,
        text=np.round(hist*100, 1),
        textposition='auto',
        hovertemplate="Range: %{x}-" + np.array2string(edges[1:], precision=1) +
                      "<br>Density: %{y:.3f}<extra></extra>"
    ))
    
    fig.update_layout(
        title={
            'text': 'Test Score Distribution - Warm Style',
            'x': 0.5,
            'y': 0.95,
            'font': dict(family="Georgia", size=24, color="#D35400")
        },
        xaxis_title="Test Score",
        yaxis_title="Density",
        showlegend=False,
        plot_bgcolor='#FDF2E9',
        width=800,
        height=500,
        font=dict(family="Georgia", size=12)
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#FAD7A0')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#FAD7A0')
    
    fig.update_traces(
        marker_color='#F39C12',
        marker_line_color='#D35400',
        marker_line_width=1.5,
        opacity=0.8
    )
    
    fig.write_image("不等宽直方图_style_5.png", scale=2)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
