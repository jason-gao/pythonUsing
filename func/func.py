#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@File    : func.py
@Time    : 2020-05-26 22:45
@Author  : jason-gao
@Email   : 3048789891@qq.com
@Devtool: PyCharm
"""
import math

# basic
print(abs(-100))
print(max(2, 3, 1, -5))
print(bool(1))
print(bool(''))
print(bool(0))
print(bool(2))

# 整数转换成十六进制

n1 = 255
n2 = 1000

print(hex(n1))
print(hex(n2))


# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))


# print(my_abs('A'))

# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，
# 用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：


def nop():
    pass


age = 10
if age >= 18:
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


# tuple
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

print(math.sqrt(2))
print(math.sqrt(3))
print(math.sqrt(4))
print(math.sqrt(5))
print(math.sqrt(6))


# def power(x):
#     return x * x
#
#
# print(power(3))
# print(power(25))


# 必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）
# 函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2))
print(power(2, 3))
print(power(2, 4))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


print(enroll('a', 'M'))
print("\n")
print(enroll('b', 'F', 7))
print('\n')
print(enroll('b', 'F', city='tianjin'))


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1,2,3]))
print(calc((1,2,3,4)))

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1,2,3))
print(calc(1,2,3,4))

