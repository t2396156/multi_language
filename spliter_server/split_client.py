# coding: utf-8
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/opt/bicheng.jin/spliter_server/gen-py')


from splitServer import splitServer
from splitServer.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import split_config

class SplitClient():
    def __init__(self):
        transport = TSocket.TSocket(split_config.IP, split_config.PORT)
        self.transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = splitServer.Client(protocol)
        self.transport.open()

    def get_split_words(self, text, language):
        json_res = self.client.get_split_words(text, language)
        return json.loads(json_res)

    def __del__(self):
        self.transport.close()

if __name__=='__main__':
    wvc = SplitClient()
    sent = sys.argv[1]
    language = sys.argv[2]
    print [sent]
    print type(wvc.get_split_words(sent, language))
    for word in wvc.get_split_words(sent, language):
        print word.encode('utf-8')

