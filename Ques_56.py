# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 12:08:27 2014

@author: Harsh Sharma

Powerful digit sum

Problem 56
Published on Friday, 7th November 2003, 06:00 pm; Solved by 31671

A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?


Answer =  972
"""

def digitSum(num):
   x=num
   a=[]
   s=0
   while(x!=0):
       a.append(x%10)
       x=x/10
   a.sort()
   for i in a:
       s+=i
   return s

ans = 0
ansNum1,ansNum2 = 0,0
for a in range(1,100):
    for b in range(1,100):
        x = a**b
        s = digitSum(x)
        ans = max(ans, s)
        if(ans == s):
            ansNum1 = a
            ansNum2 = b
            
print 'Answer = ', ans
print a**b, ' = ', a,'^',b