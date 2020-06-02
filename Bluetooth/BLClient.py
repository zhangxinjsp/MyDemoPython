#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 安装 pybluez 0.30 版本
# pip install pybluez 是0.23版本
# 需要使用 pip install git+https://github.com/pybluez/pybluez.git 安装

# 需要依赖 lightblue 模块
# lightblue 2009年 停止更新，现在没有适配的
# GitHub 上的 https://github.com/0-1-0/lightblue-0.4， Xcode工程版本是32位现在已经不兼容
# 需要到更新功能文件
# 使用http://lightblue.sourceforge.net/现在的工程进行修改
# TODO: 目前猜测，crash跟MAC_OSX 的framework的警告有关

import bluetooth

devices = bluetooth.discover_devices(lookup_names=True)

print(devices)
