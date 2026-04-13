import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess(data=None):
    # Generate synthetic test score data
    np.random.seed(42)
    scores = np.random.normal(75, 12, 200).round().astype(int)
    # Clip to valid range
    scores = np.clip(scores, 0, 100)
    
    # Create dataframe
    df = pd.DataFrame({'Test Score': scores})
    
    # Save to csv
    df.to_csv('基础直方图.csv', index=False)
    return df

def plot(data):
    # Set style
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Create histogram
    ax = sns.histplot(data=data, x='Test Score', bins=15, 
                     color='skyblue', edgecolor='black')
    
    # Add title and labels
    plt.title('Distribution of Test Scores', pad=15, fontsize=14)
    plt.xlabel('Score', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    
    # Add value annotations on bars
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                   (p.get_x() + p.get_width()/2., p.get_height()),
                   ha='center', va='bottom')
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('基础直方图.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_1(data):
    # 现代简约风格
    sns.set_style("white")
    plt.figure(figsize=(12, 7))
    
    ax = sns.histplot(data=data, x='Test Score', bins=15,
                     color='#2ecc71', alpha=0.7,
                     edgecolor='black', linewidth=1)
    
    plt.title('Distribution of Test Scores', pad=20, 
              fontsize=16, fontweight='bold', fontfamily='Arial')
    plt.xlabel('Score', fontsize=14, fontfamily='Arial')
    plt.ylabel('Frequency', fontsize=14, fontfamily='Arial')
    
    # Add mean line
    mean = data['Test Score'].mean()
    plt.axvline(mean, color='#e74c3c', linestyle='--', 
                label=f'Mean: {mean:.1f}')
    plt.legend()
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('基础直方图_style1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 深色主题风格
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    
    ax = sns.histplot(data=data, x='Test Score', bins=15,
                     color='#3498db', alpha=0.8,
                     edgecolor='white', linewidth=1.5)
    
    plt.title('Distribution of Test Scores', pad=15,
              fontsize=14, color='white', fontfamily='Helvetica')
    plt.xlabel('Score', fontsize=12, color='white')
    plt.ylabel('Frequency', fontsize=12, color='white')
    
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}',
                   (p.get_x() + p.get_width()/2., p.get_height()),
                   ha='center', va='bottom', color='white')
    
    plt.tight_layout()
    plt.savefig('基础直方图_style2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 渐变色风格
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    colors = plt.cm.viridis(np.linspace(0, 1, 15))
    ax = sns.histplot(data=data, x='Test Score', bins=15,
                     palette=colors, alpha=0.8,
                     edgecolor='white', linewidth=1)
    
    plt.title('Distribution of Test Scores\nWith Gradient Colors', 
              pad=15, fontsize=14)
    plt.xlabel('Score', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    
    plt.grid(True, linestyle=':')
    plt.tight_layout()
    plt.savefig('基础直方图_style3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 经典报告风格
    sns.set_style("ticks")
    plt.figure(figsize=(10, 6))
    
    ax = sns.histplot(data=data, x='Test Score', bins=15,
                     color='#8e44ad', alpha=0.6,
                     edgecolor='black', linewidth=1)
    
    # Add statistical info
    mean = data['Test Score'].mean()
    std = data['Test Score'].std()
    stats_text = f'Mean: {mean:.1f}\nStd: {std:.1f}'
    plt.text(0.95, 0.95, stats_text, transform=ax.transAxes,
             verticalalignment='top', horizontalalignment='right',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.title('Distribution of Test Scores', pad=15, fontsize=14)
    plt.xlabel('Score', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    
    sns.despine()
    plt.tight_layout()
    plt.savefig('基础直方图_style4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 密度曲线风格
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Create histogram with density curve
    ax = sns.histplot(data=data, x='Test Score', bins=15,
                     color='#e67e22', alpha=0.6,
                     edgecolor='black', linewidth=1,
                     stat='density')
    sns.kdeplot(data=data['Test Score'], color='#c0392b', linewidth=2)
    
    plt.title('Density Distribution of Test Scores', 
              pad=15, fontsize=14, fontfamily='Times New Roman')
    plt.xlabel('Score', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('基础直方图_style5.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate and plot data
data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
