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


def custom_horizontal_boxplot(data, orient='h', color="0.8",
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
