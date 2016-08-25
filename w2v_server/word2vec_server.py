# coding: utf-8

import gensim.models.word2vec
import sys, os
import json

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(cur_dir + '/gen-py'))

from word2vecServer import word2vecServer
from word2vecServer.ttypes import *

from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.server import TServer  
from thrift.server import TProcessPoolServer

import w2v_config

import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=cur_dir + '/../logs/word2vec.log',
                    filemode='a')

class Word2vecHandler:
    def __init__(self):
        logging.info('load word2vec model start:')
        self.w2v_models = {}
        try:
            self._init_w2v_models()
            logging.info('load word2vec model complete!')
        except Exception,e:
            logging.error('load word2vec model error:')
            logging.error(e)
            print ('load word2vec model error:')
            print (e)
            quit()
            
    def _init_w2v_models(self):
        for language, mfile in w2v_config.W2V_MODELS.items():
            self.w2v_models[language] = gensim.models.word2vec.Word2Vec.load_word2vec_format(mfile, binary=True) 

    def get_word_vec(self, word, language):
        # cant find log to be add
        find = False
        try:
            word_list = []
            word_list.append(word.lower())
            word_list.append(word.capitalize())
            word_list.append(word.upper())
            for w in word_list:
                modeler = None
                if self.w2v_models.has_key(language):
                    modeler = self.w2v_models[language]
                else:
                    logging.error("%s is not support", language)
                    return json.dumps([])
                try:
                    res = modeler[w.decode('utf-8')]
                    find = True
                    return json.dumps(res.tolist())
                except Exception,e:
                    logging.error(e)
                    print e
                    return json.dumps([])
        except KeyError:
            if find == False:
                logging.error('%s not in word2vec model', word)
            return json.dumps([])

if __name__ == '__main__':
    try:
        handler = Word2vecHandler()
        processor = word2vecServer.Processor(handler)
        transport = TSocket.TServerSocket(w2v_config.IP, w2v_config.PORT)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        server = TProcessPoolServer.TProcessPoolServer(processor, transport, tfactory, pfactory)
        print "Starting word2vec server..."  
        server.serve()  
    except Exception,e:
        logging.error(e)
        print e
    finally:
        print "done!"




