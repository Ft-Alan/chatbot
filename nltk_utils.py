import nltk
import numpy as np

# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def b_o_g(tokenised_sentence, all_words):
    tokenised_sentence = [stem(w) for w in tokenised_sentence]
    
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenised_sentence:
            bag[idx] = 1.0
    return bag