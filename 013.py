#! /usr/bin/python
# -*- coding: utf-8 -*-

print '转换';

str = u'\u81ea\u8d38\u534f\u5b9a\u906d\u5acc\u5f03 \u7279\u6717\u666e\u6253\u7684\u4ec0\u4e48\u724c';
print str;

f = open('sss.txt', 'wb');
f.write(str)