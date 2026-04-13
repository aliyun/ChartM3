import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def preprocess(data=None):
    # Generate sample data
    np.random.seed(42)
    n_points = 50
    
    # Generate study hours (1-6 hours with some noise)
    study_hours = np.random.uniform(1, 6, n_points)
    
    # Generate corresponding test scores (50-100 with positive correlation to study time)
    base_scores = 50 + (study_hours * 8)  # Base correlation
    noise = np.random.normal(0, 5, n_points)  # Add some random variation
    test_scores = base_scores + noise
    
    # Ensure test scores stay within realistic bounds
    test_scores = np.clip(test_scores, 50, 100)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Study_Hours': study_hours,
        'Test_Score': test_scores
    })
    
    # Save to CSV
    df.to_csv('基础散点图.csv', index=False)
    return df

def plot(data):
    # Set the style
    plt.style.use('seaborn-v0_8')
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create scatter plot
    ax.scatter(data['Study_Hours'], data['Test_Score'], 
              color='#1f77b4', alpha=0.6, s=100)
    
    # Customize the plot
    ax.set_xlabel('Study Time (hours)', fontsize=12)
    ax.set_ylabel('Test Score', fontsize=12)
    ax.set_title('Relationship Between Study Time and Test Scores', 
                fontsize=14, pad=15)
    
    # Set axis limits with some padding
    ax.set_xlim(0.5, 6.5)
    ax.set_ylim(45, 105)
    
    # Add grid
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Tight layout
    plt.tight_layout()
    
    # Save plot
    plt.savefig('基础散点图.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_1(data):
    # 现代简约风格
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.scatter(data['Study_Hours'], data['Test_Score'], 
              color='#2ecc71', alpha=0.7, s=120, marker='o')
    
    # 添加趋势线
    z = np.polyfit(data['Study_Hours'], data['Test_Score'], 1)
    p = np.poly1d(z)
    ax.plot(data['Study_Hours'], p(data['Study_Hours']), 
            linestyle='--', color='#e74c3c', alpha=0.8)
    
    ax.set_xlabel('Study Time (hours)', fontsize=12, fontfamily='Arial')
    ax.set_ylabel('Test Score', fontsize=12, fontfamily='Arial')
    ax.set_title('Study Time vs Test Scores\nModern Style', 
                fontsize=14, fontweight='bold', pad=15)
    
    ax.set_xlim(0.5, 6.5)
    ax.set_ylim(45, 105)
    
    plt.tight_layout()
    plt.savefig('基础散点图_style1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 暗黑主题风格
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.scatter(data['Study_Hours'], data['Test_Score'], 
              color='#f1c40f', alpha=0.8, s=100, marker='s')
    
    ax.set_xlabel('Study Time (hours)', fontsize=12, fontfamily='Times New Roman')
    ax.set_ylabel('Test Score', fontsize=12, fontfamily='Times New Roman')
    ax.set_title('Study Time vs Test Scores\nDark Theme', 
                fontsize=14, color='white', pad=15)
    
    ax.grid(True, linestyle=':', alpha=0.3, color='gray')
    ax.set_xlim(0.5, 6.5)
    ax.set_ylim(45, 105)
    
    plt.tight_layout()
    plt.savefig('基础散点图_style2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 粉彩柔和风格
    plt.style.use('seaborn-v0_8-pastel')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    scatter = ax.scatter(data['Study_Hours'], data['Test_Score'], 
                        c=data['Test_Score'], cmap='RdYlBu', 
                        alpha=0.6, s=150)
    
    plt.colorbar(scatter)
    
    ax.set_xlabel('Study Time (hours)', fontsize=12, fontfamily='Comic Sans MS')
    ax.set_ylabel('Test Score', fontsize=12, fontfamily='Comic Sans MS')
    ax.set_title('Study Time vs Test Scores\nPastel Style', 
                fontsize=14, color='#34495e', pad=15)
    
    ax.grid(False)
    ax.set_xlim(0.5, 6.5)
    ax.set_ylim(45, 105)
    
    plt.tight_layout()
    plt.savefig('基础散点图_style3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 商务专业风格
    plt.style.use('bmh')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.scatter(data['Study_Hours'], data['Test_Score'], 
              color='#2980b9', alpha=0.7, s=80, marker='^')
    
    # 添加平均线
    ax.axhline(y=data['Test_Score'].mean(), color='#c0392b', 
               linestyle='--', alpha=0.5)
    
    ax.set_xlabel('Study Time (hours)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Test Score', fontsize=12, fontweight='bold')
    ax.set_title('Study Time vs Test Scores\nProfessional Style', 
                fontsize=14, fontweight='bold', pad=15)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('基础散点图_style4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 科技感风格
    plt.style.use('seaborn-v0_8-dark')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 添加参考线
    ax.axhline(y=70, color='#95a5a6', linestyle='--', alpha=0.3)
    ax.axvline(x=3, color='#95a5a6', linestyle='--', alpha=0.3)
    
    ax.scatter(data['Study_Hours'], data['Test_Score'], 
              color='#3498db', alpha=0.8, s=100, marker='D',
              edgecolor='white', linewidth=1)
    
    ax.set_xlabel('Study Time (hours)', fontsize=12, fontfamily='Courier New')
    ax.set_ylabel('Test Score', fontsize=12, fontfamily='Courier New')
    ax.set_title('Study Time vs Test Scores\nTech Style', 
                fontsize=14, color='#3498db', pad=15)
    
    ax.grid(True, linestyle='-', alpha=0.2)
    ax.set_xlim(0.5, 6.5)
    ax.set_ylim(45, 105)
    
    plt.tight_layout()
    plt.savefig('基础散点图_style5.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate and plot data
data = preprocess()
# plot(data)
# plot_1(data)
# plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
