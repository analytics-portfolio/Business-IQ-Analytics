import pandas as pd
import pickle

def save_df_to_pickle(dataframe, filename):
    """
    Save a DataFrame to a pickle file.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame to be saved.
    - filename (str): The name of the pickle file (including file extension).

    Returns:
    - None
    """
    with open(filename, 'wb') as file:
        pickle.dump(dataframe, file)

def load_df_from_pickle(filename):
    """
    Load a DataFrame from a pickle file.

    Parameters:
    - filename (str): The name of the pickle file to load.

    Returns:
    - pd.DataFrame: The loaded DataFrame.
    """
    with open(filename, 'rb') as file:
        loaded_dataframe = pickle.load(file)
    return loaded_dataframe
