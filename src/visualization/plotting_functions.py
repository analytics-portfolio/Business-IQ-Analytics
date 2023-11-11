import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(column_data, column_name, bin=30):
    """
    Use histogram to plot distribution of a column of float values.

    Parameters:
    - data: Pandas DataFrame or Series containing the data.
    - column_name: Name of the column to plot.
    """
    # Create a histogram to visualize the distribution
    plt.figure(figsize=(8, 6))
    plt.hist(column_data, bins=bin, color='skyblue', edgecolor='black', alpha=0.7)
    
    # Add labels and a title
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {column_name}')
    
    # Show the plot
    plt.show()


def plot_horizontal_bar_chart(data, labels, title, x_label, y_label):
    """
    Create a horizontal bar chart with customizations.

    Parameters:
    - data (list): The data values for the bars.
    - labels (list): Labels for each bar.
    - title (str): The title of the chart.
    - x_label (str): Label for the x-axis.
    - y_label (str): Label for the y-axis.

    Returns:
    - None (displays the chart).
    """
    # Create a horizontal bar chart
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(labels, data, color='skyblue')
    
    # Customize the chart
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.invert_yaxis()  # Invert the y-axis to show the highest value at the top
    
    # Add data values on the bars
    for i, v in enumerate(data):
        ax.text(v + 0.1, i, str(v), color='black', va='center', fontsize=10)
    
    # Customize the grid
    ax.grid(axis='x', linestyle='--', alpha=0.6)

    # Show the chart
    plt.show()


def plot_horizontal_boxplot(data, orient='h', color="0.8",
                              title='', x_label='', y_label='', 
                              x_ticks=None, y_ticks=None, figsize=(10, 6)):
    """
    Generate a customizable horizontal box plot using Seaborn.

    Parameters:
    - data: Pandas DataFrame or Series containing the data.
    - orient: Orientation of the box plot ('h' for horizontal, 'v' for vertical).
    - color: Color of the boxes and whiskers.
    - title: Title of the plot.
    - x_label: Label for the x-axis.
    - y_label: Label for the y-axis.
    - x_ticks: Custom x-axis tick labels.
    - y_ticks: Custom y-axis tick labels.
    - figsize: Figure size (width, height) in inches.

    Returns:
    - A Seaborn box plot.
    """
    # Set Seaborn style
    sns.set(style="whitegrid")
    
    # Create the plot
    plt.figure(figsize=figsize)
    
    if orient == 'h':
        plot = sns.boxplot(data=data, orient='h', color=color)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        
        # Customize x-axis ticks if provided
        if x_ticks is not None:
            plt.xticks(x_ticks)
    elif orient == 'v':
        plot = sns.boxplot(data=data, orient='v', color=color)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        
        # Customize y-axis ticks if provided
        if y_ticks is not None:
            plt.yticks(y_ticks)
    
    plt.tight_layout()
    
    return plot

def create_location_map(data, zoom_start=12, 
                        title="Restaurant Map", 
                        icon_color="blue", 
                        save_filename="restaurant_map.html"):
    """
    Create a location visualization map using Folium.

    Parameters:
    - data (DataFrame): DataFrame containing location data (latitude, longitude, name).
    - zoom_start (int): Initial zoom level for the map (default is 12).
    - title (str): Title for the map (default is "Restaurant Map").
    - icon_color (str): Marker icon color (default is "blue").
    - save_filename (str): Filename to save the map as an HTML file (default is "restaurant_map.html").

    Returns:
    - None
    """

    # Create the map
    m = folium.Map(location=[data['latitude'].mean(), 
                             data['longitude'].mean()], 
                             zoom_start=zoom_start, 
                             tiles='cartodb positron')

    # Add markers for each location
    for _, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['name'],
            icon=folium.Icon(color=icon_color)
        ).add_to(m)

    # Add a title to the map
    folium.map.Marker(
        location=[data['latitude'].mean(), data['longitude'].mean()],
        icon=None,
        popup=folium.map.Popup(title),
    ).add_to(m)

    # Save the map as an HTML file
    m.save(save_filename)

# Example usage:
# Replace 'steakhouses' with your DataFrame containing location data.
# create_location_map(steakhouses)

def plot_bubble_chart(data, 
                    x_axis, y_axis, 
                    bubble_size, color, 
                    hover_name, 
                    title, size_max=50, 
                    figsize=(1000, 700),
                    color_discrete_sequence=None, 
                    template='plotly', 
                    x_title=None, y_title=None, 
                    color_continuous_scale=None,
                    font_size=12):

    fig = px.scatter(data,
                     x=x_axis,
                     y=y_axis,
                     size=bubble_size,
                     color=color,
                     hover_name=hover_name,
                     hover_data={x_axis: ':.2f', y_axis: True, bubble_size: True},
                     title=title,
                     size_max=size_max,
                     color_discrete_sequence=color_discrete_sequence,
                     template=template,
                     color_continuous_scale=color_continuous_scale)

    # Customize axis titles
    fig.update_layout(
        font=dict(
        family="Helvetica Neue",
        size=font_size,  # Set the font size here
        # color="RebeccaPurple"
    ),
        xaxis_title=x_title if x_title else x_axis,
        yaxis_title=y_title if y_title else y_axis,
    )

    fig.update_layout(legend = dict(font = dict(size = 11)),
                      legend_title = dict(font = dict(size = 11)))
    
    fig.update_layout(
    legend=dict(x=0.5, y=-0.2, xanchor='center', yanchor='top'), # Adjust y to move legend inside subplot
    legend_orientation='h'
)
    # fig.update_layout(width=figsize[0], height=figsize[1], autosize=True)
    fig.update_layout(autosize=True)
    fig.write_html("./demo_plots/bb_chart.html")
    fig.show()

def plot_stacked_vertical_bar_chart(data, 
                               x_col, y_col1, y_col2, 
                               x_label, y_label,
                               title='',
                               color1='green',color2='orange'):
    """
    Create a stacked vertical bar chart using Seaborn.

    Parameters:
    - data: DataFrame containing the data.
    - x_col: Name of the column for the x-axis (e.g., 'Year').
    - y_col1: Name of the first data column for stacking.
    - y_col2: Name of the second data column for stacking.
    - title: Title of the plot.

    Returns:
    - A Seaborn stacked vertical bar chart.
    """
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    sns.set(style="whitegrid")
    
    # Use the Seaborn barplot function to create the stacked bar chart
    sns.barplot(x=x_col, y=y_col1, data=data, color=color1, label=y_col1)
    sns.barplot(x=x_col, y=y_col2, data=data, color=color2, label=y_col2, bottom=data[y_col1])
    
    # Customize the plot
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    
    # Add a legend
    plt.legend(title="", loc="upper left")
    plt.savefig("./demo_plots/stacked_bar_chart.svg", format='svg')
    
    # Show the plot
    plt.show()

def plot_bar_and_line_chart(data, col_bar_y1, col_line_y2, col_x, 
                            y1_label="", y2_label="", x_label="",
                            title="",
                            bar_color="b", line_color="r",
                            figsize=(10, 6)):

    # Extract the years, number of ratings, and average star values from the data
    x = data[col_x]
    bar_y1 = data[col_bar_y1]
    line_y2 = data[col_line_y2]

    # Create a figure and axis for the plot
    fig, ax1 = plt.subplots(figsize=figsize)

    # Bar chart:
    ax1.bar(x=x, height=bar_y1, color=bar_color, alpha=0.5, label=y1_label)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y1_label)
    ax1.tick_params(axis='y')
    
    
    # Create a second y-axis for the line chart
    ax2 = ax1.twinx()

    # Line chart:
    ax2.plot(x, line_y2, color=line_color, marker='o', label=y2_label)
    ax2.set_ylabel(y2_label)
    ax2.grid(visible=False)

    # Add a legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

    # Set the title and x-axis label
    plt.title(title)
    plt.xlabel('Year')
    ax2.set_ylim(top=5, bottom=0)
    plt.savefig("./demo_plots/bar_line_chart.svg", format='svg')
    
    # save .html file
    # plt.write_html(save_filename, auto_open=False)

    # Show the plot
    plt.show()