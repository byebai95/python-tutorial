#!/usr/bin/python3
# coding=utf-8
# create-time: 2022/4/5-22:22
import time

import schedule


def job():
    print("执行中")


schedule.every(1).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
