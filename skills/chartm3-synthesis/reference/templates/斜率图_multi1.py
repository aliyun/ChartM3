import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def preprocess(data=None):
    # Create sample data
    data = pd.DataFrame({
        'Age_Group': ['18-29', '30-44', '45-60', '60+'],
        '2018': [65, 58, 45, 30],
        '2023': [92, 85, 70, 52]
    })
    
    # Melt the data for plotting
    data_melted = data.melt(
        id_vars=['Age_Group'],
        var_name='Year',
        value_name='Adoption_Rate'
    )
    
    # Save to CSV
    data_melted.to_csv('斜率图.csv', index=False)
    return data_melted

def plot(data):
    # Create figure
    fig = go.Figure()
    
    # Add lines for each age group
    colors = px.colors.qualitative.Set2
    for idx, age_group in enumerate(data['Age_Group'].unique()):
        group_data = data[data['Age_Group'] == age_group]
        
        fig.add_trace(go.Scatter(
            x=group_data['Year'],
            y=group_data['Adoption_Rate'],
            name=age_group,
            mode='lines+markers+text',
            line=dict(color=colors[idx], width=2),
            text=group_data['Adoption_Rate'].apply(lambda x: f"{x}%"),
            textposition='middle right',
            textfont=dict(size=12)
        ))

    # Update layout
    fig.update_layout(
        title="Technology Adoption Rates by Age Group (2018-2023)",
        xaxis_title="",
        yaxis_title="Adoption Rate (%)",
        plot_bgcolor='white',
        showlegend=True,
        legend_title_text="Age Groups",
        width=800,
        height=800
    )
    
    # Update axes
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray',
        range=[0, 100]
    )
    
    # Save plot
    fig.write_image("斜率图.png")
    return fig

def plot_1(data):
    # 商务风格 - 深蓝色渐变
    fig = go.Figure()
    colors = ['rgb(8,48,107)', 'rgb(8,81,156)', 'rgb(33,113,181)', 'rgb(66,146,198)']
    
    for idx, age_group in enumerate(data['Age_Group'].unique()):
        group_data = data[data['Age_Group'] == age_group]
        fig.add_trace(go.Scatter(
            x=group_data['Year'],
            y=group_data['Adoption_Rate'],
            name=age_group,
            mode='lines+markers+text',
            line=dict(color=colors[idx], width=2.5),
            marker=dict(size=8),
            text=group_data['Adoption_Rate'].apply(lambda x: f"{x}%"),
            textposition='top center',
            textfont=dict(size=11, color=colors[idx])
        ))

    fig.update_layout(
        title=dict(
            text="Technology Adoption Rates by Age Group (2018-2023)",
            font=dict(size=16, color='rgb(8,48,107)')
        ),
        xaxis_title="",
        yaxis_title="Adoption Rate (%)",
        plot_bgcolor='white',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        width=800,
        height=600
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', range=[0, 100])
    
    fig.write_image("斜率图_style_1.png")
    return fig

def plot_2(data):
    # 现代简约风格 - 黑白灰
    fig = go.Figure()
    colors = ['rgb(0,0,0)', 'rgb(70,70,70)', 'rgb(120,120,120)', 'rgb(170,170,170)']
    
    for idx, age_group in enumerate(data['Age_Group'].unique()):
        group_data = data[data['Age_Group'] == age_group]
        fig.add_trace(go.Scatter(
            x=group_data['Year'],
            y=group_data['Adoption_Rate'],
            name=age_group,
            mode='lines+markers+text',
            line=dict(color=colors[idx], width=1.5, dash='dot'),
            marker=dict(size=10, symbol='square'),
            text=group_data['Adoption_Rate'].apply(lambda x: f"{x}%"),
            textposition='bottom right',
            textfont=dict(size=10)
        ))

    fig.update_layout(
        title=dict(
            text="Technology Adoption Rates by Age Group",
            font=dict(size=14, color='black')
        ),
        plot_bgcolor='white',
        showlegend=True,
        legend_title_text="",
        width=800,
        height=600
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray', range=[0, 100])
    
    fig.write_image("斜率图_style_2.png")
    return fig

def plot_3(data):
    # 环保自然风格 - 绿色系
    fig = go.Figure()
    colors = ['rgb(0,109,44)', 'rgb(35,139,69)', 'rgb(65,171,93)', 'rgb(116,196,118)']
    
    for idx, age_group in enumerate(data['Age_Group'].unique()):
        group_data = data[data['Age_Group'] == age_group]
        fig.add_trace(go.Scatter(
            x=group_data['Year'],
            y=group_data['Adoption_Rate'],
            name=age_group,
            mode='lines+markers+text',
            line=dict(color=colors[idx], width=3),
            marker=dict(size=12, symbol='circle-open'),
            text=group_data['Adoption_Rate'].apply(lambda x: f"{x}%"),
            textposition='top right',
            textfont=dict(size=12, color=colors[idx])
        ))

    fig.update_layout(
        title=dict(
            text="Technology Adoption Trends",
            font=dict(size=18, color='rgb(0,109,44)')
        ),
        plot_bgcolor='rgb(242,250,242)',
        paper_bgcolor='rgb(242,250,242)',
        showlegend=True,
        legend=dict(bgcolor='rgba(255,255,255,0.8)'),
        width=800,
        height=600
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='white', range=[0, 100])
    
    fig.write_image("斜率图_style_3.png")
    return fig

def plot_4(data):
    # 科技感风格 - 霓虹色系
    fig = go.Figure()
    colors = ['rgb(255,64,129)', 'rgb(0,176,255)', 'rgb(57,255,20)', 'rgb(255,215,0)']
    
    for idx, age_group in enumerate(data['Age_Group'].unique()):
        group_data = data[data['Age_Group'] == age_group]
        fig.add_trace(go.Scatter(
            x=group_data['Year'],
            y=group_data['Adoption_Rate'],
            name=age_group,
            mode='lines+markers+text',
            line=dict(color=colors[idx], width=2),
            marker=dict(size=10, symbol='diamond'),
            text=group_data['Adoption_Rate'].apply(lambda x: f"{x}%"),
            textposition='top center',
            textfont=dict(size=12, color=colors[idx])
        ))

    fig.update_layout(
        title=dict(
            text="Digital Technology Adoption Matrix",
            font=dict(size=16, color='white')
        ),
        plot_bgcolor='rgb(17,17,17)',
        paper_bgcolor='rgb(17,17,17)',
        showlegend=True,
        legend=dict(
            font=dict(color='white')
        ),
        xaxis=dict(color='white'),
        yaxis=dict(color='white'),
        width=800,
        height=600
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='rgba(255,255,255,0.1)', range=[0, 100])
    
    fig.write_image("斜率图_style_4.png")
    return fig

def plot_5(data):
    # 活力青春风格 - 明亮对比色
    fig = go.Figure()
    colors = ['rgb(255,95,86)', 'rgb(255,154,0)', 'rgb(255,198,0)', 'rgb(0,184,148)']
    
    for idx, age_group in enumerate(data['Age_Group'].unique()):
        group_data = data[data['Age_Group'] == age_group]
        fig.add_trace(go.Scatter(
            x=group_data['Year'],
            y=group_data['Adoption_Rate'],
            name=age_group,
            mode='lines+markers+text',
            line=dict(color=colors[idx], width=4),
            marker=dict(size=14, symbol='star'),
            text=group_data['Adoption_Rate'].apply(lambda x: f"{x}%"),
            textposition='top center',
            textfont=dict(size=14, color=colors[idx])
        ))

    fig.update_layout(
        title=dict(
            text="✨ Tech Adoption Across Generations ✨",
            font=dict(size=20, color='rgb(44,62,80)')
        ),
        plot_bgcolor='white',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        ),
        width=800,
        height=600
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(189,195,199,0.5)', range=[0, 100])
    
    fig.write_image("斜率图_style_5.png")
    return fig


data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
