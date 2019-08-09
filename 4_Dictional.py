#!/usr/bin/python
# coding=utf-8


import json

# 读取内部方法
# print dir(json)

student = [('name', '小萌嗷'), ('number', 2012351)]
print('student 元组： ', student)
# 元组转字典
studentDict = dict(student)
print('元组转字典 student Dict:  ', studentDict)
print('学生姓名：', studentDict['name'])

# 通过参数创建
studentDict = dict(name='飞机', number=1012344)
print('参数创建 student Dict:  ', studentDict)
print('学生姓名：%(name)s' % studentDict)

# 字典中没有key 直接添加新的key
studentDict['class'] = 'magic'
print('student dict:  ', studentDict)

# 删除
del studentDict['class']
print(studentDict)
studentDict.clear()
print(studentDict)
# del studentDict  #删除后不能访问
# print(studentDict)

studentDict = dict(name='飞机', number=1012344, cls='magic')
print('student dict length: ', len(studentDict))
print('student dict type: ', type(studentDict))

# 字符串格式化
print('学生 cls：%(cls)s' % studentDict)

# seq 是序列（数组、元组）
seq = ('name', 'number', 'class')
studentDict = dict.fromkeys(seq, 'mac')
print(studentDict)

print('get sex: ', studentDict.get('sex', 'there is not this value'))

print('sex is in student ', 'sex' in studentDict)
print('name is in student ', 'name' in studentDict)

studentDict.update(dict(name='强', number=123456, cls='mas'))

print(studentDict.items())
print(studentDict.keys())
print(studentDict.values())

print(studentDict.setdefault('class', 'maaaa'))
print(studentDict)
print(studentDict.setdefault('height', 'maaaa'))
print(studentDict)

jsonObj = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}
print(jsonObj)

jsonObj['f'] = 6
print(jsonObj)

jsonStr = json.dumps(jsonObj)
print(jsonStr)

jsonStr = '["foo", {"bar":["baz", null, 1.0, 2]}]'
print(jsonStr)

jsonObj = json.loads(jsonStr)
print(jsonObj)

print(jsonObj.pop())
print(jsonObj)
