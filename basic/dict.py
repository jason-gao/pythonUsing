#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {"m": 95, "b":75, "t":85}
m = d['m']
print(m)

# 赋值
d['a'] = 67
print(d,d['a'])

d['a'] = 50
print(d,d['a'])


# key不存在报错
# print(d['c'])
'''
error:
File "/Users/crystal/codes/python/github/jason-gao/pythonUsing/basic/dict.py", line 14, in <module>
    print(d['c'])
KeyError: 'c' 
'''


'''
要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
注意：返回None的时候Python的交互环境不显示结果
'''
r = 'c' in d
print("r", r)
r1 = d.get('c')
print("r1", r1)
r2 = d.get('c', -2)
print('r2', r2)

# 删除key
# pop(key)方法，对应的value也会从dict中删除
print('d', d)
r = d.pop('b')
print('r', r, 'd', d)

# key需为不可变
key = [1,2,3]
d[key] = 'a list'
'''
Traceback (most recent call last):
  File "/Users/crystal/codes/python/github/jason-gao/pythonUsing/basic/dict.py", line 46, in <module>
    d[key] = 'a list'
TypeError: unhashable type: 'list'
'''

