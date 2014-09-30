# -*- coding: utf-8 -*-
"""
Solved on - 3/10/2011
@author: Harsh Sharma

Problem 9

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
                                    a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

ANSWER - 31875000
a =  200
b =  375
c =  425
"""


a=0
b=0
c=0
i=True
while i==True:
    for a in range(1,500):
        for b in range (1,500):
            for c in range(1,500):
                if ((a*a)+(b*b)-(c*c)==0 and a!=b):
                    if(a+b+c == 1000):
                        print a*b*c
                        print 'a = ',a
                        print 'b = ',b
                        print 'c = ',c
                        i=False
                        break
