#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-11:21

print("------以下对象的bool值都为 False ------")

print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(""))
print(bool(None))

print(bool([]))  # 空列表
print(bool(list()))
print(bool(()))  # 空元组
print(bool(tuple()))
print(bool({}))  # 空字典
print(bool(dict()))
print(bool(set()))  # 空集合

print('---------其他类型都为 True-----------')
print(bool(1))
