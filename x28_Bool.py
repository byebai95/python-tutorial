#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/4-20:55

f1 = True
f2 = False
print(f1, type(f1))
print(f2, type(f2))

# bool 可以与整数运算， True 值为 1 ，False 值为 0
print(f1 + 10)
print(f2 + 10)

# 逻辑判断，0为 False ,非零为 True
if 10.1:
    print("Talse")
else:
    print("True")
