import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess(data=None):
    # Define economic indicators
    indicators = [
        'GDP Growth', 'Inflation', 'Unemployment',
        'Interest Rate', 'Trade Balance', 'Consumer Confidence',
        'Industrial Production', 'Stock Market Index'
    ]
    
    # Generate correlation matrix with some reasonable values
    np.random.seed(42)
    n = len(indicators)
    # Create a symmetric matrix with 1s on diagonal
    corr_matrix = np.eye(n)
    for i in range(n):
        for j in range(i+1, n):
            # Generate correlation between -1 and 1
            value = np.random.uniform(-0.8, 0.8)
            corr_matrix[i,j] = value
            corr_matrix[j,i] = value
    
    # Create DataFrame
    df = pd.DataFrame(corr_matrix, 
                     columns=indicators,
                     index=indicators)
    
    # Save to CSV
    df.to_csv('基础热力图.csv')
    return df

def plot(data):
    plt.figure(figsize=(10, 8))
    
    # Create heatmap
    sns.heatmap(data, 
                cmap='RdBu_r',
                vmin=-1, vmax=1,
                center=0,
                annot=True,
                fmt='.2f',
                square=True,
                cbar_kws={'label': 'Correlation Coefficient'})

    # Customize appearance
    plt.title('Correlation Matrix of Economic Indicators', 
             pad=20, 
             fontsize=14, 
             fontweight='bold')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    plt.savefig('基础热力图.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_1(data):
    plt.style.use('seaborn-v0_8')
    plt.figure(figsize=(12, 10))
    
    sns.heatmap(data, 
                cmap='viridis',
                vmin=-1, vmax=1,
                center=0,
                annot=True,
                fmt='.2f',
                square=True,
                annot_kws={'size': 8, 'color': 'white'},
                cbar_kws={'label': 'Correlation Coefficient'})

    plt.title('Correlation Matrix of Economic Indicators', 
             pad=20, 
             fontsize=16, 
             fontweight='bold',
             fontfamily='serif')
    
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    plt.tight_layout()
    plt.savefig('基础热力图_style1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 8))
    
    sns.heatmap(data, 
                cmap='magma',
                vmin=-1, vmax=1,
                center=0,
                annot=True,
                fmt='.2f',
                square=False,
                annot_kws={'size': 10, 'color': 'white'},
                cbar_kws={'label': 'Correlation', 'orientation': 'horizontal'})

    plt.title('Economic Indicators Correlation', 
             pad=20, 
             fontsize=14, 
             color='white')
    
    plt.tight_layout()
    plt.savefig('基础热力图_style2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    plt.style.use('default')
    plt.figure(figsize=(11, 9))
    
    mask = np.triu(np.ones_like(data))
    sns.heatmap(data, 
                cmap='YlOrRd',
                vmin=-1, vmax=1,
                center=0,
                annot=True,
                fmt='.2f',
                square=True,
                mask=mask,
                annot_kws={'size': 9},
                cbar_kws={'label': 'Correlation Coefficient', 'shrink': .8})

    plt.title('Economic Indicators\nCorrelation Matrix', 
             pad=20, 
             fontsize=15,
             fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('基础热力图_style3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 8))
    
    sns.heatmap(data, 
                cmap='coolwarm',
                vmin=-1, vmax=1,
                center=0,
                annot=True,
                fmt='.2f',
                square=True,
                linewidths=0.5,
                annot_kws={'size': 8},
                cbar_kws={'label': 'Correlation', 'pad': 0.01})

    plt.title('Correlation Analysis\nEconomic Indicators', 
             pad=20, 
             fontsize=14,
             fontfamily='sans-serif')
    
    plt.xticks(rotation=30, ha='right')
    plt.yticks(rotation=30)
    
    plt.tight_layout()
    plt.savefig('基础热力图_style4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    plt.style.use('bmh')
    plt.figure(figsize=(12, 10))
    
    sns.heatmap(data, 
                cmap='PuOr',
                vmin=-1, vmax=1,
                center=0,
                annot=True,
                fmt='.2f',
                square=True,
                linewidths=1,
                linecolor='white',
                annot_kws={'size': 10, 'weight': 'bold'},
                cbar_kws={'label': 'Correlation Coefficient', 'orientation': 'horizontal'})

    plt.title('Economic Indicators Correlation Matrix', 
             pad=20, 
             fontsize=16,
             fontweight='bold')
    
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('基础热力图_style5.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate and plot data
data = preprocess()
plot(data)
plot_1(data)
plot_3(data)
plot_4(data)
plot_5(data)
plot_2(data)
