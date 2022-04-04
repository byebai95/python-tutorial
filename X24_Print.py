#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/4-19:42

# 输出数字
print(100)
print(91.24)

# 输出字符串
print("HelloWorld")
print('HelloWorld 2.0')

# 单行输出
print("Job", "Bob", "Lucy")

# 输出到文件
# a+ 表示没有则创建，有则追加
fs = open("d:/test.txt", "a+")
print("abcd", file=fs)
fs.close()

print("转义字符")
print("Hello\n") # 回车
print("Hello\tWorld") # 占用一个制表符，当前只需要3个字符位
print("Hello\bWorld") # 回退一个字符
print("Hello\rWorld") # Hello 字符被 World 覆盖
# 原字符,不对字符进行转义
print(r"Hello\n\rWorld")

