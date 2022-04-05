#!/usr/bin/python3
# coding=utf-8

tp = ('a', 'b', 100, False)

# 元组不可修改
print(tp)
print(tp[0:4:2])

# 修改会报错，'tuple' object does not support item assignment
tp[0] = 100
print(tp)

