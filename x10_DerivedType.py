#!/usr/bin/python3
# coding=utf-8

# 列表推导式
lst = [x for x in 'abc-def']
print(lst)

# 字典推导式
dct = {k: len(k) for k in lst}
print(dct)

# 集合推导式
sets = {x for x in range(1, 20)}
print(sets)

# 元组推导
tps = (x for x in range(1, 10))
print(tps)
# 元组必须使用函数才能输出
print(tuple(tps))
