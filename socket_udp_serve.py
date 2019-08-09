# coding=utf-8

import socket

# SOCK_DGRAM udp
# SOCK_STREAM tcp
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345
print("本地主机名：" + host)
host = "127.0.0.1"
s.bind((host, port))

# print "开始监听"
# s.listen(5)
# print "结束监听"
#
# c, addr = s.accept()
# print "连接地址：", addr

while True:

    msg, addr = s.recvfrom(1024)

    print("收到内容：" + msg.decode('utf8'))
    print(addr)
    if msg == "end":
        break

    msg = input("输入发送内容：")
    s.sendto(msg.encode('utf8'), addr)

s.close()
