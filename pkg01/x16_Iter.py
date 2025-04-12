#!/usr/bin/python3
# coding=utf-8
import sys

lst = [3, 2, 5, 8, 4]

it = iter(lst)

# for x in it:
#     print(x, end=" ")

# while True:
#     try:
#         print(next(it), end=" ")
#     except StopIteration:
#         # sys.exit()
#         break


# 迭代器的使用方法:

class MyIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.end:
            raise StopIteration
        return self.start


my_iter = MyIterator(0, 5)
while True:
    try:
        print(next(my_iter), end=" ")
    except StopIteration:
        break
