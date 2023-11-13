import pandas as pd
import numpy as np
import pickle
import json
import os


### LOAD DATA ###

def save_data_to_pickle(data, file_path):
    """
    Save data to a file using pickle.

    Args:
        data: The data to be saved.
        file_path (str): The file path where the data will be saved.

    Returns:
        bool: True if the data was successfully saved, False otherwise.
    """
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(data, file)
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def load_data_from_pickle(file_path):
    """
    Load data from a pickle file.

    Args:
        file_path (str): The file path from which to load the data.

    Returns:
        object: The loaded data.
    """
    try:
        with open(file_path, 'rb') as file:
            loaded_data = pickle.load(file)
        return loaded_data
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


### LOAD JSON TO CSV ###