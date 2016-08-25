# coding: utf-8

from classify_client import ClassifyClient
import classify_config
import sys

class_dic = {
'good': [''],
'': ['comunidad'],
}
cs = ClassifyClient()
text = open(sys.argv[1]).read()
print cs.get_common_class(text, class_dic)
