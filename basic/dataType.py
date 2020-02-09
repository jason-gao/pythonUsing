#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 整数
# 100 0xff00
# ！！！没有大小限制！！！ java int32 -2147483648-2147483647

# 浮点数
# 1.23
# !!!没有大小限制！！！ inf 无限大

# 字符串
# 'abc' "xyz"  "I'm OK"  'I\'m \"OK\"!'
# r''表示''内部的字符串默认不转义 print(r'\\\t\\') -> \\\t\\
# '''...'''的格式表示多行内容  print('''line1
# ... line2
# ... line3''')

# boolean
# True False
# and or not
# True and True  True and False 5 > 3 and 3 > 1
# True or False 5 > 3 or 1 > 3
# not True  not False

# demo
age = 10
if age >= 18:
    print('adult')
else:
    print('teenager')


# 空值
# None

# 变量  变量名必须是大小写英文、数字和_的组合，且不能用数字开头
# a = 1
a = 'ABC'
b = a
a = 'XYZ'
print(b)
print(a)

# 常量
PI = 3.14159265359
c = 10 // 3
print(PI, c)

# demo
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n, f, s1, s2, s3, s4)