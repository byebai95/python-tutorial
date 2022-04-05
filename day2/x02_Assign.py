#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-10:29

# 运算是从右向左
i = 10 + 20
print(i)

# 链式赋值 ,表示 python 中变量是引用类型，都指向同一块地址
a = b = c = 10
print(a, id(a))
print(b, id(b))
print(c, id(c))

print('-----------参数赋值-----------')
# 参数赋值
a = 2
print("a", a, id(a), type(a))  # 创建变量为 2 的地址

a += 10
print("a += 10", a, id(a), type(a))  # 重新创建一个变量地址 12， a 指向 4

a -= 10
print("a -= 10", a, id(a), type(a))  # 已经存在变量值为2的地址，a 重新指向 2

a *= 6
print("a *= 6", a, id(a), type(a))  # 已经存在 12的变量，a 重新指向 12的地址

a /= 3
print("a /= 3", a, id(a), type(a))  # 创建新的地址 4.0 ，a指向 4.0的地址

a //= 2
print("a //= 2", a, id(a), type(a))  # 创建新的变量 2.0

a %= 2
print("a %= 2", a, id(a), type(a))

print('-----------系类解包赋值-----------')
a, b, c = 10, 10, 30
print(a, id(a))
print(b, id(b))
print(c, id(c))
# 上述 a ,b 是同类型变量且相同，只创建一个变量地址

print('-----------交换-----------')
a, b = 10, 20
print("交换前：", a, b)
a, b = b, a
print("交换后：", a, b)
