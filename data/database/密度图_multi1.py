import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess(data=None):
    # Generate random height data
    np.random.seed(42)
    female_heights = np.random.normal(165, 7, 1000)  # mean=165cm, std=7
    male_heights = np.random.normal(178, 8, 1000)    # mean=178cm, std=8
    
    # Create DataFrame
    df = pd.DataFrame({
        'height': np.concatenate([female_heights, male_heights]),
        'gender': ['Female']*1000 + ['Male']*1000
    })
    
    # Save to CSV
    df.to_csv('密度图.csv', index=False)
    return df

def plot(data):
    # Set style
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Create density plot
    sns.kdeplot(data=data, x='height', hue='gender', 
                fill=True, common_norm=False, alpha=0.5,
                palette=['#FF69B4', '#4169E1'])
    
    # Add mean lines
    for gender in ['Female', 'Male']:
        mean = data[data['gender'] == gender]['height'].mean()
        plt.axvline(mean, color='gray', linestyle='--', alpha=0.5)
        plt.text(mean+0.5, plt.gca().get_ylim()[1]/2, 
                f'{gender} mean\n{mean:.1f}cm', 
                rotation=90, va='center')
    
    # Customize plot
    plt.title('Height Distribution by Gender', pad=20, size=14)
    plt.xlabel('Height (cm)', size=12)
    plt.ylabel('Density', size=12)
    
    # Save plot
    plt.tight_layout()
    plt.savefig('密度图.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_1(data):
    # 商务风格：深蓝色系
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 7))
    
    # 使用深蓝色系配色
    palette = ['#1f77b4', '#7cc7ff']
    sns.kdeplot(data=data, x='height', hue='gender',
                fill=True, common_norm=False, alpha=0.7,
                palette=palette, linewidth=2)
    
    for gender in ['Female', 'Male']:
        mean = data[data['gender'] == gender]['height'].mean()
        plt.axvline(mean, color='#2c3e50', linestyle='--', alpha=0.5)
        plt.text(mean+0.5, plt.gca().get_ylim()[1]/2,
                f'{gender}\n{mean:.1f}cm',
                color='#2c3e50', rotation=90, va='center')
    
    plt.title('Height Distribution by Gender', pad=20, size=16, color='#2c3e50')
    plt.xlabel('Height (cm)', size=12)
    plt.ylabel('Density', size=12)
    
    
    plt.tight_layout()
    plt.savefig('密度图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 学术风格：黑白主色
    sns.set_style("ticks")
    plt.figure(figsize=(10, 6))
    
    # 使用黑白灰配色
    palette = ['#333333', '#999999']
    sns.kdeplot(data=data, x='height', hue='gender',
                fill=True, common_norm=False, alpha=0.4,
                palette=palette, linewidth=1.5)
    
    for gender in ['Female', 'Male']:
        mean = data[data['gender'] == gender]['height'].mean()
        plt.axvline(mean, color='black', linestyle=':', alpha=0.5)
        plt.text(mean+0.5, plt.gca().get_ylim()[1]/2,
                f'{gender}: {mean:.1f}cm',
                rotation=90, va='center', fontsize=10)
    
    plt.title('Distribution of Height by Gender', pad=20, size=14)
    plt.xlabel('Height (cm)', size=11)
    plt.ylabel('Density', size=11)
    
    # 添加网格
    plt.grid(True, linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('密度图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 现代风格：渐变色
    sns.set_style("white")
    plt.figure(figsize=(11, 6))
    
    # 使用渐变色配色
    palette = ['#FF6B6B', '#4ECDC4']
    sns.kdeplot(data=data, x='height', hue='gender',
                fill=True, common_norm=False, alpha=0.6,
                palette=palette, linewidth=2)
    
    for gender in ['Female', 'Male']:
        mean = data[data['gender'] == gender]['height'].mean()
        plt.axvline(mean, color='#2c3e50', linestyle='--', alpha=0.3)
        plt.text(mean+0.5, plt.gca().get_ylim()[1]/2,
                f'{gender}\n{mean:.1f}cm',
                color='#2c3e50', rotation=90, va='center')
    
    plt.title('Height Distribution', pad=20, size=16, color='#2c3e50')
    plt.xlabel('Height (cm)', size=12, color='#2c3e50')
    plt.ylabel('Density', size=12, color='#2c3e50')
    
    # 调整背景
    plt.gca().set_facecolor('#f8f9fa')
    
    plt.tight_layout()
    plt.savefig('密度图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 复古风格：柔和色调
    sns.set_style("darkgrid")
    plt.figure(figsize=(10, 6))
    
    # 使用复古色调
    palette = ['#c17767', '#8e9b90']
    sns.kdeplot(data=data, x='height', hue='gender',
                fill=True, common_norm=False, alpha=0.5,
                palette=palette, linewidth=1.5)
    
    for gender in ['Female', 'Male']:
        mean = data[data['gender'] == gender]['height'].mean()
        plt.axvline(mean, color='#4a4a4a', linestyle='--', alpha=0.4)
        plt.text(mean+0.5, plt.gca().get_ylim()[1]/2,
                f'{gender}\n{mean:.1f}',
                color='#4a4a4a', rotation=90, va='center')
    
    plt.title('Height Distribution Analysis', pad=20, size=14, color='#4a4a4a')
    plt.xlabel('Height (cm)', size=11, color='#4a4a4a')
    plt.ylabel('Density', size=11, color='#4a4a4a')
    
    plt.tight_layout()
    plt.savefig('密度图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 明亮风格：高对比度
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 7))
    
    # 使用明亮对比色
    palette = ['#FF1E1E', '#1E8FFF']
    sns.kdeplot(data=data, x='height', hue='gender',
                fill=True, common_norm=False, alpha=0.4,
                palette=palette, linewidth=2.5)
    
    for gender in ['Female', 'Male']:
        mean = data[data['gender'] == gender]['height'].mean()
        plt.axvline(mean, color='#333333', linestyle='-', alpha=0.3, linewidth=2)
        plt.text(mean+0.5, plt.gca().get_ylim()[1]/2,
                f'{gender}\n{mean:.1f}cm',
                color='#333333', rotation=90, va='center', fontweight='bold')
    
    plt.title('Gender Height Distribution', pad=20, size=16, fontweight='bold')
    plt.xlabel('Height (cm)', size=14)
    plt.ylabel('Density', size=14)
    
    # 加粗坐标轴
    plt.gca().spines['bottom'].set_linewidth(1.5)
    plt.gca().spines['left'].set_linewidth(1.5)
    
    plt.tight_layout()
    plt.savefig('密度图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
