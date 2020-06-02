#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import shutil

fileName = "/Users/zhangxin/Desktop/asdfadfasdfasf/NetworkTransfer.swift"
tempName = "/Users/zhangxin/Desktop/asdfadfasdfasf/NetworkTransfer_temp.swift"

file = open(fileName, "r")
temp = open(tempName, 'w')

seekLocation = None

while True:
    line = file.readline()

    if seekLocation is None:
        temp.write(line)

    if 'switch req {' in line:
        seekStart = file.tell()
        break

temp.write('//askdjgalkhflkajshgkasjhgalksfhajg\n')

seekLocation = None
while True:
    line = file.readline()

    if seekLocation is not None:
        temp.write(line)

    if 'default:' in line:
        seekLocation = file.tell()
        temp.write(line)

    if line is '':
        break

file.close()
temp.close()
