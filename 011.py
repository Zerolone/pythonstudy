#!/usr/bin/python

class a:
  def aaa(self):
    print 'a--aaa';
    
class b:
  def aaa(self):
    print 'b--bbb';
    
class c(a):
  pass;

class d(b):
  pass;

class e(a,b):
  pass;

class f(b,a):
  pass;


a1 = a(); a1.aaa();
b1 = b(); b1.aaa();
c1 = c(); c1.aaa();
d1 = d(); d1.aaa();
e1 = e(); e1.aaa();
f1 = f(); f1.aaa();









