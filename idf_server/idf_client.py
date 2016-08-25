# coding: utf-8
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/opt/bicheng.jin/idf_server/gen-py')


from idfServer import idfServer
from idfServer.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import idf_config

class IdfClient():
    def __init__(self):
        transport = TSocket.TSocket(idf_config.IP, idf_config.PORT)
        self.transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = idfServer.Client(protocol)
        self.transport.open()

    def get_word_idf(self, word, language):
        res = self.client.get_word_idf(word, language)
        return res

    def __del__(self):
        self.transport.close()

if __name__=='__main__':
    wvc = IdfClient()
    word = sys.argv[1]
    language = sys.argv[2]
    print [word]
    print wvc.get_word_idf(word, language)

