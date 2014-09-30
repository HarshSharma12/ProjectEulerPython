# -*- coding: utf-8 -*-
"""
@author: Harsh Sharma

Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Answer - 1366
"""

x=2**1000
n=0
l=[]
print x
while x>0:
    n=x%10
    x=x/10
    l.append(n)

i=0
sum1=0
Sum of digits
while i<len(l):
    sum1+=l[i]
    i+=1

print 'Sum is '
print sum1
