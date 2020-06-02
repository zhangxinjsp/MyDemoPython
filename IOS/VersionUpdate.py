#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import subprocess

os.chdir('/Users/zhangxin/Desktop/project/TransAnimation')
print(os.getcwd())
cmd = "sh log.sh"
# cmd = '/usr/libexec/PlistBuddy -c "print:CFBundleVersion" "$CONFIGURATION_BUILD_DIR/$INFOPLIST_PATH"'

PLIST_INFO_PATH = "/Users/zhangxin/Desktop/project/TransAnimation/TransAnimation/Info.plist"
APP_VERSION_KEY = "CFBundleShortVersionString"
BUNDLE_VERSION_KEY = "CFBundleVersion"

os.system('/usr/libexec/PlistBuddy -c "Set :%s 1.0.13" "%s"' % (APP_VERSION_KEY, PLIST_INFO_PATH))
os.system('/usr/libexec/PlistBuddy -c "Set :%s 1.0.12" "%s"' % (BUNDLE_VERSION_KEY, PLIST_INFO_PATH))

cmd = '/usr/libexec/PlistBuddy -c "Print :%s" "%s"' % (APP_VERSION_KEY, PLIST_INFO_PATH)
process = os.popen(cmd)  # return file
output = process.read()
process.close()
print('<<<<%s>>>>' % output)

cmd = '/usr/libexec/PlistBuddy -c "Print :%s" "%s"' % (BUNDLE_VERSION_KEY, PLIST_INFO_PATH)
process = os.popen(cmd)  # return file
output = process.read()
process.close()
print('<<<<%s>>>>' % output)

# os.system('xcrun agvtool new-version -all 2.0.12')
# print('============')
# os.system('xcrun agvtool new-marketing-version -all 2.0.13')
# print('============')

cmd = 'xcrun agvtool what-marketing-version'
process = os.popen(cmd)  # return file
output = process.read()
process.close()
print('<<<<%s>>>>' % output)

cmd = 'xcrun agvtool what-version'
process = os.popen(cmd)  # return file
output = process.read()
process.close()
print('<<<<%s>>>>' % output)
# p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
# output, err = p.communicate()
# # 判断命令是否执行成功
# status = 1 if err else 0
# if status == 0:
#     print('[SUCCESS] %s' % cmd)
# else:
#     print('[ERROR] %s' % cmd)
#     print(err)
# print(output)
