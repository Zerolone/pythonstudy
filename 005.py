#!/usr/bin/python
# coding: UTF-8

'''
regex match 与 search区别
'''

import re
a = re.match('www', 'www.zerolone.com').span();
print a;

'''
a = re.match('com', 'www.zerolone.com').span();
#print a;
'''

line = '''
Cats are smarter1 than dogs
Cats are smarter2 than dogs
Cats are smarter3 than dogs
'''
matchObj = re.match ( r'are (.*?) .*', line, re.M|re.I)
if matchObj:
  print matchObj.group();
  print matchObj.group(1);
else:
  print 'no match'



matchObj = re.search( r'are (.*?) .*', line, re.M|re.I)

#print matchObj;

if matchObj:
  print matchObj.group();
  print matchObj.group(1);
else:
  print 'no match'




matchObj = re.search( r'are (.*?) .*', line, re.M|re.I)

#print matchObj;

if matchObj:
  print matchObj.group();
  print matchObj.group(1);
else:
  print 'no match'


line = '''
Cats are smarter1 than dogs
Cats are smarter2 than dogs
Cats are smarter3 than dogs
'''
matchObj = re.findall( r'are (.*?) than (.*)', line, re.M|re.I)

print matchObj;


matchObj = re.finditer( r'are (.*?) .*', line, re.M|re.I)

print matchObj;
