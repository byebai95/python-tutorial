#!/usr/bin/python3
# coding=utf-8
import glob
import os

# 获取当前工作目录
print(os.getcwd())

# 创建目录 today
# os.system('mkdir today')

# 应该是输出 os 模块文件
# print(dir(os))

# 通配符搜索文件列表
print(glob.glob('*.py'))

print(os.pardir)


