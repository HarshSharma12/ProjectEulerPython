# -*- coding: utf-8 -*-
"""
Solved on 1/8/2011

@author: Harsh Sharma

Largest prime factor

Problem 3
Published on Friday, 2nd November 2001, 06:00 pm; Solved by 234157

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


ANSWER - 6857

"""

l=[]
from math import sqrt
def primeFacts(a):
    b=2
    d=int(sqrt(a))
    l= []
    while b<d+1:
        flag = b
        if a%b==0:
            a = a/b
            l.append(b)
            b = flag-1
        b+=1
    print l
    print len(l)


#d=range(60085147100,600851475143)
primeFacts(600851475143)
