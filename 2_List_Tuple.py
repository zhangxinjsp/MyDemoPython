# 列表

# 序列
s = 'hello'
l = [1, 2, 3, ]
print('第三个字符：', s[3])
print('第一到三个字符：', s[1:3])
print('第一个开始步长为2：', s[::2])
print('第一个开始步长为-1：', s[::-1])

print('string * ', s * 3)
print('string + ', s + s)
print('list *', l * 3)

print('list len', len(l))
print('list min', min(l))
print('list max', max(l))

print('string len', len(s))
print('string min', min(s))
print('string max', max(s))

# 列表
print(type(l))
l[1] = 10
print(l)
l[2] = 'third'
print(l)

l.append(4)
print(l)
# 删除列表元素
del l[1]
print(l)

l = list('abcdefg')
print(l)

l[4:] = list('uvwxyz')
print(l)

l[7:] = []
print(l)

del l[4:]
print(l)

print(l.count('a'))

l.extend(l)
print(l)

print(l.index('b'))

l.insert(5, 4444)
print(l)

print(l.pop(2))  # 索引为可选参数，默认-1
print(l)

l.remove(4444)
print(l)

print(sorted(l))

print(sorted('zusiefsdf'))

l.reverse()
print(l)

l.sort()
print(l)

l.clear()
print(l)


# 元组

s = 'hello'
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
t = (1, 2, 3,)

print(tuple(s))
print(tuple(l))

print(t[1])
print(t[1:])

print(t + t)