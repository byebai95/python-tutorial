#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-21:31

class A:

    # 创建对象时调用
    def __init__(self):
        pass

    # + 运算符重载
    def __add__(self, other):
        pass

    # 长度运算符重载
    def __len__(self):
        pass

    #  创建对象的第一步，后续执行 init
    def __new__(cls, *args, **kwargs):
        pass
