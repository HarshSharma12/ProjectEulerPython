# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 12:48:17 2014

@author: Harsh Sharma

Amicable numbers


Problem 21
Published on Friday, 5th July 2002, 06:00 pm; Solved by 74130

Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


Answer =  31626
"""
from math import sqrt
def divisors(n):
    sqRoot = int(sqrt(n))
    arr = [1]
    for i in range(2,sqRoot+1):
        if(n%i==0):
            arr.append(i)
            arr.append(n/i)
            arr.sort()
    return arr

def divSum(n):
    d = divisors(n)    
    x=0
    for i in d:
        x+=i
    return x
       
total = 0
for i in range(1, 10000):
    newNum = divSum(i)
    if (divSum(newNum) == i and newNum!=i):
        total+=i
        print 'New = ', newNum
        print 'Original = ', i
        print 'Sum = ', total
        print '\n'

print 'Answer = ', total