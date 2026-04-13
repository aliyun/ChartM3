import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    # Create sample smartphone market share data if none provided
    if data is None:
        brands = {
            'Apple': [('iPhone 14', 15), ('iPhone 13', 12), ('iPhone 12', 8)],
            'Samsung': [('Galaxy S23', 11), ('Galaxy S22', 9), ('Galaxy A53', 7)],
            'Xiaomi': [('Redmi Note 12', 8), ('Redmi Note 11', 6)],
            'Huawei': [('P50', 5), ('Nova 10', 4)],
            'Others': [('Various Models', 15)]
        }
        
        # Create DataFrame with preserved order
        records = []
        for brand, models in brands.items():
            for model, share in models:
                records.append({
                    'Brand': brand,
                    'Model': model,
                    'Share': share
                })
        
        df = pd.DataFrame(records)
        # Ensure consistent order
        df['Brand'] = pd.Categorical(df['Brand'], categories=brands.keys(), ordered=True)
        df = df.sort_values('Brand')
        
        # Calculate brand shares
        brand_shares = df.groupby('Brand')['Share'].sum()
        df['Brand_Share'] = df['Brand'].map(brand_shares)
        
        df.to_csv('双层环图.csv', index=False)
        return df
    return data

def plot(data):
    # Color schemes for brands and their models
    colors = {
        'Apple': ['rgba(255,107,107,0.9)', 'rgba(255,135,135,0.8)', 'rgba(255,165,165,0.7)'],
        'Samsung': ['rgba(77,171,247,0.9)', 'rgba(116,192,252,0.8)', 'rgba(165,216,255,0.7)'],
        'Xiaomi': ['rgba(81,207,102,0.9)', 'rgba(105,219,124,0.8)'],
        'Huawei': ['rgba(255,212,59,0.9)', 'rgba(255,224,102,0.8)'],
        'Others': ['rgba(206,212,218,0.9)']
    }
    
    # Prepare data for plotting
    brands = data.groupby('Brand', sort=False)['Share'].sum().reset_index()
    
    # Create figure
    fig = go.Figure()
    
    # Add outer ring (models) - sorted by brand
    model_colors = []
    for brand in brands['Brand']:
        brand_data = data[data['Brand'] == brand]
        model_colors.extend(colors[brand][:len(brand_data)])
    
    # Common parameters for both rings
    common_params = dict(
        sort=False,
        direction='clockwise',
        rotation=90
    )
    fig.add_trace(go.Pie(
        values=data['Share'],
        labels=data['Model'],
        customdata=data['Brand'],
        domain={'x': [0.15, 0.85], 'y': [0.15, 0.85]},
        hole=0.75,
        name='Models',
        textinfo='label+percent',
        marker=dict(colors=model_colors),
        textposition='outside',
        **common_params,
        hovertemplate="Brand: %{customdata}<br>Model: %{label}<br>Share: %{percent}<extra></extra>"
    ))
    
    # Add inner ring (brands)
    fig.add_trace(go.Pie(
        values=brands['Share'],
        labels=brands['Brand'],
        domain={'x': [0.25, 0.75], 'y': [0.25, 0.75]},
        hole=0.6,
        name='Brands',
        textinfo='label+percent',
        marker=dict(colors=[colors[brand][0] for brand in brands['Brand']]),
        textposition='inside',
        **common_params,
        hovertemplate="Brand: %{label}<br>Total Share: %{percent}<extra></extra>"
    ))
    
    # Update layout
    fig.update_layout(
        title={
            'text': "Smartphone Market Share by Brand and Model",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        showlegend=False,
        width=800,
        height=800,
        annotations=[
            dict(
                text='Global<br>Market Share',
                x=0.5,
                y=0.5,
                font_size=14,
                showarrow=False
            )
        ]
    )
    
    # Save figure
    fig.write_image("双层环图.png")
    
    return fig

# Test the functions

def plot_1(data):
    # 商务简约风格
    colors = {
        'Apple': ['#2C3E50', '#34495E', '#415B76'],
        'Samsung': ['#2980B9', '#3498DB', '#5DADE2'],
        'Xiaomi': ['#27AE60', '#2ECC71', '#58D68D'],
        'Huawei': ['#F39C12', '#F1C40F', '#F4D03F'],
        'Others': ['#95A5A6']
    }
    
    brands = data.groupby('Brand', sort=False)['Share'].sum().reset_index()
    fig = go.Figure()
    
    model_colors = []
    for brand in brands['Brand']:
        brand_data = data[data['Brand'] == brand]
        model_colors.extend(colors[brand][:len(brand_data)])
    
    common_params = dict(
        sort=False,
        direction='clockwise',
        rotation=90
    )
    
    fig.add_trace(go.Pie(
        values=data['Share'],
        labels=data['Model'],
        customdata=data['Brand'],
        domain={'x': [0.15, 0.85], 'y': [0.15, 0.85]},
        hole=0.75,
        textinfo='label+percent',
        marker=dict(colors=model_colors),
        textposition='outside',
        **common_params
    ))
    
    fig.add_trace(go.Pie(
        values=brands['Share'],
        labels=brands['Brand'],
        domain={'x': [0.25, 0.75], 'y': [0.25, 0.75]},
        hole=0.6,
        textinfo='label+percent',
        marker=dict(colors=[colors[brand][0] for brand in brands['Brand']]),
        textposition='inside',
        **common_params
    ))
    
    fig.update_layout(
        title={
            'text': "Smartphone Market Share Analysis",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#2C3E50')
        },
        paper_bgcolor='#ECF0F1',
        plot_bgcolor='#ECF0F1',
        showlegend=False,
        width=800,
        height=800,
        annotations=[dict(
            text='Market<br>Overview',
            x=0.5,
            y=0.5,
            font_size=16,
            font_color='#2C3E50',
            showarrow=False
        )]
    )
    
    fig.write_image("双层环图_style_1.png")
    return fig

def plot_2(data):
    # 科技感风格
    colors = {
        'Apple': ['rgba(45,152,218,0.9)', 'rgba(45,152,218,0.7)', 'rgba(45,152,218,0.5)'],
        'Samsung': ['rgba(56,103,214,0.9)', 'rgba(56,103,214,0.7)', 'rgba(56,103,214,0.5)'],
        'Xiaomi': ['rgba(69,170,242,0.9)', 'rgba(69,170,242,0.7)'],
        'Huawei': ['rgba(75,123,236,0.9)', 'rgba(75,123,236,0.7)'],
        'Others': ['rgba(45,152,218,0.3)']
    }
    
    brands = data.groupby('Brand', sort=False)['Share'].sum().reset_index()
    fig = go.Figure()
    
    model_colors = []
    for brand in brands['Brand']:
        brand_data = data[data['Brand'] == brand]
        model_colors.extend(colors[brand][:len(brand_data)])
    
    common_params = dict(
        sort=False,
        direction='clockwise',
        rotation=90
    )
    
    fig.add_trace(go.Pie(
        values=data['Share'],
        labels=data['Model'],
        customdata=data['Brand'],
        domain={'x': [0.1, 0.9], 'y': [0.1, 0.9]},
        hole=0.7,
        textinfo='label+percent',
        marker=dict(colors=model_colors),
        textposition='outside',
        **common_params
    ))
    
    fig.add_trace(go.Pie(
        values=brands['Share'],
        labels=brands['Brand'],
        domain={'x': [0.2, 0.8], 'y': [0.2, 0.8]},
        hole=0.5,
        textinfo='label+percent',
        marker=dict(colors=[colors[brand][0] for brand in brands['Brand']]),
        textposition='inside',
        **common_params
    ))
    
    fig.update_layout(
        title={
            'text': "Tech Market Analysis",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#2D98DA')
        },
        paper_bgcolor='#1E272E',
        plot_bgcolor='#1E272E',
        showlegend=False,
        width=800,
        height=800,
        font=dict(color='#ffffff'),
        annotations=[dict(
            text='Market<br>Share',
            x=0.5,
            y=0.5,
            font_size=16,
            font_color='#ffffff',
            showarrow=False
        )]
    )
    
    fig.write_image("双层环图_style_2.png")
    return fig

def plot_3(data):
    # 环保自然风格
    colors = {
        'Apple': ['#88B04B', '#98C13D', '#A8D12F'],
        'Samsung': ['#79A83B', '#89B82D', '#99C81F'],
        'Xiaomi': ['#6A902B', '#7AA01D'],
        'Huawei': ['#5B781B', '#6B880D'],
        'Others': ['#4B600B']
    }
    
    brands = data.groupby('Brand', sort=False)['Share'].sum().reset_index()
    fig = go.Figure()
    
    model_colors = []
    for brand in brands['Brand']:
        brand_data = data[data['Brand'] == brand]
        model_colors.extend(colors[brand][:len(brand_data)])
    
    common_params = dict(
        sort=False,
        direction='clockwise',
        rotation=90
    )
    
    fig.add_trace(go.Pie(
        values=data['Share'],
        labels=data['Model'],
        customdata=data['Brand'],
        domain={'x': [0.12, 0.88], 'y': [0.12, 0.88]},
        hole=0.72,
        textinfo='label+percent',
        marker=dict(colors=model_colors),
        textposition='outside',
        **common_params
    ))
    
    fig.add_trace(go.Pie(
        values=brands['Share'],
        labels=brands['Brand'],
        domain={'x': [0.22, 0.78], 'y': [0.22, 0.78]},
        hole=0.55,
        textinfo='label+percent',
        marker=dict(colors=[colors[brand][0] for brand in brands['Brand']]),
        textposition='inside',
        **common_params
    ))
    
    fig.update_layout(
        title={
            'text': "Sustainable Market Overview",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#88B04B')
        },
        paper_bgcolor='#F5F7F2',
        plot_bgcolor='#F5F7F2',
        showlegend=False,
        width=800,
        height=800,
        annotations=[dict(
            text='Market<br>Distribution',
            x=0.5,
            y=0.5,
            font_size=16,
            font_color='#88B04B',
            showarrow=False
        )]
    )
    
    fig.write_image("双层环图_style_3.png")
    return fig

def plot_4(data):
    # 现代极简风格
    colors = {
        'Apple': ['#000000', '#333333', '#666666'],
        'Samsung': ['#1A1A1A', '#4D4D4D', '#808080'],
        'Xiaomi': ['#333333', '#666666'],
        'Huawei': ['#4D4D4D', '#808080'],
        'Others': ['#999999']
    }
    
    brands = data.groupby('Brand', sort=False)['Share'].sum().reset_index()
    fig = go.Figure()
    
    model_colors = []
    for brand in brands['Brand']:
        brand_data = data[data['Brand'] == brand]
        model_colors.extend(colors[brand][:len(brand_data)])
    
    common_params = dict(
        sort=False,
        direction='clockwise',
        rotation=90
    )
    
    fig.add_trace(go.Pie(
        values=data['Share'],
        labels=data['Model'],
        customdata=data['Brand'],
        domain={'x': [0.15, 0.85], 'y': [0.15, 0.85]},
        hole=0.8,
        textinfo='label+percent',
        marker=dict(colors=model_colors),
        textposition='outside',
        **common_params
    ))
    
    fig.add_trace(go.Pie(
        values=brands['Share'],
        labels=brands['Brand'],
        domain={'x': [0.3, 0.7], 'y': [0.3, 0.7]},
        hole=0.65,
        textinfo='label+percent',
        marker=dict(colors=[colors[brand][0] for brand in brands['Brand']]),
        textposition='inside',
        **common_params
    ))
    
    fig.update_layout(
        title={
            'text': "Market Share Distribution",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#000000')
        },
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF',
        showlegend=False,
        width=800,
        height=800,
        annotations=[dict(
            text='Share',
            x=0.5,
            y=0.5,
            font_size=16,
            font_color='#000000',
            showarrow=False
        )]
    )
    
    fig.write_image("双层环图_style_4.png")
    return fig

def plot_5(data):
    # 活泼明快风格
    colors = {
        'Apple': ['#FF6B6B', '#FF8787', '#FFA5A5'],
        'Samsung': ['#4DABF7', '#74C0FC', '#A5D8FF'],
        'Xiaomi': ['#51CF66', '#69DB7C'],
        'Huawei': ['#FFD43B', '#FFE066'],
        'Others': ['#CED4DA']
    }
    
    brands = data.groupby('Brand', sort=False)['Share'].sum().reset_index()
    fig = go.Figure()
    
    model_colors = []
    for brand in brands['Brand']:
        brand_data = data[data['Brand'] == brand]
        model_colors.extend(colors[brand][:len(brand_data)])
    
    common_params = dict(
        sort=False,
        direction='clockwise',
        rotation=90
    )
    
    fig.add_trace(go.Pie(
        values=data['Share'],
        labels=data['Model'],
        customdata=data['Brand'],
        domain={'x': [0.1, 0.9], 'y': [0.1, 0.9]},
        hole=0.65,
        textinfo='label+percent',
        marker=dict(colors=model_colors),
        textposition='outside',
        **common_params
    ))
    
    fig.add_trace(go.Pie(
        values=brands['Share'],
        labels=brands['Brand'],
        domain={'x': [0.25, 0.75], 'y': [0.25, 0.75]},
        hole=0.45,
        textinfo='label+percent',
        marker=dict(colors=[colors[brand][0] for brand in brands['Brand']]),
        textposition='inside',
        **common_params
    ))
    
    fig.update_layout(
        title={
            'text': "Fun Market Share View",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24, color='#FF6B6B', family='Arial Black')
        },
        paper_bgcolor='#F8F9FA',
        plot_bgcolor='#F8F9FA',
        showlegend=False,
        width=800,
        height=800,
        annotations=[dict(
            text='Share<br>Analysis',
            x=0.5,
            y=0.5,
            font_size=16,
            font_color='#FF6B6B',
            showarrow=False
        )]
    )
    
    fig.write_image("双层环图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
