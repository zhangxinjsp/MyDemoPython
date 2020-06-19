#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


# 函数装饰器，不带参数
def timer(func):
    def decor(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        d_time = end_time - start_time
        print(func.__name__)
        print("耗时 : ", d_time)

    return decor


@timer
def func_timer(ss, bb):
    print('ssss' + ss + bb)


func_timer(ss="11", bb="bb")
print(func_timer.__name__)


# 函数装饰器，带参数
def new_timer(param):
    def timer1(func):
        def decor(*args):
            start_time = time.time()
            func(*args)
            end_time = time.time()
            d_time = end_time - start_time
            print(param)
            print(func.__name__)
            print("耗时 : ", d_time)

        return decor

    return timer1


@new_timer("new timer")
def func_new_timer(ss, bb):
    print('ssss' + ss + bb)


func_new_timer("--------", "+++++++++")


# 类装饰器
class Count:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print('func is called num is:{}'.format(self.count))
        return self.func(*args, **kwargs)


@Count
def func_count():
    print('func_count...')


for i in range(3):
    func_count()


class NewCount:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, func):
        self.func = func
        return self.inner

    def inner(self, *args, **kwargs):
        print(self.name, self.age)
        self.func(*args, **kwargs)


@NewCount('cccc', 12)
def func_new_count():
    print('func_new_count...')


for i in range(3):
    func_new_count()
