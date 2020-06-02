#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

print("当前工作目录", os.getcwd())

print(os.path.expanduser('~'))
print(os.path.join(os.path.expanduser('~'), 'Desktop'))

# print os.listdir

os.mkdir("aaaaaaaaaa")
# rmdir 删除空文件夹
os.rmdir("aaaaaaaaaa")

path = "file_ford"
if os.path.exists(path):
    # 删除文件夹及内容
    shutil.rmtree(path)

os.mkdir(path)

os.chdir(path)
print("工作目录::", os.getcwd())

fileName = "file.txt"
if os.path.exists(fileName):
    os.remove(fileName)

file = open(fileName, "a+")
print("文件名：", file.name)
print("是否已关闭：", file.closed)
print("访问模式：", file.mode)

file.write("python is the bast")

# 第一个参数，偏移字节数，第二个参数，0:开始位置，1:当前位置，2:文件结尾
file.seek(10, 0)
print("当前指针位置：", file.tell())
str = file.read(10)  # 不填读取所有
print("读取字符串：", str)

file.seek(0, 2)
file.write("\nxasdiuortqwkejrhuiis张收到")

file.seek(0, 0)
print('按行读取：', file.readlines())

print("当前指针位置：", file.tell())

file.close()

shutil.copy(fileName, 'file1.txt')
os.rename('file1.txt', "file2.txt")

os.mkdir('sss')
os.rename('sss', 'aaa')

# shutil.move("file2.txt", 'aaa/file1.txt')
shutil.copy("file2.txt", 'aaa/')


def ShowPathInfo(path):
    print("*****")
    for folder, subFolders, files in os.walk(path):
        print("\n==当前遍历目录:" + folder)
        for file in files:
            print("[文件]：" + file)
        for subFolder in subFolders:
            print("[文件夹]：" + subFolder)
            ShowPathInfo(subFolder)


# os.chdir('../')
filePath = os.getcwd()
print("工作目录::", filePath)
ShowPathInfo(filePath)
