'''
装饰器是一种设计模式，它允许在不改变原有对象的情况下，动态地添加功能。

装饰器的基本思想是：在不改变原有对象（函数、类等）的情况下，动态地添加功能。

装饰器的实现方式有两种：

1. 类装饰器：使用类装饰器，可以为一个类动态地添加功能。

2. 函数装饰器：使用函数装饰器，可以为一个函数动态地添加功能。
'''


def my_decorator(func):
    def warpper(*args, **kwargs):
        print('Before function call')
        func(*args, **kwargs)
        print('After function call')

    return warpper


@my_decorator
def my_function(x, y):
    print(x + y)


print(my_function(2, 3))  # Output: Before function call 5 After function call 5
