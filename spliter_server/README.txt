分词服务：对文本进行分词
输入：text（任意语言文本utf-8） language（语言相应编码）
输出：分词完成的list

服务启动方式：python split_server.py
使用方式：python split_client.py '大声地啥啥啥' zh

spliter文件夹：包含了不同语言的分词程序和停用词文件。
split_server: split服务主程序
split_client：split客户端程序
split_config: 配置文件，包含了端口号，ip， 分词程序所在位置，以及停用词地址。