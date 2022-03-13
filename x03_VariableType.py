#!/usr/bin/python3
# coding=utf-8

# 1.python3 有6钟数据类型 Number , String ,List ,Tuple , Set ,Directory
# 2. Number String Tuple 为不可变的数据类型

# Number = int float bool complex
age = 65
# 内置 type() 函数可以查询变量类型
print(type(age))
# isinstance() 判断子类是一种父类类型
print(isinstance(type(age), int))

div = 10/3
print(div)

# //会舍去小数部分
divs = 10//3
print(divs)

cmp = 3 + 5j
print(type(cmp))


