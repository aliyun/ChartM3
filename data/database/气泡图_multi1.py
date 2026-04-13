import pandas as pd
import plotly.express as px
import plotly.io as pio

def preprocess(data=None):
    # Generate sample data for major world cities
    cities_data = {
        'city': ['Tokyo', 'New York', 'London', 'Paris', 'Beijing', 
                 'Mumbai', 'São Paulo', 'Cairo', 'Sydney', 'Singapore',
                 'Moscow', 'Berlin', 'Dubai', 'Toronto', 'Seoul'],
        'gdp_per_capita': [42000, 75000, 56000, 52000, 18000,
                          2500, 15000, 3500, 58000, 65000,
                          12000, 48000, 45000, 49000, 35000],
        'life_expectancy': [84.2, 78.5, 81.3, 82.5, 76.1,
                           69.8, 75.2, 71.5, 83.2, 83.5,
                           72.4, 81.1, 77.8, 82.4, 82.8],
        'population': [37.4, 18.8, 9.0, 11.0, 20.5,
                      20.4, 22.0, 20.9, 5.3, 5.7,
                      12.5, 3.7, 3.3, 6.2, 9.8]
    }
    
    df = pd.DataFrame(cities_data)
    
    # Save to CSV
    df.to_csv('气泡图.csv', index=False)
    return df

def plot(data):
    # Create bubble plot
    fig = px.scatter(data, 
                    x='gdp_per_capita',
                    y='life_expectancy',
                    size='population',
                    text='city',
                    color='gdp_per_capita',
                    color_continuous_scale='Viridis',
                    title='World Cities: GDP, Life Expectancy & Population',
                    labels={
                        'gdp_per_capita': 'GDP per Capita (USD)',
                        'life_expectancy': 'Life Expectancy (Years)',
                        'population': 'Population (Millions)'
                    },
                    size_max=50)

    # Customize layout
    fig.update_layout(
        plot_bgcolor='white',
        font_family='Arial',
        font_size=12,
        title_x=0.5,
        title_font_size=20,
        showlegend=True,
        width=900,
        height=600,
        margin=dict(t=80, b=60, l=60, r=60)
    )
    
    fig.update_xaxes(
        showgrid=True,
        gridwidth=0.5,
        gridcolor='lightgray',
        zeroline=False,
        showline=True,
        linewidth=1,
        linecolor='black'
    )
    
    fig.update_yaxes(
        showgrid=True,
        gridwidth=0.5,
        gridcolor='lightgray',
        zeroline=False,
        showline=True,
        linewidth=1,
        linecolor='black'
    )
    
    # Customize hover text
    fig.update_traces(
        hovertemplate="<b>%{text}</b><br>" +
        "GDP per Capita: $%{x:,.0f}<br>" +
        "Life Expectancy: %{y:.1f} years<br>" +
        "Population: %{marker.size:.1f}M<br>" +
        "<extra></extra>",
        textposition='top center'
    )

    # Save plot
    pio.write_image(fig, '气泡图.png')
    return fig


def plot_1(data):
    # 商务风格
    fig = px.scatter(data, 
                    x='gdp_per_capita',
                    y='life_expectancy',
                    size='population',
                    text='city',
                    color='gdp_per_capita',
                    color_continuous_scale=['#1a237e','#0d47a1','#1976d2','#64b5f6'],
                    title='Global Economic Indicators')
    
    fig.update_layout(
        plot_bgcolor='#283747',
        paper_bgcolor='#283747',
        font_family='Arial',
        font_color='white',
        title_x=0.5,
        width=900,
        height=600,
        margin=dict(t=80, b=60, l=60, r=60)
    )
    
    fig.update_traces(
        marker=dict(opacity=0.8),
        textposition='top center',
        textfont=dict(color='white')
    )
    
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)', showline=True, linewidth=1, linecolor='white')
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.1)', showline=True, linewidth=1, linecolor='white')
    
    pio.write_image(fig, '气泡图_style_1.png')
    return fig

def plot_2(data):
    # 柔和风格
    fig = px.scatter(data, 
                    x='gdp_per_capita',
                    y='life_expectancy',
                    size='population',
                    text='city',
                    color='gdp_per_capita',
                    color_continuous_scale=['#ffcdd2','#f8bbd0','#e1bee7'],
                    title='City Development Overview')
    
    fig.update_layout(
        plot_bgcolor='#fff9f9',
        paper_bgcolor='#fff9f9',
        font_family='Helvetica',
        title_x=0.5,
        width=900,
        height=600,
        margin=dict(t=80, b=60, l=60, r=60)
    )
    
    fig.update_traces(
        marker=dict(opacity=0.6),
        textposition='top center'
    )
    
    fig.update_xaxes(gridcolor='rgba(0,0,0,0.1)', showline=False)
    fig.update_yaxes(gridcolor='rgba(0,0,0,0.1)', showline=False)
    
    pio.write_image(fig, '气泡图_style_2.png')
    return fig

def plot_3(data):
    # 现代简约风格
    fig = px.scatter(data, 
                    x='gdp_per_capita',
                    y='life_expectancy',
                    size='population',
                    text='city',
                    color='gdp_per_capita',
                    color_continuous_scale=['#000000','#808080','#ffffff'],
                    title='Urban Development Matrix')
    
    fig.update_layout(
        plot_bgcolor='white',
        font_family='Roboto',
        title_x=0.5,
        showlegend=False,
        width=900,
        height=600,
        margin=dict(t=80, b=60, l=60, r=60)
    )
    
    fig.update_traces(
        marker=dict(line=dict(width=1, color='black')),
        textposition='top center'
    )
    
    fig.update_xaxes(showgrid=False, showline=True, linewidth=2, linecolor='black')
    fig.update_yaxes(showgrid=False, showline=True, linewidth=2, linecolor='black')
    
    pio.write_image(fig, '气泡图_style_3.png')
    return fig

def plot_4(data):
    # 科技感风格
    fig = px.scatter(data, 
                    x='gdp_per_capita',
                    y='life_expectancy',
                    size='population',
                    text='city',
                    color='gdp_per_capita',
                    color_continuous_scale=['#00ff00','#ff00ff','#00ffff'],
                    title='Digital City Analysis')
    
    fig.update_layout(
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_family='Courier New',
        font_color='#00ff00',
        title_x=0.5,
        width=900,
        height=600,
        margin=dict(t=80, b=60, l=60, r=60)
    )
    
    fig.update_traces(
        marker=dict(symbol='diamond'),
        textposition='top center',
        textfont=dict(color='#00ff00')
    )
    
    fig.update_xaxes(gridcolor='#1a1a1a', showline=True, linecolor='#00ff00')
    fig.update_yaxes(gridcolor='#1a1a1a', showline=True, linecolor='#00ff00')
    
    pio.write_image(fig, '气泡图_style_4.png')
    return fig

def plot_5(data):
    # 自然风格
    fig = px.scatter(data, 
                    x='gdp_per_capita',
                    y='life_expectancy',
                    size='population',
                    text='city',
                    color='gdp_per_capita',
                    color_continuous_scale=['#2E7D32','#388E3C','#43A047','#66BB6A'],
                    title='Sustainable City Development')
    
    fig.update_layout(
        plot_bgcolor='#f1f8e9',
        paper_bgcolor='#f1f8e9',
        font_family='Verdana',
        title_x=0.5,
        width=900,
        height=600,
        margin=dict(t=80, b=60, l=60, r=60)
    )
    
    fig.update_traces(
        marker=dict(opacity=0.7),
        textposition='top center'
    )
    
    fig.update_xaxes(gridcolor='rgba(46,125,50,0.2)', showline=True, linecolor='#2E7D32')
    fig.update_yaxes(gridcolor='rgba(46,125,50,0.2)', showline=True, linecolor='#2E7D32')
    
    pio.write_image(fig, '气泡图_style_5.png')
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
