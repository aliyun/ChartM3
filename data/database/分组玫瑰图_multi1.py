import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def preprocess(data=None):
    # Generate synthetic data
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    age_groups = ['Youth', 'Adult', 'Senior']
    
    # Create base participation rates with seasonal patterns
    base_rates = {
        'Youth':  [65, 85, 70, 45],
        'Adult':  [60, 75, 65, 40],
        'Senior': [45, 55, 50, 30]
    }
    np.random.seed(42)
    
    # Create DataFrame
    data = []
    for season in seasons:
        season_idx = seasons.index(season)
        for age in age_groups:
            value = base_rates[age][season_idx]
            # Add some random variation
            value += np.random.normal(0, 2)
            data.append({
                'Season': season,
                'Age_Group': age,
                'Participation': value
            })
    
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('分组玫瑰图.csv', index=False)
    return df

def plot(data):
    # Set style
    plt.style.use('seaborn-v0_8')
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='polar')
    
    # Define colors and width
    colors = ['#FF9999', '#66B2FF', '#99FF99']
    width = 2 * np.pi / 12  # 12 = 4 seasons * 3 groups
    
    # Convert seasons to angles
    season_map = {'Spring': 0, 'Summer': np.pi/2, 'Fall': np.pi, 'Winter': 3*np.pi/2}
    
    # Plot each age group
    for idx, age_group in enumerate(data['Age_Group'].unique()):
        group_data = data[data['Age_Group'] == age_group]
        
        # Calculate angles for this group
        angles = [season_map[s] + (width * idx) for s in group_data['Season']]
        values = group_data['Participation'].values
        
        # Create bars
        bars = ax.bar(angles, values, width=width, bottom=0,
                     alpha=0.7, color=colors[idx], label=age_group)
    
    # Customize the plot
    ax.set_theta_direction(-1)  # clockwise
    ax.set_theta_zero_location('N')  # 0 at top
    
    # Set labels at season positions
    ax.set_xticks([season_map[s] + width * 1.5 for s in season_map.keys()])
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])

    # Set y-axis limits and labels
    ax.set_ylim(0, 100)
    ax.set_rticks([20, 40, 60, 80, 100])
    ax.set_rlabel_position(0)
    
    # Add title and legend
    plt.title('Seasonal Outdoor Activity Participation by Age Group\n', 
              pad=20, size=14, weight='bold')
    plt.legend(loc='center left', bbox_to_anchor=(1.2, 0.5))
    
    # Add subtle grid
    ax.grid(True, alpha=0.2)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('分组玫瑰图.png', dpi=300, bbox_inches='tight')
    plt.close()
    

def plot_1(data):
    # 商务风格 - 深色主题
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='polar')
    
    colors = ['#4A90E2', '#50E3C2', '#F5A623']  # 专业蓝色系
    width = 2 * np.pi / 12
    
    season_map = {'Spring': 0, 'Summer': np.pi/2, 'Fall': np.pi, 'Winter': 3*np.pi/2}
    
    for idx, age_group in enumerate(data['Age_Group'].unique()):
        group_data = data[data['Age_Group'] == age_group]
        angles = [season_map[s] + (width * idx) for s in group_data['Season']]
        values = group_data['Participation'].values
        
        bars = ax.bar(angles, values, width=width, bottom=0,
                     alpha=0.8, color=colors[idx], label=age_group,
                     edgecolor='white', linewidth=0.5)
    
    ax.set_theta_direction(-1)
    ax.set_theta_zero_location('N')
    
    ax.set_xticks([season_map[s] + width * 1.5 for s in season_map.keys()])
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'],
                       fontsize=12, color='white')
    
    ax.set_ylim(0, 100)
    ax.set_rticks([20, 40, 60, 80, 100])
    ax.set_rlabel_position(0)
    
    plt.title('Seasonal Activity Participation\n', 
              pad=20, size=16, weight='bold', color='white')
    plt.legend(loc='center left', bbox_to_anchor=(1.2, 0.5),
              framealpha=0.4)
    
    ax.grid(True, alpha=0.2, color='gray')
    
    plt.tight_layout()
    plt.savefig('分组玫瑰图_style_1.png', dpi=300, bbox_inches='tight',
                facecolor='black', edgecolor='none')
    plt.close()

def plot_2(data):
    # 活泼风格 - 明亮色彩
    plt.style.use('seaborn-v0_8')
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='polar')
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']  # 明快色系
    width = 2 * np.pi / 12
    
    season_map = {'Spring': 0, 'Summer': np.pi/2, 'Fall': np.pi, 'Winter': 3*np.pi/2}
    
    for idx, age_group in enumerate(data['Age_Group'].unique()):
        group_data = data[data['Age_Group'] == age_group]
        angles = [season_map[s] + (width * idx) for s in group_data['Season']]
        values = group_data['Participation'].values
        
        bars = ax.bar(angles, values, width=width, bottom=0,
                     alpha=0.9, color=colors[idx], label=age_group,
                     edgecolor='white', linewidth=1)
        
        # 添加数值标签
        for angle, value in zip(angles, values):
            ax.text(angle, value+2, f'{int(value)}%', 
                   ha='center', va='bottom')
    
    ax.set_theta_direction(-1)
    ax.set_theta_zero_location('N')
    
    ax.set_xticks([season_map[s] + width * 1.5 for s in season_map.keys()])
    ax.set_xticklabels(['Spring 🌸', 'Summer ☀️', 'Fall 🍁', 'Winter ❄️'],
                       fontsize=12)
    
    ax.set_ylim(0, 100)
    ax.set_rticks([20, 40, 60, 80, 100])
    ax.set_rlabel_position(0)
    
    plt.title('Fun Seasonal Activities!\n', 
              pad=20, size=16, weight='bold', color='#FF6B6B')
    plt.legend(loc='center left', bbox_to_anchor=(1.2, 0.5),
              frameon=True, facecolor='white', edgecolor='#4ECDC4')
    
    ax.grid(True, alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('分组玫瑰图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 极简风格
    plt.style.use('seaborn-v0_8-white')
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='polar')
    
    colors = ['#E6E6EA', '#B9B9BE', '#8C8C91']  # 灰度渐变
    width = 2 * np.pi / 12
    
    season_map = {'Spring': 0, 'Summer': np.pi/2, 'Fall': np.pi, 'Winter': 3*np.pi/2}
    
    for idx, age_group in enumerate(data['Age_Group'].unique()):
        group_data = data[data['Age_Group'] == age_group]
        angles = [season_map[s] + (width * idx) for s in group_data['Season']]
        values = group_data['Participation'].values
        
        bars = ax.bar(angles, values, width=width, bottom=0,
                     alpha=1.0, color=colors[idx], label=age_group,
                     edgecolor='white', linewidth=0.5)
    
    ax.set_theta_direction(-1)
    ax.set_theta_zero_location('N')
    
    ax.set_xticks([season_map[s] + width * 1.5 for s in season_map.keys()])
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'],
                       fontsize=10, color='gray')
    
    ax.set_ylim(0, 100)
    ax.set_rticks([25, 50, 75, 100])
    ax.set_rlabel_position(0)
    
    plt.title('Seasonal Participation Analysis\n', 
              pad=20, size=14, weight='normal', color='gray')
    plt.legend(loc='center left', bbox_to_anchor=(1.2, 0.5),
              frameon=False)
    
    ax.grid(False)
    
    plt.tight_layout()
    plt.savefig('分组玫瑰图_style_3.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    
def plot_4(data):
    # 科技风格
    plt.style.use('seaborn-v0_8-darkgrid')
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='polar')
    
    colors = ['#00ff9f', '#00b8ff', '#001eff']  # 霓虹蓝色系
    width = 2 * np.pi / 12
    
    season_map = {'Spring': 0, 'Summer': np.pi/2, 'Fall': np.pi, 'Winter': 3*np.pi/2}
    
    for idx, age_group in enumerate(data['Age_Group'].unique()):
        group_data = data[data['Age_Group'] == age_group]
        angles = [season_map[s] + (width * idx) for s in group_data['Season']]
        values = group_data['Participation'].values
        
        bars = ax.bar(angles, values, width=width, bottom=0,
                     alpha=0.7, color=colors[idx], label=age_group,
                     edgecolor='cyan', linewidth=1)
    
    ax.set_theta_direction(-1)
    ax.set_theta_zero_location('N')
    
    ax.set_xticks([season_map[s] + width * 1.5 for s in season_map.keys()])
    ax.set_xticklabels(['SP_01', 'SU_02', 'FA_03', 'WI_04'],
                       fontsize=12, color='cyan')
    
    ax.set_ylim(0, 100)
    ax.set_rticks([20, 40, 60, 80, 100])
    ax.set_rlabel_position(0)
    
    plt.title('PARTICIPATION ANALYSIS v2.0\n', 
              pad=20, size=16, weight='bold', color='cyan')
    plt.legend(loc='center left', bbox_to_anchor=(1.2, 0.5),
              framealpha=0.1, edgecolor='cyan')
    
    ax.grid(True, alpha=0.2, color='cyan', linestyle=':')
    
    plt.tight_layout()
    plt.savefig('分组玫瑰图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()
    
def plot_5(data):
    # 典雅风格
    plt.style.use('seaborn-v0_8')
    fig = plt.figure(figsize=(11, 11))
    ax = fig.add_subplot(111, projection='polar')
    
    colors = ['#DDC3A5', '#E0A899', '#E0B5A1']  # 复古柔和色系
    width = 2 * np.pi / 12
    
    season_map = {'Spring': 0, 'Summer': np.pi/2, 'Fall': np.pi, 'Winter': 3*np.pi/2}
    
    for idx, age_group in enumerate(data['Age_Group'].unique()):
        group_data = data[data['Age_Group'] == age_group]
        angles = [season_map[s] + (width * idx) for s in group_data['Season']]
        values = group_data['Participation'].values
        
        bars = ax.bar(angles, values, width=width, bottom=0,
                     alpha=0.8, color=colors[idx], label=age_group,
                     edgecolor='#4A4A4A', linewidth=0.5)
    
    ax.set_theta_direction(-1)
    ax.set_theta_zero_location('N')
    
    ax.set_xticks([season_map[s] + width * 1.5 for s in season_map.keys()])
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'],
                       fontsize=12, fontfamily='serif')
    
    ax.set_ylim(0, 100)
    ax.set_rticks([25, 50, 75, 100])
    ax.set_rlabel_position(0)
    
    plt.title('Seasonal Participation Study\n', 
              pad=20, size=16, weight='normal', fontfamily='serif')
    plt.legend(loc='center left', bbox_to_anchor=(1.2, 0.5),
              framealpha=0.4, edgecolor='#4A4A4A')
    
    ax.grid(True, alpha=0.15, linestyle='-')
    
    plt.tight_layout()
    plt.savefig('分组玫瑰图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
# plot(data)
# plot_1(data)
# plot_2(data)
# plot_3(data)
# plot_4(data)
plot_5(data)
