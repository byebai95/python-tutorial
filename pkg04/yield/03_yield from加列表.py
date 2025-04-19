lst = [1, 2, 3, 4, 5]


def yield_from_lst():
    try:
        yield from lst
    except TypeError as e:
        print(f"TypeError: {e}. 请确保lst是一个可迭代对象。")
    except Exception as e:
        print(f"发生了一个意外错误: {e}")


if __name__ == '__main__':
    # yield from 所在的函数返回一个生成器对象，可以用for循环来迭代
    print(list(yield_from_lst()))

    try:
        for item in yield_from_lst():
            print(item)
    except Exception as e:
        print(f"主程序中发生错误: {e}")
