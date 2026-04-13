import pandas as pd
import plotly.express as px
import plotly.io as pio

def preprocess(data=None):
    # Create sample smartphone market share data
    data = pd.DataFrame({
        'Manufacturer': ['Samsung', 'Apple', 'Xiaomi', 'Oppo', 'Others'],
        'Market_Share': [21, 18, 14, 9, 38]
    })
    
    # Save to CSV
    data.to_csv('基础饼图.csv', index=False)
    return data

def plot(data):
    # Create pie chart
    fig = px.pie(data, 
                 values='Market_Share',
                 names='Manufacturer',
                 title='Global Smartphone Market Share by Manufacturer',
                 color_discrete_sequence=px.colors.qualitative.Set3,
                 hole=0.)
    
    # Update layout
    fig.update_traces(textposition='inside', 
                     textinfo='percent+label',
                     textfont_size=12)
    
    fig.update_layout(
        title_x=0.5,
        title_font_size=18,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        )
    )
    
    # Save as HTML and PNG
    fig.write_image("基础饼图.png", width=800, height=600)
    
    return fig

# Run the pipeline

def plot_1(data):
    # 商务简约风
    fig = px.pie(data, 
                 values='Market_Share',
                 names='Manufacturer',
                 title='Global Smartphone Market Share',
                 color_discrete_sequence=['#2E5077', '#4C7CAC', '#89A7C9', '#BBC9DD', '#E1E9F2'],
                 hole=0.6)
    
    fig.update_traces(textposition='outside',
                     textinfo='percent+label',
                     pull=[0.05, 0.05, 0.05, 0.05, 0.05])
    
    fig.update_layout(
        plot_bgcolor='white',
        title_x=0.5,
        title_font=dict(size=20, color='#2E5077'),
        showlegend=False,
        annotations=[dict(text='Market<br>Share', x=0.5, y=0.5, font_size=18, showarrow=False)]
    )
    
    fig.write_image("基础饼图_style_1.png", width=800, height=600)
    return fig

def plot_2(data):
    # 科技感深色风格
    fig = px.pie(data, 
                 values='Market_Share',
                 names='Manufacturer',
                 title='Smartphone Market Distribution',
                 color_discrete_sequence=['#00FF00', '#00CC00', '#009900', '#006600', '#003300'],
                 hole=0.7)
    
    fig.update_traces(textposition='inside',
                     textinfo='percent',
                     textfont=dict(color='white'))
    
    fig.update_layout(
        paper_bgcolor='black',
        plot_bgcolor='black',
        title_font=dict(color='white', size=22),
        title_x=0.5,
        font_color='white',
        showlegend=True,
        legend=dict(orientation="v", xanchor="center", x=0.9)
    )
    
    fig.write_image("基础饼图_style_2.png", width=800, height=600)
    return fig

def plot_3(data):
    # 柔和渐变风格
    fig = px.pie(data, 
                 values='Market_Share',
                 names='Manufacturer',
                 title='Smartphone Companies Market Share',
                 color_discrete_sequence=px.colors.sequential.Peach,
                 hole=0.4)
    
    fig.update_traces(textposition='inside',
                     textinfo='label+percent',
                     rotation=90)
    
    fig.update_layout(
        title_x=0.5,
        title_font=dict(size=18, family="Arial", color="#666666"),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.3)
    )
    
    fig.write_image("基础饼图_style_3.png", width=800, height=600)
    return fig

def plot_4(data):
    # 高端黑金风格
    fig = px.pie(data, 
                 values='Market_Share',
                 names='Manufacturer',
                 title='Premium Market Share Analysis',
                 color_discrete_sequence=['#FFD700', '#DAA520', '#B8860B', '#966919', '#614700'],
                 hole=0.5)
    
    fig.update_traces(textposition='outside',
                     textinfo='label+percent',
                     textfont=dict(color='black', size=14))
    
    fig.update_layout(
        title_font=dict(size=24, family="Times New Roman", color="#000000"),
        title_x=0.5,
        paper_bgcolor='white',
        plot_bgcolor='white',
        showlegend=True,
        legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1)
    )
    
    fig.write_image("基础饼图_style_4.png", width=800, height=600)
    return fig

def plot_5(data):
    # 活泼明亮风格
    fig = px.pie(data, 
                 values='Market_Share',
                 names='Manufacturer',
                 title='Smartphone Market Overview',
                 color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD'],
                 hole=0.3)
    
    fig.update_traces(textposition='inside',
                     textinfo='percent',
                     textfont=dict(size=16, color='white'))
    
    fig.update_layout(
        title_x=0.5,
        title_font=dict(size=22, family="Arial Black", color="#FF6B6B"),
        showlegend=True,
        legend=dict(
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='rgba(255,255,255,0.8)',
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="left",
            x=-0.2
        )
    )
    
    fig.write_image("基础饼图_style_5.png", width=800, height=600)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
