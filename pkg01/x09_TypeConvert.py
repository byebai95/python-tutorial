#!/usr/bin/python3
# coding=utf-8

# 隐式类型转换
a = 10
b = 10.24
print(type(a + b))

# 强制类型转换
c = float("3.14")
print(type(c))

print("--------str() 将其他类型转换为string-----------")
n1 = 10
f1 = 3.14
b1 = True
print(str(n1), type(str(n1)))
print(str(f1), type(str(f1)))
print(str(b1), type(str(b1)))

print("--------int() 将其他类型转换为int-----------")
s1 = '100'
s2 = '3.15'
s3 = 'Ok'
f2 = 'False'
print(int(s1))
# print(int(s2)) ,报错,必须是整数
# print(int(s3))
# print(int(f2))
print("--------float() 将其他类型转换为int-----------")
s1 = '100'
s2 = '3.15'
s3 = 'Ok'
n1 = 10
ff = False
print(float(s1))
print(float(s2))
# print(float(s3)) ,字符串无法转换，只能是数字
print(float(n1))
print(float(ff))
