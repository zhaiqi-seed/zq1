import socket

s = socket.socket() #创建socket对象

host = socket.gethostname() #获取本地主机名
port = 12345 #设置端口
s.bind((host, port)) #绑定端口

s.listen(5) #等待客户端链接

while True:
    c, addr = s.accept() #建立客户端连接
    print("连接地址:", addr)
    c.send(('你值得拥有更改好的工作').encode())
    c.close()
