import nltk
import os

cur_dir = os.path.split(os.path.realpath(__file__))[0]

class SpliterEs() :

    def __init__(self) :
        self.stopwords = open(cur_dir + '/stopwords_es.txt', 'r').read().split()
    
    def process(self, sent):
        sent = [word for word in nltk.word_tokenize(sent, language='spanish') if word not in self.stopwords]
        return sent
        

