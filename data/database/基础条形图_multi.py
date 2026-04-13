import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

def preprocess(data=None):
    # Create sample data about global technology platform usage
    data = pd.DataFrame({
        'Platform': ['Facebook', 'WhatsApp', 'Instagram', 'TikTok', 'Twitter', 'LinkedIn'],
        'Usage_Percentage': [65, 62, 40, 35, 25, 20]
    })
    
    # Sort by percentage descending
    data = data.sort_values('Usage_Percentage', ascending=True)
    
    # Save to CSV
    data.to_csv('基础条形图.csv', index=False)
    return data

def plot(data):
    # Set style and figure size
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Create horizontal bar plot
    ax = sns.barplot(x='Usage_Percentage', 
                     y='Platform', 
                     data=data,
                     color='#4682B4')
    
    # Customize the plot
    plt.title('Global Social Media Platform Usage 2023', 
             pad=20, 
             fontsize=14, 
             fontweight='bold')
    plt.xlabel('Usage Percentage (%)', fontsize=12)
    plt.ylabel('Platform', fontsize=12)
    
    # Add value labels on bars
    for i in ax.containers:
        ax.bar_label(i, fmt='%.0f%%', padding=5)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('基础条形图.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_1(data):
    # 现代简约风格，使用渐变色
    sns.set_style("white")
    plt.figure(figsize=(12, 7))
    
    colors = sns.color_palette("Blues", n_colors=len(data))
    ax = sns.barplot(x='Usage_Percentage', 
                     y='Platform', 
                     data=data,
                     palette=colors)
    
    plt.title('Global Social Media Platform Usage 2023', 
             pad=20, 
             fontsize=16, 
             fontweight='bold',
             fontfamily='sans-serif')
    plt.xlabel('Usage Percentage (%)', fontsize=12)
    plt.ylabel('Platform', fontsize=12)
    
    # 移除边框
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    for i in ax.containers:
        ax.bar_label(i, fmt='%.0f%%', padding=5)
    
    plt.tight_layout()
    plt.savefig('基础条形图_style1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 复古风格，使用暖色调
    sns.set_style("darkgrid")
    plt.figure(figsize=(10, 6))
    
    ax = sns.barplot(x='Usage_Percentage', 
                     y='Platform', 
                     data=data,
                     color='#D4A373',
                     edgecolor='#A98467',
                     linewidth=1)
    
    plt.title('Global Social Media Platform Usage\n2023', 
             pad=20, 
             fontsize=14, 
             fontfamily='serif',
             color='#6B4423')
    plt.xlabel('Usage Percentage (%)', fontsize=10, fontfamily='serif')
    plt.ylabel('Platform', fontsize=10, fontfamily='serif')
    
    for i in ax.containers:
        ax.bar_label(i, fmt='%.0f%%', padding=5, fontfamily='serif')
    
    plt.tight_layout()
    plt.savefig('基础条形图_style2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 商务风格，使用垂直条形图
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    
    ax = sns.barplot(x='Platform', 
                     y='Usage_Percentage', 
                     data=data.sort_values('Usage_Percentage', ascending=False),
                     color='#2B4570',
                     width=0.6)
    
    plt.title('Global Social Media Platform Usage 2023', 
             pad=20, 
             fontsize=14, 
             fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('')
    plt.ylabel('Usage Percentage (%)', fontsize=10)
    
    # 添加参考线
    plt.axhline(y=50, color='red', linestyle='--', alpha=0.3)
    
    for i in ax.containers:
        ax.bar_label(i, fmt='%.0f%%', padding=5)
    
    plt.tight_layout()
    plt.savefig('基础条形图_style3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 高对比度风格
    sns.set_style("dark")
    plt.figure(figsize=(10, 6))
    
    ax = sns.barplot(x='Usage_Percentage', 
                     y='Platform', 
                     data=data,
                     palette=sns.color_palette("husl", len(data)))
    
    plt.title('GLOBAL SOCIAL MEDIA USAGE', 
             pad=20, 
             fontsize=16, 
             fontweight='bold',
             loc='left')
    plt.xlabel('Usage Percentage (%)', fontsize=12)
    plt.ylabel('Platform', fontsize=12)
    
    # 添加百分比标签
    for i in ax.containers:
        ax.bar_label(i, fmt='%.0f%%', padding=5, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('基础条形图_style4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 极简风格
    sns.set_style("white")
    plt.figure(figsize=(10, 6))
    
    ax = sns.barplot(x='Usage_Percentage', 
                     y='Platform', 
                     data=data,
                     color='lightgray',
                     edgecolor='black',
                     linewidth=1)
    
    plt.title('Social Media Platform Usage', 
             pad=20, 
             fontsize=14, 
             fontfamily='sans-serif')
    plt.xlabel('')
    plt.ylabel('')
    
    # 移除所有边框
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    # 移除网格线
    ax.grid(False)
    
    # 在条形末端添加标签
    for i in ax.containers:
        ax.bar_label(i, fmt='%.0f%%', padding=5)
    
    plt.tight_layout()
    plt.savefig('基础条形图_style5.png', dpi=300, bbox_inches='tight')
    plt.close()


# Execute the functions
data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
