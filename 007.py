#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
  count = 0
  while count < 5:
    time.sleep(delay)
    count += 1
    aaa = threadName + '--' + time.ctime(time.time())
    print aaa;


# 创建两个线程
try:
  thread.start_new_thread(print_time, ("Thread-1", 1,))
  thread.start_new_thread(print_time, ("Thread-2", 2,))
  thread.start_new_thread(print_time, ("Thread-3", 1,))
except:
  print "Error: unable to start thread"

while 1:
  pass