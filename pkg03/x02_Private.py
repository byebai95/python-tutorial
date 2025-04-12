#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-20:45

class People:

    def __init__(self, name, sex):
        self.name = name
        self.__sex = sex

    def say(self):
        print(self.name, ":", self.__sex)


p1 = People('hangman', '男')
p1.say()

print(p1.name)

# 列出实例成员
print(dir(p1))

# 私有属性也可以访问到，需要自觉使用
print(p1._People__sex)
