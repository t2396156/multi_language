import jieba
import os

cur_dir = os.path.split(os.path.realpath(__file__))[0]


class SpliterZh() :

    def __init__(self):
       	self.stopwords = open(cur_dir + '/stopwords_zh.txt', 'r').read().split()
        self.stopwords = [word.decode('utf-8') for word in self.stopwords]
    	jieba.initialize()
	
    def process(self, sent) :
        # stopwords = open('stopwords_zh.txt', 'r').read().split()
        # stopwords = [word.decode('utf-8') for word in stopwords]
        sent = [word for word in jieba.cut(sent.strip()) if word not in self.stopwords]
        return sent
