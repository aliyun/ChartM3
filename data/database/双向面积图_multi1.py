import pandas as pd
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    """Generate and preprocess data for bilateral area chart"""
    # Generate sample monthly financial data if none provided
    if data is None:
        months = pd.date_range('2023-01-01', '2023-12-01', freq='M')
        np.random.seed(42)
        
        income = np.random.normal(5000, 500, len(months))
        expenses = np.random.normal(-4000, 600, len(months))
        
        data = pd.DataFrame({
            'Month': months,
            'Income': np.round(income, -1),  # Round to nearest 10
            'Expenses': np.round(expenses, -1)
        })
    
    # Save to CSV
    data.to_csv('双向面积图.csv', index=False)
    return data

def plot(data):
    """Create bilateral area chart"""
    fig = go.Figure()
    
    # Add income area (positive values)
    fig.add_trace(go.Scatter(
        x=data['Month'],
        y=data['Income'],
        fill='tonexty',
        name='Income',
        fillcolor='rgba(0, 123, 255, 0.3)',
        line=dict(color='rgb(0, 123, 255)', width=2)
    ))
    
    # Add expenses area (negative values)
    fig.add_trace(go.Scatter(
        x=data['Month'],
        y=data['Expenses'],
        fill='tonexty',
        name='Expenses',
        fillcolor='rgba(255, 99, 71, 0.3)',
        line=dict(color='rgb(255, 99, 71)', width=2)
    ))
    
    # Update layout
    fig.update_layout(
        title=dict(
            text='Monthly Income vs Expenses',
            x=0.5,
            xanchor='center',
            font=dict(size=24)
        ),
        xaxis=dict(
            title='Month',
            gridcolor='lightgrey',
            showgrid=True
        ),
        yaxis=dict(
            title='Amount ($)',
            gridcolor='lightgrey',
            showgrid=True,
            zeroline=True,
            zerolinecolor='black',
            zerolinewidth=2
        ),
        showlegend=True,
        legend=dict(
            x=1.02,
            y=0.98,
            bordercolor='grey',
            borderwidth=1
        ),
        hovermode='x unified',
        plot_bgcolor='white'
    )
    
    # Save figure (continued)
    fig.write_image("双向面积图.png", width=1200, height=800)
    return fig

# Example usage

def plot_1(data):
    """Modern Business Style"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Month'],
        y=data['Income'],
        fill='tonexty',
        name='Income',
        fillcolor='rgba(41, 128, 185, 0.2)',
        line=dict(color='rgb(41, 128, 185)', width=1.5)
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Month'],
        y=data['Expenses'],
        fill='tonexty',
        name='Expenses',
        fillcolor='rgba(192, 57, 43, 0.2)',
        line=dict(color='rgb(192, 57, 43)', width=1.5)
    ))
    
    fig.update_layout(
        title=dict(
            text='Monthly Income vs Expenses',
            x=0.5,
            xanchor='center',
            font=dict(size=24, family='Arial', color='#2c3e50')
        ),
        xaxis=dict(
            title='Month',
            gridcolor='#ecf0f1',
            showgrid=True,
            tickfont=dict(family='Arial')
        ),
        yaxis=dict(
            title='Amount ($)',
            gridcolor='#ecf0f1',
            showgrid=True,
            zeroline=True,
            zerolinecolor='#2c3e50',
            zerolinewidth=1.5,
            tickfont=dict(family='Arial')
        ),
        showlegend=True,
        legend=dict(
            x=0.02,
            y=0.98,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#ecf0f1'
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Arial')
    )
    
    fig.write_image("双向面积图_style_1.png", width=1200, height=800)
    return fig

def plot_2(data):
    """Dark Theme Style"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Month'],
        y=data['Income'],
        fill='tonexty',
        name='Income',
        fillcolor='rgba(46, 204, 113, 0.3)',
        line=dict(color='rgb(46, 204, 113)', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Month'],
        y=data['Expenses'],
        fill='tonexty',
        name='Expenses',
        fillcolor='rgba(231, 76, 60, 0.3)',
        line=dict(color='rgb(231, 76, 60)', width=2)
    ))
    
    fig.update_layout(
        title=dict(
            text='Monthly Income vs Expenses',
            x=0.5,
            xanchor='center',
            font=dict(size=24, color='#ecf0f1')
        ),
        xaxis=dict(
            title='Month',
            gridcolor='rgba(236, 240, 241, 0.1)',
            showgrid=True,
            tickfont=dict(color='#ecf0f1')
        ),
        yaxis=dict(
            title='Amount ($)',
            gridcolor='rgba(236, 240, 241, 0.1)',
            showgrid=True,
            zeroline=True,
            zerolinecolor='#ecf0f1',
            zerolinewidth=1,
            tickfont=dict(color='#ecf0f1')
        ),
        showlegend=True,
        legend=dict(
            x=0.02,
            y=0.98,
            font=dict(color='#ecf0f1'),
            bgcolor='rgba(0,0,0,0)'
        ),
        plot_bgcolor='rgb(22, 27, 34)',
        paper_bgcolor='rgb(22, 27, 34)',
        font=dict(color='#ecf0f1')
    )
    
    fig.write_image("双向面积图_style_2.png", width=1200, height=800)
    return fig

def plot_3(data):
    """Minimalist Style"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Month'],
        y=data['Income'],
        fill='tonexty',
        name='Income',
        fillcolor='rgba(189, 195, 199, 0.4)',
        line=dict(color='rgb(127, 140, 141)', width=1)
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Month'],
        y=data['Expenses'],
        fill='tonexty',
        name='Expenses',
        fillcolor='rgba(189, 195, 199, 0.2)',
        line=dict(color='rgb(127, 140, 141)', width=1)
    ))
    
    fig.update_layout(
        title=dict(
            text='Monthly Income vs Expenses',
            x=0.5,
            xanchor='center',
            font=dict(size=20, family='Helvetica Neue', color='#2c3e50')
        ),
        xaxis=dict(
            title='Month',
            gridcolor='#f8f9fa',
            showgrid=True
        ),
        yaxis=dict(
            title='Amount ($)',
            gridcolor='#f8f9fa',
            showgrid=True,
            zeroline=True,
            zerolinecolor='#2c3e50',
            zerolinewidth=0.5
        ),
        showlegend=True,
        legend=dict(
            x=0.02,
            y=0.98,
            bgcolor='rgba(0,0,0,0)'
        ),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    fig.write_image("双向面积图_style_3.png", width=1200, height=800)
    return fig

def plot_4(data):
    """Gradient Style"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Month'],
        y=data['Income'],
        fill='tonexty',
        name='Income',
        fillcolor='rgba(52, 152, 219, 0.4)',
        line=dict(
            color='rgb(41, 128, 185)',
            width=2,
            shape='spline'
        )
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Month'],
        y=data['Expenses'],
        fill='tonexty',
        name='Expenses',
        fillcolor='rgba(231, 76, 60, 0.4)',
        line=dict(
            color='rgb(192, 57, 43)',
            width=2,
            shape='spline'
        )
    ))
    
    fig.update_layout(
        title=dict(
            text='Monthly Income vs Expenses',
            x=0.5,
            xanchor='center',
            font=dict(size=24, family='Roboto')
        ),
        xaxis=dict(
            title='Month',
            gridcolor='rgba(189, 195, 199, 0.4)',
            showgrid=True
        ),
        yaxis=dict(
            title='Amount ($)',
            gridcolor='rgba(189, 195, 199, 0.4)',
            showgrid=True,
            zeroline=True,
            zerolinecolor='#7f8c8d',
            zerolinewidth=1.5
        ),
        showlegend=True,
        legend=dict(
            x=1.02,
            y=0.98,
            bgcolor='rgba(255,255,255,0.8)'
        ),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    fig.write_image("双向面积图_style_4.png", width=1200, height=800)
    return fig

def plot_5(data):
    """Pastel Style"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Month'],
        y=data['Income'],
        fill='tonexty',
        name='Income',
        fillcolor='rgba(172, 220, 238, 0.6)',
        line=dict(
            color='rgb(125, 206, 235)',
            width=1.5,
            shape='spline'
        )
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Month'],
        y=data['Expenses'],
        fill='tonexty',
        name='Expenses',
        fillcolor='rgba(255, 182, 193, 0.6)',
        line=dict(
            color='rgb(255, 160, 174)',
            width=1.5,
            shape='spline'
        )
    ))
    
    fig.update_layout(
        title=dict(
            text='Monthly Income vs Expenses',
            x=0.5,
            xanchor='center',
            font=dict(size=24, family='Comic Sans MS', color='#6c757d')
        ),
        xaxis=dict(
            title='Month',
            gridcolor='rgba(233, 236, 239, 0.8)',
            showgrid=True
        ),
        yaxis=dict(
            title='Amount ($)',
            gridcolor='rgba(233, 236, 239, 0.8)',
            showgrid=True,
            zeroline=True,
            zerolinecolor='#adb5bd',
            zerolinewidth=1
        ),
        showlegend=True,
        legend=dict(
            x=0.02,
            y=0.98,
            bgcolor='rgba(255,255,255,0.8)',
            bordercolor='#f8f9fa'
        ),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    fig.write_image("双向面积图_style_5.png", width=1200, height=800)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
