#! /usr/bin/python
# -*- coding: utf-8 -*-

import psutil
import time

'''

'''


#all
#print psutil.net_io_counters(True)


aaaa =  psutil.net_io_counters()


bbbb = aaaa.bytes_recv;
#bbbb = aaaa.bytes_sent;

cccc = bbbb;
for i in range(30):
  time.sleep(1);

  bbbb = psutil.net_io_counters().bytes_recv;
  #bbbb = psutil.net_io_counters().bytes_sent;
  dddd = bbbb - cccc;

  cccc = bbbb;

  dddd/=1024;
  print dddd;
  #print dddd;
