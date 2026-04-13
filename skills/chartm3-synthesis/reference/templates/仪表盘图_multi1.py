import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

def preprocess():
    # Generate 12 months of CSAT data
    dates = [(datetime.now() - timedelta(days=x*30)).strftime('%Y-%m-%d') 
             for x in range(12)][::-1]
    
    # Generate CSAT scores around 85% with some variation
    np.random.seed(42)
    scores = 85 + np.random.normal(0, 3, 12)
    scores = np.clip(scores, 0, 100)
    
    # Create DataFrame
    df = pd.DataFrame({
        'date': dates,
        'csat_score': scores
    })
    
    # Save to CSV
    df.to_csv('仪表盘图.csv', index=False)
    return df

def plot(data):
    # Get latest CSAT score
    current_score = data['csat_score'].iloc[-1]
    
    # Create gauge chart
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = current_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Customer Satisfaction Score", 'font': {'size': 24}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "royalblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 60], 'color': 'lightgray'},
                {'range': [60, 80], 'color': 'lightblue'},
                {'range': [80, 100], 'color': 'azure'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    # Update layout
    fig.update_layout(
        paper_bgcolor = "white",
        font = {'color': "darkblue", 'family': "Arial"}
    )
    
    # Save figure
    fig.write_image("仪表盘图.png")

# Run the functions

def plot_1(data):
    # 专业商务蓝风格
    current_score = data['csat_score'].iloc[-1]
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = current_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Customer Satisfaction Score", 'font': {'size': 24, 'family': 'Arial'}},
        number = {'font': {'size': 40, 'color': '#1f77b4'}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#1f77b4"},
            'bar': {'color': "#1f77b4"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#1f77b4",
            'steps': [
                {'range': [0, 60], 'color': '#E6EFF6'},
                {'range': [60, 80], 'color': '#BDD7E7'},
                {'range': [80, 100], 'color': '#6BAED6'}
            ],
            'threshold': {
                'line': {'color': "#2C3E50", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor = "white",
        font = {'color': "#1f77b4", 'family': "Arial"}
    )
    
    fig.write_image("仪表盘图_style_1.png")

def plot_2(data):
    # 环保绿色主题
    current_score = data['csat_score'].iloc[-1]
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = current_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Customer Satisfaction Score", 'font': {'size': 24, 'family': 'Verdana'}},
        number = {'font': {'size': 40, 'color': '#2ecc71'}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#27ae60"},
            'bar': {'color': "#2ecc71"},
            'bgcolor': "#f1f8e9",
            'borderwidth': 2,
            'bordercolor': "#27ae60",
            'steps': [
                {'range': [0, 60], 'color': '#c8e6c9'},
                {'range': [60, 80], 'color': '#81c784'},
                {'range': [80, 100], 'color': '#4caf50'}
            ],
            'threshold': {
                'line': {'color': "#e74c3c", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor = "#f1f8e9",
        font = {'color': "#27ae60", 'family': "Verdana"}
    )
    
    fig.write_image("仪表盘图_style_2.png")

def plot_3(data):
    # 高对比度现代风格
    current_score = data['csat_score'].iloc[-1]
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = current_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Customer Satisfaction Score", 'font': {'size': 24, 'family': 'Helvetica'}},
        number = {'font': {'size': 40, 'color': '#000000'}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': "black"},
            'bar': {'color': "#ff4757"},
            'bgcolor': "white",
            'borderwidth': 3,
            'bordercolor': "black",
            'steps': [
                {'range': [0, 60], 'color': '#f1f2f6'},
                {'range': [60, 80], 'color': '#dfe4ea'},
                {'range': [80, 100], 'color': '#ced6e0'}
            ],
            'threshold': {
                'line': {'color': "#2f3542", 'width': 5},
                'thickness': 0.8,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor = "white",
        font = {'color': "black", 'family': "Helvetica"}
    )
    
    fig.write_image("仪表盘图_style_3.png")

def plot_4(data):
    # 温暖柔和风格
    current_score = data['csat_score'].iloc[-1]
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = current_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Customer Satisfaction Score", 'font': {'size': 24, 'family': 'Georgia'}},
        number = {'font': {'size': 40, 'color': '#e17055'}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#d35400"},
            'bar': {'color': "#e17055"},
            'bgcolor': "#ffeaa7",
            'borderwidth': 2,
            'bordercolor': "#d35400",
            'steps': [
                {'range': [0, 60], 'color': '#ffd7a8'},
                {'range': [60, 80], 'color': '#ffb088'},
                {'range': [80, 100], 'color': '#ff8c69'}
            ],
            'threshold': {
                'line': {'color': "#c0392b", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor = "#ffeaa7",
        font = {'color': "#d35400", 'family': "Georgia"}
    )
    
    fig.write_image("仪表盘图_style_4.png")

def plot_5(data):
    # 科技紫色风格
    current_score = data['csat_score'].iloc[-1]
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = current_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Customer Satisfaction Score", 'font': {'size': 24, 'family': 'Roboto'}},
        number = {'font': {'size': 40, 'color': '#9b59b6'}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': "#8e44ad"},
            'bar': {'color': "#9b59b6"},
            'bgcolor': "#000000",
            'borderwidth': 2,
            'bordercolor': "#8e44ad",
            'steps': [
                {'range': [0, 60], 'color': '#2c003e'},
                {'range': [60, 80], 'color': '#411f5d'},
                {'range': [80, 100], 'color': '#553285'}
            ],
            'threshold': {
                'line': {'color': "#e056fd", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor = "black",
        font = {'color': "#9b59b6", 'family': "Roboto"}
    )
    
    fig.write_image("仪表盘图_style_5.png")

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
