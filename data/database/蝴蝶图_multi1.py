import pandas as pd
import numpy as np
import plotly.graph_objects as go

def preprocess(data=None):
    # Generate synthetic population data by age group
    age_groups = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60+']
    
    # Create somewhat realistic population distribution
    np.random.seed(42)
    base_pop = 10000
    male_pop = [(base_pop * (1 + np.random.normal(0, 0.1)) * (1 - i*0.08)) for i in range(len(age_groups))]
    female_pop = [(base_pop * (1 + np.random.normal(0, 0.1)) * (1 - i*0.08)) for i in range(len(age_groups))]
    
    # Convert male population to negative for left side plotting
    male_pop = [-x for x in male_pop]
    
    # Create dataframe
    df = pd.DataFrame({
        'Age_Group': age_groups,
        'Male': male_pop,
        'Female': female_pop
    })
    
    # Save to CSV
    df.to_csv('蝴蝶图.csv', index=False)
    return df

def plot(data):
    # Create figure
    fig = go.Figure()
    
    # Add male population bars (left side)
    fig.add_trace(go.Bar(
        y=data['Age_Group'],
        x=data['Male'],
        name='Male',
        orientation='h',
        marker_color='royalblue',
        text=[f'{abs(x):,.0f}' for x in data['Male']],
        textposition='inside',
        textfont=dict(color='white'),
    ))
    
    # Add female population bars (right side)
    fig.add_trace(go.Bar(
        y=data['Age_Group'],
        x=data['Female'],
        name='Female',
        orientation='h',
        marker_color='crimson',
        text=[f'{x:,.0f}' for x in data['Female']],
        textposition='inside',
        textfont=dict(color='white'),
    ))

    # Update layout
    fig.update_layout(
        title={
            'text': 'Population Distribution by Age and Gender',
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(size=24)
        },
        barmode='relative',
        bargap=0.1,
        xaxis=dict(
            title='Population',
            tickformat=',d',
            zeroline=True,
            zerolinecolor='black',
            zerolinewidth=2,
        ),
        yaxis=dict(
            title='Age Group',
            zeroline=False,
            gridcolor='lightgray', 
            gridwidth=0.5,
        ),
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        font=dict(size=14),
        plot_bgcolor='white',
        width=1000,
        height=600,
        margin=dict(l=80, r=80, t=100, b=80)
    )
    
    # Save plot
    fig.write_image("蝴蝶图.png")
    return fig

# Example usage

def plot_1(data):
    # 现代简约风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=data['Age_Group'],
        x=data['Male'],
        name='Male',
        orientation='h',
        marker_color='#4A90E2',
        opacity=0.85,
        text=[f'{abs(x):,.0f}' for x in data['Male']],
        textposition='outside',
        textfont=dict(color='#4A90E2'),
    ))
    
    fig.add_trace(go.Bar(
        y=data['Age_Group'],
        x=data['Female'],
        name='Female',
        orientation='h',
        marker_color='#E2A3A3',
        opacity=0.85,
        text=[f'{x:,.0f}' for x in data['Female']],
        textposition='outside',
        textfont=dict(color='#E2A3A3'),
    ))

    fig.update_layout(
        title={
            'text': 'Population Distribution',
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(size=24, family='Arial', color='#2C3E50')
        },
        barmode='relative',
        bargap=0.2,
        xaxis=dict(
            title='Population',
            tickformat=',d',
            zeroline=True,
            zerolinecolor='#2C3E50',
            zerolinewidth=1,
            gridcolor='#E5E5E5',
        ),
        yaxis=dict(
            title='Age Group',
            zeroline=False,
            gridcolor='#E5E5E5',
        ),
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        font=dict(family='Arial'),
        plot_bgcolor='white',
        width=1000,
        height=600,
        margin=dict(l=80, r=80, t=100, b=80)
    )
    
    fig.write_image("蝴蝶图_style_1.png")
    return fig

def plot_2(data):
    # 环保主题
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=data['Age_Group'],
        x=data['Male'],
        name='Male',
        orientation='h',
        marker_color='#2D5A27',
        text=[f'{abs(x):,.0f}' for x in data['Male']],
        textposition='inside',
        textfont=dict(color='white'),
    ))
    
    fig.add_trace(go.Bar(
        y=data['Age_Group'],
        x=data['Female'],
        name='Female',
        orientation='h',
        marker_color='#4CAF50',
        text=[f'{x:,.0f}' for x in data['Female']],
        textposition='inside',
        textfont=dict(color='white'),
    ))

    fig.update_layout(
        title={
            'text': 'Population Distribution by Age and Gender',
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(size=24, color='#1B4332')
        },
        barmode='relative',
        bargap=0.15,
        xaxis=dict(
            title='Population',
            tickformat=',d',
            zeroline=True,
            zerolinecolor='#1B4332',
            zerolinewidth=2,
            gridcolor='#95D5B2',
        ),
        yaxis=dict(
            title='Age Group',
            zeroline=False,
            gridcolor='#95D5B2',
        ),
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1,
            bgcolor='rgba(149, 213, 178, 0.1)'
        ),
        plot_bgcolor='#FAFFF9',
        paper_bgcolor='#FAFFF9',
        width=1000,
        height=600,
        margin=dict(l=80, r=80, t=100, b=80)
    )
    
    fig.write_image("蝴蝶图_style_2.png")
    return fig

def plot_3(data):
    # 高科技风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=data['Age_Group'],
        x=data['Male'],
        name='Male',
        orientation='h',
        marker_color='#00FF9F',
        opacity=0.8,
        text=[f'{abs(x):,.0f}' for x in data['Male']],
        textposition='inside',
        textfont=dict(color='#1A1A1A'),
    ))
    
    fig.add_trace(go.Bar(
        y=data['Age_Group'],
        x=data['Female'],
        name='Female',
        orientation='h',
        marker_color='#00D1FF',
        opacity=0.8,
        text=[f'{x:,.0f}' for x in data['Female']],
        textposition='inside',
        textfont=dict(color='#1A1A1A'),
    ))

    fig.update_layout(
        title={
            'text': 'Population Distribution Analysis',
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(size=24, color='#00FF9F')
        },
        barmode='relative',
        bargap=0.15,
        xaxis=dict(
            title='Population',
            tickformat=',d',
            zeroline=True,
            zerolinecolor='#00FF9F',
            zerolinewidth=2,
            gridcolor='#333333',
            color='#FFFFFF'
        ),
        yaxis=dict(
            title='Age Group',
            zeroline=False,
            gridcolor='#333333',
            color='#FFFFFF'
        ),
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1,
            font=dict(color='#FFFFFF')
        ),
        plot_bgcolor='#1A1A1A',
        paper_bgcolor='#1A1A1A',
        width=1000,
        height=600,
        margin=dict(l=80, r=80, t=100, b=80)
    )
    
    fig.write_image("蝴蝶图_style_3.png")
    return fig

def plot_4(data):
    # 活力风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=data['Age_Group'],
        x=data['Male'],
        name='Male',
        orientation='h',
        marker_color='#FF6B6B',
        text=[f'{abs(x):,.0f}' for x in data['Male']],
        textposition='inside',
        textfont=dict(color='white'),
    ))
    
    fig.add_trace(go.Bar(
        y=data['Age_Group'],
        x=data['Female'],
        name='Female',
        orientation='h',
        marker_color='#4ECDC4',
        text=[f'{x:,.0f}' for x in data['Female']],
        textposition='inside',
        textfont=dict(color='white'),
    ))

    fig.update_layout(
        title={
            'text': 'Population Distribution',
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(size=24, family='Helvetica', color='#2C3E50')
        },
        barmode='relative',
        bargap=0.2,
        xaxis=dict(
            title='Population',
            tickformat=',d',
            zeroline=True,
            zerolinecolor='#2C3E50',
            zerolinewidth=2,
            gridcolor='#EEEEEE',
        ),
        yaxis=dict(
            title='Age Group',
            zeroline=False,
            gridcolor='#EEEEEE',
        ),
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1,
            bgcolor='rgba(255,255,255,0.8)'
        ),
        font=dict(family='Helvetica'),
        plot_bgcolor='white',
        width=1000,
        height=600,
        margin=dict(l=80, r=80, t=100, b=80)
    )
    
    fig.write_image("蝴蝶图_style_4.png")
    return fig

def plot_5(data):
    # 复古风格
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=data['Age_Group'],
        x=data['Male'],
        name='Male',
        orientation='h',
        marker_color='#8B4513',
        opacity=0.8,
        text=[f'{abs(x):,.0f}' for x in data['Male']],
        textposition='inside',
        textfont=dict(color='white'),
    ))
    
    fig.add_trace(go.Bar(
        y=data['Age_Group'],
        x=data['Female'],
        name='Female',
        orientation='h',
        marker_color='#D2691E',
        opacity=0.8,
        text=[f'{x:,.0f}' for x in data['Female']],
        textposition='inside',
        textfont=dict(color='white'),
    ))

    fig.update_layout(
        title={
            'text': 'Population Distribution Study',
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(size=24, family='Garamond', color='#5C4033')
        },
        barmode='relative',
        bargap=0.15,
        xaxis=dict(
            title='Population',
            tickformat=',d',
            zeroline=True,
            zerolinecolor='#5C4033',
            zerolinewidth=1,
            gridcolor='#DEB887',
        ),
        yaxis=dict(
            title='Age Group',
            zeroline=False,
            gridcolor='#DEB887',
        ),
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1,
            bgcolor='rgba(222,184,135,0.1)'
        ),
        font=dict(family='Garamond'),
        plot_bgcolor='#FFF8DC',
        paper_bgcolor='#FFF8DC',
        width=1000,
        height=600,
        margin=dict(l=80, r=80, t=100, b=80)
    )
    
    fig.write_image("蝴蝶图_style_5.png")
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
