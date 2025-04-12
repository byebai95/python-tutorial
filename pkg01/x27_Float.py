#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/4-20:47

pi = 3.1415926
print(pi, type(pi))

n1 = 1.1
n2 = 2.2
print(n1 + n2)

# 浮点数计算可能不准确

from decimal import Decimal

print(Decimal("1.1") + Decimal("2.2"))
