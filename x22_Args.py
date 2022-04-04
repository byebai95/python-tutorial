#!/usr/bin/python3


def multiArgs(*a, **b):
    print(a)
    print(b)


multiArgs(1, 2, 3, d=4)
