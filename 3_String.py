# 字符串

str = 'hello mag'

# 字符串截取

print(str[4:])

# str[5:] = 'jack'  # 字符串不可以修改

# 格式化
print('he is %s' % 'jacke')

print('i am %s, and he is %s' % ('mast', 'jacke'))

print('i am %d years' % 5)
print('i am %5d years' % 6)
print('i am % 5d years' % 7)
print('i am %05d years' % 8)
print('i am %-5d years' % 9)
print('i am %+5d years' % 10)

print('i am %f years' % 5)
print('i am %.2f years' % 5)
print('i am %7.1f years' % 6)
print('i am % 7.1f years' % 7)
print('i am %07.1f years' % 8)
print('i am %-7.1f years' % 9)
print('i am %+7.1f years' % 10)

print('i am %*.*f' % (7, 2, 11))

# 方法
str = 'i CAN do it'
# find
print("find is ::", str.find('it'))
print("find is ::", str.find('do', 3, 10))  # 可以定义起点终点
print("find is ::", str.find('im'))  # 返回-1 找不到
# join 字符串数字使用指定字符相恋
num = ['1', '2', '3', '4', '5', '6']
mark = '+'
print(mark.join(num))

# upper, lower大小写转化
print(str.upper())  # 大写
print(str.lower())  # 小写
print(str.swapcase())  # 大小写呼唤

# replace
str = 'i CAN do it, i like it, it it'
print(str.replace('it', 'them'))
print(str.replace('it', 'them', 3))

# split 字符串切割
print(str.split())  # 默认空格
print(str.split('i'))
print(str.split('t', 2))

# strip 去除首位指定字符
str = '    ------love you -------      '
print(str.strip())  # 默认空格
str = '------love you ------    ---'
print(str.strip('- '))

intab = '-abio'
outtab = '~1234'
table = str.maketrans(intab, outtab)
print(str.translate(table))
