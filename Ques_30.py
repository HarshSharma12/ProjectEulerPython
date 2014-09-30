# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:01:24 2014

@author: Harsh Sharma

Digit fifth powers

Problem 30
Published on Friday, 8th November 2002, 06:00 pm; Solved by 57296

Surprisingly there are only three numbers that can be written as
the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of
fifth powers of their digits.

Answer = 443839

"""
i=2
summation = 0
ans,count = 0,0
while i<5000000:
    summation=0
    if (int(i%1000000) == 0):
        print i
    i+=1
    x=i
    while x!=0:
        dig = x%10
        x=x/10
        summation+=(dig**5)
    if(summation==i):
        print 'Num = ', i
        count+=1
        print 'Count = ', count
        ans +=i

print ans
