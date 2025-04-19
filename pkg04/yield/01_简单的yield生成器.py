import time


# 一个简单的yield函数
# yield 关键字只能在生成器函数内部使用，用于暂停和恢复函数的执行。
def simple_generator(n):
    for i in range(n):
        time.sleep(1)
        yield i


for number in simple_generator(5):
    print(number)
