#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-10:06

print('----------算术运算符----------')
print(1 + 2)
print(1 - 2)
print(2 * 4)
print(2 / 4)
print(9 % 2)
print(9 // 2)  # 整除，向下取整
print(2 ** 4)  # 幂次运算

print('----------// 负数操作,向下取整----------')
print(-9 // -2)  # 4
print(9 // -2)  # -5
print(-9 // 2)  # -5

print('----------% 负数操作----------')
print(-9 % -2)  # -1
print(9 % -2)  # -1
print(-9 % 2)  # 1

print('----------练习----------')

# 余数计算 ： 余数 = 被除数- 除数*商
print(5 % 3)  # 5-3*1 =2
print(5 % 2)  # 5 -2*2 = 1

# 注意，商是负数的向下取整
print(5 % -3)  # 5 -(-3)*(-2)= -1
print(5 % -2)  # 5 - (-2)*(-3) = -1
