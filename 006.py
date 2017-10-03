#!/usr/bin/python
# coding: UTF-8

'''
https://www.zhihu.com/question/30963225

export PATH=$PATH:/Applications/MAMP/Library/bin

brew install mysql-connector-c
sudo pip install mysql-python
'''

import sys


import MySQLdb
db = MySQLdb.connect('localhost', 'root', 'root', 'test', unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock', charset = 'utf8');

cursor = db.cursor();

sqlStr = 'select * from month limit 10;';

cursor.execute(sqlStr);

#data = cursor.fetchone();
data = cursor.fetchall();


#print data;
for v in data:
  #print r;
  print v[0];
  print v[1];
  print v[2];
  print v[3];
  print v[4];

