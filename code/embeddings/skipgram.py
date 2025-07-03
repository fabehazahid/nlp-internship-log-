import re
from gensim.models import Word2Vec

# Sample corpus
corpus = [
    "Natural language processing is powerful",
    "Skip-gram learns word representations",
    "Context is predicted using the target word"
]

# Clean and tokenize
def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()

tokenized_corpus = [preprocess(sentence) for sentence in corpus]

# Train Word2Vec using Skip-Gram (sg=1)
skipgram_model = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=100,
    window=3,
    min_count=1,
    sg=1
)

# Check the vector for a word
print("Vector for 'skipgram':")
print(skipgram_model.wv['skipgram'])

# Check most similar words
print("\nWords similar to 'context':")
print(skipgram_model.wv.most_similar('context'))
