#!/usr/bin/python
# 循环显示数字

for i in range(1,10):
  #print i;

  for j in range(1,10):
    #print j;

    for k in range(1,10):
      if(i == j or j==k or i==k):
        '1'
      else:
        print i,j, k;


