#!/usr/bin/python3
# coding=utf-8

n = 0
while n < 10:
    print(n)
    n += 1
else:
    print("while 结束")

print('-------- while-else --------')

n = 0
while n < 10:
    # if n == 9:
    #     break
    n += 1
else:
    print("while 执行完")
