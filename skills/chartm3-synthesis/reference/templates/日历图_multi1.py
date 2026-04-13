import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import calendar

def preprocess(data=None):
    np.random.seed(42)
    # Generate one month of daily data for October 2023
    dates = pd.date_range(start='2023-10-01', end='2023-10-31', freq='D')
    
    # Create base values
    base = np.ones(len(dates)) * 50
    
    # Add weekly pattern
    weekly = np.array([0.7 if d.weekday() >= 5 else 1.2 for d in dates])
    
    # Add random noise
    noise = np.random.normal(1, 0.1, len(dates))
    
    # Combine patterns
    values = base * weekly * noise
    
    # Add special event spikes
    special_dates = ['2023-10-01', '2023-10-15', '2023-10-31']
    
    # Create DataFrame
    df = pd.DataFrame({
        'date': dates,
        'value': values.round(1)
    })
    
    # Multiply values for special dates
    for date in special_dates:
        df.loc[df['date'] == date, 'value'] *= 2
    
    # Save to CSV
    df.to_csv('日历图.csv', index=False)
    return df

def plot(data):
    # Read data if filename provided
    if isinstance(data, str):
        data = pd.read_csv(data)
        data['date'] = pd.to_datetime(data['date'])
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(top=0.95)
    
    # Get the first day of the month and its weekday (0 = Monday, 6 = Sunday)
    first_day = data['date'].min()
    first_weekday = first_day.weekday()
    
    # Create calendar grid
    calendar_grid = np.full((6, 7), np.nan)  # 6 weeks x 7 days
    
    # Fill in the grid with values
    for i, row in data.iterrows():
        day = row['date'].day - 1  # 0-based day
        week = (day + first_weekday) // 7
        weekday = (day + first_weekday) % 7
        calendar_grid[week, weekday] = row['value']
    
    # Create heatmap
    im = ax.imshow(calendar_grid, cmap='Blues', aspect='equal')
    
    # Remove axis lines
    ax.spines[:].set_visible(False)
    
    # Set title
    ax.set_title('Daily Activity Heatmap - October 2023', pad=20, fontsize=14)
    
        # Configure x-axis (weekdays)
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ax.set_xticks(np.arange(len(weekdays)))
    ax.set_xticklabels(weekdays)
    
    # Configure y-axis (weeks)
    ax.set_yticks(np.arange(6))
    ax.set_yticklabels(['Week {}'.format(i+1) for i in range(6)])
    
    # Add day numbers in each cell
    for week in range(6):
        for day in range(7):
            day_number = week * 7 + day - first_weekday + 1
            if 1 <= day_number <= 31:
                ax.text(day, week, str(day_number), 
                       ha='center', va='center', 
                       color='black' if calendar_grid[week, day] < np.nanmean(calendar_grid) else 'white')
    
    # Add colorbar
    cbar = plt.colorbar(im)
    cbar.set_label('Activity Level', rotation=270, labelpad=15)
    
    # Add grid
    ax.set_xticks(np.arange(-.5, 7, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 6, 1), minor=True)
    ax.grid(which='minor', color='white', linestyle='-', linewidth=2)
    
    # Save plot
    plt.savefig('日历图.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate and plot data
data = preprocess()
plot(data)

def plot_1(data):
    # 商务简约风格
    if isinstance(data, str):
        data = pd.read_csv(data)
        data['date'] = pd.to_datetime(data['date'])
    
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(top=0.95)
    
    first_day = data['date'].min()
    first_weekday = first_day.weekday()
    
    calendar_grid = np.full((6, 7), np.nan)
    
    for i, row in data.iterrows():
        day = row['date'].day - 1
        week = (day + first_weekday) // 7
        weekday = (day + first_weekday) % 7
        calendar_grid[week, weekday] = row['value']
    
    im = ax.imshow(calendar_grid, cmap='Blues', aspect='equal')
    ax.spines[:].set_visible(False)
    
    ax.set_title('Business Activity Calendar', pad=20, fontsize=16, fontweight='bold')
    
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ax.set_xticks(np.arange(len(weekdays)))
    ax.set_xticklabels(weekdays, fontsize=10)
    
    ax.set_yticks(np.arange(6))
    ax.set_yticklabels(['Week {}'.format(i+1) for i in range(6)], fontsize=10)
    
    for week in range(6):
        for day in range(7):
            day_number = week * 7 + day - first_weekday + 1
            if 1 <= day_number <= 31:
                ax.text(day, week, str(day_number),
                       ha='center', va='center',
                       fontsize=9,
                       color='black' if calendar_grid[week, day] < np.nanmean(calendar_grid) else 'white')
    
    cbar = plt.colorbar(im)
    cbar.set_label('Activity Level', rotation=270, labelpad=15)
    
    ax.set_xticks(np.arange(-.5, 7, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 6, 1), minor=True)
    ax.grid(which='minor', color='white', linestyle='-', linewidth=1.5)
    
    plt.savefig('日历图_style_1.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_2(data):
    # 活泼明快风格
    if isinstance(data, str):
        data = pd.read_csv(data)
        data['date'] = pd.to_datetime(data['date'])
    
    plt.style.use('default')
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(top=0.95)
    
    first_day = data['date'].min()
    first_weekday = first_day.weekday()
    
    calendar_grid = np.full((6, 7), np.nan)
    
    for i, row in data.iterrows():
        day = row['date'].day - 1
        week = (day + first_weekday) // 7
        weekday = (day + first_weekday) % 7
        calendar_grid[week, weekday] = row['value']
    
    im = ax.imshow(calendar_grid, cmap='YlOrRd', aspect='equal')
    ax.spines[:].set_visible(False)
    
    ax.set_title('Vibrant Activity Calendar', pad=20, fontsize=16, fontfamily='comic sans ms')
    
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ax.set_xticks(np.arange(len(weekdays)))
    ax.set_xticklabels(weekdays, fontsize=10, rotation=30)
    
    ax.set_yticks(np.arange(6))
    ax.set_yticklabels(['Week {}'.format(i+1) for i in range(6)], fontsize=10)
    
    for week in range(6):
        for day in range(7):
            day_number = week * 7 + day - first_weekday + 1
            if 1 <= day_number <= 31:
                ax.text(day, week, str(day_number),
                       ha='center', va='center',
                       fontsize=10, fontweight='bold',
                       color='black' if calendar_grid[week, day] < np.nanmean(calendar_grid) else 'white')
    
    cbar = plt.colorbar(im)
    cbar.set_label('Activity Level', rotation=270, labelpad=15)
    
    ax.set_xticks(np.arange(-.5, 7, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 6, 1), minor=True)
    ax.grid(which='minor', color='white', linestyle='--', linewidth=2)
    
    plt.savefig('日历图_style_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_3(data):
    # 环保清新风格
    if isinstance(data, str):
        data = pd.read_csv(data)
        data['date'] = pd.to_datetime(data['date'])
    
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(top=0.95)
    
    first_day = data['date'].min()
    first_weekday = first_day.weekday()
    
    calendar_grid = np.full((6, 7), np.nan)
    
    for i, row in data.iterrows():
        day = row['date'].day - 1
        week = (day + first_weekday) // 7
        weekday = (day + first_weekday) % 7
        calendar_grid[week, weekday] = row['value']
    
    im = ax.imshow(calendar_grid, cmap='YlGn', aspect='equal', alpha=0.7)
    ax.spines[:].set_visible(False)
    
    ax.set_title('Eco-friendly Activity Calendar', pad=20, fontsize=14, color='darkgreen')
    
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ax.set_xticks(np.arange(len(weekdays)))
    ax.set_xticklabels(weekdays, fontsize=9)
    
    ax.set_yticks(np.arange(6))
    ax.set_yticklabels(['Week {}'.format(i+1) for i in range(6)], fontsize=9)
    
    for week in range(6):
        for day in range(7):
            day_number = week * 7 + day - first_weekday + 1
            if 1 <= day_number <= 31:
                ax.text(day, week, str(day_number),
                       ha='center', va='center',
                       fontsize=8,
                       color='black' if calendar_grid[week, day] < np.nanmean(calendar_grid) else 'white')
    
    cbar = plt.colorbar(im)
    cbar.set_label('Activity Level', rotation=270, labelpad=15, color='darkgreen')
    
    ax.set_xticks(np.arange(-.5, 7, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 6, 1), minor=True)
    ax.grid(which='minor', color='white', linestyle='-', linewidth=1)
    
    plt.savefig('日历图_style_3.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_4(data):
    # 现代科技风格
    if isinstance(data, str):
        data = pd.read_csv(data)
        data['date'] = pd.to_datetime(data['date'])
    
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(top=0.95)
    
    first_day = data['date'].min()
    first_weekday = first_day.weekday()
    
    calendar_grid = np.full((6, 7), np.nan)
    
    for i, row in data.iterrows():
        day = row['date'].day - 1
        week = (day + first_weekday) // 7
        weekday = (day + first_weekday) % 7
        calendar_grid[week, weekday] = row['value']
    
    im = ax.imshow(calendar_grid, cmap='plasma', aspect='equal')
    ax.spines[:].set_visible(False)
    
    ax.set_title('Tech Activity Dashboard', pad=20, fontsize=16, color='white')
    
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ax.set_xticks(np.arange(len(weekdays)))
    ax.set_xticklabels(weekdays, fontsize=10, color='white')
    
    ax.set_yticks(np.arange(6))
    ax.set_yticklabels(['Week {}'.format(i+1) for i in range(6)], fontsize=10, color='white')
    
    for week in range(6):
        for day in range(7):
            day_number = week * 7 + day - first_weekday + 1
            if 1 <= day_number <= 31:
                ax.text(day, week, str(day_number),
                       ha='center', va='center',
                       fontsize=9,
                       color='white' if calendar_grid[week, day] < np.nanmean(calendar_grid) else 'black')
    
    cbar = plt.colorbar(im)
    cbar.set_label('Activity Level', rotation=270, labelpad=15, color='white')
    
    ax.set_xticks(np.arange(-.5, 7, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 6, 1), minor=True)
    ax.grid(which='minor', color='gray', linestyle=':', linewidth=1)
    
    plt.savefig('日历图_style_4.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_5(data):
    # 优雅柔和风格
    if isinstance(data, str):
        data = pd.read_csv(data)
        data['date'] = pd.to_datetime(data['date'])
    
    plt.style.use('seaborn-v0_8-pastel')
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(top=0.95)
    
    first_day = data['date'].min()
    first_weekday = first_day.weekday()
    
    calendar_grid = np.full((6, 7), np.nan)
    
    for i, row in data.iterrows():
        day = row['date'].day - 1
        week = (day + first_weekday) // 7
        weekday = (day + first_weekday) % 7
        calendar_grid[week, weekday] = row['value']
    
    im = ax.imshow(calendar_grid, cmap='RdPu', aspect='equal', alpha=0.6)
    ax.spines[:].set_visible(False)
    
    ax.set_title('Elegant Activity Calendar', pad=20, fontsize=14, fontfamily='serif')
    
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ax.set_xticks(np.arange(len(weekdays)))
    ax.set_xticklabels(weekdays, fontsize=8, rotation=45)
    
    ax.set_yticks(np.arange(6))
    ax.set_yticklabels(['Week {}'.format(i+1) for i in range(6)], fontsize=9)
    
    for week in range(6):
        for day in range(7):
            day_number = week * 7 + day - first_weekday + 1
            if 1 <= day_number <= 31:
                ax.text(day, week, str(day_number),
                       ha='center', va='center',
                       fontsize=9, fontfamily='serif',
                       color='black' if calendar_grid[week, day] < np.nanmean(calendar_grid) else 'white')
    
    cbar = plt.colorbar(im)
    cbar.set_label('Activity Level', rotation=270, labelpad=15)
    
    ax.set_xticks(np.arange(-.5, 7, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 6, 1), minor=True)
    ax.grid(which='minor', color='white', linestyle='-', linewidth=1)
    
    plt.savefig('日历图_style_5.png', dpi=300, bbox_inches='tight')
    plt.close()

data = preprocess()
# plot(data)
# plot_1(data)
# plot_2(data)
# plot_3(data)
# plot_4(data)
plot_5(data)
