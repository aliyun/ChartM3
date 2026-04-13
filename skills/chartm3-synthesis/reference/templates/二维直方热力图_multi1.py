import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def preprocess(n_points=10000):
    # Generate correlated normal data
    np.random.seed(42)
    mean = [0, 0]
    cov = [[1, 0.5], [0.5, 1]]
    x, y = np.random.multivariate_normal(mean, cov, n_points).T
    
    # Create DataFrame
    data = pd.DataFrame({
        'x': x,
        'y': y
    })
    
    # Save to CSV
    data.to_csv('二维直方热力图.csv', index=False)
    return data

def plot(data):
    # Set style
    plt.style.use('seaborn-v0_8')
    
    # Create figure
    plt.figure(figsize=(10, 8))
    
    # Create 2D histogram
    hist = plt.hist2d(data['x'], data['y'], 
                     bins=50,
                     cmap='viridis',
                     density=True)
    
    # Add colorbar
    plt.colorbar(hist[3], label='Density')
    
    # Customize plot
    plt.title('2D Histogram Heatmap of Bivariate Normal Distribution', 
             pad=20, fontsize=12)
    plt.xlabel('X Variable', fontsize=10)
    plt.ylabel('Y Variable', fontsize=10)
    
    # Add grid
    plt.grid(True, alpha=0.3)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    plt.savefig('二维直方热力图.png', dpi=300, bbox_inches='tight')
    plt.close()


def plot_1(data):
    # 现代简约风格
    plt.style.use('seaborn-v0_8-white')
    plt.figure(figsize=(10, 8))
    
    hist = plt.hist2d(data['x'], data['y'], 
                     bins=40,
                     cmap='YlOrRd',
                     density=True)
    
    cbar = plt.colorbar(hist[3])
    cbar.set_label('Density', rotation=270, labelpad=15)
    
    plt.title('Minimalist Distribution View', 
             pad=20, fontsize=14, fontweight='bold')
    plt.xlabel('X Variable', fontsize=12)
    plt.ylabel('Y Variable', fontsize=12)
    
    plt.grid(False)
    plt.tight_layout()
    plt.savefig('二维直方热力图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 商务深色风格
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 8))
    
    hist = plt.hist2d(data['x'], data['y'], 
                     bins=50,
                     cmap='magma',
                     density=True)
    
    cbar = plt.colorbar(hist[3])
    cbar.set_label('Density', color='white')
    
    plt.title('Business Analytics View', 
             color='white', pad=20, fontsize=14)
    plt.xlabel('X Variable', color='white', fontsize=12)
    plt.ylabel('Y Variable', color='white', fontsize=12)
    
    plt.grid(True, alpha=0.2)
    plt.tight_layout()
    plt.savefig('二维直方热力图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 学术风格
    plt.style.use('seaborn-v0_8-paper')
    plt.figure(figsize=(10, 8))
    
    hist = plt.hist2d(data['x'], data['y'], 
                     bins=60,
                     cmap='Blues',
                     density=True)
    
    cbar = plt.colorbar(hist[3], location='right', pad=0.02)
    cbar.set_label('Density', rotation=270, labelpad=15)
    
    plt.title('Academic Distribution Analysis', 
             pad=20, fontsize=12, fontfamily='serif')
    plt.xlabel('X Variable', fontsize=10, fontfamily='serif')
    plt.ylabel('Y Variable', fontsize=10, fontfamily='serif')
    
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('二维直方热力图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 活泼色彩风格
    plt.style.use('seaborn-v0_8-bright')
    plt.figure(figsize=(10, 8))
    
    hist = plt.hist2d(data['x'], data['y'], 
                     bins=45,
                     cmap='rainbow',
                     density=True)
    
    cbar = plt.colorbar(hist[3])
    cbar.set_label('Density', rotation=270, labelpad=15)
    
    plt.title('Vibrant Distribution Pattern', 
             pad=20, fontsize=14, color='purple')
    plt.xlabel('X Variable', fontsize=12, color='navy')
    plt.ylabel('Y Variable', fontsize=12, color='navy')
    
    plt.grid(True, linestyle=':', alpha=0.4)
    plt.tight_layout()
    plt.savefig('二维直方热力图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 专业分析风格
    plt.style.use('default')
    plt.figure(figsize=(10, 8), facecolor='#f0f0f0')
    
    hist = plt.hist2d(data['x'], data['y'], 
                     bins=55,
                     cmap='plasma',
                     density=True)
    
    cbar = plt.colorbar(hist[3], pad=0.02)
    cbar.set_label('Density', rotation=270, labelpad=15)
    
    plt.title('Professional Distribution Analysis', 
             pad=20, fontsize=14, fontweight='bold')
    plt.xlabel('X Variable', fontsize=12)
    plt.ylabel('Y Variable', fontsize=12)
    
    plt.grid(True, linestyle='-', alpha=0.2)
    ax = plt.gca()
    ax.set_facecolor('white')
    plt.tight_layout()
    plt.savefig('二维直方热力图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
# plot(data)
# plot_1(data)
# plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
