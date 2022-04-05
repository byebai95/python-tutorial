#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-22:47

class A:
    def __enter__(self):
        print("enter 执行了")
        return self

    def show(self):
        print("show 执行", 1 / 0)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit 执行")


with A() as a:
    a.show()

# with 后面是一个上下文管理器，在 Java 可类似 AOP 功能

