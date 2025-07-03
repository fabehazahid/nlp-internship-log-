import re
from gensim.models import Word2Vec

# Sample corpus
corpus = [
    "Natural language processing is fun",
    "Word embeddings capture semantic relationships",
    "CBOW predicts a word using its context"
]

# Clean and tokenize sentences
def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()

tokenized_corpus = [preprocess(sentence) for sentence in corpus]

# Train Word2Vec using CBOW (sg=0)
cbow_model = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=100,
    window=3,
    min_count=1,
    sg=0
)

# Check the vector of a word
print("Vector for 'cbow':")
print(cbow_model.wv['cbow'])

# Check most similar words
print("\nWords similar to 'word':")
print(cbow_model.wv.most_similar('word'))
