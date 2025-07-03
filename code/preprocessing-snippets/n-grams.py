import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

nltk.download("punkt")

def generate_ngrams(text, n=2):
    tokens = word_tokenize(text.lower())
    return list(ngrams(tokens, n))

# Example usage
if __name__ == "__main__":
    text = "Natural language processing with Python is fun."
    print("Bigrams:", generate_ngrams(text, 2))
    print("Trigrams:", generate_ngrams(text, 3))
