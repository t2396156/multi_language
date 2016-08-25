此服务为获取词向量值的服务
输入1：word 输入2：language（编码参考iso639-1）
输出：word的词向量。

服务启动方式：python w2v_server.py
使用方式：python w2v_client.py today en

w2v_config：配置文件，包含了w2v模型的地址,端口号和ip地址
w2v_server：idf服务主程序
w2v_client：idf客户端程序

