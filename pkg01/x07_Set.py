#!/usr/bin/python3
# coding=utf-8

site = {'Job', 'Lucy', 'Bob'}

print(site)

# set 可以进行集合运算
a = set('abcd')
b = set('cdef')

print(a & b)
print(a | b)
print(a - b)
print(a ^ b)
