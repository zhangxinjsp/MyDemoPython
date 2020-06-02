#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import json
import time

# SOCK_DGRAM udp
# SOCK_STREAM tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = socket.gethostname()
print("本地主机名：" + host_name)
host = socket.gethostbyname(host_name)
print(host)
host = socket.gethostbyname_ex(host_name)
print(host)
print(host[2][1])

print(int(b'300', 16))

json_obj = {"principalCode": "15850679639",
            "credentialCode": "qwer1234",
            "loginType": "1",
            "clientKey": "1"}

# result = socket.getaddrinfo('sit.exd.lionaitech.com', None)

# print(result[0][4][0])
sock.connect(('sit.exd.lionaitech.com', 9002))
# sock.connect(('127.0.0.1', 12345))
print("连接主机")

json_str = json.dumps(json_obj)
send_message = 'POST /api.app/v1/user/login HTTP/1.1' + \
               '\r\nHost: sit.exd.lionaitech.com:9002' + \
               '\r\nConnection: keep-alive' + \
               '\r\nUser-Agent: LionAutoEventTracker/1 CFNetwork/1121.2.2 Darwin/19.3.0' + \
               '\r\nAccept: */*' + \
               '\r\nAccept-Language: zh-cn' + \
               '\r\nCache-Control: no-cache' + \
               '\r\nAccept-Encoding: gzip, deflate' + \
               '\r\nContent-Type: application/json' + \
               '\r\nContent-Length: %d' % len(json_str.encode('utf8')) + \
               '\r\nCLIENT-KEY: 1' + \
               '\r\nDEVICE-TYPE: APP' + \
               '\r\nSEND-DATE: %d' % time.time() + \
               '\r\nCONTENT-ENCRYPTED: 0' + \
               '\r\n\r\n' + json_str
print(send_message)
sock.send(send_message.encode('utf8'))

receive_data = bytes()
while True:
    print('receive piece')
    receive_piece = sock.recv(1024)
    receive_data += receive_piece
    print('receive package length %d' % len(receive_piece))
    # TODO：需要判断返回体的数据样式
    # 测试使用包含：Transfer-Encoding: chunked，以\r\n0\r\n\r\n来判断数据结束
    # 包含Content-Length时，以数据体长度来判断结束
    head_end_index = receive_data.find(b'\r\n0\r\n\r\n')
    if head_end_index != -1:
        break
    if not receive_piece:
        break
print('接收数据：')
print(receive_data)

receive_str = receive_data.decode('utf8')

header_str = receive_str.split('\r\n\r\n')[0]

header_list = header_str.split('\r\n')
first_line = header_list.pop(0)
http_version = first_line.split(' ')[0]
response_status = first_line.split(' ')[1]

response_header = {}

response_body_str = receive_str.split('\r\n\r\n')[1]

body_length = int(response_body_str.split('\r\n')[0], 16)
print(body_length)
body_json = json.loads(response_body_str.split('\r\n')[1])
print(body_json)
# print(receive_str.split('\r\n\r\n'))

sock.close()
