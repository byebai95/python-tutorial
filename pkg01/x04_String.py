#!/usr/bin/python3
# coding=utf-8

# +字符串连接符， * 复制字符串，后面为次数

str1 = "Hello"
str2 = "World"

print(str1 + str2)

# 字符串截取
print(str1[0:len(str1)])
print(str1[-len(str1):])

s1 = '你好 python'
s2 = "你好 python"
s3 = '''你好 ,
 python'''
s4 = """你好 ,
python"""
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
