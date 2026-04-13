import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def preprocess(data=None):
    # Generate sample quarterly sales data
    quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023']
    
    data = pd.DataFrame({
        'Quarter': quarters,
        'Laptops': [850, 920, 1050, 1200],
        'Smartphones': [1200, 1350, 1500, 1800],
        'Tablets': [450, 480, 520, 600],
        'Accessories': [300, 380, 420, 500]
    })
    
    # Save to CSV
    data.to_csv('堆叠条形图.csv', index=False)
    return data

def plot(data):
    # Set style and figure size
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Create stacked bar chart
    categories = ['Laptops', 'Smartphones', 'Tablets', 'Accessories']
    bottom = np.zeros(len(data))
    
    # Plot each category
    for i, cat in enumerate(categories):
        values = data[cat]
        plt.bar(data['Quarter'], values, bottom=bottom, label=cat)
        
        # Add value labels in the middle of each segment
        for j, v in enumerate(values):
            plt.text(j, bottom[j] + v/2, str(v), 
                    ha='center', va='center')
        bottom += values
    
    # Customize the plot
    plt.title('Quarterly Sales by Product Category', pad=20, size=14)
    plt.xlabel('Quarter')
    plt.ylabel('Sales (Thousands $)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('堆叠条形图.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_1(data):
    # 商务蓝风格
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 7))
    
    colors = ['#1f77b4', '#4585bf', '#6b93ca', '#91a1d5']
    categories = ['Laptops', 'Smartphones', 'Tablets', 'Accessories']
    bottom = np.zeros(len(data))
    
    for i, cat in enumerate(categories):
        values = data[cat]
        plt.bar(data['Quarter'], values, bottom=bottom, 
                label=cat, color=colors[i], alpha=0.8)
        for j, v in enumerate(values):
            plt.text(j, bottom[j] + v/2, str(v), 
                    ha='center', va='center', color='white', fontweight='bold')
        bottom += values
    
    plt.title('Quarterly Sales Performance', pad=20, size=16, fontweight='bold')
    plt.xlabel('Quarter', size=12)
    plt.ylabel('Sales (Thousands $)', size=12)
    plt.legend(bbox_to_anchor=(0.5, 1.15), loc='center', ncol=4)
    plt.tight_layout()
    plt.savefig('堆叠条形图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 高对比度现代风格
    plt.style.use('dark_background')
    plt.figure(figsize=(12, 7))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    categories = ['Laptops', 'Smartphones', 'Tablets', 'Accessories']
    bottom = np.zeros(len(data))
    
    for i, cat in enumerate(categories):
        values = data[cat]
        plt.bar(data['Quarter'], values, bottom=bottom, 
                label=cat, color=colors[i], alpha=0.9)
        for j, v in enumerate(values):
            plt.text(j, bottom[j] + v/2, str(v), 
                    ha='center', va='center', color='white')
        bottom += values
    
    plt.title('Product Sales Distribution', pad=20, size=16, color='white')
    plt.xlabel('Quarter', size=12)
    plt.ylabel('Sales (Thousands $)', size=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.savefig('堆叠条形图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 自然环保风格
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 7))
    
    colors = ['#8BC34A', '#66BB6A', '#4CAF50', '#43A047']
    categories = ['Laptops', 'Smartphones', 'Tablets', 'Accessories']
    bottom = np.zeros(len(data))
    
    for i, cat in enumerate(categories):
        values = data[cat]
        plt.bar(data['Quarter'], values, bottom=bottom, 
                label=cat, color=colors[i], alpha=0.7)
        for j, v in enumerate(values):
            plt.text(j, bottom[j] + v/2, str(v), 
                    ha='center', va='center', color='darkgreen')
        bottom += values
    
    plt.title('Eco-Friendly Sales Report', pad=20, size=16, color='darkgreen')
    plt.xlabel('Quarter', size=12)
    plt.ylabel('Sales (Thousands $)', size=12)
    plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=4)
    plt.tight_layout()
    plt.savefig('堆叠条形图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 时尚活力风格
    plt.style.use('seaborn-v0_8')
    plt.figure(figsize=(12, 7))
    
    colors = ['#FF61D2', '#FFA600', '#00C2A8', '#6B4CE6']
    categories = ['Laptops', 'Smartphones', 'Tablets', 'Accessories']
    bottom = np.zeros(len(data))
    
    for i, cat in enumerate(categories):
        values = data[cat]
        plt.bar(data['Quarter'], values, bottom=bottom, 
                label=cat, color=colors[i], edgecolor='white', linewidth=1)
        for j, v in enumerate(values):
            plt.text(j, bottom[j] + v/2, str(v), 
                    ha='center', va='center', color='white', fontweight='bold')
        bottom += values
    
    plt.title('Trendy Sales Overview', pad=20, size=16, fontweight='bold')
    plt.xlabel('Quarter', size=12)
    plt.ylabel('Sales (Thousands $)', size=12)
    plt.legend(bbox_to_anchor=(1.05, 0.5), loc='center left')
    plt.tight_layout()
    plt.savefig('堆叠条形图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 极简灰度风格
    plt.style.use('seaborn-v0_8-white')
    plt.figure(figsize=(12, 7))
    
    colors = ['#2C3E50', '#566573', '#808B96', '#ABB2B9']
    categories = ['Laptops', 'Smartphones', 'Tablets', 'Accessories']
    bottom = np.zeros(len(data))
    
    for i, cat in enumerate(categories):
        values = data[cat]
        plt.bar(data['Quarter'], values, bottom=bottom, 
                label=cat, color=colors[i], alpha=0.9)
        for j, v in enumerate(values):
            plt.text(j, bottom[j] + v/2, str(v), 
                    ha='center', va='center', color='white')
        bottom += values
    
    plt.title('Minimalist Sales Report', pad=20, size=16)
    plt.xlabel('Quarter', size=12)
    plt.ylabel('Sales (Thousands $)', size=12)
    plt.legend(bbox_to_anchor=(0.5, 1.1), loc='center', ncol=4)
    plt.grid(False)
    plt.tight_layout()
    plt.savefig('堆叠条形图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
# plot(data)
# plot_1(data)
# plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
