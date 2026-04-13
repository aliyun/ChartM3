import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def preprocess(data=None):
    # Create sample monthly expense breakdown data
    categories = ['Base Income', 'Taxes', 'Rent', 'Utilities', 
                 'Groceries', 'Transportation', 'Insurance',
                 'Savings', 'Discretionary']
    
    values = [5000, -1000, -1800, -200, -600, -300, -200, -400, -500]
    
    # Create DataFrame
    df = pd.DataFrame({
        'Category': categories,
        'Value': values
    })
    
    # Calculate running total
    df['Total'] = df['Value'].cumsum()
    
    # Save to CSV
    df.to_csv('瀑布图.csv', index=False)
    return df

def plot(data):
    # Setup the plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Define colors
    colors = ['#2ecc71' if x >= 0 else '#e74c3c' for x in data['Value']]
    
    # Create the waterfall chart
    pos = range(len(data['Category']))
    
    # Plot bars
    for i in range(len(data['Category'])):
        if i == 0:
            # First bar starts from 0
            plt.bar(i, data['Value'][i], bottom=0, color=colors[i])
        else:
            # Other bars start from previous total
            plt.bar(i, data['Value'][i], bottom=data['Total'][i-1], color=colors[i])
    
    # Add connecting lines
    for i in range(len(data['Category'])-1):
        plt.plot([i, i+1], [data['Total'][i], data['Total'][i]], 
                color='gray', linestyle='--', alpha=0.5)
    
    # Customize appearance
    plt.xticks(pos, data['Category'], rotation=45, ha='right')
    plt.title('Monthly Income & Expense Breakdown', pad=20)
    plt.ylabel('Amount ($)')
    
    # Add value labels
    for i, v in enumerate(data['Value']):
        if i == 0:
            y = v/2
        else:
            y = data['Total'][i-1] + v/2
        plt.text(i, y, f'${abs(v):,}', ha='center', va='center')
    
    # Final formatting
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    
    # Save plot
    plt.savefig('瀑布图.png', dpi=300, bbox_inches='tight')
    plt.close()


def plot_1(data):
    # 商务蓝风格
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    colors = ['#1f77b4' if x >= 0 else '#ff7f0e' for x in data['Value']]
    pos = range(len(data['Category']))
    
    for i in range(len(data['Category'])):
        if i == 0:
            plt.bar(i, data['Value'][i], bottom=0, color=colors[i], 
                   edgecolor='white', linewidth=1)
        else:
            plt.bar(i, data['Value'][i], bottom=data['Total'][i-1], 
                   color=colors[i], edgecolor='white', linewidth=1)
    
    for i in range(len(data['Category'])-1):
        plt.plot([i, i+1], [data['Total'][i], data['Total'][i]], 
                color='gray', linestyle='-', alpha=0.3, linewidth=2)
    
    plt.xticks(pos, data['Category'], rotation=45, ha='right', fontsize=10)
    plt.title('Monthly Income & Expense Breakdown', pad=20, 
              fontsize=14, fontweight='bold')
    plt.ylabel('Amount ($)', fontsize=12)
    
    for i, v in enumerate(data['Value']):
        if i == 0:
            y = v/2
        else:
            y = data['Total'][i-1] + v/2
        plt.text(i, y, f'${abs(v):,}', ha='center', va='center',
                fontsize=9, fontweight='bold', color='white')
    
    plt.grid(True, alpha=0.2, axis='y')
    plt.tight_layout()
    plt.savefig('瀑布图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 环保绿色主题
    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    colors = ['#2ecc71' if x >= 0 else '#e74c3c' for x in data['Value']]
    pos = range(len(data['Category']))
    
    for i in range(len(data['Category'])):
        if i == 0:
            plt.bar(i, data['Value'][i], bottom=0, color=colors[i], alpha=0.7)
        else:
            plt.bar(i, data['Value'][i], bottom=data['Total'][i-1], 
                   color=colors[i], alpha=0.7)
    
    for i in range(len(data['Category'])-1):
        plt.plot([i, i+1], [data['Total'][i], data['Total'][i]], 
                color='darkgreen', linestyle=':', alpha=0.5)
    
    plt.xticks(pos, data['Category'], rotation=45, ha='right')
    plt.title('Monthly Income & Expense Breakdown', pad=20, 
              fontsize=16, color='darkgreen')
    plt.ylabel('Amount ($)')
    
    for i, v in enumerate(data['Value']):
        if i == 0:
            y = v/2
        else:
            y = data['Total'][i-1] + v/2
        plt.text(i, y, f'${abs(v):,}', ha='center', va='center',
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
    
    plt.grid(False)
    plt.tight_layout()
    plt.savefig('瀑布图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 现代简约风格
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='white')
    
    colors = ['#34495e' if x >= 0 else '#95a5a6' for x in data['Value']]
    pos = range(len(data['Category']))
    
    for i in range(len(data['Category'])):
        if i == 0:
            plt.bar(i, data['Value'][i], bottom=0, color=colors[i])
        else:
            plt.bar(i, data['Value'][i], bottom=data['Total'][i-1], 
                   color=colors[i])
    
    for i in range(len(data['Category'])-1):
        plt.plot([i, i+1], [data['Total'][i], data['Total'][i]], 
                color='black', linestyle='-', alpha=0.2, linewidth=1)
    
    plt.xticks(pos, data['Category'], rotation=45, ha='right', 
               fontsize=10, color='black')
    plt.title('Monthly Income & Expense Breakdown', pad=20, 
              fontsize=14, color='black')
    plt.ylabel('Amount ($)', color='black')
    
    for i, v in enumerate(data['Value']):
        if i == 0:
            y = v/2
        else:
            y = data['Total'][i-1] + v/2
        plt.text(i, y, f'${abs(v):,}', ha='center', va='center',
                color='white', fontweight='bold')
    
    plt.grid(True, alpha=0.1)
    plt.tight_layout()
    plt.savefig('瀑布图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 高对比度风格
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    colors = ['#00ff00' if x >= 0 else '#ff0000' for x in data['Value']]
    pos = range(len(data['Category']))
    
    for i in range(len(data['Category'])):
        if i == 0:
            plt.bar(i, data['Value'][i], bottom=0, color=colors[i], 
                   alpha=0.8)
        else:
            plt.bar(i, data['Value'][i], bottom=data['Total'][i-1], 
                   color=colors[i], alpha=0.8)
    
    for i in range(len(data['Category'])-1):
        plt.plot([i, i+1], [data['Total'][i], data['Total'][i]], 
                color='white', linestyle='--', alpha=0.3)
    
    plt.xticks(pos, data['Category'], rotation=45, ha='right', 
               color='white')
    plt.title('Monthly Income & Expense Breakdown', pad=20, 
              color='white', fontsize=14)
    plt.ylabel('Amount ($)', color='white')
    
    for i, v in enumerate(data['Value']):
        if i == 0:
            y = v/2
        else:
            y = data['Total'][i-1] + v/2
        plt.text(i, y, f'${abs(v):,}', ha='center', va='center',
                color='white', fontweight='bold')
    
    plt.grid(True, alpha=0.1)
    plt.tight_layout()
    plt.savefig('瀑布图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 柔和暖色调风格
    plt.style.use('seaborn-v0_8-pastel')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    colors = ['#f4a582' if x >= 0 else '#92c5de' for x in data['Value']]
    pos = range(len(data['Category']))
    
    for i in range(len(data['Category'])):
        if i == 0:
            plt.bar(i, data['Value'][i], bottom=0, color=colors[i], 
                   alpha=0.7)
        else:
            plt.bar(i, data['Value'][i], bottom=data['Total'][i-1], 
                   color=colors[i], alpha=0.7)
    
    for i in range(len(data['Category'])-1):
        plt.plot([i, i+1], [data['Total'][i], data['Total'][i]], 
                color='gray', linestyle='-.', alpha=0.4)
    
    plt.xticks(pos, data['Category'], rotation=45, ha='right', 
               fontsize=10)
    plt.title('Monthly Income & Expense Breakdown', pad=20, 
              fontsize=14, color='#555555')
    plt.ylabel('Amount ($)')
    
    for i, v in enumerate(data['Value']):
        if i == 0:
            y = v/2
        else:
            y = data['Total'][i-1] + v/2
        plt.text(i, y, f'${abs(v):,}', ha='center', va='center',
                color='#555555', fontweight='bold')
    
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.savefig('瀑布图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
# plot(data)
# plot_1(data)
# plot_2(data)
# plot_3(data)
# plot_4(data)
plot_5(data)
