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
