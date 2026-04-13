import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess(data=None):
    # Generate sample data for 4 treatment groups
    np.random.seed(42)
    groups = ['Control', 'Treatment A', 'Treatment B', 'Treatment C']
    n_samples = 10
    
    data_dict = {
        'Group': [],
        'Value': []
    }
    
    # Generate random data with different means and variations
    means = [25, 35, 30, 40]
    stds = [3, 4, 3.5, 4.5]
    
    for i, group in enumerate(groups):
        values = np.random.normal(means[i], stds[i], n_samples)
        data_dict['Group'].extend([group] * n_samples)
        data_dict['Value'].extend(values)
    
    # Create DataFrame
    df = pd.DataFrame(data_dict)
    
    # Calculate summary statistics
    summary = df.groupby('Group')['Value'].agg(['mean', 'std']).round(2)
    
    # Save data
    df.to_csv('误差柱图.csv', index=False)
    
    return df

def plot(data):
    # Set style
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Create bar plot with error bars
    ax = sns.barplot(x='Group', y='Value', data=data, 
                    capsize=0.1, errwidth=2,
                    color='lightblue', alpha=0.8)
    
    # Add individual points with jitter
    sns.stripplot(x='Group', y='Value', data=data,
                 size=6, color='navy', alpha=0.4,
                 jitter=0.2)
    
    # Customize appearance
    plt.title('Effect of Different Treatments\nwith Error Bars (Mean ± SD)', 
             pad=20, fontsize=14)
    plt.xlabel('Treatment Group', fontsize=12)
    plt.ylabel('Measured Value', fontsize=12)
    
    # Add value labels on top of bars
    means = data.groupby('Group')['Value'].mean()
    for i, mean in enumerate(means):
        ax.text(i, mean, f'{mean:.1f}', 
                ha='center', va='bottom', fontsize=10)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    plt.savefig('误差柱图.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate and process data

def plot_1(data):
    # 商务风格：深蓝色系
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    colors = ['#1f77b4', '#2c3e50', '#34495e', '#2980b9']
    
    ax = sns.barplot(x='Group', y='Value', data=data, 
                    capsize=0.1, errwidth=1.5,
                    palette=colors, alpha=0.7)
    
    sns.stripplot(x='Group', y='Value', data=data,
                 size=4, color='#2c3e50', alpha=0.4,
                 jitter=0.2)
    
    plt.title('Treatment Effects Analysis', 
             pad=20, fontsize=14, fontweight='bold')
    plt.xlabel('Treatment Group', fontsize=11)
    plt.ylabel('Measured Value', fontsize=11)
    
    means = data.groupby('Group')['Value'].mean()
    for i, mean in enumerate(means):
        ax.text(i, mean, f'{mean:.1f}', 
                ha='center', va='bottom', fontsize=9,
                color='#2c3e50')
    
    plt.tight_layout()
    plt.savefig('误差柱图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 现代简约风格：单色渐变
    sns.set_style("white")
    plt.figure(figsize=(10, 6))
    colors = sns.light_palette("#5ab4ac", n_colors=4)
    
    ax = sns.barplot(x='Group', y='Value', data=data, 
                    capsize=0.05, errwidth=1,
                    palette=colors, alpha=0.9)
    
    sns.stripplot(x='Group', y='Value', data=data,
                 marker='D', size=4, color='#2c3e50', alpha=0.3,
                 jitter=0.2)
    
    plt.title('Treatment Comparison', 
             pad=20, fontsize=14, fontfamily='sans-serif')
    plt.xlabel('Group', fontsize=11)
    plt.ylabel('Value', fontsize=11)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    means = data.groupby('Group')['Value'].mean()
    for i, mean in enumerate(means):
        ax.text(i, mean, f'{mean:.1f}', 
                ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('误差柱图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 活泼风格：对比色
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
    
    ax = sns.barplot(x='Group', y='Value', data=data, 
                    capsize=0.15, errwidth=2,
                    palette=colors, alpha=0.8)
    
    sns.stripplot(x='Group', y='Value', data=data,
                 marker='o', size=7, color='#404040', alpha=0.4,
                 jitter=0.2)
    
    plt.title('Treatment Results', 
             pad=20, fontsize=16, fontweight='bold')
    plt.xlabel('Group', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    
    for spine in ax.spines.values():
        spine.set_linewidth(2)
    
    means = data.groupby('Group')['Value'].mean()
    for i, mean in enumerate(means):
        ax.text(i, mean, f'{mean:.1f}', 
                ha='center', va='bottom', fontsize=11,
                fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('误差柱图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 学术风格：黑白主题
    sns.set_style("ticks")
    plt.figure(figsize=(10, 6))
    
    ax = sns.barplot(x='Group', y='Value', data=data, 
                    capsize=0.2, errwidth=1,
                    color='white', edgecolor='black', alpha=1)
    
    sns.stripplot(x='Group', y='Value', data=data,
                 marker='^', size=5, color='black', alpha=0.5,
                 jitter=0.2)
    
    plt.title('Statistical Analysis of Treatment Effects', 
             pad=20, fontsize=14)
    plt.xlabel('Treatment Group', fontsize=11)
    plt.ylabel('Measured Value', fontsize=11)
    
    sns.despine()
    
    means = data.groupby('Group')['Value'].mean()
    for i, mean in enumerate(means):
        ax.text(i, mean, f'{mean:.1f}', 
                ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('误差柱图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 现代配色风格：渐变对比
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    ax = sns.barplot(x='Group', y='Value', data=data, 
                    capsize=0.12, errwidth=1.5,
                    palette=colors, alpha=0.85)
    
    sns.stripplot(x='Group', y='Value', data=data,
                 marker='s', size=5, color='#2C3E50', alpha=0.4,
                 jitter=0.2)
    
    plt.title('Comparative Analysis of Treatments', 
             pad=20, fontsize=14, fontweight='bold')
    plt.xlabel('Group', fontsize=11)
    plt.ylabel('Value', fontsize=11)
    
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    means = data.groupby('Group')['Value'].mean()
    for i, mean in enumerate(means):
        ax.text(i, mean, f'{mean:.1f}', 
                ha='center', va='bottom', fontsize=10,
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=1))
    
    plt.tight_layout()
    plt.savefig('误差柱图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
