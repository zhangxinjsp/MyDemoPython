#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket

from SimpleServer.DataAnalysis import DataAnalysis

HTTP_HEADER_KEY_HOST = 'Host'
HTTP_HEADER_KEY_USER_AGENT = 'User-Agent'
HTTP_HEADER_KEY_ACCEPT = 'Accept'
HTTP_HEADER_KEY_ACCEPT_ENCODING = 'Accept-Encoding'
HTTP_HEADER_KEY_ACCEPT_LANGUAGE = 'Accept-Language'
HTTP_HEADER_KEY_CONNECTION = 'Connection'
HTTP_HEADER_KEY_CONTENT_TYPE = 'Content-Type'
HTTP_HEADER_KEY_CONTENT_LENGTH = 'Content-Length'

# http request method key
HTTP_METHOD_CONNECT = "CONNECT"
HTTP_METHOD_DELETE = "DELETE"
HTTP_METHOD_GET = "GET"
HTTP_METHOD_HEAD = "HEAD"
HTTP_METHOD_OPTIONS = "OPTIONS"
HTTP_METHOD_PATCH = "PATCH"
HTTP_METHOD_POST = "POST"
HTTP_METHOD_PUT = "PUT"
HTTP_METHOD_TRACE = "TRACE"


class TcpService:
    service_socket = None

    def __init__(self):
        print('init tcp service')
        self.analysis = DataAnalysis()

    def start_service(self):
        self.service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("locol host name：" + socket.gethostname())
        host = ""
        port = 12345
        self.service_socket.bind((host, port))

        print("start listen")
        self.service_socket.listen(128)

        while True:
            print("start accept")

            client_sock, address = self.service_socket.accept()
            print("accept address：", address)

            http_method = None
            http_version = None
            header_dict = {}
            receive_body = bytes()
            while True:
                receive_piece = client_sock.recv(1024)
                receive_body += receive_piece
                print('receive package length %d' % len(receive_piece))
                # print('receive package length %d' % receive_piece)
                if b'\r\n\r\n' in receive_body and http_method is None:
                    piece_list = receive_body.split(b'\r\n\r\n')
                    http_method, http_version, header_dict = self.http_header_analysis(piece_list.pop(0))
                    receive_body = b'\r\n\r\n'.join(piece_list)

                if HTTP_HEADER_KEY_CONTENT_LENGTH in header_dict.keys():
                    content_length = int(header_dict[HTTP_HEADER_KEY_CONTENT_LENGTH])
                    if len(receive_body) >= content_length:
                        print('receive finish break')
                        break

                if b'' == receive_piece:
                    print('receive empty break')
                    break

            is_success = self.analysis.analysis_data(receive_body)

            response_message = self.splice_response_body(http_version, is_success)

            client_sock.send(response_message.encode('utf-8'))
            client_sock.close()

    def stop_service(self):
        self.service_socket.close()

    def http_header_analysis(self, header_data):
        header_message = header_data.decode('utf8')
        print('receive header is: <<<<<<<<<<<\n' + header_message + '\n>>>>>>>>>>>')

        header_list = header_message.split('\r\n')
        start_line = header_list.pop(0).split(' ')
        http_method = start_line[0]
        # url_path = start_line[1]
        http_version = start_line[2]
        header_dict = {}
        for header_item in header_list:
            header_key = header_item.split(': ')[0]
            header_value = header_item.split(': ')[1]
            header_dict[header_key] = header_value

        return http_method, http_version, header_dict

    def splice_response_body(self, http_version, is_success):
        if http_version:
            start_line = http_version + " 200 OK"
        else:
            start_line = "HTTP/1.1 200 OK"
        headers = "Server: My server" + \
                  "\r\nConnection: keep-alive" + \
                  '\r\nDate: ' + \
                  '\r\nContent-Type: application/json; charset = UTF-8' + \
                  '\r\nTransfer-Encoding: chunked'
        # 请求返回的数据形式不统一
        # 1. 当响应头里有Transfer-Encoding: chunked时，数据的是三部分的：
        #       第一部分：数据长度\r\n，
        #       第二部分：数据内容\r\n，
        #       第三部分：结束标识0\r\n\r\n。
        # 2. 当响应头里有Content-Length时，值表示返回数据的长度
        result_code = 1
        message = '失败'
        if is_success:
            result_code = 0
            message = '成功'
        body = '{"resultCode":%d,"message":"%s","data":{}}' % (result_code, message)

        body_length = len(body.encode('utf8'))
        # TODO: body 前后格式
        # 长度：16进制字符串\r\n
        # 包内容：包体内容\r\n
        # 结束符：0\r\n
        message = start_line + \
                  "\r\n" + headers + \
                  "\r\n\r\n" + str(hex(body_length)) + \
                  "\r\n" + body + \
                  "\r\n0\r\n\r\n"
        print(message.encode('utf8'))
        return message


if __name__ == '__main__':
    server = TcpService()
    server.start_service()
