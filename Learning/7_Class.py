#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyClass(object):

    def method(self):
        print('asdfasdfasdf')

    def method2(self, name, age=20):
        print(f'name is {name}, age is {age}')


a = MyClass()
a.method()
a.method2(name='zhang')
a.method2(age=10, name='zhangxin')
