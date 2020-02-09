#!/usr/bin/env python3
# -*- coding: utf-8 -*-


age = 20
if age >= 18:
    print('your age is ', age)
    print('adult')

print('------------------\n')
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

print('------------------\n')
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

print('------------------\n')

# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数
birth = input('birth: ')
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')
