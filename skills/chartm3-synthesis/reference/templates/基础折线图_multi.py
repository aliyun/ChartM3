import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

def preprocess(data=None):
    # Generate monthly dates for 2023
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
    
    # Create synthetic sales data with seasonality and trend
    np.random.seed(42)
    base = 1000
    trend = np.linspace(0, 500, 12)
    seasonality = 200 * np.sin(np.linspace(0, 2*np.pi, 12))
    noise = np.random.normal(0, 50, 12)
    sales = base + trend + seasonality + noise
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Sales': np.round(sales, 0)
    })
    
    # Save to CSV
    df.to_csv('基础折线图.csv', index=False)
    return df

def plot(data):
    # Set style
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    
    # Create line plot
    ax = sns.lineplot(data=data, x='Date', y='Sales', 
                     marker='o', markersize=8, linewidth=2,
                     color='#1f77b4')
    
    # Customize the plot
    plt.title('Monthly Sales Performance - 2023', pad=20, fontsize=14)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Sales (USD)', fontsize=12)
    
    # Rotate x-axis labels
    plt.xticks(rotation=45)
    
    # Add value annotations
    for x, y in zip(data['Date'], data['Sales']):
        plt.annotate(f'${int(y):,}', 
                    (x, y), 
                    textcoords="offset points", 
                    xytext=(0,10), 
                    ha='center')
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('基础折线图.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_1(data):
    # 现代简约风格
    sns.set_style("white")
    plt.figure(figsize=(12, 6))
    
    ax = sns.lineplot(data=data, x='Date', y='Sales', 
                     marker='o', markersize=10, linewidth=2.5,
                     color='#2ecc71')
    
    plt.title('Monthly Sales Performance - 2023', pad=20, fontsize=16, color='#2c3e50')
    plt.xlabel('Month', fontsize=12, color='#2c3e50')
    plt.ylabel('Sales (USD)', fontsize=12, color='#2c3e50')
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, color='#2c3e50')
    plt.yticks(color='#2c3e50')
    
    for x, y in zip(data['Date'], data['Sales']):
        plt.annotate(f'${int(y):,}', 
                    (x, y), 
                    textcoords="offset points", 
                    xytext=(0,10), 
                    ha='center',
                    color='#2c3e50',
                    fontsize=10)
    
    plt.tight_layout()
    plt.savefig('基础折线图_style1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 深色商务风格
    sns.set_style("darkgrid")
    plt.figure(figsize=(12, 6))
    
    plt.rcParams['figure.facecolor'] = '#2c3e50'
    plt.rcParams['axes.facecolor'] = '#2c3e50'
    
    ax = sns.lineplot(data=data, x='Date', y='Sales', 
                     marker='s', markersize=8, linewidth=3,
                     color='#e74c3c')
    
    plt.title('Monthly Sales Performance - 2023', pad=20, fontsize=16, color='white')
    plt.xlabel('Month', fontsize=12, color='white')
    plt.ylabel('Sales (USD)', fontsize=12, color='white')
    
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')
    
    for x, y in zip(data['Date'], data['Sales']):
        plt.annotate(f'${int(y):,}', 
                    (x, y), 
                    textcoords="offset points", 
                    xytext=(0,10), 
                    ha='center',
                    color='white',
                    fontsize=10)
    
    plt.tight_layout()
    plt.savefig('基础折线图_style2.png', dpi=300, bbox_inches='tight', facecolor='#2c3e50')
    plt.close()

def plot_3(data):
    # 柔和暖色风格
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    
    ax = sns.lineplot(data=data, x='Date', y='Sales', 
                     marker='o', markersize=12, linewidth=2,
                     color='#ff7f50')
    
    plt.fill_between(data['Date'], data['Sales'], alpha=0.2, color='#ff7f50')
    
    plt.title('Monthly Sales Performance - 2023', pad=20, fontsize=16, color='#696969')
    plt.xlabel('Month', fontsize=12, color='#696969')
    plt.ylabel('Sales (USD)', fontsize=12, color='#696969')
    
    plt.grid(True, linestyle='-', alpha=0.2)
    plt.xticks(rotation=45, color='#696969')
    plt.yticks(color='#696969')
    
    for x, y in zip(data['Date'], data['Sales']):
        plt.annotate(f'${int(y):,}', 
                    (x, y), 
                    textcoords="offset points", 
                    xytext=(0,15), 
                    ha='center',
                    color='#ff7f50',
                    fontsize=10)
    
    plt.tight_layout()
    plt.savefig('基础折线图_style3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 极简风格
    sns.set_style("ticks")
    plt.figure(figsize=(12, 6))
    
    ax = sns.lineplot(data=data, x='Date', y='Sales', 
                     marker='D', markersize=7, linewidth=1.5,
                     color='#34495e')
    
    plt.title('Monthly Sales Performance - 2023', pad=20, fontsize=14, color='#34495e')
    plt.xlabel('Month', fontsize=10, color='#34495e')
    plt.ylabel('Sales (USD)', fontsize=10, color='#34495e')
    
    sns.despine()
    plt.xticks(rotation=45, color='#34495e')
    plt.yticks(color='#34495e')
    
    for x, y in zip(data['Date'], data['Sales']):
        plt.annotate(f'${int(y):,}', 
                    (x, y), 
                    textcoords="offset points", 
                    xytext=(0,10), 
                    ha='center',
                    color='#34495e',
                    fontsize=9)
    
    plt.tight_layout()
    plt.savefig('基础折线图_style4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 渐变色风格
    sns.set_style("white")
    plt.figure(figsize=(12, 6))
    
    gradient_line = np.linspace(0, 1, len(data))
    points = plt.plot(data['Date'], data['Sales'], '-o')
    
    line = points[0]
    cmap = plt.cm.viridis
    alpha = 0.8
    
    line.set_color('none')
    points = line.get_xydata()
    
    for i in range(len(points)-1):
        x = [points[i][0], points[i+1][0]]
        y = [points[i][1], points[i+1][1]]
        plt.plot(x, y, c=cmap(gradient_line[i]), linewidth=3, alpha=alpha)
        plt.plot(points[i][0], points[i][1], 'o', c=cmap(gradient_line[i]), 
                markersize=10, alpha=alpha)
    
    plt.plot(points[-1][0], points[-1][1], 'o', c=cmap(gradient_line[-1]), 
            markersize=10, alpha=alpha)
    
    plt.title('Monthly Sales Performance - 2023', pad=20, fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Sales (USD)', fontsize=12)
    
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.xticks(rotation=45)
    
    for x, y in zip(data['Date'], data['Sales']):
        plt.annotate(f'${int(y):,}', 
                    (x, y), 
                    textcoords="offset points", 
                    xytext=(0,10), 
                    ha='center',
                    fontsize=10)
    
    plt.tight_layout()
    plt.savefig('基础折线图_style5.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    data = preprocess()
    plot(data)
    plot_1(data)
    plot_2(data)
    plot_3(data)
    plot_4(data)
    plot_5(data)
