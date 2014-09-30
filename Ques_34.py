# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:14:54 2014

@author: Harsh Sharma

Digit factorials

Problem 34
Published on Friday, 3rd January 2003, 06:00 pm; Solved by 49939

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the 
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Answer =  40730
"""

def factorial(n):
    fact=1    
    if(n<=1):
        return fact
    for i in range(1, n+1):
        fact*=i
    return fact

i=3
summation = 0
ans,count = 0,0
while i<9000000:
    summation=0
    if (int(i%1000000) == 0):
        print i
    i+=1
    x=i
    while x!=0:
        dig = x%10
        x=x/10
        summation+=factorial(dig)
    if(summation==i):
        print 'Num = ', i
        count+=1
        print 'Count = ', count
        ans +=i
        
print 'Answer = ', ans