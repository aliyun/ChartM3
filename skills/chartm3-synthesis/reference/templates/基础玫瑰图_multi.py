import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps

def preprocess(data=None):
    np.random.seed(42)
    # Generate sample monthly temperature data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Create realistic temperature pattern with seasonal variation
    temps = [5, 7, 12, 17, 22, 25, 28, 27, 23, 18, 12, 7]
    
    # Add some random variation
    temps = np.array(temps) + np.random.normal(0, 1, 12)
    
    # Create DataFrame
    df = pd.DataFrame({
        'month': months,
        'temperature': temps
    })
    
    # Save to CSV
    df.to_csv('基础玫瑰图.csv', index=False)
    return df

def plot(data):
    # Set style
    plt.style.use('seaborn-v0_8')
    
    # Create figure
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='polar')
    
    # Convert to radians for polar plot
    theta = np.linspace(0, 2*np.pi, len(data), endpoint=False)
    
    # Plot data
    width = 2*np.pi/len(data.temperature)
    bars = ax.bar(theta, data.temperature, width=width, alpha=0.7)
    
    # Customize colors
    cm = colormaps.get_cmap('RdYlBu_r')
    for i, bar in enumerate(bars):
        bar.set_facecolor(cm(i/len(bars)))
    
    # Customize ticks and labels
    ax.set_xticks(theta)
    ax.set_xticklabels(data.month, fontsize=10)
    
    # Add title and adjust layout
    plt.title('Monthly Temperature Distribution (°C)', pad=20, fontsize=14)
    
    # Save plot
    plt.savefig('基础玫瑰图.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_1(data):
    # Modern minimalist style
    plt.style.use('seaborn-v0_8-white')
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='polar')
    
    theta = np.linspace(0, 2*np.pi, len(data), endpoint=False)
    width = 2*np.pi/len(data.temperature)
    bars = ax.bar(theta, data.temperature, width=width, alpha=0.9)
    
    cm = colormaps.get_cmap('viridis')
    for i, bar in enumerate(bars):
        bar.set_facecolor(cm(i/len(bars)))
        bar.set_edgecolor('white')
    
    ax.set_xticks(theta)
    ax.set_xticklabels(data.month, fontsize=12, fontweight='bold')
    ax.grid(color='gray', alpha=0.2)
    
    plt.title('Monthly Temperature Distribution (°C)', 
              pad=20, fontsize=16, fontweight='bold')
    
    plt.savefig('基础玫瑰图_style1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # Warm vintage style
    plt.style.use('seaborn-v0_8-paper')
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='polar')
    
    theta = np.linspace(0, 2*np.pi, len(data), endpoint=False)
    width = 2*np.pi/len(data.temperature)
    bars = ax.bar(theta, data.temperature, width=width, alpha=0.7)
    
    cm = colormaps.get_cmap('YlOrRd')
    for i, bar in enumerate(bars):
        bar.set_facecolor(cm(i/len(bars)))
    
    ax.set_xticks(theta)
    ax.set_xticklabels(data.month, fontsize=11, font='serif')
    ax.grid(False)
    
    for t, r in zip(theta, data.temperature):
        ax.text(t, r+1, f'{r:.1f}°', 
                ha='center', va='bottom', fontsize=8)
    
    plt.title('Monthly Temperature Distribution', 
              pad=20, fontsize=14, font='serif')
    
    plt.savefig('基础玫瑰图_style2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # Dark theme
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(11, 11))
    ax = fig.add_subplot(111, projection='polar')
    
    theta = np.linspace(0, 2*np.pi, len(data), endpoint=False)
    width = 2*np.pi/len(data.temperature)
    bars = ax.bar(theta, data.temperature, width=width, alpha=0.8)
    
    cm = colormaps.get_cmap('plasma')
    for i, bar in enumerate(bars):
        bar.set_facecolor(cm(i/len(bars)))
        bar.set_edgecolor('white')
    
    ax.set_xticks(theta)
    ax.set_xticklabels(data.month, fontsize=12, color='white')
    ax.grid(color='gray', alpha=0.3)
    
    plt.title('Temperature Distribution\nThroughout the Year', 
              pad=20, fontsize=15, color='white')
    
    plt.savefig('基础玫瑰图_style3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # Pastel style
    plt.style.use('seaborn-v0_8-pastel')
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='polar')
    
    theta = np.linspace(0, 2*np.pi, len(data), endpoint=False)
    width = 2*np.pi/len(data.temperature)
    bars = ax.bar(theta, data.temperature, width=width, alpha=0.6)
    
    colors = plt.cm.Pastel1(np.linspace(0, 1, len(data)))
    for bar, color in zip(bars, colors):
        bar.set_facecolor(color)
        bar.set_edgecolor('gray')
    
    ax.set_xticks(theta)
    ax.set_xticklabels(data.month, fontsize=10)
    ax.grid(color='gray', alpha=0.2)
    
    plt.title('Monthly Temperature Analysis', 
              pad=20, fontsize=14, fontweight='light')
    
    plt.savefig('基础玫瑰图_style4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # Professional business style
    plt.style.use('bmh')
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='polar')
    
    theta = np.linspace(0, 2*np.pi, len(data), endpoint=False)
    width = 2*np.pi/len(data.temperature)
    bars = ax.bar(theta, data.temperature, width=width, alpha=1)
    
    cm = colormaps.get_cmap('Blues')
    for i, bar in enumerate(bars):
        bar.set_facecolor(cm(0.3 + i/len(bars)*0.7))
        bar.set_edgecolor('navy')
    
    ax.set_xticks(theta)
    ax.set_xticklabels(data.month, fontsize=12)
    ax.grid(color='gray', alpha=0.3, linestyle='--')
    
    for t, r in zip(theta, data.temperature):
        ax.text(t, r+0.5, f'{r:.1f}°C', 
                ha='center', va='bottom', fontsize=9)
    
    plt.title('Temperature Analysis Report', 
              pad=20, fontsize=16, fontweight='bold')
    
    plt.savefig('基础玫瑰图_style5.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate and plot data
data = preprocess()
# plot(data)
# plot_1(data)
# plot_2(data)
# plot_3(data)
plot_4(data)
plot_5(data)
