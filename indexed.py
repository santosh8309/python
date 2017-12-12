from nltk.corpus import stopwords
from nltk.stem.porter import *
import re


raw = open("test", 'r')
tokens = re.split(r'\s+', raw.read())
stemmer = PorterStemmer()
words = [stemmer.stem(word) for word in tokens]
stop_words = set(stopwords.words("english"))
punctuation = re.compile(r'[-.?!,":;()|0-9]')

word_list = [punctuation.sub('', word) for word in words]
output = open("output", 'w')
for word in word_list:
    if word not in stop_words:
       output.write(word)
       output.write('\n')

       