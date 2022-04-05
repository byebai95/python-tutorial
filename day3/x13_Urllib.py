#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-22:13

import urllib.request

response = urllib.request.urlopen("https://www.baidu.com")
print(response.read().decode("utf-8"))


