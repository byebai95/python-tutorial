import time


# 无 yield 的函数
def task():
    print("Task started")
    big_task()
    print("Task finished")


def big_task():
    print("Big task started")
    small_task()
    print("Big task finished")


def small_task():
    print("Small task started")
    time.sleep(2)
    print("Small task finished")


task()
