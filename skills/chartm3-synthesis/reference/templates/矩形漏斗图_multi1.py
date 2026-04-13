import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

def preprocess(data=None):
    # Create sample funnel data if none provided
    if data is None:
        stages = ['Website Visits', 'Product Views', 'Add to Cart', 'Purchases', 'Repeat Customers']
        values = [10000, 6000, 2500, 1200, 400]
        
        data = pd.DataFrame({
            'Stage': stages,
            'Value': values
        })
    
    # Calculate conversion rates
    data['Conversion Rate'] = data['Value'].pct_change() + 1
    data['Conversion Rate'] = data['Conversion Rate'].fillna(1)
    data['Conversion Rate'] = (data['Conversion Rate'] * 100).round(1)
    
    # Save to CSV
    data.to_csv('矩形漏斗图.csv', index=False)
    return data

def plot(data):
    # Create funnel chart
    fig = go.Figure(go.Funnel(
        y = data['Stage'],
        x = data['Value'],
        textposition = "auto",
        textinfo = "value+percent initial",
        opacity = 0.65,
        marker = {
            "color": ["#1f77b4", "#2a88bd", "#3599c6", "#40aacf", "#4bbcd8"],
            "line": {"width": [2, 2, 2, 2, 2], "color": ["white", "white", "white", "white", "white"]}
        },
        connector = {"line": {"color": "white", "width": 2}}
    ))
    
    # Update layout
    fig.update_layout(
        title = {
            'text': "Sales Funnel Analysis",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24}
        },
        font_size=14,
        showlegend = False,
        width = 800,
        height = 600,
        margin = dict(t=100, l=150, r=150, b=50),
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    # Add conversion rate annotations
    for i in range(len(data)-1):
        fig.add_annotation(
            x=data['Value'].iloc[i],
            y=data['Stage'].iloc[i],
            text=f"Conv. Rate: {data['Conversion Rate'].iloc[i+1]:.1f}%",
            showarrow=False,
            xanchor='left',
            xshift=50,
            font=dict(size=12)
        )
    
    # Save plot
    pio.write_image(fig, "矩形漏斗图.png")
    return fig


def plot_1(data):
    # 商务简约风
    fig = go.Figure(go.Funnel(
        y = data['Stage'],
        x = data['Value'],
        textposition = "auto",
        textinfo = "value+percent initial",
        opacity = 0.8,
        marker = {
            "color": ["#1f2937", "#374151", "#4b5563", "#6b7280", "#9ca3af"],
            "line": {"width": 1, "color": "white"}
        },
        connector = {"line": {"color": "white", "width": 1}}
    ))
    
    fig.update_layout(
        title = {
            'text': "Sales Funnel Analysis",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24, 'family': 'Arial', 'color': '#1f2937'}
        },
        font_size=12,
        showlegend = False,
        width = 800,
        height = 600,
        margin = dict(t=100, l=150, r=150, b=50),
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    for i in range(len(data)-1):
        fig.add_annotation(
            x=data['Value'].iloc[i],
            y=data['Stage'].iloc[i],
            text=f"Conv. Rate: {data['Conversion Rate'].iloc[i+1]:.1f}%",
            showarrow=False,
            xanchor='left',
            xshift=50,
            font=dict(size=10, color='#4b5563')
        )
    
    fig.write_image("矩形漏斗图_style_1.png")
    return fig

def plot_2(data):
    # 活力科技风
    fig = go.Figure(go.Funnel(
        y = data['Stage'],
        x = data['Value'],
        textposition = "auto",
        textinfo = "value+percent initial",
        opacity = 0.9,
        marker = {
            "color": ["#7209b7", "#560bad", "#480ca8", "#3a0ca3", "#3f37c9"],
            "line": {"width": 3, "color": "#f72585"}
        },
        connector = {"line": {"color": "#f72585", "width": 2}}
    ))
    
    fig.update_layout(
        title = {
            'text': "Sales Funnel Analysis",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 28, 'family': 'Roboto', 'color': '#7209b7'}
        },
        font_size=14,
        showlegend = False,
        width = 800,
        height = 600,
        margin = dict(t=100, l=150, r=150, b=50),
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    for i in range(len(data)-1):
        fig.add_annotation(
            x=data['Value'].iloc[i],
            y=data['Stage'].iloc[i],
            text=f"Conv. Rate: {data['Conversion Rate'].iloc[i+1]:.1f}%",
            showarrow=False,
            xanchor='left',
            xshift=50,
            font=dict(size=12, color='#560bad')
        )
    
    fig.write_image("矩形漏斗图_style_2.png")
    return fig

def plot_3(data):
    # 环保自然风
    fig = go.Figure(go.Funnel(
        y = data['Stage'],
        x = data['Value'],
        textposition = "auto",
        textinfo = "value+percent initial",
        opacity = 0.75,
        marker = {
            "color": ["#dad7cd", "#a3b18a", "#588157", "#3a5a40", "#344e41"],
            "line": {"width": 1.5, "color": "white"}
        },
        connector = {"line": {"color": "white", "width": 1.5}}
    ))
    
    fig.update_layout(
        title = {
            'text': "Sales Funnel Analysis",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24, 'family': 'Verdana', 'color': '#344e41'}
        },
        font_size=12,
        showlegend = False,
        width = 800,
        height = 600,
        margin = dict(t=100, l=150, r=150, b=50),
        paper_bgcolor='#fefae0',
        plot_bgcolor='#fefae0'
    )
    
    for i in range(len(data)-1):
        fig.add_annotation(
            x=data['Value'].iloc[i],
            y=data['Stage'].iloc[i],
            text=f"Conv. Rate: {data['Conversion Rate'].iloc[i+1]:.1f}%",
            showarrow=False,
            xanchor='left',
            xshift=50,
            font=dict(size=11, color='#3a5a40')
        )
    
    fig.write_image("矩形漏斗图_style_3.png")
    return fig

def plot_4(data):
    # 典雅复古风
    fig = go.Figure(go.Funnel(
        y = data['Stage'],
        x = data['Value'],
        textposition = "auto",
        textinfo = "value+percent initial",
        opacity = 0.85,
        marker = {
            "color": ["#cb997e", "#ddbea9", "#ffe8d6", "#b7b7a4", "#a5a58d"],
            "line": {"width": 2, "color": "#6b705c"}
        },
        connector = {"line": {"color": "#6b705c", "width": 1.5}}
    ))
    
    fig.update_layout(
        title = {
            'text': "Sales Funnel Analysis",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 26, 'family': 'Garamond', 'color': '#6b705c'}
        },
        font_size=12,
        showlegend = False,
        width = 800,
        height = 600,
        margin = dict(t=100, l=150, r=150, b=50),
        paper_bgcolor='#ffe8d6',
        plot_bgcolor='#ffe8d6'
    )
    
    for i in range(len(data)-1):
        fig.add_annotation(
            x=data['Value'].iloc[i],
            y=data['Stage'].iloc[i],
            text=f"Conv. Rate: {data['Conversion Rate'].iloc[i+1]:.1f}%",
            showarrow=False,
            xanchor='left',
            xshift=50,
            font=dict(size=11, color='#6b705c')
        )
    
    fig.write_image("矩形漏斗图_style_4.png")
    return fig

def plot_5(data):
    # 现代极简风
    fig = go.Figure(go.Funnel(
        y = data['Stage'],
        x = data['Value'],
        textposition = "auto",
        textinfo = "value+percent initial",
        opacity = 1,
        marker = {
            "color": ["#000000", "#262626", "#404040", "#525252", "#737373"],
            "line": {"width": 1, "color": "white"}
        },
        connector = {"line": {"color": "white", "width": 1}}
    ))
    
    fig.update_layout(
        title = {
            'text': "Sales Funnel Analysis",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 24, 'family': 'Helvetica', 'color': 'black'}
        },
        font_size=12,
        showlegend = False,
        width = 800,
        height = 600,
        margin = dict(t=100, l=150, r=150, b=50),
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    
    for i in range(len(data)-1):
        fig.add_annotation(
            x=data['Value'].iloc[i],
            y=data['Stage'].iloc[i],
            text=f"Conv. Rate: {data['Conversion Rate'].iloc[i+1]:.1f}%",
            showarrow=False,
            xanchor='left',
            xshift=50,
            font=dict(size=10, color='#404040')
        )
    
    fig.write_image("矩形漏斗图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
