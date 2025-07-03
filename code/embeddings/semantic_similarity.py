import re
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample corpus
corpus = [
    "Machine learning is awesome",
    "Deep learning is a subset of machine learning",
    "Artificial intelligence includes ML and DL"
]

# Preprocess
def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()

tokenized = [preprocess(sentence) for sentence in corpus]

# Train embeddings
model = Word2Vec(sentences=tokenized, vector_size=100, window=3, min_count=1, sg=1)

# Function to compare words
def compare_words(w1, w2):
    if w1 not in model.wv or w2 not in model.wv:
        print("One or both words not in vocabulary.")
        return

    v1 = model.wv[w1].reshape(1, -1)
    v2 = model.wv[w2].reshape(1, -1)
    score = cosine_similarity(v1, v2)[0][0]

    print(f"Similarity between '{w1}' and '{w2}': {score:.2f}")

# Test
compare_words("machine", "learning")
compare_words("machine", "subset")
