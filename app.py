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
steakhouses_dir = "./data/demo_data/steakhouses.pkl"
reviews_dir =  "./data/demo_data/reviews_steak.pkl"

# Import Data
steakhouses = load_df_from_pickle(steakhouses_dir)
reviews = load_df_from_pickle(reviews_dir)




# Main function
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080)