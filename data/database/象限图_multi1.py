import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def preprocess(data=None):
    # Generate sample data if none provided
    if data is None:
        companies = [
            "TechCorp", "DataSys", "CloudNet", "AIWorks", 
            "RoboTech", "SmartSol", "InfoTech", "WebPro",
            "DevCorp", "NetSys", "AppWorks", "SoftTech"
        ]
        
        np.random.seed(42)
        data = pd.DataFrame({
            'company': companies,
            'market_growth': np.random.uniform(-10, 30, len(companies)),
            'profit_margin': np.random.uniform(-5, 25, len(companies)),
            'revenue': np.random.uniform(50, 500, len(companies))
        })
    
    # Calculate quadrants
    data['quadrant'] = data.apply(lambda row: 
        'Stars' if row['market_growth'] > 10 and row['profit_margin'] > 10 else
        'Cash Cows' if row['market_growth'] <= 10 and row['profit_margin'] > 10 else
        'Dogs' if row['market_growth'] <= 10 and row['profit_margin'] <= 10 else
        'Question Marks', axis=1
    )
    
    # Save to CSV
    data.to_csv('象限图.csv', index=False)
    return data

def plot(data):
    # Create quadrant plot
    fig = go.Figure()
    
    # Add scatter plots for each quadrant with different colors
    colors = {'Stars': '#2ecc71', 'Cash Cows': '#3498db', 
             'Dogs': '#e74c3c', 'Question Marks': '#f1c40f'}
    
    for quadrant in colors.keys():
        mask = data['quadrant'] == quadrant
        
        fig.add_trace(go.Scatter(
            x=data[mask]['market_growth'],
            y=data[mask]['profit_margin'],
            mode='markers+text',
            name=quadrant,
            text=data[mask]['company'],
            textposition="top center",
            marker=dict(
                size=data[mask]['revenue']/10,
                color=colors[quadrant],
                line=dict(width=2, color='white')
            ),
                        hovertemplate=
            "<b>%{text}</b><br>" +
            "Market Growth: %{x:.1f}%<br>" +
            "Profit Margin: %{y:.1f}%<br>" +
            "Revenue: $%{marker.size:.0f}M<br>" +
            "Quadrant: " + quadrant +
            "<extra></extra>"
        ))
    
    # Add quadrant lines
    fig.add_hline(y=10, line_dash="dash", line_color="gray")
    fig.add_vline(x=10, line_dash="dash", line_color="gray")
    
    # Add quadrant labels
    fig.add_annotation(x=20, y=20, text="Stars",
                      showarrow=False, font=dict(size=16, color="darkgray"))
    fig.add_annotation(x=0, y=20, text="Cash Cows",
                      showarrow=False, font=dict(size=16, color="darkgray"))
    fig.add_annotation(x=0, y=0, text="Dogs",
                      showarrow=False, font=dict(size=16, color="darkgray"))
    fig.add_annotation(x=20, y=0, text="Question Marks",
                      showarrow=False, font=dict(size=16, color="darkgray"))
    
    # Update layout
    fig.update_layout(
        title=dict(
            text='Company Performance Analysis',
            x=0.5,
            y=0.95,
            font=dict(size=24)
        ),
        xaxis=dict(
            title='Market Growth (%)',
            zeroline=False,
            range=[-15, 35]
        ),
        yaxis=dict(
            title='Profit Margin (%)',
            zeroline=False,
            range=[-10, 30]
        ),
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        plot_bgcolor='white',
        width=1000,
        height=800
    )
    
    # Add grid
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    fig.write_image('象限图.png')
    
    return fig

# Generate and plot data
data = preprocess()
fig = plot(data)

def plot_1(data):
    # 现代简约风格 - 黑白主题
    fig = go.Figure()
    
    colors = {'Stars': '#000000', 'Cash Cows': '#333333', 
              'Dogs': '#666666', 'Question Marks': '#999999'}
    
    for quadrant in colors.keys():
        mask = data['quadrant'] == quadrant
        fig.add_trace(go.Scatter(
            x=data[mask]['market_growth'],
            y=data[mask]['profit_margin'],
            mode='markers+text',
            name=quadrant,
            text=data[mask]['company'],
            textposition="top center",
            marker=dict(
                symbol='square',
                size=data[mask]['revenue']/10,
                color=colors[quadrant],
                line=dict(width=1, color='white')
            ),
            hovertemplate="<b>%{text}</b><br>" +
                         "Market Growth: %{x:.1f}%<br>" +
                         "Profit Margin: %{y:.1f}%<br>" +
                         "Revenue: $%{marker.size:.0f}M<br>" +
                         "Quadrant: " + quadrant +
                         "<extra></extra>"
        ))
    
    fig.add_hline(y=10, line_dash="solid", line_color="black", line_width=0.5)
    fig.add_vline(x=10, line_dash="solid", line_color="black", line_width=0.5)
    
    fig.update_layout(
        title=dict(
            text='Company Performance Matrix',
            x=0.5,
            y=0.95,
            font=dict(size=24, family='Arial Black')
        ),
        xaxis=dict(
            title='Market Growth (%)',
            zeroline=False,
            range=[-15, 35],
            showgrid=False
        ),
        yaxis=dict(
            title='Profit Margin (%)',
            zeroline=False,
            range=[-10, 30],
            showgrid=False
        ),
        showlegend=True,
        legend=dict(
            yanchor="bottom",
            y=0.01,
            xanchor="right",
            x=0.99
        ),
        plot_bgcolor='white',
        width=1000,
        height=800
    )
    
    fig.write_image('象限图_style_1.png')
    return fig

def plot_2(data):
    # 科技感风格 - 深色背景+霓虹效果
    fig = go.Figure()
    
    colors = {'Stars': '#00ff00', 'Cash Cows': '#00ffff', 
              'Dogs': '#ff00ff', 'Question Marks': '#ffff00'}
    
    for quadrant in colors.keys():
        mask = data['quadrant'] == quadrant
        fig.add_trace(go.Scatter(
            x=data[mask]['market_growth'],
            y=data[mask]['profit_margin'],
            mode='markers+text',
            name=quadrant,
            text=data[mask]['company'],
            textposition="top center",
            marker=dict(
                symbol='diamond',
                size=data[mask]['revenue']/10,
                color=colors[quadrant],
                line=dict(width=2, color='white')
            ),
            hovertemplate="<b>%{text}</b><br>" +
                         "Market Growth: %{x:.1f}%<br>" +
                         "Profit Margin: %{y:.1f}%<br>" +
                         "Revenue: $%{marker.size:.0f}M<br>" +
                         "Quadrant: " + quadrant +
                         "<extra></extra>"
        ))
    
    fig.add_hline(y=10, line_dash="solid", line_color="rgba(255,255,255,0.3)")
    fig.add_vline(x=10, line_dash="solid", line_color="rgba(255,255,255,0.3)")
    
    fig.update_layout(
        title=dict(
            text='Tech Performance Matrix',
            x=0.5,
            y=0.95,
            font=dict(size=24, family='Courier New', color='white')
        ),
        xaxis=dict(
            title='Market Growth (%)',
            zeroline=False,
            range=[-15, 35],
            gridcolor='rgba(255,255,255,0.1)',
            color='white'
        ),
        yaxis=dict(
            title='Profit Margin (%)',
            zeroline=False,
            range=[-10, 30],
            gridcolor='rgba(255,255,255,0.1)',
            color='white'
        ),
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
            font=dict(color='white')
        ),
        plot_bgcolor='rgb(17,17,17)',
        paper_bgcolor='rgb(17,17,17)',
        width=1000,
        height=800
    )
    
    fig.write_image('象限图_style_2.png')
    return fig

def plot_3(data):
    # 环保自然风格 - 柔和绿色系
    fig = go.Figure()
    
    colors = {'Stars': '#2ecc71', 'Cash Cows': '#27ae60', 
              'Dogs': '#1abc9c', 'Question Marks': '#16a085'}
    
    for quadrant in colors.keys():
        mask = data['quadrant'] == quadrant
        fig.add_trace(go.Scatter(
            x=data[mask]['market_growth'],
            y=data[mask]['profit_margin'],
            mode='markers+text',
            name=quadrant,
            text=data[mask]['company'],
            textposition="top center",
            marker=dict(
                symbol='circle',
                size=data[mask]['revenue']/10,
                color=colors[quadrant],
                line=dict(width=1, color='white'),
                opacity=0.7
            ),
            hovertemplate="<b>%{text}</b><br>" +
                         "Market Growth: %{x:.1f}%<br>" +
                         "Profit Margin: %{y:.1f}%<br>" +
                         "Revenue: $%{marker.size:.0f}M<br>" +
                         "Quadrant: " + quadrant +
                         "<extra></extra>"
        ))
    
    fig.add_hline(y=10, line_dash="dot", line_color="#27ae60", line_width=1)
    fig.add_vline(x=10, line_dash="dot", line_color="#27ae60", line_width=1)
    
    fig.update_layout(
        title=dict(
            text='Sustainable Growth Matrix',
            x=0.5,
            y=0.95,
            font=dict(size=24, family='Verdana', color='#2c3e50')
        ),
        xaxis=dict(
            title='Market Growth (%)',
            zeroline=False,
            range=[-15, 35],
            gridcolor='rgba(46,204,113,0.2)'
        ),
        yaxis=dict(
            title='Profit Margin (%)',
            zeroline=False,
            range=[-10, 30],
            gridcolor='rgba(46,204,113,0.2)'
        ),
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        plot_bgcolor='rgba(46,204,113,0.05)',
        width=1000,
        height=800
    )
    
    fig.write_image('象限图_style_3.png')
    return fig

def plot_4(data):
    # 典雅商务风格 - 深蓝色系
    fig = go.Figure()
    
    colors = {'Stars': '#1f77b4', 'Cash Cows': '#17589f', 
              'Dogs': '#0f3b7a', 'Question Marks': '#082654'}
    
    for quadrant in colors.keys():
        mask = data['quadrant'] == quadrant
        fig.add_trace(go.Scatter(
            x=data[mask]['market_growth'],
            y=data[mask]['profit_margin'],
            mode='markers+text',
            name=quadrant,
            text=data[mask]['company'],
            textposition="top center",
            marker=dict(
                symbol='circle',
                size=data[mask]['revenue']/10,
                color=colors[quadrant],
                line=dict(width=2, color='white'),
                opacity=0.9
            ),
            hovertemplate="<b>%{text}</b><br>" +
                         "Market Growth: %{x:.1f}%<br>" +
                         "Profit Margin: %{y:.1f}%<br>" +
                         "Revenue: $%{marker.size:.0f}M<br>" +
                         "Quadrant: " + quadrant +
                         "<extra></extra>"
        ))
    
    fig.add_hline(y=10, line_dash="dashdot", line_color="#1f77b4")
    fig.add_vline(x=10, line_dash="dashdot", line_color="#1f77b4")
    
    fig.update_layout(
        title=dict(
            text='Enterprise Performance Analysis',
            x=0.5,
            y=0.95,
            font=dict(size=24, family='Times New Roman', color='#1f77b4')
        ),
        xaxis=dict(
            title='Market Growth (%)',
            zeroline=False,
            range=[-15, 35],
            gridcolor='rgba(31,119,180,0.1)'
        ),
        yaxis=dict(
            title='Profit Margin (%)',
            zeroline=False,
            range=[-10, 30],
            gridcolor='rgba(31,119,180,0.1)'
        ),
        showlegend=True,
        legend=dict(
            yanchor="bottom",
            y=0.01,
            xanchor="left",
            x=0.01
        ),
        plot_bgcolor='white',
        width=1000,
        height=800
    )
    
    fig.write_image('象限图_style_4.png')
    return fig

def plot_5(data):
    # 活泼清新风格 - 彩虹色系
    fig = go.Figure()
    
    colors = {'Stars': '#FF9999', 'Cash Cows': '#99FF99', 
              'Dogs': '#9999FF', 'Question Marks': '#FFFF99'}
    
    for quadrant in colors.keys():
        mask = data['quadrant'] == quadrant
        fig.add_trace(go.Scatter(
            x=data[mask]['market_growth'],
            y=data[mask]['profit_margin'],
            mode='markers+text',
            name=quadrant,
            text=data[mask]['company'],
            textposition="top center",
            marker=dict(
                symbol='star',
                size=data[mask]['revenue']/10,
                color=colors[quadrant],
                line=dict(width=1.5, color='white'),
                opacity=0.8
            ),
            hovertemplate="<b>%{text}</b><br>" +
                         "Market Growth: %{x:.1f}%<br>" +
                         "Profit Margin: %{y:.1f}%<br>" +
                         "Revenue: $%{marker.size:.0f}M<br>" +
                         "Quadrant: " + quadrant +
                         "<extra></extra>"
        ))
    
    fig.add_hline(y=10, line_dash="dot", line_color="#FF9999")
    fig.add_vline(x=10, line_dash="dot", line_color="#FF9999")
    
    fig.update_layout(
        title=dict(
            text='Growth & Performance Chart',
            x=0.5,
            y=0.95,
            font=dict(size=24, family='Comic Sans MS', color='#FF6666')
        ),
        xaxis=dict(
            title='Market Growth (%)',
            zeroline=False,
            range=[-15, 35],
            gridcolor='rgba(255,153,153,0.2)'
        ),
        yaxis=dict(
            title='Profit Margin (%)',
            zeroline=False,
            range=[-10, 30],
            gridcolor='rgba(255,153,153,0.2)'
        ),
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ),
        plot_bgcolor='rgba(255,255,255,0.9)',
        width=1000,
        height=800
    )
    
    fig.write_image('象限图_style_5.png')
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
