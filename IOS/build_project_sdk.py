#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time
import shutil

time = time.strftime("%Y%m%d%H%M%S", time.localtime())

PROJECTS = ['Base', 'Communication', 'Network', 'UIComponent', 'Account', 'Mine', 'Vehicle']
PROJECTS = ['Base']
# CONFIG = 'Debug'
CONFIG = "Release"
PROJECT_ROOT_PATH = '/Users/zhangxin/Desktop/CheryProject/CheryWorkspace/'
PROJECT_PATH = ''

OUT_ROOT_PATH = '/Users/zhangxin/Desktop/ArchiveTest/' + time + '/'
OUT_PATH = ''
OS_PATH = 'iphoneos'
SIMULATOR_PATH = 'iphonesimulator'
RESULT_PATH = 'result'

os.chdir(PROJECT_ROOT_PATH)
os.system('xcodebuild -workspace %s -configuration %s -scheme %s -sdk iphoneos' %
          ('CheryWorkspace.xcworkspace', CONFIG, 'CHYBase'))


# os.system('xcodebuild archive -archivePath %s -configuration %s -workspace %s.xcworkspace -scheme %s -sdk iphoneos' %
#           (OUT_ROOT_PATH, CONFIG, 'CheryWorkspace', 'CHYBase'))


def build_framework(project_name):
    global PROJECT_PATH
    global OUT_PATH

    # 进入项目路径
    os.chdir(PROJECT_PATH)

    # 创建编译结果保存目录
    os.makedirs(OUT_PATH[:-1])

    # 编译真机版本
    os.system('xcodebuild clean')
    os.system('xcodebuild -configuration %s -target %s -sdk iphoneos' % (CONFIG, project_name))
    # 复制真机编译结果到指定的目录
    shutil.move('build', OUT_PATH + OS_PATH)
    print('copy iphoneos to >>>>> ' + OUT_PATH + OS_PATH)

    # 编译模拟器版本
    os.system('xcodebuild clean')
    os.system('xcodebuild -configuration %s -target %s -sdk iphonesimulator' % (CONFIG, project_name))
    # 复制模拟器编译结果到指定的目录
    shutil.move('build', OUT_PATH + SIMULATOR_PATH)
    print('copy iphonesimulator to >>>>> ' + OUT_PATH + SIMULATOR_PATH)
    os.system('xcodebuild clean')

    # 创建目录用于合并模拟器和真机
    os.mkdir(OUT_PATH + RESULT_PATH)
    shutil.copytree(OUT_PATH + OS_PATH + '/Release-iphoneos/' + project_name + '.framework',
                    OUT_PATH + RESULT_PATH + '/' + project_name + '.framework')

    # 合并库架构 同时支持模拟器和真机
    lipo_os_path = OUT_PATH + OS_PATH + '/Release-iphoneos/' + project_name + '.framework/' + project_name
    lipo_simulator_path = OUT_PATH + SIMULATOR_PATH + '/Release-iphonesimulator/' + project_name + '.framework/' + project_name
    lipo_result_path = OUT_PATH + RESULT_PATH + '/' + project_name + '.framework/' + project_name

    os.system('lipo -create %s %s -output %s' % (lipo_os_path, lipo_simulator_path, lipo_result_path))
    os.system('lipo -info %s' % lipo_result_path)

# for name in PROJECTS:
#     project_name = 'CHY' + name
#     PROJECT_PATH = PROJECT_ROOT_PATH + name
#     OUT_PATH = OUT_ROOT_PATH + name + '/'
#
#     build_framework(project_name)
