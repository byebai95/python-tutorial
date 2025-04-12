#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-21:24

class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


c1 = C('小C', 22)
print(c1.__dict__)  # 输出实例的字典属性
print(C.__dict__)
print(C.__mro__)  # 类的层级结构
print(C.__bases__)  # 当前类的父类
print(A.__subclasses__())  # 输出当前类的子类
