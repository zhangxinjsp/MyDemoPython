#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import shutil
import getpass
import sys
import re

ACCOUNT = 'robot'
PASSWORD = '11111.2345'

TIME = time.strftime("%Y%m%d%H%M%S", time.localtime())

# CONFIG = 'Debug'
# DEVICE = 'iphonesimulator'

CONFIG = "Release"
DEVICE = 'iphoneos'

# print(os.environ['USER'])
USER = getpass.getuser()

SHORT_VERSION_KEY = "CFBundleShortVersionString"
BUNDLE_VERSION_KEY = "CFBundleVersion"

PROJECT_NAME = 'Base'
PROJECT_PATH = '/Users/%s/Desktop/CheryProject/library/%s' % (USER, PROJECT_NAME)

# PROJECT_PATH = os.path.dirname(__file__)
# PROJECT_NAME = PROJECT_PATH.split('/').pop()

PROJECT_PLIST_PATH = "%s/%s/Info.plist" % (PROJECT_PATH, PROJECT_NAME)
FRAMEWORK_PLIST_PATH = "%s/%sFramework/Info.plist" % (PROJECT_PATH, PROJECT_NAME)
BUNDLE_PLIST_PATH = "%s/%sBundle/Info.plist" % (PROJECT_PATH, PROJECT_NAME)

FRAMEWORK_NAME = '%s.framework' % PROJECT_NAME
PRODUCT_ROOT_PATH = '/Users/%s/Library/Developer/Xcode/DerivedData' % USER
PRODUCT_SUB_PATH = '/Build/Products/%s-%s/%s' % (CONFIG, DEVICE, FRAMEWORK_NAME)

OUT_PATH = '.build_sdk'

os.chdir(PROJECT_PATH)
print(os.getcwd())


def input_func(tip):
    if sys.version_info[0] == 2:
        return raw_input(tip)
    elif sys.version_info[0] == 3:
        return input(tip)


def version_check(version):
    regular = r'^\d+(\.\d+)+$'
    match = re.match(regular, version, re.M | re.I)
    print(match)
    if match:
        return True
    else:
        print('version is error')
        return False


def get_current_version():
    """
    获取版本号
    :return:当前版本号元组(short, build)
    """
    cmd = '/usr/libexec/PlistBuddy -c "Print :%s" "%s"' % (SHORT_VERSION_KEY, FRAMEWORK_PLIST_PATH)
    process = os.popen(cmd)
    short_version = process.read().replace('\n', '')
    process.close()

    while True:
        short_version = input_func('input version(current: %s): ' % short_version)
        if version_check(short_version):
            break

    os.system('/usr/libexec/PlistBuddy -c "Set :%s %s" "%s"' %
              (SHORT_VERSION_KEY, short_version, PROJECT_PLIST_PATH))
    os.system('/usr/libexec/PlistBuddy -c "Set :%s %s" "%s"' %
              (SHORT_VERSION_KEY, short_version, FRAMEWORK_PLIST_PATH))
    os.system('/usr/libexec/PlistBuddy -c "Set :%s %s" "%s"' %
              (SHORT_VERSION_KEY, short_version, BUNDLE_PLIST_PATH))

    cmd = '/usr/libexec/PlistBuddy -c "Print :%s" "%s"' % (BUNDLE_VERSION_KEY, FRAMEWORK_PLIST_PATH)
    process = os.popen(cmd)
    bundle_version = process.read().replace('\n', '')
    process.close()

    while True:
        bundle_version = input_func('input build(current: %s): ' % bundle_version)
        if version_check(bundle_version):
            break

    os.system('/usr/libexec/PlistBuddy -c "Set :%s %s" "%s"' %
              (BUNDLE_VERSION_KEY, bundle_version, PROJECT_PLIST_PATH))
    os.system('/usr/libexec/PlistBuddy -c "Set :%s %s" "%s"' %
              (BUNDLE_VERSION_KEY, bundle_version, FRAMEWORK_PLIST_PATH))
    os.system('/usr/libexec/PlistBuddy -c "Set :%s %s" "%s"' %
              (BUNDLE_VERSION_KEY, bundle_version, BUNDLE_PLIST_PATH))

    return short_version, bundle_version


def build_framework():
    """
    编译framework
    :return:编译结果路径
    """
    # 清除编译内容
    os.system('xcodebuild clean -workspace %s.xcworkspace -scheme %sFramework' % (PROJECT_NAME, PROJECT_NAME))
    os.system('xcodebuild clean -workspace %s.xcworkspace -scheme %sBundle' % (PROJECT_NAME, PROJECT_NAME))

    # 编译framework
    os.system('xcodebuild -workspace %s.xcworkspace -configuration %s -scheme %sFramework -sdk %s -quiet' % (
        PROJECT_NAME, CONFIG, PROJECT_NAME, DEVICE))
    os.system('xcodebuild -workspace %s.xcworkspace -configuration %s -scheme %sBundle -sdk %s -quiet' % (
        PROJECT_NAME, CONFIG, PROJECT_NAME, DEVICE))

    # 获取编译结果
    path = ''
    for folder, subFolders, files in os.walk(PRODUCT_ROOT_PATH):
        for subFolder in subFolders:
            if subFolder.startswith(PROJECT_NAME):
                path = folder + '/' + subFolder + PRODUCT_SUB_PATH
                path = path.replace(FRAMEWORK_NAME, '')
                if os.path.exists(path):
                    break
        break

    return path


def backup_upload(path, s_v, b_v):
    """
    备份结果，上传私有库
    :param path:编译结果路径
    :param s_v:short version
    :param b_v:build version
    :return:
    """
    if not os.path.exists(OUT_PATH):
        os.makedirs(OUT_PATH)

    move_path = '%s_%s_%s_%s' % (PROJECT_NAME, s_v, b_v, TIME)
    shutil.copytree(path, '%s/%s' % (OUT_PATH, move_path))

    for folder, subFolders, files in os.walk('%s/%s' % (OUT_PATH, move_path)):
        for subFolder in subFolders:
            if not subFolder.startswith(PROJECT_NAME + '.'):
                shutil.rmtree(folder + '/' + subFolder)
        break
    os.system('open ' + OUT_PATH)

    is_upload = input_func('upload(Y/N):')

    if is_upload == 'Y' or is_upload == 'y':
        os.chdir(OUT_PATH)
        os.system('jfrog rt u %s/ ios-snapshots/ --flat=false' % move_path)


# 'jfrog rt config --user=robot --password=11111.2345 --url=http://11111:9088/artifactory/ --interactive=false'

if __name__ == '__main__':
    short, build = get_current_version()
    result_path = build_framework()
    backup_upload(result_path, short, build)
