# Agentic AI Internship – Weekly Progress (Weeks 1–3)

**Fabeha Zahid Mahmood**

This repository contains the documented progress of my internship focused on Natural Language Processing (NLP) and its applications in Agentic AI. The work includes both conceptual learning and hands-on implementations of NLP pipelines, word embeddings, and transformer-based methods.

---

## Week 1 & 2 – NLP Foundations

### 1. NLP Overview
Natural Language Processing (NLP) is a core subfield of AI that deals with machine understanding, generation, and interpretation of human language. It powers applications such as chatbots, search engines, and recommendation systems.

### 2. Analysis vs Synthesis in NLP
- **Analysis:** Understanding and breaking down language (POS tagging, parsing, sentiment analysis).
- **Synthesis:** Generating new language output (translation, summarization, text generation).

### 3. Core NLP Techniques Explored
- Sentiment Analysis
- Named Entity Recognition (NER)
- Text Classification
- Topic Modeling
- Text Summarization
- Question Answering
- Language Translation

### 4. NLP Pipeline and Tools
Standard steps involved:
1. Data acquisition  
2. Text cleaning  
3. Tokenization  
4. Stopword removal  
5. Stemming/Lemmatization  
6. Embedding/vectorization  
7. Modeling and inference  

Tools used:
- **NLTK** – Tokenization, stopword removal, stemming
- **spaCy** – Tokenization, lemmatization, POS tagging, NER
- **Gensim** – Word2Vec embeddings
- **NumPy** – Vector operations, cosine similarity
- **Pandas** – Data transformation and handling

### 5. Data Cleaning with Regex
Regular expressions were used to clean unstructured text by removing URLs, special characters, HTML tags, and numbers.

### 6. Preprocessing Techniques
- **Tokenization:** Splitting text into individual tokens.
- **Stemming:** Reducing words to their root form.
- **Lemmatization:** Converting words to base form using context.

### 7. N-Grams
Explored bigrams and trigrams for phrase-level pattern analysis using a demo script.

### 8. Word Embeddings and Similarity
- Built custom Word2Vec models (CBOW and Skip-Gram).
- Used cosine similarity to compare semantic similarity between documents for tasks like book recommendation.

### 9. spaCy Overview
Used for efficient NLP operations such as:
- Tokenization
- POS tagging
- Dependency parsing
- Lemmatization
- NER

### 10. Basics of Neural Networks in NLP
Covered theoretical understanding of:
- Activation functions
- Layered architecture
- Backpropagation
- Applications in classification and sequence modeling

### 11. Transformers and Architectures
Worked on a Jupyter Notebook presentation explaining:
- Self-attention mechanism
- Positional encoding
- Encoder-decoder models
- Use in classification, QA, summarization

### 12. Vector Databases and Pinecone
Learned to store high-dimensional vectors in Pinecone for efficient similarity search and retrieval, useful in recommendation systems.

### 13. Prompt Engineering (Side Learning)
Completed Google’s AI Essentials course. Key takeaways:
- Clear and specific prompt writing
- Use of examples
- Structuring instructions to reduce ambiguity
- Adaptive prompting

---

## Week 3 – Implementation and Projects

### Code Snippets

All scripts are available in the `code/` directory.

- `regex_cleaning.py` – Clean raw text using regex
- `tokenization_practice.py` – Tokenize text with NLTK/spaCy
- `stopwords_lemmatization.py` – Remove stopwords, apply lemmatization
- `ngram_demo.py` – Generate bigrams/trigrams
- `embeddings_cosine_similarity.py` – Calculate semantic similarity
- `cbow_skipgram_word2vec.py` – Basic Word2Vec implementation (CBOW & Skip-Gram)
amongst others

### Book Recommender System

A complete book recommendation system using semantic similarity on book summaries with Word2Vec embeddings. The system uses cosine similarity to recommend similar books based on input text. Preprocessed data, model code, and results are included.

Link for access:
https://github.com/fabehazahid/Book-Recommender

### Transformers Presentation

The `transformers_presentation.ipynb` notebook contains a ten-minute conceptual walkthrough of transformers and their architecture.
---

## Files Included

- `NLP_Internship_Report_Week1_2.docx` – Written summary of weeks 1 and 2
- `resources.docx` – Study resources and notes
- `transformers_presentation.ipynb` – 
- `code/` – All implementation scripts
- `README.md` – Project overview and documentation

---
