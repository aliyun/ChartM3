import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    # Generate sample data if none provided
    if data is None:
        departments = ['Sales', 'Marketing', 'R&D', 'Operations', 'HR']
        expenses = ['Personnel', 'Equipment', 'Supplies']
        
        # Generate random but realistic budget numbers
        data = pd.DataFrame({
            'Department': departments * len(expenses),
            'Category': [exp for exp in expenses for _ in departments],
            'Value': np.random.randint(100, 1000, size=len(departments)*len(expenses))
        })
    
    # Pivot data to get it in the right format
    pivot_data = data.pivot(columns='Department', index='Category', values='Value')
    
    # Save to CSV
    pivot_data.to_csv('堆叠雷达图.csv')
    
    return pivot_data

def plot(data):
    # Read data if string path provided
    if isinstance(data, str):
        data = pd.read_csv(data, index_col=0)
    
    # Setup categories and departments
    categories = data.index.tolist()
    departments = data.columns.tolist()
    
    # Add the first department again to close the radar
    departments_closed = departments + [departments[0]]
    
    # Create figure
    fig = go.Figure()
    
    # Calculate cumulative values for stacking
    cumsum = data.cumsum()
    
    # Colors for different categories
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    # Add traces from bottom to top
    for i in range(len(categories)):
        if i == 0:
            values = data.iloc[i]
        else:
            values = cumsum.iloc[i]
            
        # Close the trace by adding first value at end
        values_closed = values.tolist() + [values[0]]
        
        fig.add_trace(go.Scatterpolar(
            r=values_closed,
            theta=departments_closed,
            name=categories[i],
            fill='tonext',  # Changed from 'tonexty' to 'tonext'
            fillcolor=colors[i],
            line=dict(color=colors[i], width=2),
            hovertemplate='Department: %{theta}<br>' +
                         f'Category: {categories[i]}<br>' +
                         'Value: %{r:,.0f}<br>' +
                         '<extra></extra>'
        ))

    # Update layout
    fig.update_layout(
        showlegend=True,
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, data.sum().max()],
                tickfont=dict(size=10),
                showline=True,
                gridcolor='lightgray'
            ),
            angularaxis=dict(
                tickfont=dict(size=12),
                rotation=90,
                direction="clockwise"
            )
        ),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=1.1,
            font=dict(size=11)
        ),
        margin=dict(r=80, t=50, b=50, l=50),
        height=600,
        width=700,
        title=dict(
            text='Department Budget Allocation by Category',
            x=0.5,
            y=0.95,
            font=dict(size=16)
        )
    )

    # Update trace colors
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    for i, trace in enumerate(fig.data):
        trace.update(fillcolor=colors[i], line=dict(color=colors[i]))

    # Save figure
    fig.write_image("堆叠雷达图.png", scale=2)
    
    return fig

# Example usage

def plot_1(data):
    # 商务深色主题
    if isinstance(data, str):
        data = pd.read_csv(data, index_col=0)
    
    categories = data.index.tolist()
    departments = data.columns.tolist()
    departments_closed = departments + [departments[0]]
    
    fig = go.Figure()
    cumsum = data.cumsum()
    
    # 深色单色渐变
    colors = ['#1a237e', '#283593', '#303f9f', '#3949ab', '#3f51b5']
    
    for i in range(len(categories)):
        values = cumsum.iloc[i] if i > 0 else data.iloc[i]
        values_closed = values.tolist() + [values[0]]
        
        fig.add_trace(go.Scatterpolar(
            r=values_closed,
            theta=departments_closed,
            name=categories[i],
            fill='tonext',
            fillcolor=colors[i],
            line=dict(color=colors[i], width=1.5),
            opacity=0.8
        ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='#1a1a1a',
        plot_bgcolor='#1a1a1a',
        polar=dict(
            radialaxis=dict(
                showline=True,
                linewidth=0.5,
                gridcolor='rgba(255,255,255,0.2)',
                tickfont=dict(size=10, color='white')
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color='white'),
                gridcolor='rgba(255,255,255,0.2)'
            )
        ),
        showlegend=True,
        legend=dict(
            font=dict(color='white', size=10),
            bgcolor='rgba(0,0,0,0)',
            bordercolor='rgba(255,255,255,0.2)'
        ),
        title=dict(
            text='Department Budget Analysis',
            font=dict(size=16, color='white')
        )
    )
    
    fig.write_image("堆叠雷达图_style_1.png", scale=2)
    return fig

def plot_2(data):
    # 环保自然风格
    if isinstance(data, str):
        data = pd.read_csv(data, index_col=0)
    
    categories = data.index.tolist()
    departments = data.columns.tolist()
    departments_closed = departments + [departments[0]]
    
    fig = go.Figure()
    cumsum = data.cumsum()
    
    # 自然绿色渐变
    colors = ['#004d40', '#00695c', '#00796b', '#00897b', '#009688']
    
    for i in range(len(categories)):
        values = cumsum.iloc[i] if i > 0 else data.iloc[i]
        values_closed = values.tolist() + [values[0]]
        
        fig.add_trace(go.Scatterpolar(
            r=values_closed,
            theta=departments_closed,
            name=categories[i],
            fill='tonext',
            fillcolor=colors[i],
            line=dict(color=colors[i], width=1),
            opacity=0.7
        ))

    fig.update_layout(
        template='simple_white',
        paper_bgcolor='#f5f5f5',
        polar=dict(
            radialaxis=dict(
                showline=True,
                linewidth=0.5,
                gridcolor='rgba(0,0,0,0.1)',
                tickfont=dict(size=10)
            ),
            angularaxis=dict(
                tickfont=dict(size=12),
                gridcolor='rgba(0,0,0,0.1)'
            )
        ),
        showlegend=True,
        title=dict(
            text='Eco-friendly Budget Distribution',
            font=dict(size=16, color='#004d40')
        )
    )
    
    fig.write_image("堆叠雷达图_style_2.png", scale=2)
    return fig

def plot_3(data):
    # 现代科技风
    if isinstance(data, str):
        data = pd.read_csv(data, index_col=0)
    
    categories = data.index.tolist()
    departments = data.columns.tolist()
    departments_closed = departments + [departments[0]]
    
    fig = go.Figure()
    cumsum = data.cumsum()
    
    # 科技蓝色系
    colors = ['#0d47a1', '#1565c0', '#1976d2', '#1e88e5', '#2196f3']
    
    for i in range(len(categories)):
        values = cumsum.iloc[i] if i > 0 else data.iloc[i]
        values_closed = values.tolist() + [values[0]]
        
        fig.add_trace(go.Scatterpolar(
            r=values_closed,
            theta=departments_closed,
            name=categories[i],
            fill='tonext',
            fillcolor=colors[i],
            line=dict(color=colors[i], width=2),
            opacity=0.9
        ))

    fig.update_layout(
        template='plotly',
        paper_bgcolor='white',
        polar=dict(
            radialaxis=dict(
                showline=True,
                linewidth=1,
                gridcolor='rgba(0,0,0,0.1)',
                tickfont=dict(size=10)
            ),
            angularaxis=dict(
                tickfont=dict(size=12),
                gridcolor='rgba(0,0,0,0.1)'
            )
        ),
        showlegend=True,
        title=dict(
            text='Tech-Budget Analysis',
            font=dict(size=16, color='#0d47a1')
        )
    )
    
    fig.write_image("堆叠雷达图_style_3.png", scale=2)
    return fig

def plot_4(data):
    # 活泼明亮风格
    if isinstance(data, str):
        data = pd.read_csv(data, index_col=0)
    
    categories = data.index.tolist()
    departments = data.columns.tolist()
    departments_closed = departments + [departments[0]]
    
    fig = go.Figure()
    cumsum = data.cumsum()
    
    # 明亮多彩配色
    colors = ['#ff1744', '#f50057', '#d500f9', '#651fff', '#3d5afe']
    
    for i in range(len(categories)):
        values = cumsum.iloc[i] if i > 0 else data.iloc[i]
        values_closed = values.tolist() + [values[0]]
        
        fig.add_trace(go.Scatterpolar(
            r=values_closed,
            theta=departments_closed,
            name=categories[i],
            fill='tonext',
            fillcolor=colors[i],
            line=dict(color=colors[i], width=2),
            opacity=0.8
        ))

    fig.update_layout(
        template='plotly',
        paper_bgcolor='#fafafa',
        polar=dict(
            radialaxis=dict(
                showline=True,
                linewidth=1,
                gridcolor='rgba(0,0,0,0.1)',
                tickfont=dict(size=10)
            ),
            angularaxis=dict(
                tickfont=dict(size=12),
                gridcolor='rgba(0,0,0,0.1)'
            )
        ),
        showlegend=True,
        title=dict(
            text='Vibrant Budget Overview',
            font=dict(size=16, color='#ff1744')
        )
    )
    
    fig.write_image("堆叠雷达图_style_4.png", scale=2)
    return fig

def plot_5(data):
    # 极简黑白风格
    if isinstance(data, str):
        data = pd.read_csv(data, index_col=0)
    
    categories = data.index.tolist()
    departments = data.columns.tolist()
    departments_closed = departments + [departments[0]]
    
    fig = go.Figure()
    cumsum = data.cumsum()
    
    # 黑白灰渐变
    colors = ['#212121', '#424242', '#616161', '#757575', '#9e9e9e']
    
    for i in range(len(categories)):
        values = cumsum.iloc[i] if i > 0 else data.iloc[i]
        values_closed = values.tolist() + [values[0]]
        
        fig.add_trace(go.Scatterpolar(
            r=values_closed,
            theta=departments_closed,
            name=categories[i],
            fill='tonext',
            fillcolor=colors[i],
            line=dict(color=colors[i], width=1),
            opacity=0.9
        ))

    fig.update_layout(
        template='simple_white',
        paper_bgcolor='white',
        polar=dict(
            radialaxis=dict(
                showline=True,
                linewidth=0.5,
                gridcolor='rgba(0,0,0,0.1)',
                tickfont=dict(size=10)
            ),
            angularaxis=dict(
                tickfont=dict(size=12),
                gridcolor='rgba(0,0,0,0.1)'
            )
        ),
        showlegend=True,
        title=dict(
            text='Minimalist Budget Analysis',
            font=dict(size=16, color='#212121')
        )
    )
    
    fig.write_image("堆叠雷达图_style_5.png", scale=2)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
