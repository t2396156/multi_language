# coding: utf-8

import numpy as np
import math
import sys, os
import json

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(cur_dir + '/gen-py'))

from classifyServer import classifyServer
from classifyServer.ttypes import *

from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.server import TServer  
from thrift.server import TProcessPoolServer

import classify_config

sys.path.append(cur_dir + '/../w2v_server')
sys.path.append(cur_dir + '/../langid_server')
sys.path.append(cur_dir + '/../kw_server')

import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=cur_dir + '/../logs/classify.log',
                filemode='a')

from word2vec_client import Word2vecClient
from language_client import LanguageClient
from kw_client import KwClient


class ClassifyHandler:
    def __init__(self):
        self.w2v_server = Word2vecClient()
        self.kw_server = KwClient()
        self.language_server = LanguageClient()
        self.emotion_class = classify_config.DEFAULT_EMOTIONS
        self.common_class = classify_config.DEFAULT_CLASS

    def cosine_dis(self, vec1, vec2):
        #考虑分母为零的，-1~1 考虑要不要加绝对值
        try:
            cosine = sum(vec1*vec2)/(math.sqrt(sum(vec2*vec2))*math.sqrt(sum(vec1*vec1)))
            return cosine
        except Exception,e:
            logging.error(e)
            return 0

    def get_similarity(self, language, dic_class, word_list):
        dis_dic = {}
        #tag类目
        #words类目扩展词
        #word_list关键词

        #try:
        for tag in dic_class.keys():
            words = dic_class[tag]
            dis_sum = 0
            for w in words:
                w_vec = np.array(self.w2v_server.get_word_vec(w.encode('utf-8'), language), dtype='float64')
                #如果拿不到值，len(w_vec)
                if len(w_vec) == 0:
                    continue
                for word in word_list:
                    ###关键词为空的情况要考虑
                    word_vec = np.array(self.w2v_server.get_word_vec(word.encode('utf-8'), language), dtype='float64')
                    #print word.encode('utf-8'),word_vec
                    if len(word_vec) == 0:
                        continue
                    dis_sum += self.cosine_dis(w_vec, word_vec)
            dis_dic[tag] = dis_sum/len(words)
        return sorted(dis_dic.items(), key=lambda x:x[1], reverse = True)
        '''
        except Exception,e:
            logging.error(e)
            return None
        '''
            
        
    def process(self, text, dic_class):
        '''
            parm:
                text:文章
                dic_class:类目
            return:
                属于每个类的概率
        '''
        try:
            language = self.language_server.get_language(text)
            res = self.kw_server.get_keyword(text, 'False')
            if res == '':
                return ''
            word_list = []
            for word,weight in res:
                word_list.append(word)
                #print word.encode('utf-8'), weight
            
            res_dict = self.get_similarity(language, dic_class, word_list)
            if res_dict is None:
                return ''
            return json.dumps(res_dict)
        except Exception,e:
            logging.error(e)
            print e
            return ''
    
    def get_emotion_class(self, text):
        #情感分类
        try:
            language = self.language_server.get_language(text)
            return self.process(text, self.emotion_class[language])
        except Exception,e:
            logging.error(e)
            print 'error'
            return 'error'

    def get_common_class(self, text, str_class):
        #通用分类
        try:
            language = self.language_server.get_language(text)
            dic_class = json.loads(str_class)
            if len(dic_class) == 0:
                dic_class = self.common_class[language]
            return self.process(text, dic_class)
        except Exception,e:
            logging.error(e)
            print 'error'
            return 'error'
        
        
if __name__ == '__main__':
    try:
        handler = ClassifyHandler()
        processor = classifyServer.Processor(handler)
        transport = TSocket.TServerSocket(classify_config.IP, classify_config.PORT)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        server = TProcessPoolServer.TProcessPoolServer(processor, transport, tfactory, pfactory)
        print "Starting classify server..."  
        logging.info("Starting classify server...")
        server.serve()  
    except Exception,e:
        print e
        logging.error(e)
        quit()
