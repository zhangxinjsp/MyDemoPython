#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import _thread
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
            self.receive_data(client_sock, address)
            # _thread.start_new_thread(self.receive_data, (client_sock, address))

    def receive_data(self, client_sock, address):
        receive_host = '%s:%d' % (address[0], address[1])
        print('accept thread: %s' % receive_host)
        http_method = None
        http_version = None
        header_dict = None
        receive_body = bytes()
        while True:
            receive_piece = client_sock.recv(1024)
            receive_body += receive_piece
            body_str = receive_body.decode('utf8')
            print('%s : receive package length %d' % (receive_host, len(receive_piece)))
            if '\r\n\r\n' in body_str and http_method is None:
                piece_list = body_str.split('\r\n\r\n')
                http_method, http_version, header_dict = self.http_header_analysis(piece_list.pop(0))
                receive_body = '\r\n\r\n'.join(piece_list).encode('utf8')

            content_length = int(header_dict[HTTP_HEADER_KEY_CONTENT_LENGTH])
            if len(receive_body) >= content_length:
                print('%s : receive finish break' % receive_host)
                break

            if '' == receive_piece.decode('utf8'):
                print('%s : receive empty break' % receive_host)
                break

        is_success = self.analysis.analysis_data(receive_body)

        response_message = self.splice_response_body(http_version, is_success)

        client_sock.send(response_message.encode('utf-8'))
        client_sock.close()

    def stop_service(self):
        self.service_socket.close()

    def http_header_analysis(self, header_message):
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
        start_line = http_version + " 200 OK\r\n"
        headers = "Server: My server\r\n"
        result_code = 1
        message = '失败'
        if is_success:
            result_code = 0
            message = '成功'
        body = '{"resultCode":%d,"message":"%s","data":{}}' % (result_code, message)

        message = start_line + headers + "\r\n" + body
        return message


if __name__ == '__main__':
    server = TcpService()
    server.start_service()
