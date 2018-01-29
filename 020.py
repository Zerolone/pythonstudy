class Animal:
  leg=4;


class AAA:
  eye=2;


class Cat(Animal, AAA):
  pass;


A = Cat();
print(A.leg);
print(A.eye);
