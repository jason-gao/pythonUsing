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

# bmi
height = 1.75
weight = 80.5

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
bmi = weight / height ** 2
if bmi < 18.5:
    print(bmi, '过轻')
elif bmi >= 18.5 and bmi <= 25:
    print(bmi, '正常')
elif bmi > 25 and bmi < 28:
    print(bmi, '过重')
elif bmi >= 28 and bmi <= 32:
    print(bmi, '肥胖')
elif bmi > 32:
    print(bmi, '严重肥胖')

# bmi advance
print('----欢迎使用BMI计算程序----')
name = input('请键入您的姓名:')
height = eval(input('请键入您的身高(m):'))
weight = eval(input('请键入您的体重(kg):'))
gender = input('请键入你的性别(F/M)')
BMI = float(float(weight) / (float(height) ** 2))
# 公式
if BMI <= 18.4:
    print('姓名:', name, '身体状态:偏瘦')
elif BMI <= 23.9:
    print('姓名:', name, '身体状态:正常')
elif BMI <= 27.9:
    print('姓名:', name, '身体状态:超重')
elif BMI >= 28:
    print('姓名:', name, '身体状态:肥胖')
import time;

# time模块
nowtime = (time.asctime(time.localtime(time.time())))
if gender == 'F':
    print('感谢', name, '女士在', nowtime, '使用本程序,祝您身体健康!')
if gender == 'M':
    print('感谢', name, '先生在', nowtime, '使用本程序,祝您身体健康!')
