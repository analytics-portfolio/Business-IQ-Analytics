import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import pickle

# Load the data from the .pkl file
# with open('reviews_steak.pkl', 'rb') as f:
#     data = pickle.load(f)

data = pd.read_pickle("https://github.com/analytics-portfolio/Business-IQ-Analytics/blob/main/data/demo_data/reviews_steak.pkl?raw=true")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    # Top Toggle Dropdown for selecting the "Name"
    dcc.Dropdown(
        id='name-dropdown',
        options=[{'label': name, 'value': name} for name in data['Name'].unique()],
        value=data['Name'].unique()[0],  # Set default value
    ),

    # Left side of the dashboard with 4 quadrants
    html.Div([
        html.Div([
            dcc.Graph(id='stacked-bar-chart')
        ], className='six columns'),

        html.Div([
            dcc.Graph(id='bar-line-chart')
        ], className='six columns')
    ], className='row'),

    # Right side of the dashboard with folium map and bubble chart
    html.Div([
        html.Div([
            dcc.Graph(id='folium-map')
        ], className='six columns'),

        html.Div([
            dcc.Graph(id='bubble-chart')
        ], className='six columns')
    ], className='row')
])

# Define callback functions to update graphs based on dropdown selection
@app.callback(
    [Output('stacked-bar-chart', 'figure'),
     Output('bar-line-chart', 'figure'),
     Output('folium-map', 'figure'),
     Output('bubble-chart', 'figure')],
    [Input('name-dropdown', 'value')]
)
def update_graphs(selected_name):
    # Create and update the figures based on the selected "Name"
    # You'll need to define the logic for each graph here

    # Example: Create a dummy figure for the stacked bar chart
    stacked_bar_chart_figure = {
        'data': [{'x': [1, 2, 3], 'y': [10, 20, 30], 'type': 'bar', 'name': 'Trace 1'},
                 {'x': [1, 2, 3], 'y': [5, 10, 15], 'type': 'bar', 'name': 'Trace 2'}],
        'layout': {'title': f'Stacked Bar Chart for {selected_name}'}
    }

    # Repeat the above for other charts (bar-line chart, folium map, bubble chart)

    return stacked_bar_chart_figure, bar_line_chart_figure, folium_map_figure, bubble_chart_figure

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)