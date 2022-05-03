import spacy
import sqlite3
import pandas as pd

def extract_nonstops(text):
    nlp = spacy.load("en_core_web_sm")
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    result = []
    doc = nlp(text.lower())
    for token in doc:
        if not (token.text in nlp.Defaults.stop_words or token.text in punctuation):
            result.append(token.lemma_)
    return result


def extract_all_words(text):
    nlp = spacy.load("en_core_web_sm")
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    result = []
    pos_tag = [ 'ADJ', 'NOUN']
    doc = nlp(text.lower())
    for token in doc:
        if (token.pos_ in pos_tag) and not (token.text in nlp.Defaults.stop_words or token.text in punctuation):
            result.append(token.lemma_)
    return result

def words_count(words):
    kwds = {}
    for w in words:
        if w not in kwds:
            kwds[w]=1
        else:
            kwds[w]+=1
    return kwds

def common_words(words_dict, n=3):
    vals = list(words_dict.values())
    vals.sort(reverse=True)
    words = [k for k,v in words_dict.items() if v >= vals[n-1]]
    return words

def extract_words(text, n=3):
    hotwords = extract_all_words(text)
    words_dict = words_count(hotwords)
    vals = list(words_dict.values())
    vals.sort(reverse=True)
    words = [k for k,v in words_dict.items() if v >= vals[n-1]]
    words = ', '.join(words)
    return words


# Extract default values for 'unitest'

if __name__ == '__main__':

    # Test NLP functions
    text = '''Python is one of the most popular programming languages today
and is easy for beginners to learn because of its readability.
It is a free, open-source programming language with extensive support modules
and community development, easy integration with web services, user-friendly
data structures, and GUI-based desktop applications. '''

    nostops = extract_nonstops(text)
    hotwords = extract_words(text)
    words = extract_all_words(text)
    words_dict = words_count(words)
    keywords = common_words(words_dict)
    print('extract_nonstops >>>', nostops)
    print('extract_all_words >>>', words)
    print('extract_words >>>', hotwords)
    print('words_count  >>>',words_dict)
    print('words_count  >>>',keywords)

