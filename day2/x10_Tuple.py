#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-15:07

print('-----------元组的创建方式------------')

# 方式一
t1 = ('name', 100, True)
print(t1, type(t1))

t2 = 'lucy', 10
print(t2, type(t2))  # ,如果只有一个元素，需要加 ,

t3 = tuple((1, 2, 3, 4))
print(t3, type(t3))

# 元组中存储的是引用，引用本身不可修改，但是引用指向的可变对象可以进行修改

print('-----------元组的创建方式------------')
t1 = ('name', 100, True, [1, 2, 3])

t1[3].append(4)

for value in t1:
    print(value)
