import spacy
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text)
    result = [token.lemma_ for token in doc if token.text.lower() not in STOP_WORDS and token.is_alpha]
    return result

# Example usage
if __name__ == "__main__":
    text = "Cats are running quickly through the garden while chasing birds."
    processed = preprocess(text)
    print("Processed Tokens:", processed)
