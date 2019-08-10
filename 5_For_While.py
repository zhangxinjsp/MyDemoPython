import math

from math import sin

print(sin(1))

r = 5
print(math.pi * r ** 2)

x, y = 1, 2
print(x, y)

x, y = y, x
print(x, y)

testDict = {'name': 'xuusa', 'fame': 'fraaa'}

key, value = testDict.popitem()
print(key, value)

seqaa = 1, 2, 3
print(seqaa)

x, y, z = seqaa
print(x, y, z)
# 可以是任何序列
for letter in 'xasdfajkghas':
    print(letter)

for key, value in testDict.items():
    print(key, ':', value)

for i in range(2, 10, 2):
    print(i)

# zip合并序列，返回元组， 以短序列为最终长度
for i in zip(range(9), range(10, 14)):
    print(i)

print(sorted(testDict))

# 阿姆斯特朗数，计算
n = 1
while True:
    nStr = str(n)
    total = 0
    for s in nStr:
        total += int(s) ** len(nStr)
    if total == n:
        print(n)
    n += 1
