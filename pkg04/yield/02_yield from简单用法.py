def sub_generator():
    yield 1
    yield 2


def main_generator():
    yield from sub_generator()
    yield 3
    yield 4


# yield from 后面的对象必须是一个可迭代对象，或者是一个生成器函数。
# 它会把这个可迭代对象里面的元素一个个的 yield 出来。
# 这里的 sub_generator() 函数是一个生成器函数，它会 yield 1 和 yield 2。
# 而 main_generator() 函数的 yield from 后面跟的是 sub_generator() 函数，
if __name__ == '__main__':
    for i in main_generator():
        print(i)
