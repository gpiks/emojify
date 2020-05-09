from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import re

special_characters = re.compile('[\.,@_!#$%^&*()<>?/\|}{~:]') 

def remove_stop_words(text):
    tokenized_text = word_tokenize(text)

    stop_words=set(stopwords.words("english"))
    filtered_text = []
    for w in tokenized_text:
        if w not in stop_words and not special_characters.search(w):
            filtered_text.append(w)

    return filtered_text
