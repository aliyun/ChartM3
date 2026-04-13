import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.patches import Rectangle
import math

def preprocess(data=None):
    """Generate sample progress data"""
    if data is None:
        data = pd.DataFrame({
            'task': ['Project A', 'Project B', 'Project C', 'Project D'],
            'progress': [75, 45, 90, 30]
        })
    
    data['progress'] = data['progress'].clip(0, 100)
    data.to_csv('半圆环进度图.csv', index=False)
    return data

def plot(data):
    """Create improved semi-circular progress charts"""
    n_tasks = len(data)
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs = axs.ravel()
    
    # Enhanced color scheme
    bg_color = '#EAECEE'
    progress_color = '#2874A6'
    text_color = '#2C3E50'
    
    for idx, (task, progress) in enumerate(zip(data['task'], data['progress'])):
        ax = axs[idx]
        
        # Calculate angles for upper semi-circle
        start_angle = 180
        end_angle = 0
        progress_angle = start_angle - (progress/100) * 180
        
        # Draw background arc
        bg_arc = Arc((0.5, 0.4), 0.7, 0.7, theta1=end_angle, theta2=start_angle,
                    color=bg_color, linewidth=15, zorder=1)
        ax.add_patch(bg_arc)
        
        # Draw progress arc
        progress_arc = Arc((0.5, 0.4), 0.7, 0.7, theta1=progress_angle, 
                         theta2=start_angle, color=progress_color, linewidth=15,
                         zorder=2)
        ax.add_patch(progress_arc)
        
        # Add percentage text in center
        ax.text(0.5, 0.4, f'{progress}%', ha='center', va='center',
                fontsize=24, fontweight='bold', color=text_color)
        
        # Add task name at bottom
        ax.text(0.5, 0.3, task, ha='center', va='center',
                fontsize=12, color=text_color)
        
        # Add 0% and 100% marks
        ax.text(0.15, 0.4, '0%', ha='right', va='center',
                fontsize=10, color=text_color, alpha=0.6)
        ax.text(0.85, 0.4, '100%', ha='left', va='center',
                fontsize=10, color=text_color, alpha=0.6)

        # Add tick marks
        for tick in range(0, 101, 20):
            angle = np.radians(180 - tick * 1.8)  # Convert percentage to angle
            tick_len = 0.06
            x = 0.5 + 0.35 * np.cos(angle)  # Radius = 0.35
            y = 0.4 + 0.35 * np.sin(angle)
            dx = tick_len * np.cos(angle)
            dy = tick_len * np.sin(angle)
            
            # Draw tick marks
            if tick % 20 == 0:
                ax.plot([x, x-dx*0.5], [y, y-dy*0.5], 
                       color=text_color, linewidth=1, alpha=0.3)
        
        # Configure axes
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 0.8)
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('半圆环进度图.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

# Test the functions

def plot_1(data):
    """商务蓝风格"""
    n_tasks = len(data)
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs = axs.ravel()
    
    bg_color = '#E8EEF4'
    progress_color = '#1F618D'
    text_color = '#2C3E50'
    
    for idx, (task, progress) in enumerate(zip(data['task'], data['progress'])):
        ax = axs[idx]
        
        start_angle = 180
        end_angle = 0
        progress_angle = start_angle - (progress/100) * 180
        
        bg_arc = Arc((0.5, 0.4), 0.7, 0.7, theta1=end_angle, theta2=start_angle,
                    color=bg_color, linewidth=18, zorder=1)
        ax.add_patch(bg_arc)
        
        progress_arc = Arc((0.5, 0.4), 0.7, 0.7, theta1=progress_angle, 
                         theta2=start_angle, color=progress_color, linewidth=18,
                         zorder=2)
        ax.add_patch(progress_arc)
        
        ax.text(0.5, 0.45, f'{progress}%', ha='center', va='center',
                fontsize=28, fontweight='bold', color=text_color)
        ax.text(0.5, 0.32, task, ha='center', va='center',
                fontsize=14, color=text_color, style='italic')
        
        ax.text(0.15, 0.4, '0%', ha='right', va='center',
                fontsize=12, color=text_color, alpha=0.7)
        ax.text(0.85, 0.4, '100%', ha='left', va='center',
                fontsize=12, color=text_color, alpha=0.7)

        for tick in range(0, 101, 25):
            angle = np.radians(180 - tick * 1.8)
            tick_len = 0.05
            x = 0.5 + 0.35 * np.cos(angle)
            y = 0.4 + 0.35 * np.sin(angle)
            dx = tick_len * np.cos(angle)
            dy = tick_len * np.sin(angle)
            ax.plot([x, x-dx], [y, y-dy], color=text_color, linewidth=1.5, alpha=0.3)
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 0.8)
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('半圆环进度图_style_1.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

def plot_2(data):
    """极简黑白风格"""
    n_tasks = len(data)
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs = axs.ravel()
    
    bg_color = '#EEEEEE'
    progress_color = '#333333'
    text_color = '#000000'
    
    for idx, (task, progress) in enumerate(zip(data['task'], data['progress'])):
        ax = axs[idx]
        
        start_angle = 180
        end_angle = 0
        progress_angle = start_angle - (progress/100) * 180
        
        bg_arc = Arc((0.5, 0.4), 0.7, 0.7, theta1=end_angle, theta2=start_angle,
                    color=bg_color, linewidth=12, zorder=1)
        ax.add_patch(bg_arc)
        
        progress_arc = Arc((0.5, 0.4), 0.7, 0.7, theta1=progress_angle, 
                         theta2=start_angle, color=progress_color, linewidth=12,
                         zorder=2)
        ax.add_patch(progress_arc)
        
        ax.text(0.5, 0.4, f'{progress}%', ha='center', va='center',
                fontsize=24, fontweight='light', color=text_color)
        ax.text(0.5, 0.3, task, ha='center', va='center',
                fontsize=10, color=text_color)
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 0.8)
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('半圆环进度图_style_2.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

def plot_3(data):
    """多彩活泼风格"""
    n_tasks = len(data)
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs = axs.ravel()
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    bg_colors = ['#FFE3E3', '#D4F4F1', '#D5EEF7', '#E0F0E9']
    
    for idx, (task, progress) in enumerate(zip(data['task'], data['progress'])):
        ax = axs[idx]
        
        start_angle = 180
        end_angle = 0
        progress_angle = start_angle - (progress/100) * 180
        
        bg_arc = Arc((0.5, 0.4), 0.7, 0.7, theta1=end_angle, theta2=start_angle,
                    color=bg_colors[idx], linewidth=15, zorder=1)
        ax.add_patch(bg_arc)
        
        progress_arc = Arc((0.5, 0.4), 0.7, 0.7, theta1=progress_angle, 
                         theta2=start_angle, color=colors[idx], linewidth=15,
                         zorder=2)
        ax.add_patch(progress_arc)
        
        ax.text(0.5, 0.4, f'{progress}%', ha='center', va='center',
                fontsize=26, fontweight='bold', color=colors[idx])
        ax.text(0.5, 0.25, task, ha='center', va='center',
                fontsize=12, color=colors[idx], fontweight='bold')
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 0.8)
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('半圆环进度图_style_3.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

def plot_4(data):
    """科技感风格"""
    n_tasks = len(data)
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs = axs.ravel()
    
    bg_color = '#1C2833'
    progress_color = '#00FF00'
    text_color = '#FFFFFF'
    
    for idx, (task, progress) in enumerate(zip(data['task'], data['progress'])):
        ax = axs[idx]
        ax.set_facecolor(bg_color)
        
        start_angle = 180
        end_angle = 0
        progress_angle = start_angle - (progress/100) * 180
        
        bg_arc = Arc((0.5, 0.4), 0.7, 0.7, theta1=end_angle, theta2=start_angle,
                    color='#2C3E50', linewidth=15, zorder=1)
        ax.add_patch(bg_arc)
        
        progress_arc = Arc((0.5, 0.4), 0.7, 0.7, theta1=progress_angle, 
                         theta2=start_angle, color=progress_color, linewidth=15,
                         alpha=0.8, zorder=2)
        ax.add_patch(progress_arc)
        
        ax.text(0.5, 0.4, f'{progress}%', ha='center', va='center',
                fontsize=24, color=progress_color, fontweight='bold')
        ax.text(0.5, 0.3, task, ha='center', va='center',
                fontsize=12, color=text_color, family='monospace')
        
        for tick in range(0, 101, 10):
            angle = np.radians(180 - tick * 1.8)
            tick_len = 0.04
            x = 0.5 + 0.35 * np.cos(angle)
            y = 0.4 + 0.35 * np.sin(angle)
            dx = tick_len * np.cos(angle)
            dy = tick_len * np.sin(angle)
            ax.plot([x, x-dx], [y, y-dy], color=progress_color, linewidth=1, alpha=0.3)
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 0.8)
        ax.axis('off')
    
    fig.patch.set_facecolor(bg_color)
    plt.tight_layout()
    plt.savefig('半圆环进度图_style_4.png', dpi=300, bbox_inches='tight', 
                facecolor=bg_color, edgecolor='none')
    plt.close()

def plot_5(data):
    """柔和自然风格"""
    n_tasks = len(data)
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs = axs.ravel()
    
    colors = ['#A8E6CF', '#DCEDC1', '#FFD3B6', '#FFAAA5']
    bg_color = '#F8F9F9'
    text_color = '#666666'
    
    for idx, (task, progress) in enumerate(zip(data['task'], data['progress'])):
        ax = axs[idx]
        
        start_angle = 180
        end_angle = 0
        progress_angle = start_angle - (progress/100) * 180
        
        bg_arc = Arc((0.5, 0.4), 0.7, 0.7, theta1=end_angle, theta2=start_angle,
                    color='#EAEDED', linewidth=20, zorder=1)
        ax.add_patch(bg_arc)
        
        progress_arc = Arc((0.5, 0.4), 0.7, 0.7, theta1=progress_angle, 
                         theta2=start_angle, color=colors[idx], linewidth=20,
                         zorder=2)
        ax.add_patch(progress_arc)
        
        ax.text(0.5, 0.4, f'{progress}%', ha='center', va='center',
                fontsize=22, color=text_color, fontweight='light')
        ax.text(0.5, 0.28, task, ha='center', va='center',
                fontsize=11, color=text_color)
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 0.8)
        ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('半圆环进度图_style_5.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
