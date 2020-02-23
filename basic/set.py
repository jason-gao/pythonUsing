#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
#要创建一个set，需要提供一个list作为输入集合
s = set([1,3,2])
print('s', s)

# 重复元素在set中自动被过滤
s = set([1,1,3,3,2])
print('s', s)

# 添加元素
s.add(4)
print('s', s)
s.add(4)
print('s', s)

# 删除元素
s.remove(4)
print('s', s)

# 交集 并集
s1 = set([1,2,3])
s2 = set([2,3,4])
r = s1 & s2
print('r', r)
r2 = s1 | s2
print('r2', r2)

# 不可变对象
# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的
a = ['c', 'b', 'a']
a.sort()
print('a', a)

a = 'abc'
b = a.replace('a', 'A')
print('a', a, 'b', b)


#


