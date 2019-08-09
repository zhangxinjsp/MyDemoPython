# coding=utf-8

import math

a = 30
b = 21

# 整数
print('======整数============')
print('a + b = ', a + b)
print('a - b = ', a - b)
print('a * b = ', a * b)
print('a ** b = ', a ** b)
print('a / b = ', a / b)
print('a // b = ', a // b)  # 地板除，整数的除法还是整数
print('a % b = ', a % b)

# 浮点型
c = 3.3
d = 102
e = 10.5
print('======浮点型============')
print(c * d)
print(d / c)
print(d // c)

print('======转换============')
print(int(c))
print(float(d))
print(complex(d))
print(complex(d, a))

print(math.pi)
print(math.e)

print('a' in 'abcdef')
print('a' not in 'abcdef')

print(a is b)
print(a is not b)
