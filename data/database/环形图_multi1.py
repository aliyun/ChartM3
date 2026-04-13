import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def preprocess(data=None):
    # Create sample monthly expense data
    expenses = {
        'Category': ['Housing', 'Food', 'Transport', 'Utilities', 
                    'Healthcare', 'Entertainment'],
        'Amount': [1500, 800, 400, 300, 200, 300]
    }
    
    df = pd.DataFrame(expenses)
    # Calculate percentages
    df['Percentage'] = df['Amount'] / df['Amount'].sum() * 100
    
    # Save to CSV
    df.to_csv('环形图.csv', index=False)
    return df

def plot(data):
    # Set style
    plt.style.use('seaborn-v0_8')
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Color palette
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ff99cc','#99ffcc']
    
    # Create donut chart
    wedges, texts, autotexts = ax.pie(data['Percentage'], 
                                     labels=data['Category'],
                                     colors=colors,
                                     autopct='%1.1f%%',
                                     pctdistance=0.85,
                                     wedgeprops=dict(width=0.5))
    
    # Add center text
    total = f'Total\n${data["Amount"].sum():,.0f}'
    plt.text(0, 0, total, ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Customize text properties
    plt.setp(autotexts, size=9, weight="bold")
    plt.setp(texts, size=10)
    
    # Add title
    plt.title('Monthly Household Expenses Distribution', pad=20, size=14, fontweight='bold')
    
    # Add legend
    plt.legend(data['Category'], 
              title="Categories",
              loc="upper left",
              bbox_to_anchor=(1, 0, 0.5, 1))
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('环形图.png', bbox_inches='tight', dpi=300)
    plt.close()


def plot_1(data):
    # 商务蓝色主题
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(10, 8))
    
    blues = ['#1f77b4', '#3186bc', '#4394c3', '#54a3cc', '#65b1d4', '#76c0dd']
    
    wedges, texts, autotexts = ax.pie(data['Percentage'], 
                                     labels=data['Category'],
                                     colors=blues,
                                     autopct='%1.1f%%',
                                     pctdistance=0.85,
                                     wedgeprops=dict(width=0.5, edgecolor='white', linewidth=2))
    
    total = f'Total\n${data["Amount"].sum():,.0f}'
    plt.text(0, 0, total, ha='center', va='center', fontsize=12, fontweight='bold')
    
    plt.setp(autotexts, size=9, weight="bold", color='white')
    plt.setp(texts, size=10)
    
    plt.title('Business Expense Analysis', pad=20, size=14, fontweight='bold')
    plt.legend(data['Category'], title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.savefig('环形图_style_1.png', bbox_inches='tight', dpi=300)
    plt.close()

def plot_2(data):
    # 极简黑白主题
    plt.style.use('seaborn-v0_8-white')
    fig, ax = plt.subplots(figsize=(10, 8))
    
    grays = ['#333333', '#4d4d4d', '#666666', '#808080', '#999999', '#b3b3b3']
    
    wedges, texts, autotexts = ax.pie(data['Percentage'], 
                                     labels=data['Category'],
                                     colors=grays,
                                     autopct='%1.1f%%',
                                     pctdistance=0.75,
                                     wedgeprops=dict(width=0.3, edgecolor='white'))
    
    total = f'Total\n${data["Amount"].sum():,.0f}'
    plt.text(0, 0, total, ha='center', va='center', fontsize=12)
    
    plt.setp(autotexts, size=8)
    plt.setp(texts, size=9)
    
    plt.title('Minimalist Expense Overview', pad=20, size=12)
    plt.legend(data['Category'], title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.savefig('环形图_style_2.png', bbox_inches='tight', dpi=300)
    plt.close()

def plot_3(data):
    # 活泼多彩主题
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD', '#FFD93D']
    
    wedges, texts, autotexts = ax.pie(data['Percentage'], 
                                     labels=data['Category'],
                                     colors=colors,
                                     autopct='%1.1f%%',
                                     pctdistance=0.85,
                                     explode=[0.05]*len(data),
                                     wedgeprops=dict(width=0.6))
    
    total = f'Total\n${data["Amount"].sum():,.0f}'
    plt.text(0, 0, total, ha='center', va='center', fontsize=14, fontweight='bold')
    
    plt.setp(autotexts, size=10, weight="bold")
    plt.setp(texts, size=11)
    
    plt.title('Fun Budget Distribution!', pad=20, size=16, fontweight='bold')
    plt.legend(data['Category'], title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.savefig('环形图_style_3.png', bbox_inches='tight', dpi=300)
    plt.close()

def plot_4(data):
    # 自然绿色主题
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(10, 8))
    
    greens = ['#2d5a27', '#387c5c', '#449c71', '#4fbc85', '#5adc9a', '#65fcaf']
    
    wedges, texts, autotexts = ax.pie(data['Percentage'], 
                                     labels=data['Category'],
                                     colors=greens,
                                     autopct='%1.1f%%',
                                     pctdistance=0.8,
                                     wedgeprops=dict(width=0.4, alpha=0.8))
    
    total = f'Total\n${data["Amount"].sum():,.0f}'
    plt.text(0, 0, total, ha='center', va='center', fontsize=12, color='#2d5a27')
    
    plt.setp(autotexts, size=9, color='white')
    plt.setp(texts, size=10, color='#2d5a27')
    
    plt.title('Eco-friendly Budget Report', pad=20, size=14, color='#2d5a27')
    plt.legend(data['Category'], title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.savefig('环形图_style_4.png', bbox_inches='tight', dpi=300)
    plt.close()

def plot_5(data):
    # 复古暖色主题
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(10, 8))
    
    vintage_colors = ['#8B4513', '#DEB887', '#D2691E', '#F4A460', '#CD853F', '#DAA520']
    
    wedges, texts, autotexts = ax.pie(data['Percentage'], 
                                     labels=data['Category'],
                                     colors=vintage_colors,
                                     autopct='%1.1f%%',
                                     pctdistance=0.75,
                                     wedgeprops=dict(width=0.55, edgecolor='wheat', linewidth=2))
    
    total = f'Total\n${data["Amount"].sum():,.0f}'
    plt.text(0, 0, total, ha='center', va='center', fontsize=12, color='#8B4513')
    
    plt.setp(autotexts, size=9, color='white')
    plt.setp(texts, size=10, color='#8B4513')
    
    plt.title('Vintage Expense Summary', pad=20, size=14, color='#8B4513', fontweight='bold')
    plt.legend(data['Category'], title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    
    plt.tight_layout()
    plt.savefig('环形图_style_5.png', bbox_inches='tight', dpi=300)
    plt.close()

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
