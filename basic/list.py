#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list是一种有序的集合，可以随时添加和删除其中的元素


classmates = ['Michael', 'Bob', 'Tracy']

print(classmates)
print(len(classmates))
print(classmates[0], classmates[1], classmates[2])
# IndexError: list index out of range
# print(classmates[3])

# last index len(classmates) - 1

# 获取最后一个元素
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print(classmates)
# 插入指定位置
classmates.insert(1, 'jack')
print(classmates)

# 删除末尾的元素
classmates.pop()
print(classmates)

# 删除指定位置的元素
print(classmates.pop(1))
print(classmates)

# 替换 赋值
classmates[1] = 'job'
print(classmates)

# 元素类型可以不同
L = ['Apple', 123, True]
print(L)
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print(len(s))

p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s)
print(p[1])
print(s[2][1])
print(s[0])

L = []
print(len(L))
