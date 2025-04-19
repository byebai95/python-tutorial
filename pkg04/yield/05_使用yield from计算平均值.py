def sub_generator():
    count = 0
    total = 0
    average = 0
    while True:
        new_num = yield average
        if new_num is None:
            break
        count += 1
        total += new_num
        average = total / count
    return total, count, average


def proxy_generator():
    while True:
        total, count, average = yield from sub_generator()
        print(f"总和：{total}, 数量：{count}, 平均值：{average}")


if __name__ == '__main__':
    generator = proxy_generator()
    next(generator)  # 启动生成器

    # send()方法可以向生成器发送数据，并获取生成器的返回值, 返回值是yield语句的表达式的值， send发送的值给yield左侧的变量
    print(generator.send(10))
    print(generator.send(20))
    print(generator.send(30))
    print(generator.send(None))  # 结束生成器
