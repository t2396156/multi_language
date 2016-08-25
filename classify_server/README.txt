此服务为获取分类的服务
默认分类为情感分类。可以进入client端修改。
输入1：text 
输出：正面情感和负面情感的权重。

服务启动方式：python classify_server.py
使用方式：python classify_client.py XXX.txt

classify_config：配置文件，包含了分类和情感的缺省类目，端口号和ip地址
classify_server：idf服务主程序
classify_client：idf客户端程序


