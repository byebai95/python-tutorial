#!/usr/bin/python3
# coding=utf-8

# n = 0
#
# for n in range(5):
#     print(n)
# else:
#     print("for 循环结束")


for _ in range(1, 3):
    print('循环体')

print("---------水仙花数-------------")

for index in range(100, 1000):
    a = index % 10
    # b = int(index / 10) % 10
    # c = int(index / 10 / 10)
    b = index // 10 % 10
    c = index // 10 // 10
    if a ** 3 + b ** 3 + c ** 3 == index:
        print(index)

print("---------for-else-------------")

for i in range(1, 3):
    # if i == 2:
    #     break
    pass
else:
    print("循环正常执行结束")
