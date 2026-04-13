import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def preprocess(data=None):
    """Generate sample progress data for three metrics and save to CSV"""
    # Create sample data if none provided
    if data is None:
        data = pd.DataFrame({
            'metric': ['Sales Target', 'Customer Satisfaction', 'Team Efficiency'],
            'current_value': [82, 95, 68],
            'target_value': [100, 100, 100],
            'color': ['#FF6B6B', '#4ECDC4', '#45B7D1']  # Different colors for each metric
        })
    
    # Calculate percentage
    data['percentage'] = (data['current_value'] / data['target_value'] * 100).round(1)
    
    # Save to CSV
    data.to_csv('圆环进度图.csv', index=False)
    return data

def plot(data=None):

    def create_circle_progress(ax, percentage, color, title):
        """Helper function to create individual circular progress chart"""
        # Set chart parameters
        center = (0.5, 0.5)
        radius = 0.3
        thickness = 0.05
        
        # Calculate angles
        angle = percentage/100 * 360
        
        # Create background circle
        background = plt.Circle(center, radius, fill=False, 
                            color='#E6E6E6', linewidth=thickness*100)
        ax.add_patch(background)
        
        # Create progress arc
        progress = plt.matplotlib.patches.Arc(center, radius*2, radius*2,
                                            theta1=0, theta2=angle,
                                            color=color, linewidth=thickness*100)
        ax.add_patch(progress)
        
        # Add percentage text
        ax.text(0.5, 0.5, f"{percentage}%",
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=20,
                color='#2C3E50')
        
        # Add title
        ax.text(0.5, 0.85, title,
                horizontalalignment='center',
                fontsize=12,
                color='#2C3E50')
        
        # Set equal aspect ratio and remove axes
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Set bounds
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
    
    """Create three circular progress charts"""
    # Load data if not provided
    if data is None:
        data = pd.read_csv('圆环进度图.csv')
    
    # Create figure with three subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    plt.subplots_adjust(wspace=0.3)
    
    # Create each progress chart
    for ax, (_, row) in zip([ax1, ax2, ax3], data.iterrows()):
        create_circle_progress(
            ax=ax,
            percentage=row['percentage'],
            color=row['color'],
            title=row['metric']
        )
    
    # Add overall title
    plt.suptitle('Key Performance Indicators', fontsize=14, y=1.05)
    
    # Save plot
    plt.savefig('圆环进度图.png', bbox_inches='tight', dpi=300)
    plt.close()

def plot_1(data=None):
    """商务简约风格 - 蓝色渐变"""
    if data is None:
        data = pd.read_csv('圆环进度图.csv')
    
    def create_circle_progress(ax, percentage, base_color, title):
        center = (0.5, 0.5)
        radius = 0.35
        thickness = 0.08
        
        angle = percentage/100 * 360
        
        background = plt.Circle(center, radius, fill=False, 
                            color='#F5F5F5', linewidth=thickness*100)
        ax.add_patch(background)
        
        progress = plt.matplotlib.patches.Arc(center, radius*2, radius*2,
                                            theta1=0, theta2=angle,
                                            color=base_color, linewidth=thickness*100)
        ax.add_patch(progress)
        
        ax.text(0.5, 0.5, f"{percentage}%",
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=24,
                weight='bold',
                color='#2C3E50')
        
        ax.text(0.5, 0.8, title,
                horizontalalignment='center',
                fontsize=14,
                color='#2C3E50')
        
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    plt.subplots_adjust(wspace=0.3)
    
    colors = ['#1f77b4', '#2ecc71', '#3498db']
    
    for ax, (_, row), color in zip([ax1, ax2, ax3], data.iterrows(), colors):
        create_circle_progress(ax, row['percentage'], color, row['metric'])
    
    plt.suptitle('Performance Metrics', fontsize=16, y=1.05)
    plt.savefig('圆环进度图_style_1.png', bbox_inches='tight', dpi=300, facecolor='white')
    plt.close()

def plot_2(data=None):
    """科技感风格"""
    if data is None:
        data = pd.read_csv('圆环进度图.csv')
    
    def create_circle_progress(ax, percentage, color, title):
        center = (0.5, 0.5)
        radius = 0.35
        thickness = 0.06
        
        angle = percentage/100 * 360
        
        background = plt.Circle(center, radius, fill=False, 
                            color='#2C3E50', linewidth=thickness*100)
        ax.add_patch(background)
        
        progress = plt.matplotlib.patches.Arc(center, radius*2, radius*2,
                                            theta1=0, theta2=angle,
                                            color=color, linewidth=thickness*100)
        ax.add_patch(progress)
        
        ax.text(0.5, 0.5, f"{percentage}%",
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=24,
                weight='bold',
                color=color)
        
        ax.text(0.5, 0.8, title,
                horizontalalignment='center',
                fontsize=14,
                color='white')
        
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_facecolor('#1a1a1a')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5), facecolor='#1a1a1a')
    plt.subplots_adjust(wspace=0.3)
    
    colors = ['#00ff00', '#00ffff', '#ff00ff']
    
    for ax, (_, row), color in zip([ax1, ax2, ax3], data.iterrows(), colors):
        create_circle_progress(ax, row['percentage'], color, row['metric'])
    
    plt.suptitle('System Performance', fontsize=16, y=1.05, color='white')
    plt.savefig('圆环进度图_style_2.png', bbox_inches='tight', dpi=300, facecolor='#1a1a1a')
    plt.close()

def plot_3(data=None):
    """清新活泼风格"""
    if data is None:
        data = pd.read_csv('圆环进度图.csv')
    
    def create_circle_progress(ax, percentage, color, title):
        center = (0.5, 0.5)
        radius = 0.35
        thickness = 0.1
        
        angle = percentage/100 * 360
        
        background = plt.Circle(center, radius, fill=False, 
                            color='#f0f0f0', linewidth=thickness*100)
        ax.add_patch(background)
        
        progress = plt.matplotlib.patches.Arc(center, radius*2, radius*2,
                                            theta1=0, theta2=angle,
                                            color=color, linewidth=thickness*100)
        ax.add_patch(progress)
        
        ax.text(0.5, 0.5, f"{percentage}%",
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=22,
                color='#555555')
        
        ax.text(0.5, 0.85, title,
                horizontalalignment='center',
                fontsize=13,
                color='#333333')
        
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    plt.subplots_adjust(wspace=0.3)
    
    colors = ['#FF9999', '#66CC99', '#99CCFF']
    
    for ax, (_, row), color in zip([ax1, ax2, ax3], data.iterrows(), colors):
        create_circle_progress(ax, row['percentage'], color, row['metric'])
    
    plt.suptitle('Progress Overview', fontsize=16, y=1.05)
    plt.savefig('圆环进度图_style_3.png', bbox_inches='tight', dpi=300, facecolor='white')
    plt.close()

def plot_4(data=None):
    """现代轻奢风格"""
    if data is None:
        data = pd.read_csv('圆环进度图.csv')
    
    def create_circle_progress(ax, percentage, color, title):
        center = (0.5, 0.5)
        radius = 0.35
        thickness = 0.08
        
        angle = percentage/100 * 360
        
        background = plt.Circle(center, radius, fill=False, 
                            color='#E5E5E5', linewidth=thickness*100)
        ax.add_patch(background)
        
        progress = plt.matplotlib.patches.Arc(center, radius*2, radius*2,
                                            theta1=0, theta2=angle,
                                            color=color, linewidth=thickness*100)
        ax.add_patch(progress)
        
        ax.text(0.5, 0.5, f"{percentage}%",
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=24,
                fontweight='light',
                color='#333333')
        
        ax.text(0.5, 0.8, title,
                horizontalalignment='center',
                fontsize=14,
                fontweight='light',
                color='#333333')
        
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    plt.subplots_adjust(wspace=0.3)
    
    colors = ['#B8860B', '#CD7F32', '#C0C0C0']
    
    for ax, (_, row), color in zip([ax1, ax2, ax3], data.iterrows(), colors):
        create_circle_progress(ax, row['percentage'], color, row['metric'])
    
    plt.suptitle('Performance Analytics', fontsize=16, y=1.05)
    plt.savefig('圆环进度图_style_4.png', bbox_inches='tight', dpi=300, facecolor='white')
    plt.close()

def plot_5(data=None):
    """暗黑模式"""
    if data is None:
        data = pd.read_csv('圆环进度图.csv')
    
    def create_circle_progress(ax, percentage, color, title):
        center = (0.5, 0.5)
        radius = 0.35
        thickness = 0.07
        
        angle = percentage/100 * 360
        
        background = plt.Circle(center, radius, fill=False, 
                            color='#333333', linewidth=thickness*100)
        ax.add_patch(background)
        
        progress = plt.matplotlib.patches.Arc(center, radius*2, radius*2,
                                            theta1=0, theta2=angle,
                                            color=color, linewidth=thickness*100)
        ax.add_patch(progress)
        
        ax.text(0.5, 0.5, f"{percentage}%",
                horizontalalignment='center',
                verticalalignment='center',
                fontsize=24,
                color='white')
        
        ax.text(0.5, 0.8, title,
                horizontalalignment='center',
                fontsize=14,
                color='#CCCCCC')
        
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_facecolor('#1a1a1a')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5), facecolor='#1a1a1a')
    plt.subplots_adjust(wspace=0.3)
    
    colors = ['#FF5F5F', '#50FA7B', '#8BE9FD']
    
    for ax, (_, row), color in zip([ax1, ax2, ax3], data.iterrows(), colors):
        create_circle_progress(ax, row['percentage'], color, row['metric'])
    
    plt.suptitle('Performance Dashboard', fontsize=16, y=1.05, color='white')
    plt.savefig('圆环进度图_style_5.png', bbox_inches='tight', dpi=300, facecolor='#1a1a1a')
    plt.close()

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
