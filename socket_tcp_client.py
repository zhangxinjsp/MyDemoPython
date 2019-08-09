#coding=utf-8

import socket

#SOCK_DGRAM udp
#SOCK_STREAM tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
print("本地主机名：" + host)

host = "127.0.0.1"
s.connect((host, port))
print("连接主机")

while True :
    msg = input("输入发送内容：")
    s.send(msg.encode('utf8'))
    if msg == "end":
        break
    print("收到内容：" + s.recv(1024).decode('utf8'))

s.close()
