import re, string
from collections import Counter
from sklearn.model_selection import train_test_split

# Text cleaning helper functions
def clean_text(text):
    """Basic text cleaning: lowercasing, removing punctuation and digits."""
    text = text.lower()  # Lowercasing
    text = re.sub(r'\d+', '', text)  # Removing digits
    text = text.translate(str.maketrans('', '', string.punctuation))  # Removing punctuation
    return text

def remove_stopwords(text, stopwords):
    """Remove stopwords from text."""
    words = text.split()
    return ' '.join([word for word in words if word not in stopwords])

# Tokenization
def tokenize(text, token='whitespace'):
    """
    Tokenizes text based on the specified token.
    
    Parameters:
    - text (str): The text to tokenize.
    - token (str): The token type to use for splitting. Options are:
        - 'whitespace': Split on whitespace (default).
        - 'custom': Use a custom regular expression (provide custom regex as a second argument).
    
    Returns:
    - list: List of tokens.
    """
    
    if token == 'whitespace':
        return text.split()  # Splits on any whitespace
    elif isinstance(token, str):
        return re.split(token, text)  # Uses custom regex if provided
    else:
        raise ValueError("Invalid token type specified. Use 'whitespace', or a custom regex.") 

def word_counts(text):
    """Returns a frequency distribution of words in text."""
    tokens = tokenize(text)
    return Counter(tokens)

# Data splitting
def split_data(X, y, test_size=0.2, random_state=42):
    """Splits data into training and testing sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

