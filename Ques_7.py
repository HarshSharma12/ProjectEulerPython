# -*- coding: utf-8 -*-
"""
Solved on - 1/8/2011

@author: Harsh Sharma

10001st prime
Problem 7
Published on Friday, 28th December 2001, 06:00 pm; Solved by 195407

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Answer:	104743

"""
from math import sqrt
n=1
a=0
l=[]
while n<10001:
    a+=1
    b=2
    d=sqrt(a)
    while b<d+1:
        if a%b==0:
            break
        elif (b>=d):
           l.append(a)
           break
        b+=1
    n=len(l)
    n+=1
    

print len(l)
print a


