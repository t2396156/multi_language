# coding: utf-8

import gensim.models.word2vec
import sys, os
import json

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(cur_dir + '/gen-py'))

from splitServer import splitServer
from splitServer.ttypes import *

from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.server import TServer  
from thrift.server import TProcessPoolServer

import split_config

import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=os.path.join(cur_dir + '/../logs/split.log'),
                filemode='a')

class SplitHandler:
    def __init__(self):
        self.spliters = {}
        self._init_spliters()

    def _init_spliters(self):
        try:
            logging.info('init spliter start:')
            for language, conf in split_config.SPLITERS.items():
                mname = conf["module"]
                cname = conf["clazz"]
                modul = __import__(mname, fromlist=[cname,])
                clazz = getattr(modul, cname)
                spliter = clazz()
                self.spliters[language] = spliter
            logging.info('init spliter success !')
        except Exception,e:
            print e
            logging.error(e)
            quit()
    
    def get_split_words(self, text, language):
        try:
            if language not in self.spliters.keys():
                spliter = self.spliters['com']
                print language, 'is not supported'
            else:
                spliter = self.spliters[language]
            res = spliter.process(text)
            #注意，有些语言是不能够用空格分的，用默认分词会有问题    
            return json.dumps(res)
        except Exception,e:
            return json.dumps([])
            logging.error(e)

if __name__ == '__main__':
    try:
        handler = SplitHandler()
        processor = splitServer.Processor(handler)
        transport = TSocket.TServerSocket(split_config.IP, split_config.PORT)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        server = TProcessPoolServer.TProcessPoolServer(processor, transport, tfactory, pfactory)
        print "Starting split server..."  
        server.serve()  
    except Exception,e:
        logging.error(e)
        print e
        quit()
    finally:
        print "done!"







