#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-15:22

print('-------集合的创建--------')
s1 = {1, 2, 3, 4, 'Hello'}
print(s1, type(s1))

s2 = set([10, 11, 'A'])
print(s2, type(s2))

s3 = set((10, 11, 'Nice'))
print(s3, type(s3))

print('-------集合的增删改--------')
s1 = {1, 2, 3, 4, 'Hello'}
print("原集合", s1)
s1.add(1)
s1.update([2, 10])
print(s1)

# s1.pop() #删除任意一个元素
# print(s1)

s1.remove('Hello')  # 删除不存在的会报错
print(s1)

s1.discard('O')
print(s1)

s1.clear()

del s1

print('-------集合数学运算--------')
s1 = {10, 20, 30}
s2 = {20, 30, 40}

print(s1.intersection(s2))  # 取交集
print(s1 & s2)

print(s1.union(s2))
print(s1 | s2)  # 取并集

print(s1 - s2)  # 取差集

print('-------集合生成式--------')
s1 = {i for i in range(10)}
print(s1)