# coding: utf-8
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/opt/bicheng.jin/kw_server/gen-py')


from kwServer import kwServer
from kwServer.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import kw_config

class KwClient():
    def __init__(self):
        transport = TSocket.TSocket(kw_config.IP, kw_config.PORT)
        self.transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = kwServer.Client(protocol)
        self.transport.open()

    def get_keyword(self, text, phrase='True', nums=20):
        json_res = self.client.get_keyword(text, phrase, nums).replace('_', ' ')
        print json_res
        return json.loads(json_res)

    def __del__(self):
        self.transport.close()

if __name__=='__main__':
    wvc = KwClient()
    text = open(sys.argv[1]).read()
    phrase = sys.argv[2]
    nums = sys.argv[3]
    #print [text]
    for word, v in wvc.get_keyword(text, phrase, int(nums)):
        print word.encode('utf-8'), v

