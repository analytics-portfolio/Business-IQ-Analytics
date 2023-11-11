import pandas as pd
import numpy as np


import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output

from functions_for_analysis.plotting_functions import *
from functions_for_analysis.data_analysis_function import *

app = dash.Dash(__name__)
steakhouses_dir = "../data/demo_data/steakhouses.pkl"
reviews_dir =  "../data/demo_data/reviews_steak.pkl"

# Import Data
steakhouses = load_df_from_pickle(steakhouses_dir)
reviews = load_df_from_pickle(reviews_dir)

app.layout = html.Div([
    dcc.Graph(
        id='interactive-graph',
        figure=px.scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13])
    )
])

# @app.callback(
#     Output('interactive-graph', 'figure'),
#     [Input('dropdown-menu', 'value')]  # Add inputs based on your design
# )
# def update_graph(selected_value):
#     # Modify the figure based on user input
#     # Update the 'figure' property of the graph accordingly
#     # Example: filtered_data = your_data[your_data['column'] == selected_value]
#     return px.scatter(filtered_data, x='x_column', y='y_column')


# Main function
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080)