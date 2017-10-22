#! /usr/bin/python
# -*- coding: utf-8 -*-

'''
snmpwalk -v 2c -c root 192.168.99.101 if
snmpwalk -v 2c -c root localhost if

snmpwalk -v 2c -c public 192.168.99.101 .1.3.6.1.2.1.25.2.2
snmpwalk -v 2c -c public 192.168.99.101

snmputil get localhost 192.168.99.101 .1.3.6.1.2.1.1.5.0
snmputil get localhost public .1.3.6.1.2.1.1.5.0

untest

http://www.linuxidc.com/Linux/2014-09/107002.htm
'''

# Author: leexide@126.com
# Python监控网卡流量
"""
1、实现原理：通过SNMP协议获取系统信息，再进行相应的计算和格式化，最后输出结果
2、特别注意：被监控的机器上需要支持snmp。yum install -y net-snmp*安装


snmpwalk -v 1 -c public 192.168.99.101 IF-MIB::ifInOctets.1
snmpwalk -v 1 -c public 192.168.99.101 IF-MIB::ifOutOctets.1

snmpwalk -v 2c -c public 192.168.99.101 .1.3.6.1.2.1.2.2.1.10.2 receive



"""
# !/usr/bin/python
import re
import os
import time


# get SNMP-MIB2 of the devices
def getAllitems(host, oid):
  sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')[:-1]
  return sn1


# get network device
def getDevices(host):
  device_mib = getAllitems(host, 'RFC1213-MIB::ifDescr')
  device_list = []
  for item in device_mib:
    if re.search('eth', item):
      device_list.append(item.split(':')[3].strip())
  return device_list


# get network date
def getDate(host, oid):
  date_mib = getAllitems(host, oid)[1:]
  date = []
  for item in date_mib:
    byte = float(item.split(':')[3].strip())
    date.append(str(round(byte / 1024, 2)) + ' KB')
  return date


if __name__ == '__main__':
  #hosts = ['192.168.10.1', '192.168.10.2']
  hosts = ['192.168.99.101', 'localhost']
  for host in hosts:

    for i in range(2):
      device_list = getDevices(host)

      inside = getDate(host, 'IF-MIB::ifInOctets')
      outside = getDate(host, 'IF-MIB::ifOutOctets')

      print inside, outside;

      #time.sleep(1);

    '''
    print '==========' + host + '=========='
    for i in range(len(inside)):
      print '%s : RX: %-15s  TX: %s ' % (device_list[i], inside[i], outside[i])
    print
    '''

