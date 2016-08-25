# coding: utf-8

import gensim
import re
import sys, os
import json

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(cur_dir + '/gen-py'))
#print os.path.join(cur_dir + '/gen-py')

from kwServer import kwServer
from kwServer.ttypes import *

from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.server import TServer  
from thrift.server import TProcessPoolServer

import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=cur_dir + '/../logs/keywords.log',
                filemode='a')

import kw_config
sys.path.append(cur_dir + '/../idf_server')
sys.path.append(cur_dir + '/../spliter_server')
sys.path.append(cur_dir + '/../langid_server')

from idf_client import IdfClient
from split_client import SplitClient
from language_client import LanguageClient

class KwHandler:
    def __init__(self):
        self.tf_idf_dict= {} #{word: tfidf}
        self.tf_dict = {} #{word: tf}
        self.paras = [] #段落
        self.sentences = [] #句子
        self.words = [] #所有的单词
        self.idf_server = IdfClient()
        self.split_server = SplitClient()
        self.language_server = LanguageClient()

    def _init_variable(self):
        #批量清空
        self.tf_idf_dict = {}
        self.tf_dict = {}
        self.paras = []
        self.sentences = []
        self.words = []

    def phrase_detect(self, text):
        '''
            parm:
                text:分词之后的二维数组
            return:
                text_tri:合并短语之后的二维数组
        '''
        #短语合成，gensim自带的短语合成，跟语言无关
        #mini_count 出现次数小于mini_count就忽略不记
        #threshold 经验值是5，有待考证
        try:
            bigram = gensim.models.phrases.Phrases(text, min_count=2, threshold=5, delimiter='_')
            text_bi = bigram[text]
            trigram = gensim.models.phrases.Phrases(text_bi, min_count=1, threshold=1, delimiter='_')
            text_tri = trigram[text_bi]
            return text_tri
        except Exception,e:
            return None
            logging.error(e)

    def compute_tfidf(self, language):
        #计算tf-idf
        try:
            for word in self.tf_dict.keys():
                if len(word) < 2:
                    continue
                idf = self.idf_server.get_word_idf(word.lower().encode('utf-8'), language)
                tf = self.tf_dict[word]
                weight = tf * idf
                self.tf_idf_dict[word] = weight
        except Exception,e:
            logging.error(e)

    def count_word(self):
        #统计词频
        for word in self.words:
            word = word.strip()
            if not word:
                continue
            self.tf_dict[word] = self.tf_dict.get(word, 0) + 1

    def get_sentence(self, text):
        '''
        分句，返回句子的list
        一定要注意，在分句前，吧中文转成unicode格式，因为此处的中文标点为unicode编码。
        '''
        try:
            text = text.decode('utf-8')
            self.paras = [para.strip() for para in text.split('\n')]
            for paras in self.paras:
                sents = re.split(u'。|？|；|！|，|,|!|;|\\?|\\.', paras)  # 在正则中‘.’表示任意字符，\\.才是英文句号             
                sent = [sen.strip() for sen in sents if sen.strip() != '']
                if len(sent) == 0:
                    continue
                self.sentences.extend(sent)
        except Exception,e:
            print e
            logging.error(e)


    def get_keyword(self, text, phrase=True, nums=20):
        '''
            parm:
                text:待提取的文本
                phrase:是否短语合并，默认为True
                nums:提取关键词的个数，默认为20个
            return:
                数组
                没有关键词，默认为[]
        '''

        try:
            self._init_variable()
            language = self.language_server.get_language(text)
            logging.info(language)
            sents_splited = [] #是一个二维数组，保存分词之后的结果
            self.get_sentence(text)
            for sent in self.sentences:
                sents_splited.append(self.split_server.get_split_words(sent.encode('utf-8'), language))
            if bool(phrase) == True: #短语合并
                sents_splited = self.phrase_detect(sents_splited)
                if sents_splited == None:
                    return ''
            for line in sents_splited:
                for word in line:
                    self.words.append(word)
            self.count_word()
            self.compute_tfidf(language)
            if len(self.tf_idf_dict) == 0:
                return ''
            sorted_keywords = sorted(self.tf_idf_dict.iteritems(), key=lambda x: x[1], reverse=True)
            return json.dumps(sorted_keywords[:nums])
        except Exception,e:
            print e
            logging.error(e)
            return ''


if __name__ == '__main__':
    try:
        handler = KwHandler()
        processor = kwServer.Processor(handler)
        transport = TSocket.TServerSocket(kw_config.IP, kw_config.PORT)
        
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        server = TProcessPoolServer.TProcessPoolServer(processor, transport, tfactory, pfactory)
        print "Starting kw server..."  
        logging.info("Starting kw server...")
        server.serve()  
    except Exception,e:
        print e
        logging.error(e)
    finally:
        print "done!"


