#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 什么都不做的函数
def do_nothing():
    pass


print('什么都不做的函数')
do_nothing()


# 参数必传函数
def param_one(param):
    print(f'传入参数值: {param}')


param_one('hello')


# 默认值参数  ⚠️默认参数只能从后往前排（有默认参数之后的所有参数都必须有默认参数）
def default_param(name='default', age=23):
    print(f'name is {name}')
    print(f'age is {age}')


default_param()
default_param('val')
default_param(age=40)


# 关键字参数
def person_info(name, age):
    print('name is ', name)
    print('age is ', age)


print(f'----------参数顺序传入--------')
person_info('zhangxin', 30)
print(f'----------参数指定传入---------')
person_info(age=20, name='xxxxx')


# 可变参数(元组)
def multi_param(name, *otherparam):
    print(f'name is {name}')
    print(f'other param is {otherparam}')


multi_param('name')
multi_param('name', 21, 'beijing')


# 可变参数(dict)
def multi_param_2(name, **other):
    print('name is ', name)
    print('other is ', other)


multi_param_2('namesssss', age=10, sex='mail')

# 变量
# ⚠️  在函数内部对全局变量操作时需要使用关键字global
num = 100
num1 = 100
print(num, ',', num1)


def sum_num():
    global num
    num = 200
    num1 = 200
    print(num, ',', num1)


sum_num()
print(num, ',', num1)


# 返回值函数
def powss(a, b):
    return a ** b


print(f'a^b = {powss(2, 3)}')


# 函数的嵌套返回
def func_count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = func_count()
print(f'{f1()}')
print(f'{f2()}')
print(f'{f3()}')

# 匿名函数的使用

print([item for item in filter(lambda s: s > 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])])

filterObj = filter(lambda s: s > 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
for item in filterObj:
    print(f'filter item {item}')

c = lambda x: x ** 2
print(c(12))

c = lambda x, y=2: x ** y  # 默认参数
print(c(12))
print(c(12, 3))
