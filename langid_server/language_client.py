# coding: utf-8
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/opt/bicheng.jin/langid_server/gen-py')


from languageServer import languageServer
from languageServer.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import lang_config

class LanguageClient():
    def __init__(self):
        transport = TSocket.TSocket(lang_config.IP, lang_config.PORT)
        self.transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = languageServer.Client(protocol)
        self.transport.open()

    def get_language(self, text):
        res = self.client.get_language(text)
        return res

    def __del__(self):
        self.transport.close()

if __name__=='__main__':
    lid = LanguageClient()
    text = sys.argv[1]
    print [text]
    print lid.get_language(text)

