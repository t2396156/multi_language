#!/bin/sh

python -u w2v_server/word2vec_server.py
python -u spliter_server/split_server.py
python -u langid_server/language_server.py
python -u idf_server/idf_server.py
