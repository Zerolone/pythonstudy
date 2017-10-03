#!/usr/bin/python

class Employee:
  empCount = 0;
  
  def __init__(self, name, salary):
    self.name = name;
    self.salary=salary;
    Employee.empCount+=1;
    
  def displayCount(self):
    print 'Total Employee %d' % Employee.empCount;
    
  def displayEmployee(self):
    print 'name:', self.name , ', salary:', self.salary;
    
 
a = Employee('zer0', 111);
a.age = 10;
a.displayCount();
a.displayEmployee();

print a.age;
del a.age;
print a.age;

'''
b = Employee('bbb', 1122);
b.displayCount();
b.displayEmployee();

a.displayCount();
'''

