import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def preprocess(data=None):
    # Create sample smartphone market share data
    data = {
        'Region': ['North America', 'Europe', 'Asia', 'Latin America'] * 3,
        'Brand': ['Apple'] * 4 + ['Samsung'] * 4 + ['Xiaomi'] * 4,
        'Market_Share': [45, 35, 25, 30,  # Apple
                        30, 40, 35, 35,  # Samsung
                        10, 15, 30, 20]   # Xiaomi
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('分组条形图.csv', index=False)
    return df

def plot(data):
    # Set the style
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Create grouped bar chart
    chart = sns.barplot(data=data, 
                       x='Region', 
                       y='Market_Share',
                       hue='Brand',
                       palette=['#FF6B6B', '#4ECDC4', '#45B7D1'])
    
    # Customize the chart
    plt.title('Smartphone Market Share by Region and Brand (2023)', 
             pad=20, 
             fontsize=14)
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Market Share (%)', fontsize=12)
    
    # Add value labels on bars
    for container in chart.containers:
        chart.bar_label(container, fmt='%.0f%%', padding=3)
    
    # Adjust legend
    plt.legend(title='Brand', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('分组条形图.png', bbox_inches='tight', dpi=300)
    plt.close()

# Execute the functions

def plot_1(data):
    # 现代商务风格：蓝色单色系
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10, 6))
    
    colors = ['#1f77b4', '#4495c1', '#7db3d4']
    chart = sns.barplot(data=data, x='Region', y='Market_Share', hue='Brand',
                       palette=colors, alpha=0.8)
    
    plt.title('Smartphone Market Share Analysis', pad=20, 
             fontsize=14, fontweight='bold')
    plt.xlabel('Region', fontsize=11)
    plt.ylabel('Market Share (%)', fontsize=11)
    
    for container in chart.containers:
        chart.bar_label(container, fmt='%.0f%%', padding=3)
    
    plt.legend(title='Brand', bbox_to_anchor=(1.05, 0.5), loc='center left')
    plt.tight_layout()
    plt.savefig('分组条形图_style_1.png', bbox_inches='tight', dpi=300)
    plt.close()

def plot_2(data):
    # 极简风格
    plt.style.use('bmh')
    plt.figure(figsize=(10, 6))
    
    colors = ['#2c3e50', '#7f8c8d', '#bdc3c7']
    chart = sns.barplot(data=data, x='Region', y='Market_Share', hue='Brand',
                       palette=colors, width=0.7)
    
    plt.title('Market Share Distribution', pad=20, fontsize=14)
    plt.xlabel('Region', fontsize=11)
    plt.ylabel('Market Share (%)', fontsize=11)
    
    for container in chart.containers:
        chart.bar_label(container, fmt='%.0f%%', padding=3)
    
    plt.legend(title='Brand', loc='upper right')
    plt.grid(False)
    plt.tight_layout()
    plt.savefig('分组条形图_style_2.png', bbox_inches='tight', dpi=300)
    plt.close()

def plot_3(data):
    # 活泼风格：对比色
    plt.style.use('seaborn-v0_8')
    plt.figure(figsize=(10, 6))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    chart = sns.barplot(data=data, x='Region', y='Market_Share', hue='Brand',
                       palette=colors, saturation=.8)
    
    plt.title('Global Smartphone Market Share', 
             pad=20, fontsize=14, fontweight='bold')
    plt.xlabel('Region', fontsize=11)
    plt.ylabel('Market Share (%)', fontsize=11)
    
    for container in chart.containers:
        chart.bar_label(container, fmt='%.0f%%', padding=3)
    
    plt.legend(title='Brand', bbox_to_anchor=(0.5, 1.15), 
              loc='upper center', ncol=3)
    plt.tight_layout()
    plt.savefig('分组条形图_style_3.png', bbox_inches='tight', dpi=300)
    plt.close()

def plot_4(data):
    # 专业数据风格
    plt.style.use('seaborn-v0_8-paper')
    plt.figure(figsize=(10, 6))
    
    colors = ['#003f5c', '#58508d', '#bc5090']
    chart = sns.barplot(data=data, x='Region', y='Market_Share', hue='Brand',
                       palette=colors, width=0.8)
    
    plt.title('Smartphone Market Share Analysis (2023)', 
             pad=20, fontsize=14)
    plt.xlabel('Region', fontsize=11)
    plt.ylabel('Market Share (%)', fontsize=11)
    
    for container in chart.containers:
        chart.bar_label(container, fmt='%.0f%%', padding=3)
    
    plt.legend(title='Brand', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('分组条形图_style_4.png', bbox_inches='tight', dpi=300)
    plt.close()

def plot_5(data):
    # 渐变色风格
    plt.style.use('seaborn-v0_8-bright')
    plt.figure(figsize=(10, 6))
    
    colors = sns.color_palette("YlOrRd", n_colors=3)
    chart = sns.barplot(data=data, x='Region', y='Market_Share', hue='Brand',
                       palette=colors, width=0.75)
    
    plt.title('Regional Market Share Comparison', 
             pad=20, fontsize=14, fontweight='bold')
    plt.xlabel('Region', fontsize=11)
    plt.ylabel('Market Share (%)', fontsize=11)
    
    for container in chart.containers:
        chart.bar_label(container, fmt='%.0f%%', padding=3)
    
    plt.legend(title='Brand', bbox_to_anchor=(0.5, -0.15), 
              loc='upper center', ncol=3)
    plt.tight_layout()
    plt.savefig('分组条形图_style_5.png', bbox_inches='tight', dpi=300)
    plt.close()

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
