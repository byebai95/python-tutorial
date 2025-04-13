# 有 yield 的函数
import time


def task():
    print("Task started")
    big_task()
    print("Task finished")


# small_task()  返回生成器，函数本身不会被执行
def big_task():
    print("Big task started")
    gen = small_task()
    print("Big task finished")


def small_task():
    print("Small task started")
    yield time.sleep, 2
    print("Small task finished")


task()
