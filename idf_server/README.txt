此服务为获取idf值的服务
输入1：word 输入2：language（编码参考iso639-1）
输出：word的idf值。

服务启动方式：python idf_server.py
使用方式：python idf_client.py today en

idf_config：配置文件，包含了idf模型的地址，端口号和ip地址
idf_server：idf服务主程序
idf_client：idf客户端程序
model：idf模型读取程序

