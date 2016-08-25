# coding: utf-8

import sys, os
import json

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(cur_dir + '/gen-py'))

from idfServer import idfServer
from idfServer.ttypes import *

from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.server import TServer  
from thrift.server import TProcessPoolServer

import idf_config
import model

import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=cur_dir + '/../logs/idf_server.log',
                    filemode='a')

class IdfHandler:
    def __init__(self):
        logging.info('load idf start:')
        self.idf_models = {}
        try:
            self._init_idf_models()
        except Exception,e:
            logging.error('load idf error !')
            logging.error(e)
            print 'load idf error !'
            quit()
        logging.info('idf_init complete!')
        
    def _init_idf_models(self):
        for language, mfile in idf_config.IDF_MODELS.items():
            modeler = model.Model()
            modeler.load(mfile)
            self.idf_models[language] = modeler

    def get_word_idf(self, word, language):
        logging.info(str(word) + '\t' + str(language))
        # cant find log to be add
        idf = 5
        try:
            modeler = self.idf_models[language] 
            idf = modeler.wd_idf.get(word.decode('utf-8').lower().strip(), 5.0)
        except Exception,e:
            logging.error("can't find idf of language %s or the word %s's idf is not find !"%(language, word))
            logging.error(e)
        return idf

try:
    handler = IdfHandler()
    processor = idfServer.Processor(handler)
    transport = TSocket.TServerSocket(idf_config.IP, idf_config.PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TProcessPoolServer.TProcessPoolServer(processor, transport, tfactory, pfactory)
    print "Starting idf server..."  
    server.serve()
except Exception,e:
    logging.error(e)
    print e
finally:
    print "done!"






