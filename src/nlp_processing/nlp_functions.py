import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from afinn import Afinn

from nltk.util import ngrams
from collections import Counter

stop_words = set(stopwords.words('english'))


def calculate_sentiment(review_column):
    # Tokenize and preprocess the review text
    def preprocess_text(text):
        tokens = nltk.word_tokenize(text.lower())  # Tokenization and lowercasing
        tokens = [token for token in tokens if token.isalpha()]  # Remove punctuation
        tokens = [token for token in tokens if token not in stopwords.words('english')]  # Remove stopwords
        return tokens

    # Function to handle negation
    def handle_negation(tokens):
        negation = False
        negated_tokens = []
        for token in tokens:
            if token in ["not", "no", "never"]:
                negation = not negation
            elif negation:
                negated_tokens.append("neg_" + token)
            else:
                negated_tokens.append(token)
        return negated_tokens

    # Calculate sentiment score for a list of tokens
    def calculate_token_sentiment(tokens):
        if len(tokens) >= 5:  # Apply sentiment analysis only if there are 5 or more tokens
            sentiment_scores = [afinn.score(token) for token in tokens]
            return sum(sentiment_scores) / max(len(tokens), 1)  # Calculate mean score
        else:
            return None  # Return None for short reviews
        
    # Preprocess and handle negation for each review
    processed_reviews = review_column.apply(preprocess_text)
    negated_reviews = processed_reviews.apply(handle_negation)

    # Calculate sentiment scores for each review
    sentiment_scores = negated_reviews.apply(calculate_token_sentiment)

    return sentiment_scores

# Optionally, apply thresholds or labels to categorize sentiment
def categorize_sentiment(score):
    if score > 0:
        return 'positive'
    elif score < 0:
        return 'negative'
    else:
        return 'neutral'


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