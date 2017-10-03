#!/usr/bin/python
# coding: UTF-8

'''
regex
'''

import re
a = re.match('www', 'www.zerolone.com').span();
print a;

'''
a = re.match('com', 'www.zerolone.com').span();
#print a;
'''

line = "Cats are smarter than dogs"
matchObj = re.match ( r'(.*) are (.*?) .*', line, re.M|re.I)
matchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

#print matchObj;

if matchObj:
  print matchObj.group();
  print matchObj.group(1);
  print matchObj.group(2);


