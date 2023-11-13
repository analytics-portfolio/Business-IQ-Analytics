import pandas as pd
import numpy as np

import dash
from dash.dependencies import Input, Output
from dash import html, dcc

import plotly.express as px
import plotly.graph_objects as go

import sys
# sys.path.append('../data_manipulation/')
# from data_manipulation import *

steakhouses_dir = "../data/demo_data/steakhouses.pkl"
reviews_dir =  "../data/demo_data/reviews_steak.pkl"

app = dash.Dash(__name__)

# Import Data
# steakhouses = load_df_from_pickle(steakhouses_dir)
# reviews = load_df_from_pickle(reviews_dir)

data = pd.read_pickle("https://github.com/analytics-portfolio/Business-IQ-Analytics/blob/main/data/demo_data/reviews_steak.pkl?raw=true")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    # Split the screen into two vertical spaces
    html.Div([
        # Left side with 4 quadrants
        html.Div([
            # Upper left quadrant - Stacked Bar Chart (Placeholder)
            dcc.Graph(id='stacked-bar-chart'),

            # Lower left quadrant - Bar and Line Chart (Placeholder)
            dcc.Graph(id='bar-line-chart')
        ], style={'width': '50%', 'display': 'inline-block'}),

        # Right side - Bubble Chart
        html.Div([
            dcc.Graph(
                id='bubble-chart',
                figure=plot_bubble_chart(data)  # Assuming your function returns a Figure object
            )
        ], style={'width': '50%', 'display': 'inline-block'}),
    ])
])

# Define callbacks to update graphs if necessary
@app.callback(
    Output('stacked-bar-chart', 'figure'),
    [Input('input-component', 'value')]  # Example of an input component
)
def update_stacked_bar_chart(value):
    # Logic to update stacked bar chart
    # Placeholder for demo
    return px.bar(data, x="x-axis", y="y-axis", color="category")

@app.callback(
    Output('bar-line-chart', 'figure'),
    [Input('input-component', 'value')]  # Example of an input component
)
def update_bar_line_chart(value):
    # Logic to update bar and line chart
    # Placeholder for demo
    return px.bar(data, x="x-axis", y="y-axis")

# Assuming your bubble chart function is defined elsewhere:
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

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
