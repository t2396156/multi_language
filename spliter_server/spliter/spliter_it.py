import nltk
import os
cur_dir = os.path.split(os.path.realpath(__file__))[0]

class SpliterIt() :

    def __init__(self) :
        self.stopwords = open(cur_dir + '/stopwords_it.txt', 'r').read().split()
    
    def process(self, sent):
        sent = [word for word in nltk.word_tokenize(sent, language='italian') if word not in self.stopwords]
        return sent
        

