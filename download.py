#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

import urllib

url = 'http://image.nationalgeographic.com.cn/2017/1122/20171122113404332.jpg'
filename = url.split('/').pop()
print("path :", filename)

if os.path.exists(filename):
    print('exists')
else:
    urllib.urlretrieve(url, filename)

# urllib2.Request(url)
