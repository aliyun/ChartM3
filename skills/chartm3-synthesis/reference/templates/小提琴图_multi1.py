import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess(data=None):
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate sample data
    n_students = 100
    subjects = ['Math', 'Science', 'English', 'History']
    
    # Create different distributions for each subject
    data = []
    for subject in subjects:
        if subject == 'Math':
            scores = np.random.normal(75, 12, n_students)
        elif subject == 'Science':
            scores = np.random.normal(72, 10, n_students)
        elif subject == 'English':
            scores = np.random.normal(78, 8, n_students)
        else:  # History
            scores = np.random.normal(70, 15, n_students)
            
        # Clip scores to be between 0 and 100
        scores = np.clip(scores, 0, 100)
        
        # Add to data list
        for score in scores:
            data.append({
                'Subject': subject,
                'Score': score
            })
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('小提琴图.csv', index=False)
    return df

def plot(data):
    # Set the style
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    
    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Create the strip plot with violin overlay
    ax = sns.stripplot(data=data, x='Subject', y='Score', 
                      size=6, alpha=0.4, jitter=0.2)
    sns.violinplot(data=data, x='Subject', y='Score', 
                  alpha=0.2, inner=None)
    
    # Customize the plot
    plt.title('Student Scores by Subject', pad=20, size=14)
    plt.xlabel('Subject', labelpad=10, size=12)
    plt.ylabel('Score', labelpad=10, size=12)
    
    # Add grid lines
    plt.grid(True, axis='y', alpha=0.3)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('小提琴图.png', dpi=300, bbox_inches='tight')
    plt.close()

# Test the functions

def plot_1(data):
    # 商务风格：深蓝色系
    plt.style.use('seaborn-v0_8-white')
    colors = ['#1f77b4', '#2c5985', '#3b4d6b', '#253547']
    
    plt.figure(figsize=(10, 6))
    ax = sns.stripplot(data=data, x='Subject', y='Score', 
                      size=4, alpha=0.3, jitter=0.2,
                      palette=colors)
    sns.violinplot(data=data, x='Subject', y='Score', 
                  alpha=0.15, inner=None, palette=colors)
    
    plt.title('Academic Performance Analysis', pad=20, 
              fontsize=14, fontweight='bold')
    plt.xlabel('Subject Areas', labelpad=10, fontsize=12)
    plt.ylabel('Performance Score', labelpad=10, fontsize=12)
    
    plt.grid(True, axis='y', alpha=0.2, linestyle='--')
    plt.tight_layout()
    plt.savefig('小提琴图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 现代简约风格：单色渐变
    plt.style.use('seaborn-v0_8-white')
    colors = ['#ff9999', '#ff6666', '#ff3333', '#ff0000']
    
    plt.figure(figsize=(10, 6))
    sns.stripplot(data=data, x='Subject', y='Score', 
                 size=3, alpha=0.2, jitter=0.2,
                 color='#ff3333')
    sns.violinplot(data=data, x='Subject', y='Score', 
                  alpha=0.1, inner=None, palette=colors)
    
    plt.title('Score Distribution', y=1.02, fontsize=14)
    plt.xlabel('Subject', fontsize=11)
    plt.ylabel('Score', fontsize=11)
    
    plt.grid(False)
    plt.tight_layout()
    plt.savefig('小提琴图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 学术风格：黑白主题
    plt.style.use('grayscale')
    
    plt.figure(figsize=(10, 6))
    sns.stripplot(data=data, x='Subject', y='Score', 
                 size=4, alpha=0.4, jitter=0.2,
                 color='black')
    sns.violinplot(data=data, x='Subject', y='Score', 
                  alpha=0.1, inner=None, color='gray')
    
    plt.title('Statistical Analysis of Student Scores', 
              fontname='Times New Roman', pad=20, fontsize=14)
    plt.xlabel('Academic Subject', fontname='Times New Roman', fontsize=12)
    plt.ylabel('Score Range', fontname='Times New Roman', fontsize=12)
    
    plt.grid(True, axis='y', linestyle='-', alpha=0.2)
    plt.tight_layout()
    plt.savefig('小提琴图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 活泼风格：彩色主题
    plt.style.use('seaborn-v0_8')
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
    
    plt.figure(figsize=(10, 6))
    sns.stripplot(data=data, x='Subject', y='Score', 
                 size=5, alpha=0.5, jitter=0.3,
                 palette=colors, marker='o')
    sns.violinplot(data=data, x='Subject', y='Score', 
                  alpha=0.2, inner=None, palette=colors)
    
    plt.title('Student Score Dashboard! 📚', fontsize=14, pad=20)
    plt.xlabel('Subject 📖', fontsize=12, labelpad=10)
    plt.ylabel('Score 📊', fontsize=12, labelpad=10)
    
    plt.grid(True, axis='y', alpha=0.3, linestyle=':')
    plt.tight_layout()
    plt.savefig('小提琴图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 复古风格：柔和色调
    plt.style.use('seaborn-v0_8-pastel')
    colors = ['#d5a6bd', '#b4c7e7', '#c5e0b4', '#ffe699']
    
    plt.figure(figsize=(10, 6))
    sns.stripplot(data=data, x='Subject', y='Score', 
                 size=4, alpha=0.4, jitter=0.2,
                 palette=colors)
    sns.violinplot(data=data, x='Subject', y='Score', 
                  alpha=0.3, inner=None, palette=colors)
    
    plt.title('Academic Results Overview', 
             fontsize=14, pad=20, fontfamily='serif')
    plt.xlabel('Course', fontsize=12, labelpad=10, fontfamily='serif')
    plt.ylabel('Achievement', fontsize=12, labelpad=10, fontfamily='serif')
    
    plt.grid(True, axis='y', alpha=0.2, linestyle='-.')
    plt.tight_layout()
    plt.savefig('小提琴图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
