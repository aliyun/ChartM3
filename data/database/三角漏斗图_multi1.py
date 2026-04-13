import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Polygon

def preprocess(data=None):
    """
    Generate and preprocess funnel chart data
    """
    if data is None:
        data = {
            'stage': ['Leads', 'Prospects', 'Opportunities', 'Proposals', 'Deals'],
            'value': [1000, 750, 400, 150, 50]
        }
        df = pd.DataFrame(data)
    else:
        df = data.copy()
    
    # Calculate conversion rates
    df['conv_rate'] = df['value'].pct_change() * 100
    df['total_conv'] = df['value'] / df['value'].iloc[0] * 100
    
    # Format percentages
    df['conv_rate'] = df['conv_rate'].round(1)
    df['total_conv'] = df['total_conv'].round(1)
    
    df.to_csv('三角漏斗图.csv', index=False)
    return df

def get_trapezoid_coords(y_bottom, y_top, x_top, x_bottom):
    """Calculate coordinates for a trapezoid"""
    return np.array([
        [-x_top/2, y_top],     # top left
        [x_top/2, y_top],      # top right
        [x_bottom/2, y_bottom],# bottom right
        [-x_bottom/2, y_bottom] # bottom left
    ])

def plot(data):
    """
    Create rectangular funnel chart with trapezoids
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Configuration
    n_stages = len(data)
    total_height = 10
    stage_height = total_height / n_stages
    max_width = 8
    colors = plt.cm.Blues(np.linspace(0.4, 0.8, n_stages))
    
    # Calculate widths proportional to values
    max_value = data['value'].iloc[0]
    widths = data['value'] / max_value * max_width
    
    # Plot trapezoids
    for i in range(n_stages):
        y_bottom = total_height - (i + 1) * stage_height
        y_top = total_height - i * stage_height
        
        # Get trapezoid coordinates
        if i == n_stages - 1:  # Last stage
            coords = get_trapezoid_coords(y_bottom, y_top, widths.iloc[i], widths.iloc[i])
        else:
            coords = get_trapezoid_coords(y_bottom, y_top, widths.iloc[i], widths.iloc[i+1])
        
        # Create and add trapezoid
        trapezoid = Polygon(
            coords, 
            facecolor=colors[i], 
            edgecolor='white',
            alpha=0.9
        )
        ax.add_patch(trapezoid)
        
        # Add stage labels on the left
        ax.text(
            -max_width/1.8, 
            (y_top + y_bottom)/2,
            f"{data['stage'].iloc[i]}",
            ha='right',
            va='center',
            fontsize=10
        )
        
        # Add values in the middle of trapezoid
        ax.text(
            0,
            (y_top + y_bottom)/2,
            f"{data['value'].iloc[i]:,}",
            ha='center',
            va='center',
            fontsize=10,
            color='white',
            fontweight='bold'
        )
        
        # Add conversion rates on the right
        if i > 0:
            ax.text(
                max_width/1.8,
                (y_top + y_bottom)/2,
                f"Conv: {data['conv_rate'].iloc[i]}%\nTotal: {data['total_conv'].iloc[i]}%",
                ha='left',
                va='center',
                fontsize=8
            )
    
    # Configure plot
    ax.set_xlim(-max_width, max_width)
    ax.set_ylim(0, total_height)
    
    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Add title
    plt.title('Sales Pipeline Conversion Funnel', pad=20, fontsize=14)
    
    # Save plot
    plt.tight_layout()
    plt.savefig('三角漏斗图.png', dpi=300, bbox_inches='tight')
    return fig

# Example usage

def plot_1(data):
    """Modern Business Style"""
    fig, ax = plt.subplots(figsize=(10, 8))
    n_stages = len(data)
    total_height = 10
    stage_height = total_height / n_stages
    max_width = 8
    
    # 使用商务蓝色渐变
    colors = plt.cm.GnBu(np.linspace(0.3, 0.9, n_stages))
    
    max_value = data['value'].iloc[0]
    widths = data['value'] / max_value * max_width
    
    for i in range(n_stages):
        y_bottom = total_height - (i + 1) * stage_height
        y_top = total_height - i * stage_height
        
        if i == n_stages - 1:
            coords = get_trapezoid_coords(y_bottom, y_top, widths.iloc[i], widths.iloc[i])
        else:
            coords = get_trapezoid_coords(y_bottom, y_top, widths.iloc[i], widths.iloc[i+1])
        
        trapezoid = Polygon(
            coords,
            facecolor=colors[i],
            edgecolor='white',
            alpha=0.9,
            linewidth=2
        )
        ax.add_patch(trapezoid)
        
        ax.text(
            -max_width/1.8,
            (y_top + y_bottom)/2,
            f"{data['stage'].iloc[i]}",
            ha='right',
            va='center',
            fontsize=11,
            fontweight='bold',
            fontfamily='Arial'
        )
        
        ax.text(
            0,
            (y_top + y_bottom)/2,
            f"{data['value'].iloc[i]:,}",
            ha='center',
            va='center',
            fontsize=11,
            color='white',
            fontweight='bold',
            fontfamily='Arial'
        )
        
        if i > 0:
            ax.text(
                max_width/1.8,
                (y_top + y_bottom)/2,
                f"Conv: {data['conv_rate'].iloc[i]}%\nTotal: {data['total_conv'].iloc[i]}%",
                ha='left',
                va='center',
                fontsize=9,
                fontfamily='Arial'
            )
    
    ax.set_xlim(-max_width, max_width)
    ax.set_ylim(0, total_height)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    plt.title('Sales Pipeline Conversion Funnel', pad=20, fontsize=14, fontweight='bold', fontfamily='Arial')
    plt.tight_layout()
    plt.savefig('三角漏斗图_style_1.png', dpi=300, bbox_inches='tight')
    return fig

def plot_2(data):
    """Minimalist Style"""
    fig, ax = plt.subplots(figsize=(10, 8), facecolor='#f5f5f5')
    ax.set_facecolor('#f5f5f5')
    
    n_stages = len(data)
    total_height = 10
    stage_height = total_height / n_stages
    max_width = 8
    
    # 使用单色灰度
    colors = plt.cm.Greys(np.linspace(0.3, 0.7, n_stages))
    
    max_value = data['value'].iloc[0]
    widths = data['value'] / max_value * max_width
    
    for i in range(n_stages):
        y_bottom = total_height - (i + 1) * stage_height
        y_top = total_height - i * stage_height
        
        if i == n_stages - 1:
            coords = get_trapezoid_coords(y_bottom, y_top, widths.iloc[i], widths.iloc[i])
        else:
            coords = get_trapezoid_coords(y_bottom, y_top, widths.iloc[i], widths.iloc[i+1])
            
        trapezoid = Polygon(
            coords,
            facecolor=colors[i],
            edgecolor='none',
            alpha=0.8
        )
        ax.add_patch(trapezoid)
        
        ax.text(
            -max_width/1.8,
            (y_top + y_bottom)/2,
            f"{data['stage'].iloc[i]}",
            ha='right',
            va='center',
            fontsize=10,
            color='#404040',
            fontfamily='Arial'
        )
        
        ax.text(
            0,
            (y_top + y_bottom)/2,
            f"{data['value'].iloc[i]:,}",
            ha='center',
            va='center',
            fontsize=10,
            color='white',
            fontfamily='Arial'
        )
        
        if i > 0:
            ax.text(
                max_width/1.8,
                (y_top + y_bottom)/2,
                f"{data['conv_rate'].iloc[i]}%",
                ha='left',
                va='center',
                fontsize=9,
                color='#404040',
                fontfamily='Arial'
            )
    
    ax.set_xlim(-max_width, max_width)
    ax.set_ylim(0, total_height)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    plt.title('Conversion Funnel', pad=20, fontsize=14, color='#404040', fontfamily='Arial')
    plt.tight_layout()
    plt.savefig('三角漏斗图_style_2.png', dpi=300, bbox_inches='tight', facecolor='#f5f5f5')
    return fig

def plot_3(data):
    """Vibrant Style"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    n_stages = len(data)
    total_height = 10
    stage_height = total_height / n_stages
    max_width = 8
    
    # 使用彩虹色系
    colors = plt.cm.rainbow(np.linspace(0, 1, n_stages))
    
    max_value = data['value'].iloc[0]
    widths = data['value'] / max_value * max_width
    
    for i in range(n_stages):
        y_bottom = total_height - (i + 1) * stage_height
        y_top = total_height - i * stage_height
        
        if i == n_stages - 1:
            coords = get_trapezoid_coords(y_bottom, y_top, widths.iloc[i], widths.iloc[i])
        else:
            coords = get_trapezoid_coords(y_bottom, y_top, widths.iloc[i], widths.iloc[i+1])
            
        trapezoid = Polygon(
            coords,
            facecolor=colors[i],
            edgecolor='white',
            alpha=1,
            linewidth=2
        )
        ax.add_patch(trapezoid)
        
        ax.text(
            -max_width/1.8,
            (y_top + y_bottom)/2,
            f"{data['stage'].iloc[i]}",
            ha='right',
            va='center',
            fontsize=11,
            fontweight='bold'
        )
        
        ax.text(
            0,
            (y_top + y_bottom)/2,
            f"{data['value'].iloc[i]:,}",
            ha='center',
            va='center',
            fontsize=11,
            color='white',
            fontweight='bold'
        )
        
        if i > 0:
            ax.text(
                max_width/1.8,
                (y_top + y_bottom)/2,
                f"↓ {data['conv_rate'].iloc[i]}%",
                ha='left',
                va='center',
                fontsize=10,
                fontweight='bold'
            )
    
    ax.set_xlim(-max_width, max_width)
    ax.set_ylim(0, total_height)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    plt.title('Fun Sales Funnel', pad=20, fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('三角漏斗图_style_3.png', dpi=300, bbox_inches='tight')
    return fig

def plot_4(data):
    """Dark Tech Style"""
    fig, ax = plt.subplots(figsize=(10, 8), facecolor='#1a1a1a')
    ax.set_facecolor('#1a1a1a')
    
    n_stages = len(data)
    total_height = 10
    stage_height = total_height / n_stages
    max_width = 8
    
    # 使用霓虹蓝色系
    colors = plt.cm.plasma(np.linspace(0.2, 0.8, n_stages))
    
    max_value = data['value'].iloc[0]
    widths = data['value'] / max_value * max_width
    
    for i in range(n_stages):
        y_bottom = total_height - (i + 1) * stage_height
        y_top = total_height - i * stage_height
        
        if i == n_stages - 1:
            coords = get_trapezoid_coords(y_bottom, y_top, widths.iloc[i], widths.iloc[i])
        else:
            coords = get_trapezoid_coords(y_bottom, y_top, widths.iloc[i], widths.iloc[i+1])
            
        trapezoid = Polygon(
            coords,
            facecolor=colors[i],
            edgecolor='#ffffff',
            alpha=0.8,
            linewidth=1
        )
        ax.add_patch(trapezoid)
        
        ax.text(
            -max_width/1.8,
            (y_top + y_bottom)/2,
            f"{data['stage'].iloc[i]}",
            ha='right',
            va='center',
            fontsize=10,
            color='#ffffff',
            fontfamily='monospace'
        )
        
        ax.text(
            0,
            (y_top + y_bottom)/2,
            f"{data['value'].iloc[i]:,}",
            ha='center',
            va='center',
            fontsize=10,
            color='#ffffff',
            fontfamily='monospace'
        )
        
        if i > 0:
            ax.text(
                max_width/1.8,
                (y_top + y_bottom)/2,
                f"[{data['conv_rate'].iloc[i]}%]",
                ha='left',
                va='center',
                fontsize=9,
                color='#ffffff',
                fontfamily='monospace'
            )
    
    ax.set_xlim(-max_width, max_width)
    ax.set_ylim(0, total_height)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    plt.title('Pipeline Analysis', pad=20, fontsize=14, color='#ffffff', fontfamily='monospace')
    plt.tight_layout()
    plt.savefig('三角漏斗图_style_4.png', dpi=300, bbox_inches='tight', facecolor='#1a1a1a')
    return fig

def plot_5(data):
    """Natural Style"""
    fig, ax = plt.subplots(figsize=(10, 8), facecolor='#fafaf8')
    ax.set_facecolor('#fafaf8')
    
    n_stages = len(data)
    total_height = 10
    stage_height = total_height / n_stages
    max_width = 8
    
    # 使用自然色系
    colors = ['#8cb369', '#f4e285', '#f4a259', '#5b8e7d', '#bc4b51']
    
    max_value = data['value'].iloc[0]
    widths = data['value'] / max_value * max_width
    
    for i in range(n_stages):
        y_bottom = total_height - (i + 1) * stage_height
        y_top = total_height - i * stage_height
        
        if i == n_stages - 1:
            coords = get_trapezoid_coords(y_bottom, y_top, widths.iloc[i], widths.iloc[i])
        else:
            coords = get_trapezoid_coords(y_bottom, y_top, widths.iloc[i], widths.iloc[i+1])
            
        trapezoid = Polygon(
            coords,
            facecolor=colors[i],
            edgecolor='white',
            alpha=0.9,
            linewidth=1.5
        )
        ax.add_patch(trapezoid)
        
        ax.text(
            -max_width/1.8,
            (y_top + y_bottom)/2,
            f"{data['stage'].iloc[i]}",
            ha='right',
            va='center',
            fontsize=11,
            color='#2f4858',
            fontfamily='serif'
        )
        
        ax.text(
            0,
            (y_top + y_bottom)/2,
            f"{data['value'].iloc[i]:,}",
            ha='center',
            va='center',
            fontsize=11,
            color='white',
            fontweight='light',
            fontfamily='serif'
        )
        
        if i > 0:
            ax.text(
                max_width/1.8,
                (y_top + y_bottom)/2,
                f"Conv. {data['conv_rate'].iloc[i]}%",
                ha='left',
                va='center',
                fontsize=10,
                color='#2f4858',
                fontfamily='serif'
            )
    
    ax.set_xlim(-max_width, max_width)
    ax.set_ylim(0, total_height)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    plt.title('Sales Journey', pad=20, fontsize=16, color='#2f4858', fontfamily='serif')
    plt.tight_layout()
    plt.savefig('三角漏斗图_style_5.png', dpi=300, bbox_inches='tight', facecolor='#fafaf8')
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
