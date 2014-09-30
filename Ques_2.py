# -*- coding: utf-8 -*-
"""
Solved on - 1/08/2011

@author: Harsh Sharma

Even Fibonacci numbers
Problem 2
Published on Friday, 19th October 2001, 06:00 pm; Solved by 320483

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

ANSWER - 4613732

"""

a=0
b=1
s=0
l=[]
while s<4000001:
    s=a+b
    b=a
    a=s
    l.append(s)

def f(x):
    return x%2==0

d = reduce(lambda x, y: x+y, filter(f,l))
print d
