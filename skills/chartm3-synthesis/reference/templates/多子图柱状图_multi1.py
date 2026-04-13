import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def preprocess(data=None):
    """Generate or process data for multiple subplot bar chart."""
    # Generate sample data if none provided
    if data is None:
        regions = ['North', 'South', 'East', 'West']
        products = ['Electronics', 'Furniture', 'Clothing']
        
        data_list = []
        for region in regions:
            for product in products:
                # Generate random sales between 100-1000
                sales = round(np.random.uniform(100, 1000))
                data_list.append({
                    'Region': region,
                    'Product': product,
                    'Sales': sales
                })
        
        df = pd.DataFrame(data_list)
        # Save to CSV
        df.to_csv('多子图柱状图.csv', index=False)
        return df
    return data

def plot(data):
    """Create multiple subplot bar chart."""
    # Create figure with 2x2 subplot grid
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[f"{region} Region" for region in ['North', 'South', 'East', 'West']],
        vertical_spacing=0.15,
        horizontal_spacing=0.1
    )

    # Colors for product categories
    colors = {'Electronics': '#1f77b4', 'Furniture': '#ff7f0e', 'Clothing': '#2ca02c'}
    
    # Create subplots
    for i, region in enumerate(['North', 'South', 'East', 'West']):
        row = (i // 2) + 1
        col = (i % 2) + 1
        
        region_data = data[data['Region'] == region]
        
        fig.add_trace(
            go.Bar(
                name='Electronics',
                x=['Electronics'],
                y=[region_data[region_data['Product'] == 'Electronics']['Sales'].iloc[0]],
                marker_color=colors['Electronics'],
                text=[region_data[region_data['Product'] == 'Electronics']['Sales'].iloc[0]],
                textposition='auto',
                showlegend=(i == 0)  # Show legend only for first subplot
            ),
            row=row, col=col
        )

                # Add other product bars
        fig.add_trace(
            go.Bar(
                name='Furniture',
                x=['Furniture'],
                y=[region_data[region_data['Product'] == 'Furniture']['Sales'].iloc[0]],
                marker_color=colors['Furniture'],
                text=[region_data[region_data['Product'] == 'Furniture']['Sales'].iloc[0]],
                textposition='auto',
                showlegend=(i == 0)
            ),
            row=row, col=col
        )
        
        fig.add_trace(
            go.Bar(
                name='Clothing',
                x=['Clothing'], 
                y=[region_data[region_data['Product'] == 'Clothing']['Sales'].iloc[0]],
                marker_color=colors['Clothing'],
                text=[region_data[region_data['Product'] == 'Clothing']['Sales'].iloc[0]],
                textposition='auto',
                showlegend=(i == 0)
            ),
            row=row, col=col
        )

    # Update layout
    fig.update_layout(
        title_text="Regional Sales by Product Category",
        title_x=0.5,
        title_font_size=20,
        showlegend=True,
        legend_title="Product Categories",
        height=800,
        width=1000,
        template='plotly_white',
        barmode='group'
    )

    # Update axes
    fig.update_yaxes(title_text="Sales Volume", range=[0, data['Sales'].max() * 1.1])
    
    # Save figure
    fig.write_image("多子图柱状图.png")

# Example usage

def plot_1(data):
    """Modern minimalist style with monochromatic blue."""
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[f"{region} Region" for region in ['North', 'South', 'East', 'West']],
        vertical_spacing=0.15,
        horizontal_spacing=0.1
    )
    
    colors = {'Electronics': '#2C5F9E', 'Furniture': '#4682B4', 'Clothing': '#87CEEB'}
    
    for i, region in enumerate(['North', 'South', 'East', 'West']):
        row = (i // 2) + 1
        col = (i % 2) + 1
        region_data = data[data['Region'] == region]
        
        for product in ['Electronics', 'Furniture', 'Clothing']:
            fig.add_trace(
                go.Bar(
                    name=product,
                    x=[product],
                    y=[region_data[region_data['Product'] == product]['Sales'].iloc[0]],
                    marker_color=colors[product],
                    text=[region_data[region_data['Product'] == product]['Sales'].iloc[0]],
                    textposition='auto',
                    showlegend=(i == 0)
                ),
                row=row, col=col
            )

    fig.update_layout(
        title_text="Regional Sales Analysis",
        title_x=0.5,
        title_font=dict(size=24, family='Arial', color='#2C5F9E'),
        showlegend=True,
        legend_title="Products",
        height=800,
        width=1000,
        template='plotly_white',
        barmode='group',
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family='Arial')
    )
    
    fig.update_yaxes(title_text="Sales Volume", range=[0, data['Sales'].max() * 1.1], gridcolor='#E5E5E5')
    fig.write_image("多子图柱状图_style_1.png")

def plot_2(data):
    """Vibrant contrasting colors with dark theme."""
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[f"{region} Region" for region in ['North', 'South', 'East', 'West']],
        vertical_spacing=0.15,
        horizontal_spacing=0.1
    )
    
    colors = {'Electronics': '#FF6B6B', 'Furniture': '#4ECDC4', 'Clothing': '#FFE66D'}
    
    for i, region in enumerate(['North', 'South', 'East', 'West']):
        row = (i // 2) + 1
        col = (i % 2) + 1
        region_data = data[data['Region'] == region]
        
        for product in ['Electronics', 'Furniture', 'Clothing']:
            fig.add_trace(
                go.Bar(
                    name=product,
                    x=[product],
                    y=[region_data[region_data['Product'] == product]['Sales'].iloc[0]],
                    marker_color=colors[product],
                    text=[region_data[region_data['Product'] == product]['Sales'].iloc[0]],
                    textposition='auto',
                    showlegend=(i == 0)
                ),
                row=row, col=col
            )

    fig.update_layout(
        title_text="Regional Sales Distribution",
        title_x=0.5,
        title_font=dict(size=24, color='white'),
        showlegend=True,
        legend_title="Products",
        height=800,
        width=1000,
        template='plotly_dark',
        barmode='group',
        paper_bgcolor='#2D3436',
        plot_bgcolor='#2D3436',
        font=dict(color='white')
    )
    
    fig.update_yaxes(title_text="Sales Volume", range=[0, data['Sales'].max() * 1.1], gridcolor='#404040')
    fig.write_image("多子图柱状图_style_2.png")

def plot_3(data):
    """Professional gradient style."""
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[f"{region} Region" for region in ['North', 'South', 'East', 'West']],
        vertical_spacing=0.15,
        horizontal_spacing=0.1
    )
    
    colors = {'Electronics': '#003f5c', 'Furniture': '#58508d', 'Clothing': '#bc5090'}
    
    for i, region in enumerate(['North', 'South', 'East', 'West']):
        row = (i // 2) + 1
        col = (i % 2) + 1
        region_data = data[data['Region'] == region]
        
        for product in ['Electronics', 'Furniture', 'Clothing']:
            fig.add_trace(
                go.Bar(
                    name=product,
                    x=[product],
                    y=[region_data[region_data['Product'] == product]['Sales'].iloc[0]],
                    marker_color=colors[product],
                    text=[region_data[region_data['Product'] == product]['Sales'].iloc[0]],
                    textposition='auto',
                    showlegend=(i == 0)
                ),
                row=row, col=col
            )

    fig.update_layout(
        title_text="Sales Performance by Region",
        title_x=0.5,
        title_font=dict(size=22, family='Helvetica'),
        showlegend=True,
        legend_title="Product Categories",
        height=800,
        width=1000,
        template='simple_white',
        barmode='group',
        font=dict(family='Helvetica')
    )
    
    fig.update_yaxes(title_text="Sales Volume", range=[0, data['Sales'].max() * 1.1])
    fig.write_image("多子图柱状图_style_3.png")

def plot_4(data):
    """Pastel colors with rounded corners."""
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[f"{region} Region" for region in ['North', 'South', 'East', 'West']],
        vertical_spacing=0.15,
        horizontal_spacing=0.1
    )
    
    colors = {'Electronics': '#FFB5B5', 'Furniture': '#B5D8FF', 'Clothing': '#B5FFB5'}
    
    for i, region in enumerate(['North', 'South', 'East', 'West']):
        row = (i // 2) + 1
        col = (i % 2) + 1
        region_data = data[data['Region'] == region]
        
        for product in ['Electronics', 'Furniture', 'Clothing']:
            fig.add_trace(
                go.Bar(
                    name=product,
                    x=[product],
                    y=[region_data[region_data['Product'] == product]['Sales'].iloc[0]],
                    marker_color=colors[product],
                    text=[region_data[region_data['Product'] == product]['Sales'].iloc[0]],
                    textposition='auto',
                    showlegend=(i == 0)
                ),
                row=row, col=col
            )

    fig.update_layout(
        title_text="Regional Sales Overview",
        title_x=0.5,
        title_font=dict(size=24, family='Comic Sans MS', color='#666666'),
        showlegend=True,
        legend_title="Products",
        height=800,
        width=1000,
        template='simple_white',
        barmode='group',
        paper_bgcolor='#FAFAFA',
        plot_bgcolor='#FAFAFA',
        font=dict(family='Comic Sans MS')
    )
    
    fig.update_yaxes(title_text="Sales Volume", range=[0, data['Sales'].max() * 1.1], gridcolor='#E5E5E5')
    fig.write_image("多子图柱状图_style_4.png")

def plot_5(data):
    """Material design inspired."""
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[f"{region} Region" for region in ['North', 'South', 'East', 'West']],
        vertical_spacing=0.15,
        horizontal_spacing=0.1
    )
    
    colors = {'Electronics': '#6200EA', 'Furniture': '#00BFA5', 'Clothing': '#FFD600'}
    
    for i, region in enumerate(['North', 'South', 'East', 'West']):
        row = (i // 2) + 1
        col = (i % 2) + 1
        region_data = data[data['Region'] == region]
        
        for product in ['Electronics', 'Furniture', 'Clothing']:
            fig.add_trace(
                go.Bar(
                    name=product,
                    x=[product],
                    y=[region_data[region_data['Product'] == product]['Sales'].iloc[0]],
                    marker_color=colors[product],
                    text=[region_data[region_data['Product'] == product]['Sales'].iloc[0]],
                    textposition='auto',
                    showlegend=(i == 0)
                ),
                row=row, col=col
            )

    fig.update_layout(
        title_text="Regional Sales Metrics",
        title_x=0.5,
        title_font=dict(size=24, family='Roboto', color='#212121'),
        showlegend=True,
        legend_title="Product Types",
        height=800,
        width=1000,
        template='simple_white',
        barmode='group',
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family='Roboto')
    )
    
    fig.update_yaxes(title_text="Sales Volume", range=[0, data['Sales'].max() * 1.1], gridcolor='#E0E0E0')
    fig.write_image("多子图柱状图_style_5.png")

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
