#coding=utf-8

import zipfile
import os

newZipFile = zipfile.ZipFile('../file_zip.zip', 'w')
#newZipFile.write('file_ford')

def packagePath(path):
    print("*****")
    for folder, subFolders, files in os.walk(path):
        print("\n==当前遍历目录:"+folder)
        for file in files:
            print("[文件]："+file)
            newZipFile.write('%s/%s' % (folder, file))
        for subFolder in subFolders:
            print("[文件夹]："+subFolder)
            packagePath(subFolder)

print "工作目录::", os.getcwd()
packagePath('file_ford')

newZipFile.close()

viewZipFile = zipfile.ZipFile('../file_zip.zip', 'r')
print viewZipFile.namelist()

#解压
viewZipFile.extractall("../")
viewZipFile.close()








