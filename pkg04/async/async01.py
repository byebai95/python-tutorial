import time


def test():
    print("test begin")
    say()
    print("test finished")


def say():
    time.sleep(2)
    print("say hello")


test()
