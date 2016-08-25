# coding: utf-8

import langid
import sys, os

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(cur_dir + '/gen-py'))

from languageServer import languageServer
from languageServer.ttypes import *

from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.server import TServer  
from thrift.server import TProcessPoolServer

import lang_config

import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=cur_dir + '/../logs/langid.log',
                filemode='a')

class LanguageHandler:
    def __init__(self):
        #必须在这里跑一次
        language = langid.classify('test')[0]
        pass

    def get_language(self, text):
        try:
            language = langid.classify(text)[0]
            return language
        except Exception,e:
            logging.error(e)

if __name__ == '__main__':
    try:
        handler = LanguageHandler()
        processor = languageServer.Processor(handler)
        transport = TSocket.TServerSocket(lang_config.IP, lang_config.PORT)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        server = TProcessPoolServer.TProcessPoolServer(processor, transport, tfactory, pfactory)
        print "Starting language server..."  
        server.serve()  
    except Exception,e:
        logging.error(e)
        print e
    finally:
        print "done!"
