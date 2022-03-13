#!/usr/bin/python3
# coding=utf-8
import sys

lst = [3, 2, 5, 8, 4]

it = iter(lst)

# for x in it:
#     print(x, end=" ")

while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        sys.exit()
