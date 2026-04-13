import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess(data=None):
    np.random.seed(42)
    # Generate sample data if none provided
    if data is None:
        categories = ['Electronics', 'Clothing', 'Books', 'Home & Garden', 
                     'Sports', 'Toys', 'Beauty', 'Automotive']
        sales = [round(x, 1) for x in np.random.normal(500, 150, len(categories))]
        data = pd.DataFrame({
            'Category': categories,
            'Sales': sales
        })
        
    # Sort data by sales value descending
    data = data.sort_values('Sales', ascending=True)
    
    # Save to CSV
    data.to_csv('棒棒糖图.csv', index=False)
    return data

def plot(data):
    # Set style and figure size
    plt.style.use('seaborn-v0_8')
    plt.figure(figsize=(10, 6))
    
    # Create the lollipop plot
    plt.hlines(y=range(len(data)), xmin=0, xmax=data['Sales'], 
              color='grey', alpha=0.4, linewidth=1)
    plt.plot(data['Sales'], range(len(data)), 'o', 
            markersize=10, color='#2ecc71', alpha=0.8)
    
    # Customize the plot
    plt.yticks(range(len(data)), data['Category'], fontsize=10)
    plt.xlabel('Sales ($ thousands)', fontsize=12)
    plt.title('Sales by Product Category', fontsize=14, pad=15)
    
    # Add value labels
    for i, v in enumerate(data['Sales']):
        plt.text(v + 5, i, f'${v:,.1f}k', 
                va='center', fontsize=9)
    
    # Customize grid and spines
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('棒棒糖图.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate and plot example
data = preprocess()
plot(data)

def plot_1(data):
    # 商务风格-蓝色渐变
    plt.style.use('seaborn-v0_8-white')
    plt.figure(figsize=(10, 6))
    
    colors = plt.cm.Blues(np.linspace(0.4, 0.8, len(data)))
    
    plt.hlines(y=range(len(data)), xmin=0, xmax=data['Sales'], 
              color='darkgrey', alpha=0.3, linewidth=2)
    
    for i in range(len(data)):
        plt.plot(data['Sales'].iloc[i], i, 'o', 
                markersize=12, color=colors[i], alpha=0.9)
    
    plt.yticks(range(len(data)), data['Category'], fontsize=10)
    plt.xlabel('Sales ($ thousands)', fontsize=11, color='#444444')
    plt.title('Sales by Product Category', fontsize=13, pad=15, color='#333333')
    
    for i, v in enumerate(data['Sales']):
        plt.text(v + 5, i, f'${v:,.1f}k', 
                va='center', fontsize=9, color='#666666')
    
    plt.grid(axis='x', linestyle=':', alpha=0.3)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('棒棒糖图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 活力风格-对比色
    plt.style.use('seaborn-v0_8')
    plt.figure(figsize=(10, 6), facecolor='#f8f9fa')
    
    plt.hlines(y=range(len(data)), xmin=0, xmax=data['Sales'], 
              color='#ff6b6b', alpha=0.4, linewidth=2, linestyle='--')
    plt.plot(data['Sales'], range(len(data)), 'o', 
            markersize=14, color='#4ecdc4', alpha=0.9)
    
    plt.yticks(range(len(data)), data['Category'], fontsize=10)
    plt.xlabel('Sales ($ thousands)', fontsize=11)
    plt.title('Sales by Product Category', fontsize=14, pad=15, color='#2c3e50')
    
    for i, v in enumerate(data['Sales']):
        plt.text(v + 5, i, f'${v:,.1f}k', 
                va='center', fontsize=10, color='#2c3e50',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
    
    plt.grid(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('棒棒糖图_style_2.png', dpi=300, bbox_inches='tight', facecolor='#f8f9fa')
    plt.close()

def plot_3(data):
    # 深色科技风
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6), facecolor='#1a1a1a')
    
    plt.hlines(y=range(len(data)), xmin=0, xmax=data['Sales'], 
              color='#404040', alpha=0.6, linewidth=1.5)
    plt.plot(data['Sales'], range(len(data)), '*', 
            markersize=15, color='#00ff88', alpha=0.9)
    
    plt.yticks(range(len(data)), data['Category'], fontsize=10, color='#ffffff')
    plt.xlabel('Sales ($ thousands)', fontsize=11, color='#ffffff')
    plt.title('Sales by Product Category', fontsize=14, pad=15, color='#ffffff')
    
    for i, v in enumerate(data['Sales']):
        plt.text(v + 5, i, f'${v:,.1f}k', 
                va='center', fontsize=9, color='#00ff88')
    
    plt.grid(axis='x', linestyle='--', alpha=0.2)
    
    plt.tight_layout()
    plt.savefig('棒棒糖图_style_3.png', dpi=300, bbox_inches='tight', facecolor='#1a1a1a')
    plt.close()

def plot_4(data):
    # 清新柔和风格
    plt.style.use('seaborn-v0_8-pastel')
    plt.figure(figsize=(10, 6))
    
    colors = plt.cm.RdYlBu(np.linspace(0.2, 0.8, len(data)))
    
    plt.hlines(y=range(len(data)), xmin=0, xmax=data['Sales'], 
              color='#cccccc', alpha=0.4, linewidth=3, linestyle='-')
    
    for i in range(len(data)):
        plt.plot(data['Sales'].iloc[i], i, 'D', 
                markersize=10, color=colors[i], alpha=0.7)
    
    plt.yticks(range(len(data)), data['Category'], fontsize=10)
    plt.xlabel('Sales ($ thousands)', fontsize=11)
    plt.title('Sales by Product Category', fontsize=14, pad=15)
    
    for i, v in enumerate(data['Sales']):
        plt.text(v + 5, i, f'${v:,.1f}k', 
                va='center', fontsize=9, color='#666666')
    
    plt.grid(axis='x', linestyle='-', alpha=0.1)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('棒棒糖图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 复古风格
    plt.style.use('seaborn-v0_8')
    plt.figure(figsize=(10, 6), facecolor='#f5f5dc')
    
    plt.hlines(y=range(len(data)), xmin=0, xmax=data['Sales'], 
              color='#8b4513', alpha=0.3, linewidth=2)
    plt.plot(data['Sales'], range(len(data)), 's', 
            markersize=8, color='#8b4513', alpha=0.8)
    
    plt.yticks(range(len(data)), data['Category'], fontsize=10, color='#654321')
    plt.xlabel('Sales ($ thousands)', fontsize=11, color='#654321')
    plt.title('Sales by Product Category', fontsize=14, pad=15, 
             color='#654321', fontstyle='italic')
    
    for i, v in enumerate(data['Sales']):
        plt.text(v + 5, i, f'${v:,.1f}k', 
                va='center', fontsize=9, color='#654321',
                fontstyle='italic')
    
    plt.grid(axis='x', linestyle=':', alpha=0.3, color='#8b4513')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('棒棒糖图_style_5.png', dpi=300, bbox_inches='tight', facecolor='#f5f5dc')
    plt.close()

data = preprocess()
# plot(data)
# plot_1(data)
# plot_2(data)
# plot_3(data)
plot_4(data)
plot_5(data)
