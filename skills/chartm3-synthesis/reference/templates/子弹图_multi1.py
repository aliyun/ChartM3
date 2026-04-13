import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    """Generate and preprocess data for bullet chart"""
    
    # Generate sample data if none provided
    if data is None:
        categories = ['Electronics', 'Clothing', 'Food', 'Home Goods']
        
        data = pd.DataFrame({
            'Category': categories,
            'Actual': [850, 650, 480, 520],
            'Target': [800, 700, 500, 600],
            'Poor': [0, 0, 0, 0],
            'Fair': [500, 400, 300, 400],
            'Good': [700, 600, 400, 500],
            'Maximum': [1000, 800, 600, 700]
        })
    
    # Save to CSV
    data.to_csv('子弹图.csv', index=False)
    return data

def plot(data):
    """Create bullet chart visualization"""
    
    # Figure setup
    fig = go.Figure()
    
    # Add traces for each category
    for idx, row in data.iterrows():
        
        # Add background ranges
        fig.add_trace(go.Bar(
            name='Good',
            y=[row['Category']],
            x=[row['Maximum']],
            marker_color='rgb(235,235,235)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            name='Fair',
            y=[row['Category']],
            x=[row['Good']],
            marker_color='rgb(220,220,220)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            name='Poor',
            y=[row['Category']],
            x=[row['Fair']],
            marker_color='rgb(200,200,200)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        # Add actual value bar
        fig.add_trace(go.Bar(
            name='Actual',
            y=[row['Category']],
            x=[row['Actual']],
            marker_color='rgb(0,109,172)',
            orientation='h',
            width=0.3,
            base=0
        ))
        
        # Add target line
        fig.add_trace(go.Bar(
            name='Target',
            y=[row['Category']],
            x=[row['Target']],
            marker_color='rgb(0,0,0)',
            orientation='h',
            width=0.08,
            base=0
        ))

    # Update layout
    fig.update_layout(
        title={
            'text': 'Sales Performance by Category',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        barmode='overlay',
        height=400,
        showlegend=False,
        margin=dict(l=20, r=20, t=70, b=20),
        xaxis=dict(
            title='Sales (thousands)',
            zeroline=False,
            showgrid=True,
            gridcolor='rgb(235,235,235)'
        ),
        yaxis=dict(
            title=None,
            zeroline=False,
            showgrid=False
        ),
        plot_bgcolor='white'
    )

    # Add value annotations
    for idx, row in data.iterrows():
        fig.add_annotation(
            x=row['Actual'],
            y=row['Category'],
            text=f"Actual: {row['Actual']}k",
            showarrow=False,
            xshift=10,
            yshift=20,
            font=dict(size=10)
        )
        fig.add_annotation(
            x=row['Target'],
            y=row['Category'],
            text=f"Target: {row['Target']}k",
            showarrow=False,
            xshift=10,
            yshift=-20, 
            font=dict(size=10)
        )

    # Save plot
    fig.write_image("子弹图.png", width=800, height=400)
    return fig

def plot_1(data):
    """商务蓝风格"""
    fig = go.Figure()
    
    for idx, row in data.iterrows():
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Maximum']],
            marker_color='rgba(200,210,220,0.3)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Good']],
            marker_color='rgba(180,190,200,0.4)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Fair']],
            marker_color='rgba(160,170,180,0.5)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Actual']],
            marker_color='rgb(0,82,154)',
            orientation='h',
            width=0.3,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Target']],
            marker_color='rgb(28,28,28)',
            orientation='h',
            width=0.08,
            base=0
        ))

    fig.update_layout(
        title={
            'text': 'Business Performance Analysis',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='rgb(0,82,154)')
        },
        barmode='overlay',
        height=400,
        showlegend=False,
        margin=dict(l=20, r=20, t=70, b=20),
        xaxis=dict(
            title='Sales (thousands)',
            zeroline=False,
            showgrid=True,
            gridcolor='rgb(240,240,240)'
        ),
        yaxis=dict(
            zeroline=False,
            showgrid=False
        ),
        plot_bgcolor='white'
    )

    for idx, row in data.iterrows():
        fig.add_annotation(
            x=row['Actual'],
            y=row['Category'],
            text=f"Actual: {row['Actual']}k",
            showarrow=False,
            xshift=10,
            yshift=20,
            font=dict(size=10, color='rgb(0,82,154)')
        )
        fig.add_annotation(
            x=row['Target'],
            y=row['Category'],
            text=f"Target: {row['Target']}k",
            showarrow=False,
            xshift=10,
            yshift=-20,
            font=dict(size=10)
        )

    fig.write_image("子弹图_style_1.png", width=800, height=400)
    return fig

def plot_2(data):
    """活力橙风格"""
    fig = go.Figure()
    
    for idx, row in data.iterrows():
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Maximum']],
            marker_color='rgba(255,240,230,0.5)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Good']],
            marker_color='rgba(255,220,200,0.5)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Fair']],
            marker_color='rgba(255,200,170,0.5)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Actual']],
            marker_color='rgb(255,90,0)',
            orientation='h',
            width=0.3,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Target']],
            marker_color='rgb(51,51,51)',
            orientation='h',
            width=0.08,
            base=0
        ))

    fig.update_layout(
        title={
            'text': 'Dynamic Performance Tracking',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='rgb(255,90,0)')
        },
        barmode='overlay',
        height=400,
        showlegend=False,
        margin=dict(l=20, r=20, t=70, b=20),
        xaxis=dict(
            title='Sales (thousands)',
            zeroline=False,
            showgrid=True,
            gridcolor='rgba(255,200,170,0.3)'
        ),
        yaxis=dict(
            zeroline=False,
            showgrid=False
        ),
        plot_bgcolor='white'
    )

    for idx, row in data.iterrows():
        fig.add_annotation(
            x=row['Actual'],
            y=row['Category'],
            text=f"Actual: {row['Actual']}k",
            showarrow=False,
            xshift=10,
            yshift=20,
            font=dict(size=10, color='rgb(255,90,0)')
        )
        fig.add_annotation(
            x=row['Target'],
            y=row['Category'],
            text=f"Target: {row['Target']}k",
            showarrow=False,
            xshift=10,
            yshift=-20,
            font=dict(size=10)
        )

    fig.write_image("子弹图_style_2.png", width=800, height=400)
    return fig

def plot_3(data):
    """环保绿风格"""
    fig = go.Figure()
    
    for idx, row in data.iterrows():
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Maximum']],
            marker_color='rgba(230,240,220,0.5)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Good']],
            marker_color='rgba(200,220,180,0.5)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Fair']],
            marker_color='rgba(170,200,140,0.5)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Actual']],
            marker_color='rgb(76,140,43)',
            orientation='h',
            width=0.3,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Target']],
            marker_color='rgb(45,87,44)',
            orientation='h',
            width=0.08,
            base=0
        ))

    fig.update_layout(
        title={
            'text': 'Sustainable Growth Metrics',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='rgb(76,140,43)')
        },
        barmode='overlay',
        height=400,
        showlegend=False,
        margin=dict(l=20, r=20, t=70, b=20),
        xaxis=dict(
            title='Sales (thousands)',
            zeroline=False,
            showgrid=True,
            gridcolor='rgba(170,200,140,0.3)'
        ),
        yaxis=dict(
            zeroline=False,
            showgrid=False
        ),
        plot_bgcolor='white'
    )

    for idx, row in data.iterrows():
        fig.add_annotation(
            x=row['Actual'],
            y=row['Category'],
            text=f"Actual: {row['Actual']}k",
            showarrow=False,
            xshift=10,
            yshift=20,
            font=dict(size=10, color='rgb(76,140,43)')
        )
        fig.add_annotation(
            x=row['Target'],
            y=row['Category'],
            text=f"Target: {row['Target']}k",
            showarrow=False,
            xshift=10,
            yshift=-20,
            font=dict(size=10)
        )

    fig.write_image("子弹图_style_3.png", width=800, height=400)
    return fig

def plot_4(data):
    """高对比风格"""
    fig = go.Figure()
    
    for idx, row in data.iterrows():
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Maximum']],
            marker_color='rgb(240,240,240)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Good']],
            marker_color='rgb(220,220,220)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Fair']],
            marker_color='rgb(200,200,200)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Actual']],
            marker_color='rgb(255,0,0)',
            orientation='h',
            width=0.3,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Target']],
            marker_color='rgb(0,0,0)',
            orientation='h',
            width=0.08,
            base=0
        ))

    fig.update_layout(
        title={
            'text': 'Performance Contrast Analysis',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='rgb(0,0,0)')
        },
        barmode='overlay',
        height=400,
        showlegend=False,
        margin=dict(l=20, r=20, t=70, b=20),
        xaxis=dict(
            title='Sales (thousands)',
            zeroline=False,
            showgrid=True,
            gridcolor='rgb(240,240,240)'
        ),
        yaxis=dict(
            zeroline=False,
            showgrid=False
        ),
        plot_bgcolor='white'
    )

    for idx, row in data.iterrows():
        fig.add_annotation(
            x=row['Actual'],
            y=row['Category'],
            text=f"Actual: {row['Actual']}k",
            showarrow=False,
            xshift=10,
            yshift=20,
            font=dict(size=10, color='rgb(255,0,0)')
        )
        fig.add_annotation(
            x=row['Target'],
            y=row['Category'],
            text=f"Target: {row['Target']}k",
            showarrow=False,
            xshift=10,
            yshift=-20,
            font=dict(size=10)
        )

    fig.write_image("子弹图_style_4.png", width=800, height=400)
    return fig
    

def plot_5(data):
    """柔和渐变风格"""
    fig = go.Figure()
    
    for idx, row in data.iterrows():
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Maximum']],
            marker_color='rgba(230,230,250,0.3)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Good']],
            marker_color='rgba(210,210,240,0.4)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Fair']],
            marker_color='rgba(190,190,230,0.5)',
            orientation='h',
            width=0.5,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Actual']],
            marker_color='rgb(147,112,219)',
            orientation='h',
            width=0.3,
            base=0
        ))
        
        fig.add_trace(go.Bar(
            y=[row['Category']],
            x=[row['Target']],
            marker_color='rgb(75,0,130)',
            orientation='h',
            width=0.08,
            base=0
        ))

    fig.update_layout(
        title={
            'text': 'Gentle Performance View',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='rgb(147,112,219)')
        },
        barmode='overlay',
        height=400,
        showlegend=False,
        margin=dict(l=20, r=20, t=70, b=20),
        xaxis=dict(
            title='Sales (thousands)',
            zeroline=False,
            showgrid=True,
            gridcolor='rgba(230,230,250,0.5)'
        ),
        yaxis=dict(
            zeroline=False,
            showgrid=False
        ),
        plot_bgcolor='white'
    )

    for idx, row in data.iterrows():
        fig.add_annotation(
            x=row['Actual'],
            y=row['Category'],
            text=f"Actual: {row['Actual']}k",
            showarrow=False,
            xshift=10,
            yshift=20,
            font=dict(size=10, color='rgb(147,112,219)')
        )
        fig.add_annotation(
            x=row['Target'],
            y=row['Category'],
            text=f"Target: {row['Target']}k",
            showarrow=False,
            xshift=10,
            yshift=-20,
            font=dict(size=10)
        )

    fig.write_image("子弹图_style_5.png", width=800, height=400)
    return fig


data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
