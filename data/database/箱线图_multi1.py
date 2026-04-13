import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess(data=None):
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate synthetic data for 4 different groups
    n_samples = 100
    
    group1 = np.random.normal(50, 10, n_samples)
    group2 = np.random.normal(65, 8, n_samples)
    group3 = np.random.normal(45, 12, n_samples)
    group4 = np.random.normal(55, 15, n_samples)
    
    # Add some controlled outliers
    group1[0] = 90
    group2[-1] = 30
    group3[50] = 85
    group4[75] = 15
    
    # Create DataFrame
    df = pd.DataFrame({
        'Group A': group1,
        'Group B': group2,
        'Group C': group3,
        'Group D': group4
    })
    
    # Melt the DataFrame for seaborn
    df_melted = df.melt(var_name='Group', value_name='Value')
    
    # Round values to 1 decimal place
    df_melted['Value'] = df_melted['Value'].round(1)
    
    # Save to CSV
    df_melted.to_csv('箱线图.csv', index=False)
    return df_melted

def plot(data):
    # Set style
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Create box plot
    box_plot = sns.boxplot(
        data=data,
        x='Group',
        y='Value',
        palette='Set3',
        width=0.7,
        showfliers=False,
        fliersize=8
    )
    
    # Add strip plot to show actual points
    sns.stripplot(
        data=data,
        x='Group',
        y='Value',
        color='gray',
        alpha=0.4,
        size=4,
        jitter=0.2
    )
    
    # Customize plot
    plt.title('Distribution of Values by Group', pad=15, size=14, fontweight='bold')
    plt.xlabel('Group', labelpad=10, size=12)
    plt.ylabel('Value', labelpad=10, size=12)
    
    # Add statistical annotations
    for i in range(len(data['Group'].unique())):
        group_data = data[data['Group'] == data['Group'].unique()[i]]['Value']
        median = group_data.median()
        q1 = group_data.quantile(0.25)
        q3 = group_data.quantile(0.75)
        
        # Add median value annotation
        plt.text(i, median, f'M:{median:.1f}', 
                horizontalalignment='center',
                verticalalignment='bottom',
                fontsize=10)
        
        # Add Q1 and Q3 annotations
        plt.text(i-0.2, q1, f'Q1:{q1:.1f}', 
                horizontalalignment='right',
                verticalalignment='center',
                fontsize=8)
        plt.text(i+0.2, q3, f'Q3:{q3:.1f}',
                horizontalalignment='left',
                verticalalignment='center',
                fontsize=8)

    # Customize grid
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    plt.savefig('箱线图.png', dpi=300, bbox_inches='tight')
    plt.close()

# Execute the functions

def plot_1(data):
    # 专业商务风格
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.figure(figsize=(10, 6))
    
    colors = ['#1f77b4', '#2c3e50', '#34495e', '#2980b9']
    box_plot = sns.boxplot(data=data, x='Group', y='Value',
                          palette=colors, width=0.5,
                          showfliers=True)
    
    sns.stripplot(data=data, x='Group', y='Value',
                  color='#7f8c8d', alpha=0.3, size=4)
    
    plt.title('Value Distribution Analysis', pad=15,
              fontname='Arial', fontsize=14, fontweight='bold')
    plt.xlabel('Business Units', labelpad=10, fontsize=12)
    plt.ylabel('Performance Metrics', labelpad=10, fontsize=12)
    
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('箱线图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 清新自然风格
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    colors = ['#a8e6cf', '#dcedc1', '#ffd3b6', '#ffaaa5']
    box_plot = sns.boxplot(data=data, x='Group', y='Value',
                          palette=colors, width=0.6,
                          showfliers=False)
    
    sns.stripplot(data=data, x='Group', y='Value',
                  color='#79bd9a', alpha=0.4, size=5)
    
    plt.title('Natural Distribution View', pad=15,
              fontname='Verdana', fontsize=14)
    plt.xlabel('Categories', labelpad=10, fontsize=11)
    plt.ylabel('Values', labelpad=10, fontsize=11)
    
    plt.grid(True, linestyle='-', alpha=0.2)
    plt.tight_layout()
    plt.savefig('箱线图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 现代科技风格
    sns.set_style("dark")
    plt.figure(figsize=(10, 6))
    
    colors = ['#00b4d8', '#0077b6', '#023e8a', '#03045e']
    box_plot = sns.boxplot(data=data, x='Group', y='Value',
                          palette=colors, width=0.4,
                          showfliers=True)
    
    sns.stripplot(data=data, x='Group', y='Value',
                  color='#90e0ef', alpha=0.5, size=4, marker='D')
    
    plt.title('Tech Distribution Dashboard', pad=15,
              fontname='Courier New', fontsize=14, fontweight='bold')
    plt.xlabel('Segments', labelpad=10, fontsize=12)
    plt.ylabel('Metrics', labelpad=10, fontsize=12)
    
    plt.grid(True, linestyle=':', alpha=0.4)
    plt.tight_layout()
    plt.savefig('箱线图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 活泼明快风格
    sns.set_style("white")
    plt.figure(figsize=(10, 6))
    
    colors = ['#FF9AA2', '#FFB7B2', '#FFDAC1', '#E2F0CB']
    box_plot = sns.boxplot(data=data, x='Group', y='Value',
                          palette=colors, width=0.7,
                          showfliers=True)
    
    sns.stripplot(data=data, x='Group', y='Value',
                  color='#B5EAD7', alpha=0.6, size=6, marker='o')
    
    plt.title('Fun Distribution View! 🎈', pad=15,
              fontname='Comic Sans MS', fontsize=14)
    plt.xlabel('Fun Groups', labelpad=10, fontsize=12)
    plt.ylabel('Happy Values', labelpad=10, fontsize=12)
    
    plt.grid(False)
    plt.tight_layout()
    plt.savefig('箱线图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 极简黑白风格
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    colors = ['#f8f9fa', '#e9ecef', '#dee2e6', '#ced4da']
    box_plot = sns.boxplot(data=data, x='Group', y='Value',
                          palette=colors, width=0.5,
                          showfliers=False)
    
    sns.stripplot(data=data, x='Group', y='Value',
                  color='black', alpha=0.2, size=3)
    
    plt.title('Minimalist Distribution', pad=15,
              fontname='Helvetica', fontsize=14, fontweight='light')
    plt.xlabel('Groups', labelpad=10, fontsize=10)
    plt.ylabel('Values', labelpad=10, fontsize=10)
    
    plt.grid(True, linestyle='-', alpha=0.1)
    plt.tight_layout()
    plt.savefig('箱线图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
