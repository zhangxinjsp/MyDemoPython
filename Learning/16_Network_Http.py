#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip3 install httplib2

import http.client  # 前生是httplib
import http.server

import httplib2

import json


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.0"
    server_version = "PSHS/0.1"
    sys_version = "Python/3.7.x"
    target = "D:/web"

    def do_GET(self):
        if self.path == "/" or self.path == "/index":
            print(self.path)
            req = {"success": "true"}
            self.send_response(200)
            self.send_header("Content-type", "json")
            self.end_headers()
            rspstr = json.dumps(req)
            self.wfile.write(rspstr.encode("utf-8"))

        else:
            print("get path error")

    def do_POST(self):
        if self.path == "/signin":
            print("postmsg recv, path right")
        else:
            print("postmsg recv, path error")
            data = self.rfile.read(int(self.headers["content-length"]))
            data = json.loads(data)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            rspstr = "recv ok, data = "
            rspstr += json.dumps(data, ensure_ascii=False)
            self.wfile.write(rspstr.encode("utf-8"))


def http_server():
    server = http.server.HTTPServer(('', '12345'), MyRequestHandler)

    server.serve_forever()


def http_client():
    req_headers = {
        'MobileType': 'Android',
        'DeviceToken': 'xxxxxxxxx',
        'OSVersion': '1.0.3',
        'AppVersion': '14',
        'Host': '192.xxx.x.xxxx'}

    req_conn = http.client.HTTPConnection("192.xxx.x.xxxx")
    req_conn.request(method="GET", url="/Login?username=1416&password=123", body=None, headers=req_headers)
    res = req_conn.getresponse()
    print(res.status, res.reason)
    print(res.msg)
    print(res.read())


def func_httplib2():
    url = 'http://sit.exd.lionaitech.com:9002/api.app/v1/user/login'

    json_obj = {"principalCode": "15850679639",
                "credentialCode": "qwer1234",
                "loginType": "1",
                "clientKey": "1"}

    opener = httplib2.Http()

    resp, content = opener.request(url, 'POST', json.dumps(json_obj))
    print(resp)
    print(content.decode('utf8'))


if __name__ == '__main__':
    print('')
    func_httplib2()
