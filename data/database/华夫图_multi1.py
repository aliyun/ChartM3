import pandas as pd
import numpy as np
from pywaffle import Waffle
import matplotlib.pyplot as plt

def preprocess(data=None):
    """
    Generate or process data for waffle chart
    Returns a DataFrame with activities and their percentages
    """
    # Generate sample data if none provided
    if data is None:
        data = {
            'Activity': ['Work', 'Sleep', 'Leisure', 'Chores', 'Exercise'],
            'Percentage': [40, 30, 15, 10, 5]
        }
        df = pd.DataFrame(data)
    else:
        df = data
    
    # Validate percentages sum to 100
    assert np.isclose(df['Percentage'].sum(), 100), "Percentages must sum to 100"
    
    # Save to CSV
    df.to_csv('华夫图.csv', index=False)
    return df

def plot(data):
    """
    Create a waffle chart from the provided data
    """
    # Convert data to lists
    values = data['Percentage'].tolist()
    labels = data['Activity'].tolist()
    
    # Define colors
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD']
    
    # Create figure
    plt.figure(
        FigureClass=Waffle,
        rows=10,
        values=values,
        colors=colors[:len(values)],
        labels=labels,
        figsize=(10, 6),
        title={
            'label': 'Daily Time Distribution',
            'loc': 'center',
            'pad': 20
        },
        legend={
            'loc': 'lower center',
            'bbox_to_anchor': (0.5, -0.2),
            'ncol': len(labels),
            'framealpha': 0
        },
        block_aspect_ratio=0.75,
        interval_ratio_x=0.2,
        interval_ratio_y=0.2
    )
    
    # Save plot
    plt.savefig('华夫图.png', bbox_inches='tight', dpi=300, pad_inches=0.5)
    plt.close()


def plot_1(data):
    """
    商务专业风格：蓝灰色调
    """
    values = data['Percentage'].tolist()
    labels = data['Activity'].tolist()
    
    colors = ['#2C3E50', '#34495E', '#5D6D7E', '#85929E', '#ABB2B9']
    
    plt.figure(
        FigureClass=Waffle,
        rows=10,
        values=values,
        colors=colors[:len(values)],
        labels=labels,
        figsize=(12, 7),
        title={
            'label': 'Daily Time Distribution',
            'loc': 'left',
            'pad': 20
        },
        legend={
            'loc': 'center right',
            'bbox_to_anchor': (1.2, 0.5),
            'framealpha': 0
        },
        block_aspect_ratio=0.9,
        interval_ratio_x=0.1,
        interval_ratio_y=0.1
    )
    
    plt.savefig('华夫图_style_1.png', bbox_inches='tight', dpi=300, pad_inches=0.5)
    plt.close()

def plot_2(data):
    """
    活泼创意风格：彩虹色系
    """
    values = data['Percentage'].tolist()
    labels = data['Activity'].tolist()
    
    colors = ['#FF6B6B', '#4ECDC4', '#FFE66D', '#6C5B7B', '#FF8B94']
    
    plt.figure(
        FigureClass=Waffle,
        rows=8,
        values=values,
        colors=colors[:len(values)],
        labels=labels,
        figsize=(10, 8),
        title={
            'label': 'Fun Daily Activities',
            'loc': 'center',
            'pad': 15
        },
        legend={
            'loc': 'lower center',
            'bbox_to_anchor': (0.5, -0.15),
            'ncol': len(labels),
            'framealpha': 0
        },
        block_aspect_ratio=0.6,
        interval_ratio_x=0.3,
        interval_ratio_y=0.3
    )
    
    plt.savefig('华夫图_style_2.png', bbox_inches='tight', dpi=300, pad_inches=0.5)
    plt.close()

def plot_3(data):
    """
    自然环保风格：绿色系
    """
    values = data['Percentage'].tolist()
    labels = data['Activity'].tolist()
    
    colors = ['#8BC34A', '#4CAF50', '#009688', '#66BB6A', '#81C784']
    
    plt.figure(
        FigureClass=Waffle,
        rows=12,
        values=values,
        colors=colors[:len(values)],
        labels=labels,
        figsize=(11, 6),
        title={
            'label': 'Eco-friendly Time Analysis',
            'loc': 'center',
            'pad': 25
        },
        legend={
            'loc': 'center left',
            'bbox_to_anchor': (-0.2, 0.5),
            'framealpha': 0
        },
        block_aspect_ratio=0.8,
        interval_ratio_x=0.15,
        interval_ratio_y=0.15
    )
    
    plt.savefig('华夫图_style_3.png', bbox_inches='tight', dpi=300, pad_inches=0.5)
    plt.close()

def plot_4(data):
    """
    现代简约风格：黑白灰+强调色
    """
    values = data['Percentage'].tolist()
    labels = data['Activity'].tolist()
    
    colors = ['#212121', '#FF5252', '#424242', '#616161', '#9E9E9E']
    
    plt.figure(
        FigureClass=Waffle,
        rows=15,
        values=values,
        colors=colors[:len(values)],
        labels=labels,
        figsize=(9, 7),
        title={
            'label': 'Time Distribution',
            'loc': 'left',
            'pad': 10
        },
        legend={
            'loc': 'upper right',
            'framealpha': 0
        },
        block_aspect_ratio=1,
        interval_ratio_x=0.05,
        interval_ratio_y=0.05
    )
    
    plt.savefig('华夫图_style_4.png', bbox_inches='tight', dpi=300, pad_inches=0.5)
    plt.close()

def plot_5(data):
    """
    渐变主题风格：蓝色渐变
    """
    values = data['Percentage'].tolist()
    labels = data['Activity'].tolist()
    
    colors = ['#01579B', '#0277BD', '#0288D1', '#039BE5', '#03A9F4']
    
    plt.figure(
        FigureClass=Waffle,
        rows=10,
        values=values,
        colors=colors[:len(values)],
        labels=labels,
        figsize=(12, 6),
        title={
            'label': 'Daily Activities Overview',
            'loc': 'center',
            'pad': 20
        },
        legend={
            'loc': 'center',
            'bbox_to_anchor': (0.5, -0.2),
            'ncol': len(labels),
            'framealpha': 0.7
        },
        block_aspect_ratio=0.7,
        interval_ratio_x=0.2,
        interval_ratio_y=0.2
    )
    
    plt.savefig('华夫图_style_5.png', bbox_inches='tight', dpi=300, pad_inches=0.5)
    plt.close()

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
