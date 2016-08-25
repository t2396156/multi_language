# coding: utf-8
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('./gen-py')


from classifyServer import classifyServer
from classifyServer.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import classify_config

class ClassifyClient():
    def __init__(self):
        transport = TSocket.TSocket(classify_config.IP, classify_config.PORT)
        self.transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = classifyServer.Client(protocol)
        self.transport.open()

    def get_common_class(self, text, dic_class):
        str_class = json.dumps(dic_class)
        json_res = self.client.get_common_class(text, str_class)
        return json.loads(json_res)

    def get_emotion_class(self, text):
        json_res = self.client.get_emotion_class(text)
        print '###############3'
        print json_res
        print '$$$$$$$$$$$$$'
        return json.loads(json_res)

    def __del__(self):
        self.transport.close()

if __name__=='__main__':
    wvc = ClassifyClient()
    text = open(sys.argv[1]).read()
    #language = sys.argv[2]
    print [text]
    for word, l in wvc.get_emotion_class(text):
        print word.encode('utf-8'), l
    # print wvc.get_word_vec(word, language)

