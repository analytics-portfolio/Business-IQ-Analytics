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

reviews = pd.read_pickle("https://github.com/analytics-portfolio/Business-IQ-Analytics/blob/main/data/demo_data/reviews_steak.pkl?raw=true")

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
# def plot_bubble_chart(data):
#     ...

### BUBBLE CHART DATA
top_7_num_reviewed = reviews[['name']].value_counts().head(7)

top_7_num_reviewed = [i[0] for i in top_7_num_reviewed.index]

bb_chart = {
    'Restaurant': [],
    'Average_Star_Rating': [],
    'Number_of_Reviews': [],
    'Years_of_Operation': []
}
for r in top_7_num_reviewed:
    bb_chart['Restaurant'].append(r)
    data = reviews.loc[reviews['name'] == r]
    avg_rating = sum(data['stars_x'])/len(data['stars_x'])
    bb_chart['Average_Star_Rating'].append(round(avg_rating, 3))

    num_rev = len(data['stars_x'])
    bb_chart['Number_of_Reviews'].append(num_rev)

    year_op = max(data.dt_year) - min(data.dt_year)
    bb_chart['Years_of_Operation'].append(year_op)


# Run the app
if __name__ == '__main__':
    
    app.run_server(debug=True)
