#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging

# DEBUG:小问题，一般在调试时才会使用
# INFO：正常运行消息
# WARNING：警告，可能有问题
# ERROR：错误，导致程序部分处理失败
# CRITICAL：致命的问题，程序都要完蛋

logging.basicConfig(filename="../runlog.txt", level=logging.DEBUG, format="%(asctime)s-%(levelname)s:%(message)s")
# logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s-%(levelname)s:%(message)s")

logging.disable(logging.DEBUG)

logging.debug("debug日志")  # 不会输出
logging.error("error日志")  # 会输出
logging.critical("critical日志")  # 会输出

ss = 'a0 a0aa0a0 a0 a0 a0a00a0aa00a0aa0a0a00a '
ss = ss.replace('a0', '')
print(ss)
