#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-11:53

r = range(10)
print(r)  # 返回一个迭代器对象
print(list(r))  # 默认从 0 开始，步长为 1 , 一个参数表示结束标志

r = range(2, 10)
print(list(r))  # 2个参数表示开始位置与结束位置

r = range(2, 10, 2)  # 三个参数表示开始，结束，步长
print(list(r))

# range() 函数只记录开始结束与步长，只有在使用的时候才会计算并创建空间

# in , not in 用于判断元素是否存在
print(2 in r)
print(10 not in r)
