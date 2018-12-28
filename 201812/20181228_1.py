# -*- coding: utf-8 -*-
"""
20181228_1.py
super()用法实例
https://mozillazg.com/2016/12/python-super-is-not-as-simple-as-you-thought.html
"""

class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m
        

class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)

        self.n += 3


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)

        self.n += 4


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self,m):
        print('self is {0} @D.add'.format(self))
        super().add(m)

        self.n += 5


d = D()
d.add(2)
print(d.n)

