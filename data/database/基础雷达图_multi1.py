import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    """
    Generate sample data for a simple radar chart showing student's academic performance
    """
    # Generate sample data if none provided
    if data is None:
        data = pd.DataFrame({
            'Subject': ['Mathematics', 'Physics', 'Chemistry', 
                       'Biology', 'Literature', 'History'],
            'Score': [92, 85, 88, 75, 82, 78]
        })
    
    # Save data to CSV
    data.to_csv('基础雷达图.csv', index=False)
    return data

def plot(data=None):
    """
    Create a simple radar chart with comprehensive styling
    """
    # Load data if not provided
    if data is None:
        data = pd.read_csv('基础雷达图.csv')
    
    # Prepare data for radar chart
    categories = data['Subject'].tolist()
    values = data['Score'].tolist()
    
    # Add first value at end to close the polygon
    values.append(values[0])
    categories.append(categories[0])
    
    # Create figure
    fig = go.Figure()
    
    # Add trace
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(64, 149, 191, 0.3)',
        line=dict(color='rgb(64, 149, 191)', width=2),
        mode='lines+markers+text',
        text=[f'{v}' for v in values],
        textposition='top center',
        marker=dict(size=8, color='rgb(64, 149, 191)'),
        name='Performance'
    ))
    
    # Update layout with comprehensive styling
    fig.update_layout(
        title=dict(
            text='Student Academic Performance<br><sup>Score Distribution Across Subjects</sup>',
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor='top',
            font=dict(size=20)
        ),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10),
                ticksuffix='',
                showline=True,
                linecolor='lightgray',
                gridcolor='lightgray'
            ),
            angularaxis=dict(
                tickfont=dict(size=12),
                rotation=90,
                direction='clockwise',
                gridcolor='lightgray'
            ),
            bgcolor='white'
        ),
        showlegend=False,
        paper_bgcolor='white',
        plot_bgcolor='white',
        width=700,
        height=700
    )
    
    # Save figure
    fig.write_image("基础雷达图.png")
    return fig
    
# Example usage

def plot_1(data=None):
    """
    商务风格：深蓝色调，专业稳重
    """
    if data is None:
        data = pd.read_csv('data.csv')
    
    categories = data['Subject'].tolist()
    values = data['Score'].tolist()
    values.append(values[0])
    categories.append(categories[0])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(25, 55, 109, 0.4)',
        line=dict(color='rgb(25, 55, 109)', width=2.5),
        mode='lines+markers+text',
        text=[f'{v}' for v in values],
        textposition='top center',
        marker=dict(size=8, symbol='circle', color='rgb(25, 55, 109)'),
        name='Performance'
    ))
    
    fig.update_layout(
        title=dict(
            text='Academic Performance Analysis',
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor='top',
            font=dict(size=24, color='rgb(25, 55, 109)', family='Arial Black')
        ),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10, color='rgb(25, 55, 109)'),
                linecolor='rgba(25, 55, 109, 0.2)',
                gridcolor='rgba(25, 55, 109, 0.2)'
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color='rgb(25, 55, 109)'),
                rotation=90,
                direction='clockwise',
                gridcolor='rgba(25, 55, 109, 0.2)'
            ),
            bgcolor='white'
        ),
        showlegend=False,
        paper_bgcolor='white',
        width=700,
        height=700
    )
    
    fig.write_image("基础雷达图_style_1.png")
    return fig

def plot_2(data=None):
    """
    极简风格：黑白灰
    """
    if data is None:
        data = pd.read_csv('data.csv')
    
    categories = data['Subject'].tolist()
    values = data['Score'].tolist()
    values.append(values[0])
    categories.append(categories[0])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(200, 200, 200, 0.3)',
        line=dict(color='rgb(100, 100, 100)', width=1),
        mode='lines+markers',
        marker=dict(size=6, symbol='circle', color='black'),
        name='Performance'
    ))
    
    fig.update_layout(
        title=dict(
            text='Performance',
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor='top',
            font=dict(size=20, color='black', family='Helvetica')
        ),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=8),
                linecolor='lightgray',
                gridcolor='lightgray'
            ),
            angularaxis=dict(
                tickfont=dict(size=10),
                rotation=90,
                direction='clockwise',
                gridcolor='lightgray'
            ),
            bgcolor='white'
        ),
        showlegend=False,
        paper_bgcolor='white',
        width=700,
        height=700
    )
    
    fig.write_image("基础雷达图_style_2.png")
    return fig

def plot_3(data=None):
    """
    活泼风格：多彩渐变
    """
    if data is None:
        data = pd.read_csv('data.csv')
    
    categories = data['Subject'].tolist()
    values = data['Score'].tolist()
    values.append(values[0])
    categories.append(categories[0])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(255, 65, 54, 0.3)',
        line=dict(
            color='rgb(255, 65, 54)',
            width=3,
        ),
        mode='lines+markers+text',
        text=[f'{v}' for v in values],
        textposition='top center',
        marker=dict(
            size=12,
            symbol='star',
            color='rgb(255, 65, 54)'
        ),
        name='Performance'
    ))
    
    fig.update_layout(
        title=dict(
            text='Student Scores! 🌟',
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor='top',
            font=dict(size=24, color='rgb(255, 65, 54)', family='Comic Sans MS')
        ),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10),
                linecolor='rgba(255, 65, 54, 0.2)',
                gridcolor='rgba(255, 65, 54, 0.2)'
            ),
            angularaxis=dict(
                tickfont=dict(size=12),
                rotation=90,
                direction='clockwise',
                gridcolor='rgba(255, 65, 54, 0.2)'
            ),
            bgcolor='white'
        ),
        showlegend=False,
        paper_bgcolor='white',
        width=700,
        height=700
    )
    
    fig.write_image("基础雷达图_style_3.png")
    return fig

def plot_4(data=None):
    """
    科技风格：霓虹蓝
    """
    if data is None:
        data = pd.read_csv('data.csv')
    
    categories = data['Subject'].tolist()
    values = data['Score'].tolist()
    values.append(values[0])
    categories.append(categories[0])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(0, 255, 255, 0.1)',
        line=dict(color='rgb(0, 255, 255)', width=2),
        mode='lines+markers+text',
        text=[f'{v}' for v in values],
        textposition='top center',
        marker=dict(
            size=8,
            symbol='diamond',
            color='rgb(0, 255, 255)',
            line=dict(color='rgb(0, 255, 255)', width=1)
        ),
        name='Performance'
    ))
    
    fig.update_layout(
        title=dict(
            text='Performance Analytics',
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor='top',
            font=dict(size=24, color='rgb(0, 255, 255)', family='Monaco')
        ),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10, color='rgb(0, 255, 255)'),
                linecolor='rgba(0, 255, 255, 0.2)',
                gridcolor='rgba(0, 255, 255, 0.2)'
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color='rgb(0, 255, 255)'),
                rotation=90,
                direction='clockwise',
                gridcolor='rgba(0, 255, 255, 0.2)'
            ),
            bgcolor='rgb(0, 0, 20)'
        ),
        showlegend=False,
        paper_bgcolor='rgb(0, 0, 20)',
        width=700,
        height=700
    )
    
    fig.write_image("基础雷达图_style_4.png")
    return fig

def plot_5(data=None):
    """
    复古风格：柔和色调
    """
    if data is None:
        data = pd.read_csv('data.csv')
    
    categories = data['Subject'].tolist()
    values = data['Score'].tolist()
    values.append(values[0])
    categories.append(categories[0])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(205, 164, 133, 0.4)',
        line=dict(color='rgb(205, 164, 133)', width=2),
        mode='lines+markers+text',
        text=[f'{v}' for v in values],
        textposition='top center',
        marker=dict(
            size=10,
            symbol='circle',
            color='rgb(205, 164, 133)',
            line=dict(color='rgb(165, 124, 93)', width=1)
        ),
        name='Performance'
    ))
    
    fig.update_layout(
        title=dict(
            text='Academic Report Card',
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor='top',
            font=dict(size=24, color='rgb(165, 124, 93)', family='Palatino')
        ),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10, color='rgb(165, 124, 93)'),
                linecolor='rgba(165, 124, 93, 0.3)',
                gridcolor='rgba(165, 124, 93, 0.3)'
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color='rgb(165, 124, 93)'),
                rotation=90,
                direction='clockwise',
                gridcolor='rgba(165, 124, 93, 0.3)'
            ),
            bgcolor='rgb(253, 246, 236)'
        ),
        showlegend=False,
        paper_bgcolor='rgb(253, 246, 236)',
        width=700,
        height=700
    )
    
    fig.write_image("基础雷达图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
