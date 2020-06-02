#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  pip3 install requests
import os
import time
import requests
import base64
import zipfile

print('上传数据压缩打包')
os.chdir('/Users/zhangxin/Desktop')
FRAMEWORK_NAME = 'CHYBase.framework'
FRAMEWORK_NAME = 'log.txt'

print('上传 本地 服务器')
data = open(FRAMEWORK_NAME, "rb")
auth = base64.b64encode('robot:lion.2345'.encode(encoding='utf8'))

resp = requests.put("http://xsnjxz.f3322.net:9088/artifactory/android-snapshots/" + FRAMEWORK_NAME,
                    headers={'Authorization': 'Basic ' + str(auth, 'utf8')},
                    data=data)
print('返回错误码：' + str(resp.status_code))
print('上传结果：' + resp.text)
