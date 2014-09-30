# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:18:39 2014

@author: Harsh Sharma

Double-base palindromes

Problem 36
Published on Friday, 31st January 2003, 06:00 pm; Solved by 48445

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are 
palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not 
include leading zeros.)


Answer =  872187
"""
from numpy import binary_repr

def isPal(n):
    x=n
    new=0
    while x!=0:
        dig = x%10
        x=int(x/10)
        new=new*10+dig
    return (new == n)

i=0
count =0
total = 0
while(i<1000000):
    i+=1
    if(isPal(i) and isPal(int(binary_repr(i)))):
        count+=1
        print i
        print binary_repr(i)
        total+=i
print 'Answer = ', total
        
    