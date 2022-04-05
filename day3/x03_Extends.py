#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-21:06

class Animal(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def info(self):
        print(self.name, self.sex)


# 继承，python 支持多继承
class Cat(Animal):
    def __init__(self, name, sex, color):
        super().__init__(name, sex)
        self.color = color

    # 此处进行方法重写
    def info(self):
        super().info()
        print(self.color)

    def __str__(self):
        return '我的姓名是{}，我的性别是{}，我的颜色是{}'.format(self.name, self.sex, self.color)


a1 = Cat('日本猫', '雄性', '灰色')
a1.info()

# 默认调用 __str__
print(a1)
