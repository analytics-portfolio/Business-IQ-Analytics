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


### LOAD EXCEL TO DF ###

def load_excel_to_dataframe(file_path, sheet_name=None):
    """
    Load data from an Excel file into a Pandas DataFrame.

    Args:
        file_path (str): The file path of the Excel file to be loaded.
        sheet_name (str or int, optional): The name or index of the sheet to read from. Defaults to the first sheet.

    Returns:
        pd.DataFrame: The loaded data as a Pandas DataFrame.
    """
    try:
        if sheet_name is None:
            # Load the first sheet by default
            df = pd.read_excel(file_path)
        else:
            # Load a specific sheet
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

