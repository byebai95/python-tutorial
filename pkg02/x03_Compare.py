#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-10:50

# 基本比较运算符
a, b = 10, 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# == 比较的是 value
# is/is not 比较的是 id

print('------------------')
a, b = 10, 10
print(a == b)
print(a is b)
print(id(a))
print(id(b))

