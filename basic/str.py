#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理
# 1字节 11111111 255 2个字节 65535  4个字节 4294967295
# 最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码 A 65 z 122
# Unicode把所有语言都统一到一套编码里
# 本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间
# 字符	ASCII	     Unicode	                UTF-8
# A	    01000001	00000000 01000001	        01000001
# 中	x	        01001110 00101101	        11100100 10111000 10101101


# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码
# 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件


# 函数获取字符的整数表示
print(ord('A'))
print(ord('中'))
# 函数把编码转换为对应的字符
print(chr(20013))
print('\u4e2d\u6587')
# 编码为指定的bytes
print('ABC'.encode('ascii'), '中文'.encode('utf-8'))
# 把bytes变为str
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
# 字符数
print(len('ABC'), len('中文'))
# 字节数
print(len(b'ABC'),len(b'\xe4\xb8\xad\xe6\x96\x87'),len('中文'.encode('utf-8')))

# 字符串格式化
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制

print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# %s永远起作用，它会把任何数据类型转换为字符串
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)  # %是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

s1 = 72
s2 = 85
r = (1-72/85)*100
print('提升了 {0:.1f}%'.format(r))
print('提升了 %.1f%%' % r)

print('中文'.encode('gb2312'))

