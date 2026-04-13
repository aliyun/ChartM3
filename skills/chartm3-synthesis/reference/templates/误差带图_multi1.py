import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import seaborn as sns

def preprocess(data=None):
    np.random.seed(42)
    # Generate 90 days of data
    dates = pd.date_range(start='2023-01-01', periods=90, freq='D')
    
    # Create smooth temperature curve with seasonal component
    t = np.linspace(0, 4*np.pi, 90)
    base_temp = 20 + 5*np.sin(t)  # Mean around 20°C with 5°C seasonal variation
    
    # Add random noise
    noise = np.random.normal(0, 0.5, 90)
    temps = base_temp + noise
    
    # Calculate confidence bands (±2°C with some variation)
    error = 1.5 + 0.5*np.random.random(90)
    upper_bound = temps + error
    lower_bound = temps - error
    
    # Create DataFrame
    df = pd.DataFrame({
        'date': dates,
        'temperature': temps,
        'upper_bound': upper_bound,
        'lower_bound': lower_bound
    })
    
    # Save to CSV
    df.to_csv('误差带图.csv', index=False)
    return df

def plot(data):
    # Set style
    plt.style.use('seaborn-v0_8')
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot error bands
    ax.fill_between(data['date'], 
                    data['lower_bound'],
                    data['upper_bound'],
                    alpha=0.2, 
                    color='#3498db',
                    label='Confidence Interval')
    
    # Plot main line
    ax.plot(data['date'], 
            data['temperature'], 
            color='#2980b9',
            linewidth=2,
            label='Temperature')
    
    # Customize appearance
    ax.set_title('Daily Temperature Forecast with Confidence Intervals', 
                fontsize=14, pad=20)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Temperature (°C)', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    # Rotate x-axis labels
    plt.xticks(rotation=45)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('误差带图.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate and plot data
data = preprocess()
plot(data)

def plot_1(data):
    # 商务专业风格
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.fill_between(data['date'], 
                    data['lower_bound'],
                    data['upper_bound'],
                    alpha=0.15, 
                    color='#2c3e50')
    
    ax.plot(data['date'], 
            data['temperature'], 
            color='#2c3e50',
            linewidth=2.5,
            label='Temperature')
    
    ax.set_title('Temperature Forecast Analysis', 
                fontsize=16, pad=20, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Temperature (°C)', fontsize=12)
    ax.grid(True, alpha=0.2)
    ax.legend(loc='upper right', frameon=True)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('误差带图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 科技感深色主题
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.fill_between(data['date'], 
                    data['lower_bound'],
                    data['upper_bound'],
                    alpha=0.3, 
                    color='#00ff88')
    
    ax.plot(data['date'], 
            data['temperature'], 
            color='#00ff88',
            linewidth=2,
            linestyle='--',
            marker='o',
            markersize=4)
    
    ax.set_title('Temperature Monitoring System', 
                fontsize=14, pad=20, color='white')
    ax.set_xlabel('Date', fontsize=10, color='white')
    ax.set_ylabel('Temperature (°C)', fontsize=10, color='white')
    ax.grid(True, alpha=0.1, linestyle=':')
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('误差带图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 自然环保主题
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.fill_between(data['date'], 
                    data['lower_bound'],
                    data['upper_bound'],
                    alpha=0.2, 
                    color='#7fb800')
    
    ax.plot(data['date'], 
            data['temperature'], 
            color='#446600',
            linewidth=2.5)
    
    ax.set_title('Environmental Temperature Trends', 
                fontsize=14, pad=20, color='#446600')
    ax.set_xlabel('Date', fontsize=11)
    ax.set_ylabel('Temperature (°C)', fontsize=11)
    ax.grid(False)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('误差带图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 现代简约风格
    plt.style.use('seaborn-v0_8-white')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.fill_between(data['date'], 
                    data['lower_bound'],
                    data['upper_bound'],
                    alpha=0.1, 
                    color='#888888')
    
    ax.plot(data['date'], 
            data['temperature'], 
            color='#333333',
            linewidth=1.5)
    
    ax.set_title('Temperature Analysis', 
                fontsize=12, pad=15)
    ax.set_xlabel('Date', fontsize=10)
    ax.set_ylabel('Temperature (°C)', fontsize=10)
    ax.grid(True, alpha=0.1)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('误差带图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 活力多彩风格
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.fill_between(data['date'], 
                    data['lower_bound'],
                    data['upper_bound'],
                    alpha=0.3, 
                    color='#ff9933')
    
    ax.plot(data['date'], 
            data['temperature'], 
            color='#ff5500',
            linewidth=2,
            marker='o',
            markersize=3,
            markerfacecolor='white')
    
    ax.set_title('Dynamic Temperature Changes', 
                fontsize=15, pad=20, color='#ff5500')
    ax.set_xlabel('Date', fontsize=11)
    ax.set_ylabel('Temperature (°C)', fontsize=11)
    ax.grid(True, alpha=0.2, linestyle='--')
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('误差带图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
# plot(data)
# plot_1(data)
# plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
