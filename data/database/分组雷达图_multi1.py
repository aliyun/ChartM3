import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    # Generate sample data if none provided
    if data is None:
        # Create sample data for 3 car models with 6 metrics
        models = ['Luxury Sedan', 'Sports Car', 'SUV']
        metrics = ['Speed', 'Handling', 'Comfort', 'Fuel Economy', 'Safety', 'Reliability']
        
        data = pd.DataFrame({
            'Model': models * len(metrics),
            'Metric': sorted(metrics * len(models)),
            'Score': [
                # Luxury Sedan scores
                75, 70, 90, 65, 85, 80,
                # Sports Car scores
                95, 90, 60, 50, 70, 65,
                # SUV scores
                60, 65, 85, 75, 90, 85
            ]
        })
        
    # Save processed data
    data.to_csv('分组雷达图.csv', index=False)
    return data

def plot(data):
    # Define colors for each model
    # colors = {'Luxury Sedan': '#1f77b4', 
    #           'Sports Car': '#ff7f0e', 
    #           'SUV': '#2ca02c'}
    colors = {
        'Luxury Sedan': {'line': 'rgb(31, 119, 180)', 'fill': 'rgba(31, 119, 180, 0.2)'}, 
        'Sports Car': {'line': 'rgb(255, 127, 14)', 'fill': 'rgba(255, 127, 14, 0.2)'}, 
        'SUV': {'line': 'rgb(44, 160, 44)', 'fill': 'rgba(44, 160, 44, 0.2)'}
    }
    
    # Create figure
    fig = go.Figure()
    
    # Get unique models and metrics
    models = data['Model'].unique()
    metrics = data['Metric'].unique()
    
    # Add traces for each model
    for model in models:
        model_data = data[data['Model'] == model]
        
        fig.add_trace(go.Scatterpolar(
            r=model_data['Score'].tolist() + [model_data['Score'].iloc[0]],  # Close the polygon
            theta=model_data['Metric'].tolist() + [model_data['Metric'].iloc[0]],  # Close the polygon
            name=model,
            line=dict(color=colors[model]['line'], width=2),
            fill='toself',
            fillcolor=colors[model]['fill']
        ))

    # Update layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10),
                ticksuffix='',
                showline=True,
                linewidth=1,
                gridwidth=1
            ),
            angularaxis=dict(
                tickfont=dict(size=12),
                rotation=90,
                direction='clockwise'
                    ),
        ),
        showlegend=True,
        legend=dict(
            x=1.1,
            y=0.5,
            font=dict(size=12)
        ),
        title=dict(
            text='Car Models Performance Comparison',
            x=0.5,
            y=0.95,
            font=dict(size=16)
        ),
        margin=dict(l=80, r=80, t=80, b=80),
        height=700,
        width=800,
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    # Save figure
    fig.write_image("分组雷达图.png")
    return fig


def plot_1(data):
    # 商务简约风格
    colors = {
        'Luxury Sedan': {'line': '#2c3e50', 'fill': 'rgba(44, 62, 80, 0.1)'}, 
        'Sports Car': {'line': '#34495e', 'fill': 'rgba(52, 73, 94, 0.1)'}, 
        'SUV': {'line': '#7f8c8d', 'fill': 'rgba(127, 140, 141, 0.1)'}
    }
    
    fig = go.Figure()
    models = data['Model'].unique()
    metrics = data['Metric'].unique()
    
    for model in models:
        model_data = data[data['Model'] == model]
        fig.add_trace(go.Scatterpolar(
            r=model_data['Score'].tolist() + [model_data['Score'].iloc[0]],
            theta=model_data['Metric'].tolist() + [model_data['Metric'].iloc[0]],
            name=model,
            line=dict(color=colors[model]['line'], width=1.5),
            fill='toself',
            fillcolor=colors[model]['fill']
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10, color='#2c3e50'),
                showline=True,
                linewidth=0.5,
                gridwidth=0.5
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color='#2c3e50'),
                rotation=90,
                direction='clockwise'
            ),
        ),
        showlegend=True,
        legend=dict(
            x=1.1,
            y=0.5,
            font=dict(size=12, color='#2c3e50')
        ),
        title=dict(
            text='Car Models Performance Comparison',
            x=0.5,
            y=0.95,
            font=dict(size=16, color='#2c3e50')
        ),
        margin=dict(l=80, r=80, t=80, b=80),
        height=700,
        width=800,
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    fig.write_image("分组雷达图_style_1.png")
    return fig

def plot_2(data):
    # 科技感风格
    colors = {
        'Luxury Sedan': {'line': '#00bcd4', 'fill': 'rgba(0, 188, 212, 0.2)'}, 
        'Sports Car': {'line': '#03a9f4', 'fill': 'rgba(3, 169, 244, 0.2)'}, 
        'SUV': {'line': '#039be5', 'fill': 'rgba(3, 155, 229, 0.2)'}
    }
    
    fig = go.Figure()
    models = data['Model'].unique()
    metrics = data['Metric'].unique()
    
    for model in models:
        model_data = data[data['Model'] == model]
        fig.add_trace(go.Scatterpolar(
            r=model_data['Score'].tolist() + [model_data['Score'].iloc[0]],
            theta=model_data['Metric'].tolist() + [model_data['Metric'].iloc[0]],
            name=model,
            line=dict(color=colors[model]['line'], width=2),
            fill='toself',
            fillcolor=colors[model]['fill']
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10, color='#424242'),
                showline=True,
                linewidth=1,
                gridwidth=1,
                gridcolor='rgba(189, 189, 189, 0.5)'
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color='#424242'),
                rotation=90,
                direction='clockwise'
            ),
        ),
        showlegend=True,
        legend=dict(
            x=1.1,
            y=0.5,
            font=dict(size=12)
        ),
        title=dict(
            text='Car Models Performance Comparison',
            x=0.5,
            y=0.95,
            font=dict(size=16, color='#424242')
        ),
        margin=dict(l=80, r=80, t=80, b=80),
        height=700,
        width=800,
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    fig.write_image("分组雷达图_style_2.png")
    return fig

def plot_3(data):
    # 环保主题
    colors = {
        'Luxury Sedan': {'line': '#4caf50', 'fill': 'rgba(76, 175, 80, 0.2)'}, 
        'Sports Car': {'line': '#8bc34a', 'fill': 'rgba(139, 195, 74, 0.2)'}, 
        'SUV': {'line': '#cddc39', 'fill': 'rgba(205, 220, 57, 0.2)'}
    }
    
    fig = go.Figure()
    models = data['Model'].unique()
    metrics = data['Metric'].unique()
    
    for model in models:
        model_data = data[data['Model'] == model]
        fig.add_trace(go.Scatterpolar(
            r=model_data['Score'].tolist() + [model_data['Score'].iloc[0]],
            theta=model_data['Metric'].tolist() + [model_data['Metric'].iloc[0]],
            name=model,
            line=dict(color=colors[model]['line'], width=2),
            fill='toself',
            fillcolor=colors[model]['fill']
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10, color='#33691e'),
                showline=True,
                linewidth=1,
                gridwidth=1,
                gridcolor='rgba(156, 204, 101, 0.3)'
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color='#33691e'),
                rotation=90,
                direction='clockwise'
            ),
        ),
        showlegend=True,
        legend=dict(
            x=1.1,
            y=0.5,
            font=dict(size=12, color='#33691e')
        ),
        title=dict(
            text='Car Models Performance Comparison',
            x=0.5,
            y=0.95,
            font=dict(size=16, color='#33691e')
        ),
        margin=dict(l=80, r=80, t=80, b=80),
        height=700,
        width=800,
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    fig.write_image("分组雷达图_style_3.png")
    return fig

def plot_4(data):
    # 活泼风格
    colors = {
        'Luxury Sedan': {'line': '#f44336', 'fill': 'rgba(244, 67, 54, 0.2)'}, 
        'Sports Car': {'line': '#ff9800', 'fill': 'rgba(255, 152, 0, 0.2)'}, 
        'SUV': {'line': '#ffd600', 'fill': 'rgba(255, 214, 0, 0.2)'}
    }
    
    fig = go.Figure()
    models = data['Model'].unique()
    metrics = data['Metric'].unique()
    
    for model in models:
        model_data = data[data['Model'] == model]
        fig.add_trace(go.Scatterpolar(
            r=model_data['Score'].tolist() + [model_data['Score'].iloc[0]],
            theta=model_data['Metric'].tolist() + [model_data['Metric'].iloc[0]],
            name=model,
            line=dict(color=colors[model]['line'], width=3),
            fill='toself',
            fillcolor=colors[model]['fill']
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10),
                showline=True,
                linewidth=1.5,
                gridwidth=1.5,
                gridcolor='rgba(158, 158, 158, 0.3)'
            ),
            angularaxis=dict(
                tickfont=dict(size=12),
                rotation=90,
                direction='clockwise'
            ),
        ),
        showlegend=True,
        legend=dict(
            x=1.1,
            y=0.5,
            font=dict(size=12)
        ),
        title=dict(
            text='Car Models Performance Comparison',
            x=0.5,
            y=0.95,
            font=dict(size=16)
        ),
        margin=dict(l=80, r=80, t=80, b=80),
        height=700,
        width=800,
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    fig.write_image("分组雷达图_style_4.png")
    return fig

def plot_5(data):
    # 复古风格
    colors = {
        'Luxury Sedan': {'line': '#795548', 'fill': 'rgba(121, 85, 72, 0.1)'}, 
        'Sports Car': {'line': '#8d6e63', 'fill': 'rgba(141, 110, 99, 0.1)'}, 
        'SUV': {'line': '#a1887f', 'fill': 'rgba(161, 136, 127, 0.1)'}
    }
    
    fig = go.Figure()
    models = data['Model'].unique()
    metrics = data['Metric'].unique()
    
    for model in models:
        model_data = data[data['Model'] == model]
        fig.add_trace(go.Scatterpolar(
            r=model_data['Score'].tolist() + [model_data['Score'].iloc[0]],
            theta=model_data['Metric'].tolist() + [model_data['Metric'].iloc[0]],
            name=model,
            line=dict(color=colors[model]['line'], width=1.5, dash='dot'),
            fill='toself',
            fillcolor=colors[model]['fill']
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10, color='#3e2723'),
                showline=True,
                linewidth=0.5,
                gridwidth=0.5,
                gridcolor='rgba(62, 39, 35, 0.2)'
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color='#3e2723'),
                rotation=90,
                direction='clockwise'
            ),
        ),
        showlegend=True,
        legend=dict(
            x=1.1,
            y=0.5,
            font=dict(size=12, color='#3e2723')
        ),
        title=dict(
            text='Car Models Performance Comparison',
            x=0.5,
            y=0.95,
            font=dict(size=16, color='#3e2723')
        ),
        margin=dict(l=80, r=80, t=80, b=80),
        height=700,
        width=800,
        paper_bgcolor='rgba(238, 232, 205, 0.3)',
        plot_bgcolor='rgba(238, 232, 205, 0.3)'
    )
    
    fig.write_image("分组雷达图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
