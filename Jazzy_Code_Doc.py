#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import getpass

USER = getpass.getuser()

PROJECT_NAME = 'Base'
PROJECT_PATH = '/Users/%s/Desktop/CheryProject/library/%s' % (USER, PROJECT_NAME)

# PROJECT_PATH = os.path.dirname(__file__)
# PROJECT_NAME = PROJECT_PATH.split('/').pop()

OUT_PATH = '.build_sdk'

os.chdir(PROJECT_PATH)
print(os.getcwd())


def generated_document(version, build):
    """
    安装环境：sudo gem install jazzy
    :param version:
    :param build:
    :return:
    """
    build_arguments = '--xcodebuild-arguments -workspace,%s.xcworkspace,-scheme,%sFramework,-sdk,iphonesimulator' % (
        PROJECT_NAME, PROJECT_NAME)

    os.system('jazzy %s --module %s --output %s/document --author CheryLion --module-version "%s(%s)"' % (
        build_arguments, PROJECT_NAME, OUT_PATH, version, build))


if __name__ == '__main__':
    generated_document('0.0.1', '0.0.3')
