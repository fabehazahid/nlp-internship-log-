from gensim.models import Word2Vec
import re

# Sample corpus with basic NLP and ML related sentences
corpus = [
    "Data science involves machine learning and statistics",
    "Natural language processing includes text mining",
    "Artificial intelligence is related to deep learning"
]

# Function to clean and tokenize the text
def preprocess(text):
    text = text.lower()  # convert to lowercase
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    return text.split()  # split into tokens (words)

# Apply preprocessing to all sentences
tokenized = [preprocess(s) for s in corpus]

# Train Word2Vec model using Skip-Gram (sg=1)
# vector_size: dimensionality of word vectors
# window: context window size
# min_count: minimum frequency to include a word
model = Word2Vec(
    sentences=tokenized,
    vector_size=100,
    window=3,
    min_count=1,
    sg=1  # sg=1 means Skip-Gram, sg=0 would mean CBOW
)

# Function to expand a single-word query with similar terms
def expand_query(term, topn=3):
    if term not in model.wv:
        print(f"'{term}' not in vocabulary.")
        return

    print(f"Query term: {term}")
    print("Related terms:")
    for word, score in model.wv.most_similar(term, topn=topn):
        print(f"- {word} ({score:.2f})")

# Example queries to test the model
expand_query("learning")
expand_query("text")
