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
host = ""
s.bind((host, port))

while True:

    msg, addr = s.recvfrom(1024)

    print("收到内容：" + msg.decode('utf8'))
    print(addr)
    if msg == "end":
        break

    msg = input("输入发送内容：")
    s.sendto(msg.encode('utf8'), addr)

s.close()
