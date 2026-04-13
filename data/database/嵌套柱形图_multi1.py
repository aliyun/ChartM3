import pandas as pd
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots

def preprocess(data=None):
    """
    Generate or process data for nested bar chart visualization.
    Creates sample data if none provided.
    """
    if data is None:
        main_categories = ['Electronics', 'Furniture', 'Clothing']
        data = []
        
        for main_cat in main_categories:
            total = np.random.randint(800, 1200)
            
            if main_cat == 'Electronics':
                subs = {'Phones': total * 0.4, 
                       'Computers': total * 0.35,
                       'Accessories': total * 0.15}
            elif main_cat == 'Furniture':
                subs = {'Living Room': total * 0.45,
                       'Bedroom': total * 0.30,
                       'Office': total * 0.15}
            else:
                subs = {'Men': total * 0.35,
                       'Women': total * 0.40,
                       'Children': total * 0.15}
            
            # Round values to integers
            subs = {k: int(v) for k, v in subs.items()}
            
            data.append({
                'Category': main_cat,
                'Total': total,
                'SubCategories': subs
            })
    
    df = pd.DataFrame(data)
    df.to_csv('嵌套柱形图.csv', index=False)
    return df

def plot(data):
    """
    Create nested bar chart visualization with stacked sub-categories.
    """
    fig = go.Figure()
    
    # Color schemes
    main_colors = {
        'Electronics': 'rgba(31, 119, 180, 0.3)',
        'Furniture': 'rgba(255, 127, 14, 0.3)',
        'Clothing': 'rgba(44, 160, 44, 0.3)'
    }
    
    sub_colors = {
        'Electronics': ['rgb(8, 69, 148)', 'rgb(33, 113, 181)', 'rgb(66, 146, 198)'],
        'Furniture': ['rgb(217, 72, 1)', 'rgb(253, 141, 60)', 'rgb(253, 187, 132)'],
        'Clothing': ['rgb(27, 120, 55)', 'rgb(65, 171, 93)', 'rgb(116, 196, 118)']
    }

    # Helper function for number formatting
    def format_number(num):
        return f"{num:,.0f}"

    # Calculate x-positions with proper spacing
    x_positions = list(range(len(data)))
    
    # Add main category bars
    for idx, row in data.iterrows():
        # Add main category bar
        fig.add_trace(go.Bar(
            name=f"Total {row['Category']}",
            x=[idx],
            y=[row['Total']],
            marker_color=main_colors[row['Category']],
            width=0.6,
            text=format_number(row['Total']),
            textposition='outside',
            textfont=dict(size=14),
            legendgroup='Total',
            legendgrouptitle_text="Main Categories",
            showlegend=True
        ))
        
        # Add stacked sub-category bars
        y_bottom = 0  # Track the bottom position for stacking
        sub_cats = row['SubCategories']
        for sub_idx, (sub_name, sub_value) in enumerate(sub_cats.items()):
            fig.add_trace(go.Bar(
                name=f"{sub_name} ({row['Category']})",
                x=[idx],
                y=[sub_value],
                base=y_bottom,  # Start from previous bar's top
                marker_color=sub_colors[row['Category']][sub_idx],
                width=0.45,
                text=format_number(sub_value),
                textposition='inside',
                textfont=dict(size=12, color='white'),
                legendgroup=f'Sub {row["Category"]}',
                legendgrouptitle_text=f"{row['Category']} Sub-categories",
                showlegend=True
            ))
            y_bottom += sub_value  # Update bottom position for next bar

    # Update layout
    fig.update_layout(
        title='Revenue Breakdown by Category',
        title_x=0.5,
        barmode='overlay',
        height=700,
        width=1000,
        showlegend=True,
        
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5,
            font=dict(size=12),
                        tracegroupgap=40,
            traceorder='grouped'
        ),
        margin=dict(
            l=50,
            r=50,
            t=100,
            b=200
        ),
        yaxis=dict(
            title='Revenue',
            titlefont=dict(size=14),
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(211,211,211,0.5)'
        ),
        xaxis=dict(
            title='Categories',
            titlefont=dict(size=14),
            ticktext=data['Category'].tolist(),
            tickvals=list(range(len(data))),
            tickfont=dict(size=12)
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Arial')
    )

    fig.write_image("嵌套柱形图.png", scale=2)
    return fig

def plot_1(data):
    """
    商务风格：深色主题，专业稳重
    """
    fig = go.Figure()
    
    # 深色商务配色
    main_colors = {
        'Electronics': 'rgba(41, 50, 65, 0.3)',
        'Furniture': 'rgba(69, 77, 93, 0.3)',
        'Clothing': 'rgba(89, 96, 109, 0.3)'
    }
    
    sub_colors = {
        'Electronics': ['#1f3163', '#2a4484', '#3857a5'],
        'Furniture': ['#515a77', '#677088', '#7d869a'],
        'Clothing': ['#2c3850', '#3e4b63', '#505e76']
    }

    def format_number(num):
        return f"{num:,.0f}"

    x_positions = list(range(len(data)))
    
    for idx, row in data.iterrows():
        fig.add_trace(go.Bar(
            name=f"Total {row['Category']}",
            x=[idx],
            y=[row['Total']],
            marker_color=main_colors[row['Category']],
            marker_line_color='rgba(255,255,255,0.3)',
            marker_line_width=1,
            width=0.6,
            text=format_number(row['Total']),
            textposition='outside',
            textfont=dict(size=14, color='#293241'),
            legendgroup='Total',
            showlegend=True
        ))
        
        y_bottom = 0
        sub_cats = row['SubCategories']
        for sub_idx, (sub_name, sub_value) in enumerate(sub_cats.items()):
            fig.add_trace(go.Bar(
                name=f"{sub_name}",
                x=[idx],
                y=[sub_value],
                base=y_bottom,
                marker_color=sub_colors[row['Category']][sub_idx],
                marker_line_color='rgba(255,255,255,0.5)',
                marker_line_width=1,
                width=0.45,
                text=format_number(sub_value),
                textposition='inside',
                textfont=dict(size=12, color='white'),
                legendgroup=row['Category'],
                showlegend=True
            ))
            y_bottom += sub_value

    fig.update_layout(
        title=dict(
            text='Revenue Breakdown by Category',
            font=dict(size=24, color='#293241'),
            x=0.5,
            y=0.95
        ),
        barmode='overlay',
        height=700,
        width=1000,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#293241',
            borderwidth=1
        ),
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family='Arial', color='#293241'),
        yaxis=dict(
            gridcolor='rgba(41,50,65,0.1)',
            linecolor='#293241',
            linewidth=1,
            title='Revenue'
        ),
        xaxis=dict(
            ticktext=data['Category'].tolist(),
            tickvals=list(range(len(data))),
            linecolor='#293241',
            linewidth=1
        )
    )

    fig.write_image("嵌套柱形图_style_1.png", scale=2)
    return fig

def plot_2(data):
    """
    现代简约风格：渐变色系
    """
    fig = go.Figure()
    
    main_colors = {
        'Electronics': 'rgba(255, 75, 104, 0.2)',
        'Furniture': 'rgba(255, 145, 77, 0.2)',
        'Clothing': 'rgba(255, 198, 54, 0.2)'
    }
    
    sub_colors = {
        'Electronics': ['#ff4b68', '#ff7285', '#ff99a3'],
        'Furniture': ['#ff914d', '#ffab74', '#ffc59b'],
        'Clothing': ['#ffc636', '#ffd469', '#ffe29c']
    }

    def format_number(num):
        return f"{num:,.0f}"

    x_positions = list(range(len(data)))
    
    for idx, row in data.iterrows():
        fig.add_trace(go.Bar(
            name=f"Total {row['Category']}",
            x=[idx],
            y=[row['Total']],
            marker_color=main_colors[row['Category']],
            width=0.7,
            text=format_number(row['Total']),
            textposition='outside',
            textfont=dict(size=14),
            legendgroup='Total',
            showlegend=True
        ))
        
        y_bottom = 0
        sub_cats = row['SubCategories']
        for sub_idx, (sub_name, sub_value) in enumerate(sub_cats.items()):
            fig.add_trace(go.Bar(
                name=f"{sub_name}",
                x=[idx],
                y=[sub_value],
                base=y_bottom,
                marker_color=sub_colors[row['Category']][sub_idx],
                width=0.55,
                text=format_number(sub_value),
                textposition='inside',
                textfont=dict(size=12, color='white'),
                legendgroup=row['Category'],
                showlegend=True
            ))
            y_bottom += sub_value

    fig.update_layout(
        title=dict(
            text='Revenue Breakdown by Category',
            font=dict(size=24),
            x=0.5,
            y=0.95
        ),
        barmode='overlay',
        height=700,
        width=1000,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5
        ),
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family='Helvetica'),
        yaxis=dict(
            gridcolor='rgba(0,0,0,0.05)',
            showline=False
        ),
        xaxis=dict(
            ticktext=data['Category'].tolist(),
            tickvals=list(range(len(data))),
            showline=False
        )
    )

    fig.write_image("嵌套柱形图_style_2.png", scale=2)
    return fig

def plot_3(data):
    """
    科技风格：蓝色渐变主题
    """
    fig = go.Figure()
    
    main_colors = {
        'Electronics': 'rgba(0, 150, 255, 0.2)',
        'Furniture': 'rgba(0, 200, 255, 0.2)',
        'Clothing': 'rgba(0, 255, 255, 0.2)'
    }
    
    sub_colors = {
        'Electronics': ['#0096ff', '#33abff', '#66c0ff'],
        'Furniture': ['#00c8ff', '#33d4ff', '#66dfff'],
        'Clothing': ['#00ffff', '#33ffff', '#66ffff']
    }

    def format_number(num):
        return f"{num:,.0f}"

    x_positions = list(range(len(data)))
    
    for idx, row in data.iterrows():
        fig.add_trace(go.Bar(
            name=f"Total {row['Category']}",
            x=[idx],
            y=[row['Total']],
            marker_color=main_colors[row['Category']],
            marker_line_color='rgba(255,255,255,0.5)',
            width=0.65,
            text=format_number(row['Total']),
            textposition='outside',
            textfont=dict(size=14),
            legendgroup='Total',
            showlegend=True
        ))
        
        y_bottom = 0
        sub_cats = row['SubCategories']
        for sub_idx, (sub_name, sub_value) in enumerate(sub_cats.items()):
            fig.add_trace(go.Bar(
                name=f"{sub_name}",
                x=[idx],
                y=[sub_value],
                base=y_bottom,
                marker_color=sub_colors[row['Category']][sub_idx],
                width=0.5,
                text=format_number(sub_value),
                textposition='inside',
                textfont=dict(size=12, color='white'),
                legendgroup=row['Category'],
                showlegend=True
            ))
            y_bottom += sub_value

    fig.update_layout(
        title=dict(
            text='Revenue Breakdown by Category',
            font=dict(size=24),
            x=0.5,
            y=0.95
        ),
        barmode='overlay',
        height=700,
        width=1000,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(240,240,240,0.9)'
        ),
        paper_bgcolor='#f8f9fa',
        plot_bgcolor='#f8f9fa',
        font=dict(family='Arial'),
        yaxis=dict(
            gridcolor='rgba(255,255,255,0.5)',
            showline=True,
            linecolor='rgba(0,0,0,0.1)'
        ),
        xaxis=dict(
            ticktext=data['Category'].tolist(),
            tickvals=list(range(len(data))),
            showline=True,
            linecolor='rgba(0,0,0,0.1)'
        )
    )

    fig.write_image("嵌套柱形图_style_3.png", scale=2)
    return fig

def plot_4(data):
    """
    自然环保风格：绿色主题
    """
    fig = go.Figure()
    
    main_colors = {
        'Electronics': 'rgba(76, 175, 80, 0.2)',
        'Furniture': 'rgba(139, 195, 74, 0.2)',
        'Clothing': 'rgba(205, 220, 57, 0.2)'
    }
    
    sub_colors = {
        'Electronics': ['#4caf50', '#66bb6a', '#81c784'],
        'Furniture': ['#8bc34a', '#9ccc65', '#aed581'],
        'Clothing': ['#cddc39', '#d4e157', '#dce775']
    }

    def format_number(num):
        return f"{num:,.0f}"

    x_positions = list(range(len(data)))
    
    for idx, row in data.iterrows():
        fig.add_trace(go.Bar(
            name=f"Total {row['Category']}",
            x=[idx],
            y=[row['Total']],
            marker_color=main_colors[row['Category']],
            width=0.65,
            text=format_number(row['Total']),
            textposition='outside',
            textfont=dict(size=14),
            legendgroup='Total',
            showlegend=True
        ))
        
        y_bottom = 0
        sub_cats = row['SubCategories']
        for sub_idx, (sub_name, sub_value) in enumerate(sub_cats.items()):
            fig.add_trace(go.Bar(
                name=f"{sub_name}",
                x=[idx],
                y=[sub_value],
                base=y_bottom,
                marker_color=sub_colors[row['Category']][sub_idx],
                width=0.5,
                text=format_number(sub_value),
                textposition='inside',
                textfont=dict(size=12, color='white'),
                legendgroup=row['Category'],
                showlegend=True
            ))
            y_bottom += sub_value

    fig.update_layout(
        title=dict(
            text='Revenue Breakdown by Category',
            font=dict(size=24),
            x=0.5,
            y=0.95
        ),
        barmode='overlay',
        height=700,
        width=1000,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(255,255,255,0.9)'
        ),
        paper_bgcolor='#f1f8e9',
        plot_bgcolor='#f1f8e9',
        font=dict(family='Verdana'),
        yaxis=dict(
            gridcolor='rgba(255,255,255,0.5)',
            showline=True,
            linecolor='rgba(76,175,80,0.3)'
        ),
        xaxis=dict(
            ticktext=data['Category'].tolist(),
            tickvals=list(range(len(data))),
            showline=True,
            linecolor='rgba(76,175,80,0.3)'
        )
    )

    fig.write_image("嵌套柱形图_style_4.png", scale=2)
    return fig

def plot_5(data):
    """
    时尚风格：高对比度配色
    """
    fig = go.Figure()
    
    main_colors = {
        'Electronics': 'rgba(233, 30, 99, 0.2)', 
        'Furniture': 'rgba(156, 39, 176, 0.2)',
        'Clothing': 'rgba(103, 58, 183, 0.2)'
    }
    
    sub_colors = {
        'Electronics': ['#e91e63', '#ec407a', '#f06292'],
        'Furniture': ['#9c27b0', '#ab47bc', '#ba68c8'],
        'Clothing': ['#673ab7', '#7e57c2', '#9575cd']
    }

    def format_number(num):
        return f"{num:,.0f}"

    x_positions = list(range(len(data)))
    
    for idx, row in data.iterrows():
        fig.add_trace(go.Bar(
            name=f"Total {row['Category']}",
            x=[idx],
            y=[row['Total']],
            marker_color=main_colors[row['Category']],
            marker_line_color='rgba(255,255,255,0.5)',
            marker_line_width=2,
            width=0.7,
            text=format_number(row['Total']),
            textposition='outside',
            textfont=dict(size=14),
            legendgroup='Total',
            showlegend=True
        ))
        
        y_bottom = 0
        sub_cats = row['SubCategories']
        for sub_idx, (sub_name, sub_value) in enumerate(sub_cats.items()):
            fig.add_trace(go.Bar(
                name=f"{sub_name}",
                x=[idx],
                y=[sub_value],
                base=y_bottom,
                marker_color=sub_colors[row['Category']][sub_idx],
                marker_line_color='rgba(255,255,255,0.5)',
                marker_line_width=1,
                width=0.55,
                text=format_number(sub_value),
                textposition='inside',
                textfont=dict(size=12, color='white'),
                legendgroup=row['Category'],
                showlegend=True
            ))
            y_bottom += sub_value

    fig.update_layout(
        title=dict(
            text='Revenue Breakdown by Category',
            font=dict(size=24, family='Roboto'),
            x=0.5,
            y=0.95
        ),
        barmode='overlay',
        height=700,
        width=1000,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='rgba(0,0,0,0.1)',
            borderwidth=1
        ),
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family='Roboto'),
        yaxis=dict(
            gridcolor='rgba(0,0,0,0.05)',
            showline=True,
            linecolor='rgba(0,0,0,0.1)',
            linewidth=1,
            title=dict(
                text='Revenue',
                font=dict(size=14)
            )
        ),
        xaxis=dict(
            ticktext=data['Category'].tolist(),
            tickvals=list(range(len(data))),
            showline=True,
            linecolor='rgba(0,0,0,0.1)',
            linewidth=1,
            title=dict(
                text='Categories',
                font=dict(size=14)
            )
        )
    )

    # 添加水印效果
    fig.add_annotation(
        text="Fashion Style",
        x=0.5,
        y=0.5,
        showarrow=False,
        font=dict(
            size=60,
            color='rgba(0,0,0,0.03)'
        ),
        xref='paper',
        yref='paper'
    )

    fig.write_image("嵌套柱形图_style_5.png", scale=2)
    return fig

data = preprocess()
plot(data)
plot_1(data)
plot_2(data)
plot_3(data)
plot_4(data)
plot_5(data)
