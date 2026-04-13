import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess(data=None):
    # Generate synthetic age data for different education levels
    np.random.seed(42)
    
    # Generate ages with different distributions for each education level
    high_school = np.random.normal(35, 8, 500)
    bachelors = np.random.normal(42, 10, 700)
    graduate = np.random.normal(48, 9, 300)
    
    # Create dataframe
    df = pd.DataFrame({
        'Age': np.concatenate([high_school, bachelors, graduate]),
        'Education': ['High School']*500 + ['Bachelor\'s']*700 + ['Graduate']*300
    })
    
    # Clean up ages to realistic values
    df['Age'] = df['Age'].clip(18, 80).round()
    
    # Save to CSV
    df.to_csv('堆叠直方图.csv', index=False)
    return df

def plot(data):
    # Set style
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Create stacked histogram
    sns.histplot(
        data=data,
        x="Age",
        hue="Education",
        multiple="stack",
        bins=25,
        alpha=0.6
    )
    
    # Customize plot
    plt.title("Age Distribution by Education Level", pad=20, fontsize=14)
    plt.xlabel("Age", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('堆叠直方图.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate and plot data
df = preprocess()
plot(df)

def plot_1(data):
    # 商务风格：蓝色调配色方案
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 7))
    
    colors = ['#1f77b4', '#7aa6c2', '#aed1e6']
    sns.histplot(
        data=data,
        x="Age",
        hue="Education",
        multiple="stack",
        bins=20,
        alpha=0.7,
        palette=colors
    )
    
    plt.title("Age Distribution by Education Level", pad=20, fontsize=16, fontweight='bold')
    plt.xlabel("Age", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('堆叠直方图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 极简风格：灰度配色
    sns.set_style("white")
    plt.figure(figsize=(10, 6))
    
    colors = ['#2c2c2c', '#666666', '#999999']
    sns.histplot(
        data=data,
        x="Age",
        hue="Education",
        multiple="stack",
        bins=15,
        alpha=0.6,
        palette=colors,
        linewidth=0.5
    )
    
    plt.title("Age Distribution by Education Level", pad=15, fontsize=14)
    plt.xlabel("Age", fontsize=10)
    plt.ylabel("Count", fontsize=10)
    
    plt.grid(False)
    
    plt.tight_layout()
    plt.savefig('堆叠直方图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 活泼风格：明亮对比色
    sns.set_style("white")
    plt.figure(figsize=(11, 6))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    sns.histplot(
        data=data,
        x="Age",
        hue="Education",
        multiple="stack",
        bins=25,
        alpha=0.8,
        palette=colors
    )
    
    plt.title("Age Distribution by Education Level", pad=20, fontsize=15, color='#444444')
    plt.xlabel("Age", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    
    
    plt.tight_layout()
    plt.savefig('堆叠直方图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 科技风格：深色背景
    plt.style.use('dark_background')
    plt.figure(figsize=(12, 7))
    
    colors = ['#00ff9f', '#00b8ff', '#fb6087']
    sns.histplot(
        data=data,
        x="Age",
        hue="Education",
        multiple="stack",
        bins=30,
        alpha=0.7,
        palette=colors
    )
    
    plt.title("Age Distribution by Education Level", pad=20, fontsize=16, color='white')
    plt.xlabel("Age", fontsize=12, color='white')
    plt.ylabel("Count", fontsize=12, color='white')
    
    plt.grid(True, alpha=0.2)
    
    plt.tight_layout()
    plt.savefig('堆叠直方图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 渐变色风格
    sns.set_style("ticks")
    plt.figure(figsize=(10, 6))
    
    colors = sns.color_palette("YlOrRd", n_colors=3)
    sns.histplot(
        data=data,
        x="Age",
        hue="Education",
        multiple="stack",
        bins=20,
        alpha=0.75,
        palette=colors
    )
    
    plt.title("Age Distribution by Education Level", pad=15, fontsize=14)
    plt.xlabel("Age", fontsize=11)
    plt.ylabel("Count", fontsize=11)
    
    sns.despine(left=True)
    
    plt.tight_layout()
    plt.savefig('堆叠直方图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
# plot(data)
# plot_1(data)
# plot_2(data)
# plot_3(data)
# plot_4(data)
plot_5(data)
