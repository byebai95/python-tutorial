#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-17:02

class Student:
    # 这是类属性，所有实例共享
    native_address = "深圳"

    def __init__(self, name, age):
        # 这是实例属性，不共享,所有实例都有的属性
        self.age = name
        self.name = age

    def eat(self):
        print("学生在吃饭---实例方法")

    @classmethod
    def sleep(cls):
        print("学生在睡觉---类方法")

    @staticmethod
    def work():
        print("在工作--静态方法")


print('-------类对象信息--------')
print(id(Student))
print(type(Student))
print(Student)

print('------实例使用--------')
stu1 = Student('Job', 20)
stu1.eat()
stu1.sleep()
stu1.work()

# Student.eat() 报错，类对象不能调用实例方法
Student.sleep()
Student.work()
Student.eat(stu1)

print('------动态绑定属性--------')
stu1 = Student('Jack', 20)
stu2 = Student('Lucy', 18)
stu1.sex = 'boy'
print(stu1.name, stu1.age, stu1.sex)
# print(stu2.sex) ,报错，动态属性只绑定在 stu1

print('------动态绑定方法--------')


def say():
    print("类外方法")


stu1.method = say
stu1.method()
