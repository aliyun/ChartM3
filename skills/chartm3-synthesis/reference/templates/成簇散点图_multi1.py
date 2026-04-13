import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess(data=None):
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate class scores with slight differences
    class_a = np.random.normal(75, 10, 30)
    class_b = np.random.normal(72, 12, 30)
    class_c = np.random.normal(78, 8, 30)
    class_d = np.random.normal(70, 15, 30)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Class': np.repeat(['A', 'B', 'C', 'D'], 30),
        'Score': np.concatenate([class_a, class_b, class_c, class_d])
    })
    
    # Clip scores to valid range
    df['Score'] = df['Score'].clip(0, 100)
    
    # Save to CSV
    df.to_csv('成簇散点图.csv', index=False)
    return df

def plot(data):
    # Set style
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Create swarmplot
    sns.swarmplot(data=data, x='Class', y='Score', 
                  palette='Blues',
                  size=8)
    
    # Customize plot
    plt.title('Distribution of Test Scores by Class', pad=15, fontsize=14)
    plt.xlabel('Class Section', labelpad=10)
    plt.ylabel('Test Score', labelpad=10)
    
    # Add horizontal line at mean
    plt.axhline(y=data['Score'].mean(), color='gray', 
                linestyle='--', alpha=0.5)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    plt.savefig('成簇散点图.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate and plot data
data = preprocess()
plot(data)

def plot_1(data):
    # 商务简约风格
    sns.set_style("white")
    plt.figure(figsize=(10, 6))
    
    # 使用商务蓝色系
    colors = ["#1f77b4", "#4b96c4", "#7cb5d4", "#afd4e4"]
    
    sns.swarmplot(data=data, x='Class', y='Score', 
                  palette=colors,
                  size=7,
                  alpha=0.7)
    
    plt.title('Distribution of Test Scores by Class', 
              pad=15, fontsize=14, fontweight='bold')
    plt.xlabel('Class Section', labelpad=10)
    plt.ylabel('Test Score', labelpad=10)
    
    # 添加细网格线
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    
    plt.savefig('成簇散点图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 现代活力风格
    sns.set_style("dark")
    plt.figure(figsize=(10, 6))
    
    # 使用鲜艳对比色
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]
    
    sns.swarmplot(data=data, x='Class', y='Score', 
                  palette=colors,
                  size=9,
                  alpha=0.8)
    
    plt.title('Class Performance Distribution', 
              pad=15, fontsize=16, color="#2D3E50")
    plt.xlabel('Class Section', labelpad=10)
    plt.ylabel('Test Score', labelpad=10)
    
    plt.grid(False)
    plt.tight_layout()
    
    plt.savefig('成簇散点图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 优雅柔和风格
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # 使用柔和渐变色
    colors = ["#E8D5C4", "#D7C0AE", "#C3A492", "#967E76"]
    
    sns.swarmplot(data=data, x='Class', y='Score', 
                  palette=colors,
                  size=8,
                  alpha=0.6)
    
    plt.title('Test Score Distribution Analysis', 
              pad=15, fontsize=14, style='italic')
    plt.xlabel('Class Section', labelpad=10)
    plt.ylabel('Test Score', labelpad=10)
    
    plt.grid(True, linestyle='-', alpha=0.2)
    plt.tight_layout()
    
    plt.savefig('成簇散点图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 信息图表风格
    sns.set_style("ticks")
    plt.figure(figsize=(10, 6))
    
    # 使用高对比度配色
    colors = ["#003f5c", "#58508d", "#bc5090", "#ff6361"]
    
    sns.swarmplot(data=data, x='Class', y='Score', 
                  palette=colors,
                  size=8)
    
    plt.title('Score Distribution by Class Section', 
              pad=15, fontsize=14, fontweight='bold')
    plt.xlabel('Class Section', labelpad=10)
    plt.ylabel('Test Score', labelpad=10)
    
    # 添加均值线
    plt.axhline(y=data['Score'].mean(), color='black', 
                linestyle='--', alpha=0.5, label='Mean Score')
    plt.legend()
    
    sns.despine()
    plt.tight_layout()
    
    plt.savefig('成簇散点图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 自然色调风格
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # 使用自然色系
    colors = ["#8B4513", "#A0522D", "#CD853F", "#DEB887"]
    
    sns.swarmplot(data=data, x='Class', y='Score', 
                  palette=colors,
                  size=7,
                  alpha=0.75)
    
    plt.title('Class Score Distribution', 
              pad=15, fontsize=14, color="#654321")
    plt.xlabel('Class Section', labelpad=10)
    plt.ylabel('Test Score', labelpad=10)
    
    plt.grid(True, linestyle=':', alpha=0.3)
    plt.tight_layout()
    
    plt.savefig('成簇散点图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
