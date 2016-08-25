import nltk
import os

cur_dir = os.path.split(os.path.realpath(__file__))[0]
print cur_dir

class SpliterCom() :

    def __init__(self) :
        self.stopwords = open(cur_dir + '/stopwords_en.txt', 'r').read().split()

    def process(self, sent) :
        sent = [word for word in sent.split() if word not in self.stopwords]
        return sent


