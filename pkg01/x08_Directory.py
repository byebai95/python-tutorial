#!/usr/bin/python3
# coding=utf-8

# 字典是k-v存储的

dct = {"name": "张三", "age": 25, "sex": "boy"}

print(dct)
print(dct["name"])

# key 不存在会报错
# print(dct["address"])
print(dct.get("address", "not found"))

dt = {1: "apple", 2: "banana", 3: "orange"}
print(dt)
