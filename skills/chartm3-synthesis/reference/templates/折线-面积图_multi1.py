import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def preprocess(data=None):
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate dates for one year
    dates = pd.date_range(start='2023-01-01', periods=12, freq='M')
    
    # Generate page views with seasonal pattern
    base_views = np.linspace(20000, 40000, 12)
    seasonal = 5000 * np.sin(np.linspace(0, 2*np.pi, 12))
    page_views = (base_views + seasonal + np.random.normal(0, 1000, 12)).astype(int)
    
    # Generate conversion rates
    conversion_rate = (4 + 2 * np.sin(np.linspace(0, 2*np.pi, 12)) + 
                      np.random.normal(0, 0.3, 12)).round(2)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Page_Views': page_views,
        'Conversion_Rate': conversion_rate
    })
    
    # Save to CSV
    df.to_csv('折线-面积图.csv', index=False)
    return df

def plot(data):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add area trace for page views
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Page_Views'],
            name="Page Views",
            fill='tozeroy',
            fillcolor='rgba(135, 206, 250, 0.3)',
            line=dict(color='rgb(135, 206, 250)', width=1),
            mode='lines'
        ),
        secondary_y=False
    )
    
    # Add line trace for conversion rate
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Conversion_Rate'],
            name="Conversion Rate (%)",
            line=dict(color='rgb(70, 130, 180)', width=2),
            mode='lines+markers'
        ),
        secondary_y=True
    )
    
    # Update layout
    fig.update_layout(
        title="Monthly Website Performance Metrics",
        title_x=0.5,
        plot_bgcolor='white',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        )
    )

    # Update axes
    fig.update_xaxes(
        title_text="Date",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        zeroline=False
    )
    
    fig.update_yaxes(
        title_text="Page Views",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        zeroline=False,
        secondary_y=False
    )
    
    fig.update_yaxes(
        title_text="Conversion Rate (%)",
        showgrid=False,
        zeroline=False,
        secondary_y=True
    )

    # Save figure
    fig.write_image("折线-面积图.png", width=1200, height=800)
    return fig

# Generate and plot data

def plot_1(data):
    # 现代简约风格
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Page_Views'],
            name="Page Views",
            fill='tozeroy',
            fillcolor='rgba(241, 243, 244, 0.6)',
            line=dict(color='#34495e', width=1),
            mode='lines'
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Conversion_Rate'],
            name="Conversion Rate (%)",
            line=dict(color='#e74c3c', width=2),
            mode='lines+markers',
            marker=dict(size=8, symbol='circle')
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title=dict(
            text="Monthly Performance Metrics",
            font=dict(size=24, color='#2c3e50', family='Arial, sans-serif'),
            x=0.5,
            y=0.95
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(255, 255, 255, 0.8)'
        )
    )

    fig.update_xaxes(
        title_text="Date",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(189,189,189,0.2)',
        zeroline=False
    )
    
    fig.update_yaxes(
        title_text="Page Views",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(189,189,189,0.2)',
        zeroline=False,
        secondary_y=False
    )
    
    fig.update_yaxes(
        title_text="Conversion Rate (%)",
        showgrid=False,
        zeroline=False,
        secondary_y=True
    )

    fig.write_image("折线-面积图_style_1.png", width=1200, height=800)
    return fig

def plot_2(data):
    # 深色科技风格
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Page_Views'],
            name="Page Views",
            fill='tozeroy',
            fillcolor='rgba(0, 255, 255, 0.1)',
            line=dict(color='cyan', width=1.5),
            mode='lines'
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Conversion_Rate'],
            name="Conversion Rate (%)",
            line=dict(color='#00ff00', width=2),
            mode='lines+markers',
            marker=dict(size=8, symbol='diamond')
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title=dict(
            text="Performance Analytics Dashboard",
            font=dict(size=24, color='#ffffff', family='Arial Black'),
            x=0.5,
            y=0.95
        ),
        plot_bgcolor='rgb(17,17,17)',
        paper_bgcolor='rgb(17,17,17)',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            font=dict(color='#ffffff'),
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(0,0,0,0.5)'
        )
    )

    fig.update_xaxes(
        title_text="Date",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(255,255,255,0.1)',
        zeroline=False,
        color='#ffffff'
    )
    
    fig.update_yaxes(
        title_text="Page Views",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(255,255,255,0.1)',
        zeroline=False,
        secondary_y=False,
        color='#ffffff'
    )
    
    fig.update_yaxes(
        title_text="Conversion Rate (%)",
        showgrid=False,
        zeroline=False,
        secondary_y=True,
        color='#ffffff'
    )

    fig.write_image("折线-面积图_style_2.png", width=1200, height=800)
    return fig

def plot_3(data):
    # 柔和渐变风格
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Page_Views'],
            name="Page Views",
            fill='tozeroy',
            fillcolor='rgba(255, 182, 193, 0.3)',
            line=dict(color='#ff69b4', width=1),
            mode='lines'
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Conversion_Rate'],
            name="Conversion Rate (%)",
            line=dict(color='#9370db', width=2.5),
            mode='lines+markers',
            marker=dict(size=10, symbol='star')
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title=dict(
            text="Website Performance Overview",
            font=dict(size=24, color='#696969', family='Verdana'),
            x=0.5,
            y=0.95
        ),
        plot_bgcolor='rgba(255,255,255,0.9)',
        paper_bgcolor='white',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(255,255,255,0.8)'
        )
    )

    fig.update_xaxes(
        title_text="Date",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(233,233,233,0.6)',
        zeroline=False
    )
    
    fig.update_yaxes(
        title_text="Page Views",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(233,233,233,0.6)',
        zeroline=False,
        secondary_y=False
    )
    
    fig.update_yaxes(
        title_text="Conversion Rate (%)",
        showgrid=False,
        zeroline=False,
        secondary_y=True
    )

    fig.write_image("折线-面积图_style_3.png", width=1200, height=800)
    return fig

def plot_4(data):
    # 商务专业风格
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Page_Views'],
            name="Page Views",
            fill='tozeroy',
            fillcolor='rgba(47, 85, 151, 0.2)',
            line=dict(color='rgb(47, 85, 151)', width=1),
            mode='lines'
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Conversion_Rate'],
            name="Conversion Rate (%)",
            line=dict(color='rgb(192, 80, 77)', width=2),
            mode='lines+markers',
            marker=dict(size=8, symbol='square')
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title=dict(
            text="Business Performance Analysis",
            font=dict(size=24, color='#333333', family='Arial'),
            x=0.5,
            y=0.95
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(255, 255, 255, 0.8)'
        )
    )

    fig.update_xaxes(
        title_text="Date",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(204,204,204,0.3)',
        zeroline=False
    )
    
    fig.update_yaxes(
        title_text="Page Views",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(204,204,204,0.3)',
        zeroline=False,
        secondary_y=False
    )
    
    fig.update_yaxes(
        title_text="Conversion Rate (%)",
        showgrid=False,
        zeroline=False,
        secondary_y=True
    )

    fig.write_image("折线-面积图_style_4.png", width=1200, height=800)
    return fig

def plot_5(data):
    # 活泼明亮风格
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Page_Views'],
            name="Page Views",
            fill='tozeroy',
            fillcolor='rgba(255, 195, 0, 0.3)',
            line=dict(color='#ffc300', width=2),
            mode='lines'
        ),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(
            x=data['Date'],
            y=data['Conversion_Rate'],
            name="Conversion Rate (%)",
            line=dict(color='#ff006e', width=3),
            mode='lines+markers',
            marker=dict(size=12, symbol='circle-open')
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title=dict(
            text="✨ Interactive Performance Report ✨",
            font=dict(size=24, color='#3a86ff', family='Trebuchet MS'),
            x=0.5,
            y=0.95
        ),
        plot_bgcolor='rgba(255,255,255,0.9)',
        paper_bgcolor='white',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            bgcolor='rgba(255,255,255,0.8)'
        )
    )

    fig.update_xaxes(
        title_text="Date",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(158,158,158,0.2)',
        zeroline=False
    )
    
    fig.update_yaxes(
        title_text="Page Views",
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(158,158,158,0.2)',
        zeroline=False,
        secondary_y=False
    )
    
    fig.update_yaxes(
        title_text="Conversion Rate (%)",
        showgrid=False,
        zeroline=False,
        secondary_y=True
    )

    fig.write_image("折线-面积图_style_5.png", width=1200, height=800)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
