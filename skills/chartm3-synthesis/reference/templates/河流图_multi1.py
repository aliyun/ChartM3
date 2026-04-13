import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def preprocess(data=None):
    # Generate dates from 2010 to 2022
    dates = pd.date_range(start='2010-01-01', end='2022-12-31', freq='M')
    
    # Generate smooth trends for different energy types
    np.random.seed(42)
    solar = 10 + np.linspace(0, 80, len(dates)) + np.random.normal(0, 3, len(dates))
    wind = 30 + np.linspace(0, 60, len(dates)) + np.sin(np.linspace(0, 8*np.pi, len(dates)))*10
    hydro = 50 + np.random.normal(0, 4, len(dates)) + np.sin(np.linspace(0, 4*np.pi, len(dates)))*15
    biomass = 20 + np.linspace(0, 30, len(dates)) + np.random.normal(0, 2, len(dates))
    
    # Create dataframe
    df = pd.DataFrame({
        'Date': dates,
        'Solar': solar,
        'Wind': wind,
        'Hydro': hydro,
        'Biomass': biomass
    })
    
    # Ensure all values are positive
    for col in ['Solar', 'Wind', 'Hydro', 'Biomass']:
        df[col] = df[col].clip(lower=0)
    
    # Save to CSV
    df.to_csv('河流图.csv', index=False)
    return df

def plot(data):
    # Set style
    plt.style.use('seaborn-v0_8')
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Define colors
    colors = ['#ffb55a', '#2ecc71', '#3498db', '#95a5a6']
    
    # Create streamgraph
    ax.stackplot(data['Date'], 
                [data[col] for col in ['Solar', 'Wind', 'Hydro', 'Biomass']],
                labels=['Solar', 'Wind', 'Hydro', 'Biomass'],
                colors=colors,
                baseline='sym')  # symmetric around central axis
    
    # Customize plot
    ax.set_title('Renewable Energy Production (2010-2022)', 
                fontsize=14, pad=20)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Energy Production (TWh)', fontsize=12)
    
    # # Format x-axis
    ax.xaxis.set_major_locator(plt.LinearLocator(2))
    ax.xaxis.set_major_formatter(plt.FixedFormatter('%Y'))
    
    # Add legend
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('河流图.png', dpi=300, bbox_inches='tight')
    plt.close()

# Execute the functions

def plot_1(data):
    # 商务风格：深色背景，金属色系
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ['#DAA520', '#C0C0C0', '#B87333', '#FFD700']
    
    ax.stackplot(data['Date'], 
                [data[col] for col in ['Solar', 'Wind', 'Hydro', 'Biomass']],
                labels=['Solar', 'Wind', 'Hydro', 'Biomass'],
                colors=colors,
                baseline='sym',
                alpha=0.7)
    
    ax.set_title('Renewable Energy Production Trends', 
                fontsize=16, pad=20, color='white')
    ax.set_xlabel('Year', fontsize=12, color='white')
    ax.set_ylabel('Energy Production (TWh)', fontsize=12, color='white')
    
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.savefig('河流图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 环保主题：绿色渐变
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ['#8bc34a', '#4caf50', '#009688', '#2e7d32']
    
    ax.stackplot(data['Date'], 
                [data[col] for col in ['Solar', 'Wind', 'Hydro', 'Biomass']],
                labels=['Solar', 'Wind', 'Hydro', 'Biomass'],
                colors=colors,
                baseline='sym')
    
    ax.set_facecolor('#f1f8e9')
    fig.patch.set_facecolor('#f1f8e9')
    
    ax.set_title('Green Energy Development', 
                fontsize=14, pad=20, color='#1b5e20')
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Energy Production (TWh)', fontsize=12)
    
    ax.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('河流图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 现代科技风格：蓝色系
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ['#03A9F4', '#2196F3', '#1976D2', '#0D47A1']
    
    ax.stackplot(data['Date'], 
                [data[col] for col in ['Solar', 'Wind', 'Hydro', 'Biomass']],
                labels=['Solar', 'Wind', 'Hydro', 'Biomass'],
                colors=colors,
                baseline='sym')
    
    ax.set_title('Energy Production Analysis', 
                fontsize=14, pad=20, fontweight='bold')
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Energy Production (TWh)', fontsize=12)
    
    ax.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=4)
    plt.tight_layout()
    plt.savefig('河流图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 活泼风格：明亮色彩
    plt.style.use('seaborn-v0_8-bright')
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    ax.stackplot(data['Date'], 
                [data[col] for col in ['Solar', 'Wind', 'Hydro', 'Biomass']],
                labels=['Solar', 'Wind', 'Hydro', 'Biomass'],
                colors=colors,
                baseline='sym',
                alpha=0.8)
    
    ax.set_title('Renewable Energy Mix', 
                fontsize=16, pad=20)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Energy Production (TWh)', fontsize=12)
    
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.savefig('河流图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 极简风格：单色渐变
    plt.style.use('bmh')
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ['#d4e6f1', '#a9cce3', '#7fb3d5', '#5499c7']
    
    ax.stackplot(data['Date'], 
                [data[col] for col in ['Solar', 'Wind', 'Hydro', 'Biomass']],
                labels=['Solar', 'Wind', 'Hydro', 'Biomass'],
                colors=colors,
                baseline='sym')
    
    ax.set_title('Energy Production Overview', 
                fontsize=14, pad=20)
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Energy Production (TWh)', fontsize=12)
    
    ax.legend(loc='upper left', frameon=False)
    ax.grid(False)
    plt.tight_layout()
    plt.savefig('河流图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
# plot(data)
# plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
