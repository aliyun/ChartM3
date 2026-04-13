import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def preprocess(data=None):
    # Generate sample data if none provided
    categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Sports']
    years = [2020, 2021, 2022]
    
    # Create sample sales data
    np.random.seed(42)
    data = []
    for cat in categories:
        for year in years:
            sales = np.random.uniform(50, 200)
            data.append([cat, year, sales])
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Category', 'Year', 'Sales'])
    
    # Save to CSV
    df.to_csv('堆叠玫瑰图.csv', index=False)
    return df

def plot(data):
    # Set style
    plt.style.use('seaborn-v0_8')
    
    # Create figure
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='polar')
    
    # Process data for plotting
    categories = data['Category'].unique()
    years = sorted(data['Year'].unique())
    n_categories = len(categories)
    width = 2 * np.pi / n_categories
    
    # Color palette
    colors = plt.cm.Blues(np.linspace(0.4, 0.8, len(years)))
    
    # Plot bars
    for i, category in enumerate(categories):
        theta = i * width
        bottom = 0
        category_data = data[data['Category'] == category]
        
        for year, color in zip(years, colors):
            value = category_data[category_data['Year'] == year]['Sales'].values[0]
            ax.bar(theta, value, width=width*0.8, bottom=bottom, 
                  color=color, alpha=0.8, label=year if i == 0 else "")
            bottom += value
    
    # Customize plot
    ax.set_xticks(np.linspace(0, 2*np.pi, n_categories, endpoint=False))
    ax.set_xticklabels(categories)
    ax.set_title('Sales Performance by Category and Year', pad=20, size=14)
    
    # Add legend
    ax.legend(title='Year', bbox_to_anchor=(1.2, 0.5), loc='center')
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('堆叠玫瑰图.png', dpi=300, bbox_inches='tight')
    plt.close()

# Example usage

def plot_1(data):  # 商务风格
    plt.style.use('seaborn-v0_8-darkgrid')
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='polar')
    
    categories = data['Category'].unique()
    years = sorted(data['Year'].unique())
    n_categories = len(categories)
    width = 2 * np.pi / n_categories
    
    colors = ['#1f77b4', '#2c5985', '#3b3b6d']  # 专业蓝色渐变
    
    for i, category in enumerate(categories):
        theta = i * width
        bottom = 0
        category_data = data[data['Category'] == category]
        
        for year, color in zip(years, colors):
            value = category_data[category_data['Year'] == year]['Sales'].values[0]
            ax.bar(theta, value, width=width*0.8, bottom=bottom,
                  color=color, alpha=0.9, edgecolor='white', linewidth=0.5,
                  label=year if i == 0 else "")
            bottom += value
    
    ax.set_xticks(np.linspace(0, 2*np.pi, n_categories, endpoint=False))
    ax.set_xticklabels(categories, fontsize=10, fontweight='bold')
    ax.set_title('Sales Performance Analysis\n2020-2022', pad=20, size=14, fontweight='bold')
    
    ax.legend(title='Year', bbox_to_anchor=(1.2, 0.5), loc='center',
             frameon=True, edgecolor='gray')
    
    plt.tight_layout()
    plt.savefig('堆叠玫瑰图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):  # 极简风格
    plt.style.use('seaborn-v0_8-whitegrid')
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='polar')
    
    categories = data['Category'].unique()
    years = sorted(data['Year'].unique())
    n_categories = len(categories)
    width = 2 * np.pi / n_categories
    
    colors = ['#f0f0f0', '#bdbdbd', '#636363']  # 灰度渐变
    
    for i, category in enumerate(categories):
        theta = i * width
        bottom = 0
        category_data = data[data['Category'] == category]
        
        for year, color in zip(years, colors):
            value = category_data[category_data['Year'] == year]['Sales'].values[0]
            ax.bar(theta, value, width=width*0.8, bottom=bottom,
                  color=color, alpha=1, edgecolor='white', linewidth=0.8,
                  label=year if i == 0 else "")
            bottom += value
    
    ax.set_xticks(np.linspace(0, 2*np.pi, n_categories, endpoint=False))
    ax.set_xticklabels(categories, fontsize=9)
    ax.set_title('Sales Distribution', pad=20, size=12)
    
    ax.legend(title='Year', bbox_to_anchor=(1.15, 0.5), loc='center',
             frameon=False)
    
    plt.tight_layout()
    plt.savefig('堆叠玫瑰图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):  # 活泼风格
    plt.style.use('seaborn-v0_8')
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='polar')
    
    categories = data['Category'].unique()
    years = sorted(data['Year'].unique())
    n_categories = len(categories)
    width = 2 * np.pi / n_categories
    
    colors = ['#FF9999', '#66B2FF', '#99FF99']  # 明亮对比色
    
    for i, category in enumerate(categories):
        theta = i * width
        bottom = 0
        category_data = data[data['Category'] == category]
        
        for year, color in zip(years, colors):
            value = category_data[category_data['Year'] == year]['Sales'].values[0]
            ax.bar(theta, value, width=width*0.9, bottom=bottom,
                  color=color, alpha=0.7, edgecolor='white', linewidth=1,
                  label=year if i == 0 else "")
            bottom += value
    
    ax.set_xticks(np.linspace(0, 2*np.pi, n_categories, endpoint=False))
    ax.set_xticklabels(categories, fontsize=10)
    ax.set_title('Fun Sales Overview!', pad=20, size=14, color='#FF6B6B')
    
    ax.legend(title='Year', bbox_to_anchor=(1.2, 0.5), loc='center',
             frameon=True, facecolor='white', edgecolor='#FF6B6B')
    
    plt.tight_layout()
    plt.savefig('堆叠玫瑰图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):  # 复古风格
    plt.style.use('seaborn-v0_8-paper')
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='polar')
    
    categories = data['Category'].unique()
    years = sorted(data['Year'].unique())
    n_categories = len(categories)
    width = 2 * np.pi / n_categories
    
    colors = ['#8B4513', '#D2691E', '#DEB887']  # 复古棕色系
    
    for i, category in enumerate(categories):
        theta = i * width
        bottom = 0
        category_data = data[data['Category'] == category]
        
        for year, color in zip(years, colors):
            value = category_data[category_data['Year'] == year]['Sales'].values[0]
            ax.bar(theta, value, width=width*0.8, bottom=bottom,
                  color=color, alpha=0.8, edgecolor='#463E3F', linewidth=0.5,
                  label=year if i == 0 else "")
            bottom += value
    
    ax.set_xticks(np.linspace(0, 2*np.pi, n_categories, endpoint=False))
    ax.set_xticklabels(categories, fontsize=9, color='#463E3F')
    ax.set_title('Historical Sales Review', pad=20, size=14, color='#463E3F',
                 fontfamily='serif')
    
    ax.legend(title='Year', bbox_to_anchor=(1.15, 0.5), loc='center',
             frameon=True, facecolor='#FFF8DC')
    
    plt.tight_layout()
    plt.savefig('堆叠玫瑰图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):  # 科技风格
    plt.style.use('dark_background')
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='polar')
    
    categories = data['Category'].unique()
    years = sorted(data['Year'].unique())
    n_categories = len(categories)
    width = 2 * np.pi / n_categories
    
    colors = ['#00ffff', '#00ccff', '#0099ff']  # 霓虹蓝
    
    for i, category in enumerate(categories):
        theta = i * width
        bottom = 0
        category_data = data[data['Category'] == category]
        
        for year, color in zip(years, colors):
            value = category_data[category_data['Year'] == year]['Sales'].values[0]
            ax.bar(theta, value, width=width*0.8, bottom=bottom,
                  color=color, alpha=0.8, edgecolor='#ffffff', linewidth=0.5,
                  label=year if i == 0 else "")
            bottom += value
    
    ax.set_xticks(np.linspace(0, 2*np.pi, n_categories, endpoint=False))
    ax.set_xticklabels(categories, fontsize=10, color='#ffffff')
    ax.set_title('Sales Analytics Dashboard', pad=20, size=14, color='#00ffff')
    
    ax.legend(title='Year', bbox_to_anchor=(1.2, 0.5), loc='center',
             frameon=True, facecolor='black', edgecolor='#00ffff')
    
    plt.tight_layout()
    plt.savefig('堆叠玫瑰图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
