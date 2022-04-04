#!/usr/bin/python3
import attr


@attr.s
class Cat:
    name = attr.ib()
    age = attr.ib()


Cat("小喵", 20)
