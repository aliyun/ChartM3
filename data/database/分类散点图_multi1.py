import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess(data=None):
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate data
    subjects = ['Math', 'Science', 'English', 'History']
    scores = []
    subject_labels = []
    
    for subject in subjects:
        # Generate 30 scores for each subject with slight variations in mean
        mean = np.random.uniform(70, 85)
        std = 8
        subject_scores = np.clip(np.random.normal(mean, std, 30), 0, 100)
        scores.extend(subject_scores)
        subject_labels.extend([subject] * 30)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Subject': subject_labels,
        'Score': scores
    })
    
    # Save to CSV
    df.to_csv('分类散点图.csv', index=False)
    return df

def plot(data):
    # Set style
    sns.set_style("whitegrid")
    
    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Create stripplot
    sns.stripplot(data=data, x='Subject', y='Score', 
                 size=8, jitter=0.2, alpha=0.6, 
                 palette='Set2')
    
    # Customize plot
    plt.title('Student Performance Across Subjects', 
             fontsize=14, pad=15)
    plt.xlabel('Subject', fontsize=12, labelpad=10)
    plt.ylabel('Test Score', fontsize=12, labelpad=10)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    plt.savefig('分类散点图.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate and plot data
data = preprocess()
plot(data)

def plot_1(data):
    # 商务风格
    plt.style.use('seaborn-v0_8')
    plt.figure(figsize=(10, 6))
    
    # 使用蓝色渐变色板
    colors = ['#1f77b4', '#3186bc', '#4396c4', '#55a7cc']
    
    sns.stripplot(data=data, x='Subject', y='Score',
                 size=8, jitter=0.2, alpha=0.7,
                 palette=colors, edgecolor='white', linewidth=1)
    
    # 添加均值线
    sns.boxplot(data=data, x='Subject', y='Score',
                showfliers=False, width=0.3,
                color='none', showmeans=True,
                meanprops={"marker":"o",
                          "markerfacecolor":"white",
                          "markeredgecolor":"#1f77b4",
                          "markersize":"10"})
    
    plt.title('Performance Analysis by Subject', fontsize=14, pad=15)
    plt.xlabel('Academic Subject', fontsize=11)
    plt.ylabel('Score Distribution', fontsize=11)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('分类散点图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 学术风格
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # 黑白配色
    sns.stripplot(data=data, x='Subject', y='Score',
                 size=7, jitter=0.2, alpha=0.6,
                 color='black', marker='o')
    
    # 添加violin plot作为背景
    sns.violinplot(data=data, x='Subject', y='Score',
                  color='none', inner=None, alpha=0.3)
    
    plt.title('Distribution of Student Scores by Subject\n', 
             fontsize=12, fontweight='bold')
    plt.xlabel('Subject Category')
    plt.ylabel('Test Scores (0-100)')
    
    # 添加统计信息
    for i, subject in enumerate(data['Subject'].unique()):
        mean = data[data['Subject']==subject]['Score'].mean()
        plt.text(i, -5, f'μ={mean:.1f}', ha='center')
    
    plt.tight_layout()
    plt.savefig('分类散点图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 活泼风格
    sns.set_style("white")
    plt.figure(figsize=(10, 6))
    
    # 明亮的对比色
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    sns.stripplot(data=data, x='Subject', y='Score',
                 size=9, jitter=0.25, alpha=0.6,
                 palette=colors, marker='o',
                 edgecolor='white', linewidth=1)
    
    plt.title('✨ Student Score Distribution ✨', 
             fontsize=15, pad=15)
    plt.xlabel('Subject Area', fontsize=12)
    plt.ylabel('Achievement Score', fontsize=12)
    
    # 添加装饰性元素
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('分类散点图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 极简风格
    sns.set_style("white")
    plt.figure(figsize=(10, 6))
    
    # 单色系
    sns.stripplot(data=data, x='Subject', y='Score',
                 size=6, jitter=0.2, alpha=0.4,
                 color='#2c3e50', marker='.')
    
    plt.title('Score Distribution', fontsize=12, pad=15)
    plt.xlabel('Subject')
    plt.ylabel('Score')
    
    # 最小化视觉元素
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_color('#dddddd')
    plt.gca().spines['bottom'].set_color('#dddddd')
    plt.grid(False)
    
    plt.tight_layout()
    plt.savefig('分类散点图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 现代风格
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    
    # 霓虹风格配色
    colors = ['#FF0080', '#FF00FF', '#8000FF', '#0080FF']
    
    sns.stripplot(data=data, x='Subject', y='Score',
                 size=8, jitter=0.2, alpha=0.6,
                 palette=colors, marker='o',
                 edgecolor='white', linewidth=0.5)
    
    plt.title('Student Performance Matrix', 
             fontsize=14, pad=15, color='white')
    plt.xlabel('Subject', fontsize=12, color='white')
    plt.ylabel('Score', fontsize=12, color='white')
    
    # 添加背景网格
    plt.grid(True, alpha=0.1)
    
    plt.tight_layout()
    plt.savefig('分类散点图_style_5.png', dpi=300, bbox_inches='tight',
                facecolor='black', edgecolor='none')
    plt.close()

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
