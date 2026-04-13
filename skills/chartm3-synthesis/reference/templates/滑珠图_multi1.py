import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def preprocess(data=None):
    """Generate and preprocess data for dumbbell plot"""
    if data is None:
        # Generate sample data
        data = pd.DataFrame({
            'Country': ['Brazil', 'India', 'China', 'Russia', 'Mexico', 
                       'Indonesia', 'South Africa', 'Turkey'],
            'Literacy_2000': [86.4, 61.0, 90.9, 99.4, 90.5, 88.5, 82.4, 87.3],
            'Literacy_2020': [93.2, 74.4, 96.8, 99.7, 95.2, 95.7, 87.0, 96.1]
        })
    
    # Sort by change magnitude
    data['Change'] = data['Literacy_2020'] - data['Literacy_2000']
    data = data.sort_values('Change', ascending=True)
    
    # Save processed data
    data.to_csv('滑珠图.csv', index=False)
    return data

def plot(data):
    """Create a dumbbell plot"""
    # Set style
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot parameters
    colors = {'start': '#E64B35', 'end': '#4DBBD5', 'line': '#CCCCCC'}
    point_size = 100
    line_width = 1.5
    
    # Create plot elements
    y_range = range(len(data))
    
    # Plot lines
    for idx in y_range:
        ax.plot([data['Literacy_2000'].iloc[idx], data['Literacy_2020'].iloc[idx]], 
                [idx, idx], 
                color=colors['line'], 
                linewidth=line_width,
                zorder=1)
    
    # Plot points
    start_points = ax.scatter(data['Literacy_2000'], y_range,
                            s=point_size, color=colors['start'],
                            label='2000', zorder=2)
    end_points = ax.scatter(data['Literacy_2020'], y_range,
                           s=point_size, color=colors['end'],
                           label='2020', zorder=2)
    
    # Add value labels
    for idx in y_range:
        ax.text(data['Literacy_2000'].iloc[idx]-1, idx, 
                f"{data['Literacy_2000'].iloc[idx]}%",
                ha='right', va='center')
        ax.text(data['Literacy_2020'].iloc[idx]+1, idx,
                f"{data['Literacy_2020'].iloc[idx]}%",
                ha='left', va='center')
    
    # Customize plot
    ax.set_yticks(y_range)
    ax.set_yticklabels(data['Country'])
    ax.set_xlabel('Literacy Rate (%)')
    ax.set_title('Change in Literacy Rates (2000-2020)', pad=20)
    
    # Add legend
    ax.legend(loc='upper right', title='Year')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save plot
    plt.savefig('滑珠图.png', dpi=300, bbox_inches='tight')
    plt.close()

# Example usage

def plot_1(data):
    """商务简约风格"""
    plt.style.use('seaborn-v0_8-white')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = {'start': '#2C3E50', 'end': '#3498DB', 'line': '#BDC3C7'}
    point_size = 80
    line_width = 1
    
    y_range = range(len(data))
    
    for idx in y_range:
        ax.plot([data['Literacy_2000'].iloc[idx], data['Literacy_2020'].iloc[idx]], 
                [idx, idx], 
                color=colors['line'],
                linewidth=line_width,
                linestyle='--')
    
    ax.scatter(data['Literacy_2000'], y_range,
              s=point_size, color=colors['start'],
              label='2000', zorder=2)
    ax.scatter(data['Literacy_2020'], y_range,
              s=point_size, color=colors['end'],
              label='2020', zorder=2)
    
    for idx in y_range:
        ax.text(data['Literacy_2000'].iloc[idx]-0.5, idx,
                f"{data['Literacy_2000'].iloc[idx]}%",
                ha='right', va='center', fontsize=8)
        ax.text(data['Literacy_2020'].iloc[idx]+0.5, idx,
                f"{data['Literacy_2020'].iloc[idx]}%",
                ha='left', va='center', fontsize=8)
    
    ax.set_yticks(y_range)
    ax.set_yticklabels(data['Country'], fontsize=10)
    ax.set_xlabel('Literacy Rate (%)', fontsize=10)
    ax.set_title('Literacy Rate Changes (2000-2020)', 
                 fontsize=12, pad=20)
    
    ax.legend(loc='upper right', title='Year')
    plt.tight_layout()
    plt.savefig('滑珠图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    """渐变色科技风格"""
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = {'start': '#1f77b4', 'end': '#2ecc71', 'line': '#34495e'}
    point_size = 120
    line_width = 2
    
    y_range = range(len(data))
    
    for idx in y_range:
        ax.plot([data['Literacy_2000'].iloc[idx], data['Literacy_2020'].iloc[idx]], 
                [idx, idx], 
                color=colors['line'],
                alpha=0.3,
                linewidth=line_width)
    
    ax.scatter(data['Literacy_2000'], y_range,
              s=point_size, color=colors['start'],
              label='2000', alpha=0.8)
    ax.scatter(data['Literacy_2020'], y_range,
              s=point_size, color=colors['end'],
              label='2020', alpha=0.8)
    
    for idx in y_range:
        ax.text(data['Literacy_2000'].iloc[idx]-0.5, idx,
                f"{data['Literacy_2000'].iloc[idx]}%",
                ha='right', va='center',
                color='white', fontsize=8)
        ax.text(data['Literacy_2020'].iloc[idx]+0.5, idx,
                f"{data['Literacy_2020'].iloc[idx]}%",
                ha='left', va='center',
                color='white', fontsize=8)
    
    ax.grid(True, alpha=0.1)
    ax.set_yticks(y_range)
    ax.set_yticklabels(data['Country'], fontsize=10)
    ax.set_xlabel('Literacy Rate (%)', fontsize=10)
    ax.set_title('Literacy Rate Changes (2000-2020)',
                 fontsize=12, pad=20, color='white')
    
    ax.legend(loc='upper right', title='Year')
    plt.tight_layout()
    plt.savefig('滑珠图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    """活泼多彩风格"""
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = {'start': '#FF6B6B', 'end': '#4ECDC4', 'line': '#95A5A6'}
    point_size = 100
    line_width = 1.5
    
    y_range = range(len(data))
    
    for idx in y_range:
        ax.plot([data['Literacy_2000'].iloc[idx], data['Literacy_2020'].iloc[idx]], 
                [idx, idx], 
                color=colors['line'],
                linewidth=line_width,
                linestyle=':')
    
    ax.scatter(data['Literacy_2000'], y_range,
              s=point_size, color=colors['start'],
              marker='o', label='2000')
    ax.scatter(data['Literacy_2020'], y_range,
              s=point_size, color=colors['end'],
              marker='s', label='2020')
    
    for idx in y_range:
        ax.text(data['Literacy_2000'].iloc[idx]-0.5, idx,
                f"{data['Literacy_2000'].iloc[idx]}%",
                ha='right', va='center',
                fontsize=9, color=colors['start'])
        ax.text(data['Literacy_2020'].iloc[idx]+0.5, idx,
                f"{data['Literacy_2020'].iloc[idx]}%",
                ha='left', va='center',
                fontsize=9, color=colors['end'])
    
    ax.set_yticks(y_range)
    ax.set_yticklabels(data['Country'], fontsize=10)
    ax.set_xlabel('Literacy Rate (%)', fontsize=10)
    ax.set_title('Literacy Rate Changes\n2000 vs 2020',
                 fontsize=14, pad=20)
    
    ax.legend(loc='upper right', title='Year')
    plt.tight_layout()
    plt.savefig('滑珠图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    """单色系典雅风格"""
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = {'start': '#8E44AD', 'end': '#9B59B6', 'line': '#D5D8DC'}
    point_size = 90
    line_width = 1
    
    y_range = range(len(data))
    
    for idx in y_range:
        ax.plot([data['Literacy_2000'].iloc[idx], data['Literacy_2020'].iloc[idx]], 
                [idx, idx], 
                color=colors['line'],
                linewidth=line_width)
    
    ax.scatter(data['Literacy_2000'], y_range,
              s=point_size, color=colors['start'],
              label='2000', alpha=0.7)
    ax.scatter(data['Literacy_2020'], y_range,
              s=point_size, color=colors['end'],
              label='2020', alpha=0.7)
    
    for idx in y_range:
        ax.text(data['Literacy_2000'].iloc[idx]-0.5, idx,
                f"{data['Literacy_2000'].iloc[idx]}%",
                ha='right', va='center',
                fontsize=8, style='italic')
        ax.text(data['Literacy_2020'].iloc[idx]+0.5, idx,
                f"{data['Literacy_2020'].iloc[idx]}%",
                ha='left', va='center',
                fontsize=8, style='italic')
    
    ax.set_yticks(y_range)
    ax.set_yticklabels(data['Country'], fontsize=10)
    ax.set_xlabel('Literacy Rate (%)', fontsize=10)
    ax.set_title('Evolution of Literacy Rates\n2000-2020',
                 fontsize=12, pad=20)
    
    ax.legend(loc='upper right', title='Year')
    plt.tight_layout()
    plt.savefig('滑珠图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    """复古暖色调风格"""
    plt.style.use('seaborn-v0_8-paper')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = {'start': '#E67E22', 'end': '#D35400', 'line': '#FAD7A0'}
    point_size = 110
    line_width = 1.8
    
    y_range = range(len(data))
    
    for idx in y_range:
        ax.plot([data['Literacy_2000'].iloc[idx], data['Literacy_2020'].iloc[idx]], 
                [idx, idx], 
                color=colors['line'],
                linewidth=line_width,
                linestyle='-.')
    
    ax.scatter(data['Literacy_2000'], y_range,
              s=point_size, color=colors['start'],
              marker='^', label='2000')
    ax.scatter(data['Literacy_2020'], y_range,
              s=point_size, color=colors['end'],
              marker='v', label='2020')
    
    for idx in y_range:
        ax.text(data['Literacy_2000'].iloc[idx]-0.5, idx,
                f"{data['Literacy_2000'].iloc[idx]}%",
                ha='right', va='center',
                fontsize=9, family='serif')
        ax.text(data['Literacy_2020'].iloc[idx]+0.5, idx,
                f"{data['Literacy_2020'].iloc[idx]}%",
                ha='left', va='center',
                fontsize=9, family='serif')
    
    ax.set_yticks(y_range)
    ax.set_yticklabels(data['Country'], fontsize=10, family='serif')
    ax.set_xlabel('Literacy Rate (%)', fontsize=10, family='serif')
    ax.set_title('20 Years of Literacy Progress\n2000-2020',
                 fontsize=14, pad=20, family='serif')
    
    ax.legend(loc='upper right', title='Year')
    plt.tight_layout()
    plt.savefig('滑珠图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
# plot(data)
# plot_1(data)
# plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
