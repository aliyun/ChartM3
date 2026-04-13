import pandas as pd
import plotly.express as px
import plotly.io as pio

def preprocess():
    # Create sample data for market share visualization
    data = pd.DataFrame([
        ['Total', 'Enterprise', 40],
        ['Total', 'Consumer', 60],
        ['Enterprise', 'Cloud', 15],
        ['Enterprise', 'Security', 10],
        ['Enterprise', 'Services', 15],
        ['Consumer', 'Mobile', 25],
        ['Consumer', 'PC', 20],
        ['Consumer', 'IoT', 15]
    ], columns=['parent', 'segment', 'value'])
    
    # Save to CSV
    data.to_csv('嵌套饼图.csv', index=False)
    return data

def plot(data):
    # Create sunburst chart
    fig = px.sunburst(
        data,
        path=['parent', 'segment'],
        values='value',
        title='Market Share Distribution',
        color_discrete_sequence=px.colors.qualitative.Set3,
        height=700
    )
    
    # Update layout
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        showlegend=True,
        uniformtext=dict(minsize=12)
    )
    
    # Update traces
    fig.update_traces(
        textinfo='label+percent parent',
        hovertemplate='<b>%{label}</b><br>Share: %{value}%'
    )
    
    # Save plot
    pio.write_image(fig, '嵌套饼图.png')
    return fig

def plot_1(data):
    # 商务简约风
    fig = px.sunburst(
        data,
        path=['parent', 'segment'],
        values='value',
        title='Market Share Distribution - Business Style',
        color_discrete_sequence=['#1f77b4', '#2c3e50', '#3498db', '#95a5a6', '#34495e', '#2980b9'],
        height=700
    )
    
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        plot_bgcolor='white',
        paper_bgcolor='white',
        title_font_family='Arial Black',
        showlegend=True,
        uniformtext=dict(minsize=12)
    )
    
    fig.update_traces(
        textinfo='label+percent parent',
        hovertemplate='<b>%{label}</b><br>Share: %{value}%',
        insidetextfont=dict(size=14),
        opacity=0.9
    )
    
    pio.write_image(fig, '嵌套饼图_style_1.png')
    return fig

def plot_2(data):
    # 现代科技风
    fig = px.sunburst(
        data,
        path=['parent', 'segment'],
        values='value',
        title='Market Share Distribution - Tech Style',
        color_discrete_sequence=['#00ff00', '#00cc00', '#009900', '#006600', '#003300'],
        height=700
    )
    
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_color='white',
        title_font_family='Courier New',
        showlegend=True
    )
    
    fig.update_traces(
        textinfo='label+percent parent',
        hovertemplate='<b>%{label}</b><br>Share: %{value}%',
        insidetextfont=dict(size=12, color='white'),
        opacity=0.8
    )
    
    pio.write_image(fig, '嵌套饼图_style_2.png')
    return fig

def plot_3(data):
    # 柔和清新风
    fig = px.sunburst(
        data,
        path=['parent', 'segment'],
        values='value',
        title='Market Share Distribution - Fresh Style',
        color_discrete_sequence=['#FFB5C5', '#FFE4E1', '#FFC0CB', '#FFF0F5', '#FFE4E1'],
        height=700
    )
    
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        plot_bgcolor='#FFF5EE',
        paper_bgcolor='#FFF5EE',
        title_font_family='Comic Sans MS',
        showlegend=True
    )
    
    fig.update_traces(
        textinfo='label+percent parent',
        hovertemplate='<b>%{label}</b><br>Share: %{value}%',
        insidetextfont=dict(size=12),
        opacity=1
    )
    
    pio.write_image(fig, '嵌套饼图_style_3.png')
    return fig

def plot_4(data):
    # 专业数据分析风
    fig = px.sunburst(
        data,
        path=['parent', 'segment'],
        values='value',
        title='Market Share Distribution - Analytics Style',
        color_discrete_sequence=px.colors.sequential.Viridis,
        height=700
    )
    
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        plot_bgcolor='white',
        paper_bgcolor='white',
        title_font_family='Arial',
        showlegend=True,
        annotations=[
            dict(text="Data Source: Market Analysis 2023", 
                 x=0.02, y=-0.1, showarrow=False, xref='paper', yref='paper')
        ]
    )
    
    fig.update_traces(
        textinfo='label+value+percent parent',
        hovertemplate='<b>%{label}</b><br>Share: %{value}%<br>Parent: %{parent}',
        insidetextfont=dict(size=11)
    )
    
    pio.write_image(fig, '嵌套饼图_style_4.png')
    return fig

def plot_5(data):
    # 高对比度风格
    fig = px.sunburst(
        data,
        path=['parent', 'segment'],
        values='value',
        title='Market Share Distribution - High Contrast',
        color_discrete_sequence=['#FF4500', '#FFD700', '#FF6347', '#FFA500', '#FF8C00'],
        height=700
    )
    
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        font_color='white',
        title_font_family='Helvetica',
        showlegend=True,
        uniformtext=dict(minsize=14)
    )
    
    fig.update_traces(
        textinfo='label+percent parent',
        hovertemplate='<b>%{label}</b><br>Share: %{value}%',
        insidetextfont=dict(size=13, color='white'),
        opacity=0.95
    )
    
    pio.write_image(fig, '嵌套饼图_style_5.png')
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
