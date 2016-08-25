#!/bin/sh

ps -ef | grep word2vec_server.py | grep -v grep | cut -c 9-15 | xargs kill -s 9
ps -ef | grep language_server.py | grep -v grep | cut -c 9-15 | xargs kill -s 9
ps -ef | grep split_server.py | grep -v grep | cut -c 9-15 | xargs kill -s 9
ps -ef | grep idf_server.py | grep -v grep | cut -c 9-15 | xargs kill -s 9
ps -ef | grep kw_server.py | grep -v grep | cut -c 9-15 | xargs kill -s 9
ps -ef | grep classify_server.py | grep -v grep | cut -c 9-15 | xargs kill -s 9
