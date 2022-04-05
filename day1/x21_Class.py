#!/usr/bin/python3

class Animal:

    def __init__(self):
        self.type = 'super'
        print("Animal init")

    def eat(self):
        print("Animal eat")


a1 = Animal()
a1.eat()
print(a1.type)


class People(Animal):
    age = 10

    def __init__(self):
        super().__init__()
        self.type = 'sub'
        print("People init")

    def eat(self):
        print("People eat")

    def __call__(self, *args, **kwargs):
        print("People call", args, kwargs)


a2 = People()
a2.eat()
print(a2.type)
print(a2.age)

a2(20, '123', {"name": "hangnail"}, a=5)
