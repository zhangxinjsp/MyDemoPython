#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket

# SOCK_DGRAM udp
# SOCK_STREAM tcp
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

host = socket.gethostname()
port = 12345
print("本地主机名：" + host)

host = "<broadcast>"
# s.connect((host, port))
print("连接主机")

while True:
    msg = input("输入发送内容：")
    s.sendto(msg.encode('utf8'), (host, port))
    if msg == "end":
        break
    print("收到内容：" + s.recv(1024).decode('utf8'))

s.close()
