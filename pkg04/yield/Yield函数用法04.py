# 有 yield 的函数
import time


def task():
    print("Task started")
    big_task()
    print("Task finished")


def big_task():
    print("Big task started")
    yield from small_task()
    print("Big task finished")


def small_task():
    print("Small task started")
    yield time.sleep, 2
    print("Small task finished")


task()
