#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 元组 tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
print(classmates[0], classmates[-1])

t = ()
print(t)

# 数字1 非tuple
t = (1)
print(t)

# 字符串a，非tuple
t = ('a')
print(t)

# 定义一个元素的tuple 加一个逗号,，以免你误解成数学计算意义上的括号
t = (1,)
print(t)

# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
