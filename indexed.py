from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re



raw = open("test",'r')
word_list = re.split(r'\s+', raw.read())
stop_words = set(stopwords.words("english"))
punctuation = re.compile(r'[-.?!,":;()|0-9]')

word_list = [punctuation.sub("",words) for words in word_list]

for word in word_list:
    tokens = []
    tokens +=  word_tokenize(word)
    for i in tokens:
        if i not in stop_words:
            print(i)






