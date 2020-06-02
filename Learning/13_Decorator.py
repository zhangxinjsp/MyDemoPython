#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


# 装饰器，计算插入10000条数据需要的时间
def timer(func):
    def decor(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        d_time = end_time - start_time
        print(func.__name__)
        print("这次插入10000条数据耗时 : ", d_time)

    return decor


@timer
def fuc(ss, bb):
    print('ssss' + ss + bb)


fuc("11", "bb")


def new_timer(param):
    def timer1(func):
        def decor(*args):
            start_time = time.time()
            func(*args)
            end_time = time.time()
            d_time = end_time - start_time
            print(param)
            print(func.__name__)
            print("这次插入10000条数据耗时 : ", d_time)

        return decor

    return timer1


@new_timer("aasdfasdf")
def fuc1(ss, bb):
    print('ssss' + ss + bb)


fuc1("--------", "+++++++++")
