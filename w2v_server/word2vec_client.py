# coding: utf-8
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/opt/bicheng.jin/w2v_server/gen-py')


from word2vecServer import word2vecServer
from word2vecServer.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import w2v_config

class Word2vecClient():
    def __init__(self):
        transport = TSocket.TSocket(w2v_config.IP, w2v_config.PORT)
        self.transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = word2vecServer.Client(protocol)
        self.transport.open()

    def get_word_vec(self, word, language):
        json_res = self.client.get_word_vec(word, language)
        return json.loads(json_res)

    def __del__(self):
        self.transport.close()

if __name__=='__main__':
    wvc = Word2vecClient()
    word = sys.argv[1]
    language = sys.argv[2]
    print [word]
    print wvc.get_word_vec(word, language)

