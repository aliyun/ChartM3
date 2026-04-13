import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def preprocess(data=None):
    np.random.seed(42)
    # Generate synthetic fitness center visit data
    days = range(7)  # 0=Monday to 6=Sunday
    hours = range(24)
    
    # Create all day-hour combinations
    data = [(day, hour) for day in days for hour in hours]
    df = pd.DataFrame(data, columns=['day', 'hour'])
    
    # Generate visit counts with realistic patterns
    def generate_count(row):
        day, hour = row['day'], row['hour']
        
        # Base count
        count = np.random.poisson(5)
        
        # Morning peak (6-8am)
        if 6 <= hour <= 8:
            count += np.random.poisson(20)
            
        # Evening peak (5-7pm)
        if 17 <= hour <= 19:
            count += np.random.poisson(25)
            
        # Weekend patterns
        if day >= 5:  # Saturday and Sunday
            if 9 <= hour <= 16:  # More daytime activity
                count += np.random.poisson(15)
            
        # Reduce late night/early morning
        if 23 <= hour or hour <= 4:
            count = int(count * 0.3)
            
        return count
    
    df['count'] = df.apply(generate_count, axis=1)
    
    # Save to CSV
    df.to_csv('矩阵气泡图.csv', index=False)
    return df

def plot(data):
    # Set style
    plt.style.use('seaborn-v0_8')
    
    # Create figure with appropriate size
    plt.figure(figsize=(12, 6))
    
    # Create bubble plot
    plt.scatter(data['hour'], data['day'], s=data['count']*20, 
               alpha=0.6, c='#3182bd')
    
    # Customize layout
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.yticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 
                         'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.xticks(range(0, 24, 2))
    
    # Labels and title
    plt.xlabel('Hour of Day', fontsize=12)
    plt.ylabel('Day of Week', fontsize=12)
    plt.title('Fitness Center Visit Patterns', fontsize=14, pad=20)
    
    # Add legend for bubble sizes
    legend_elements = [plt.scatter([], [], s=s*20, c='#3182bd', alpha=0.6,
                                 label=f'{s} visits')
                      for s in [10, 25, 40]]
    plt.legend(handles=legend_elements, title='Visit Frequency', title_fontsize=10, bbox_to_anchor=(1.15, 1))
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('矩阵气泡图.png', dpi=300, bbox_inches='tight')
    plt.close()


def plot_1(data):
    # 商务风格 - 深蓝色调
    plt.style.use('seaborn-v0_8-dark')
    plt.figure(figsize=(12, 6))
    
    sizes = data['count']*20
    colors = ['#1f77b4', '#7cc7ff']
    cm = plt.cm.get_cmap('Blues')
    scatter = plt.scatter(data['hour'], data['day'], s=sizes,
                         c=data['count'], cmap=cm, alpha=0.7)
    
    plt.grid(True, linestyle=':', alpha=0.3)
    plt.yticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
               fontsize=10, fontweight='bold')
    plt.xticks(range(0, 24, 2), fontsize=10)
    
    plt.xlabel('Hour of Day', fontsize=12, fontweight='bold')
    plt.ylabel('Day of Week', fontsize=12, fontweight='bold')
    plt.title('Fitness Center Visit Patterns\nBusiness Style', 
              fontsize=14, pad=20, fontweight='bold')
    
    cbar = plt.colorbar(scatter)
    cbar.set_label('Visit Count', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('矩阵气泡图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 极简风格 - 单色系
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 6), facecolor='white')
    
    plt.scatter(data['hour'], data['day'], s=data['count']*20,
                c='#2ecc71', alpha=0.5)
    
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.yticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 
                         'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.xticks(range(0, 24, 2))
    
    plt.xlabel('Hour', fontsize=10)
    plt.ylabel('Day', fontsize=10)
    plt.title('Fitness Center Visits\nMinimalist Style', 
              fontsize=12, pad=20)
    
    legend_elements = [plt.scatter([], [], s=s*20, c='#2ecc71', alpha=0.5,
                                 label=f'{s}')
                      for s in [10, 25, 40]]
    plt.legend(handles=legend_elements, title='Visits', 
              loc='center left', bbox_to_anchor=(1, 0.5))
    
    plt.tight_layout()
    plt.savefig('矩阵气泡图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 活泼风格 - 多彩配色
    plt.style.use('default')
    plt.figure(figsize=(12, 6))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD']
    scatter = plt.scatter(data['hour'], data['day'], s=data['count']*20,
                         c=data['count'], cmap='viridis', alpha=0.7)
    
    plt.grid(False)
    plt.yticks(range(7), ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
               fontsize=10, fontfamily='Comic Sans MS')
    plt.xticks(range(0, 24, 2), fontsize=10)
    
    plt.xlabel('Time of Day', fontsize=12)
    plt.ylabel('Weekday', fontsize=12)
    plt.title('Gym Visit Patterns 🏋️\nPlayful Style', 
              fontsize=14, pad=20)
    
    cbar = plt.colorbar(scatter)
    cbar.set_label('Number of Visits')
    
    plt.tight_layout()
    plt.savefig('矩阵气泡图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 科技风格 - 深色背景
    plt.style.use('dark_background')
    plt.figure(figsize=(12, 6))
    
    scatter = plt.scatter(data['hour'], data['day'], s=data['count']*20,
                         c=data['count'], cmap='plasma', alpha=0.8)
    
    plt.grid(True, linestyle='--', alpha=0.2)
    plt.yticks(range(7), ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
               fontsize=10, color='white')
    plt.xticks(range(0, 24, 2), color='white')
    
    plt.xlabel('Hour', fontsize=12, color='white')
    plt.ylabel('Day', fontsize=12, color='white')
    plt.title('Fitness Center Analytics\nTech Style', 
              fontsize=14, pad=20, color='white')
    
    cbar = plt.colorbar(scatter)
    cbar.set_label('Visit Frequency', color='white')
    
    plt.tight_layout()
    plt.savefig('矩阵气泡图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 经典热力图风格
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(12, 6))
    
    sizes = data['count']*20
    colors = data['count']
    scatter = plt.scatter(data['hour'], data['day'], s=sizes,
                         c=colors, cmap='YlOrRd', alpha=0.7)
    
    plt.grid(True, linestyle='-', alpha=0.2)
    plt.yticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 
                         'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.xticks(range(0, 24, 2))
    
    plt.xlabel('Hour of Day', fontsize=10)
    plt.ylabel('Day of Week', fontsize=10)
    plt.title('Fitness Center Visit Patterns\nHeatmap Style', 
              fontsize=12, pad=20)
    
    cbar = plt.colorbar(scatter)
    cbar.set_label('Visit Count')
    
    plt.tight_layout()
    plt.savefig('矩阵气泡图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
# plot(data)
# plot_1(data)
# plot_2(data)
# plot_3(data)
# plot_4(data)
plot_5(data)
