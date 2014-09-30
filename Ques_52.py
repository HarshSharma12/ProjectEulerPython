# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 12:03:27 2014

@author: Harsh Sharma

Permuted multiples
Problem 52
Published on Friday, 12th September 2003, 06:00 pm; Solved by 35917

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

Answer =  142857
"""

def digits(num):
   x=num
   a=[]
   while(x!=0):
       a.append(x%10)
       x=x/10
   a.sort()
   return a

i=2
while True:
    i=i+1
    if(digits(i) == digits(2*i)== digits(3*i)== digits(4*i)== digits(5*i)== digits(6*i)):
        print 'Answer = ',i
        break