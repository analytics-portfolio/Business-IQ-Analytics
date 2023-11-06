import pandas as pd
import pickle

### LOAD DATA ###
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

###----------

def count_bigrams(df, text_col):
    # Tokenize the text and create bigrams
    bigrams = []
    stop_words = set(stopwords.words('english'))

    for text in df[text_col]:
         # char.isalnum() or
        text = ''.join(char for char in text if char.isalnum() or char.isspace())  # Remove punctuation and special characters
        tokens = nltk.word_tokenize(text.lower())  # Convert text to lowercase and tokenize
        bigrams.extend(list(ngrams(tokens, 2)))

    # Filter out bigrams with stop words
    filtered_bigrams = [bigram for bigram in bigrams if bigram[0] not in stop_words and bigram[1] not in stop_words]

    # Count the occurrences of each unique bigram pair
    bigram_counts = Counter(filtered_bigrams)

    # print(bigram_counts.items())
    # # Create a DataFrame with (word1, word2) and count columns
    w1 = [' '.join(i) for i in list(bigram_counts.keys())]
    w2 = list(bigram_counts.values())
    bigram_df = pd.DataFrame(zip(w1, w2), columns=['word', 'count'])
    # bigram_df['count'] = bigram_df['count']

    # # Sort the DataFrame by count in descending order
    bigram_df = bigram_df.sort_values(by='count', ascending=False).reset_index()

    return bigram_df