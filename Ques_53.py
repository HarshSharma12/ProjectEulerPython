# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 15:29:04 2014

@author: Harsh Sharma

Combinatoric selections


Problem 53
Published on Friday, 26th September 2003, 06:00 pm; Solved by 32628

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
                nCr =  n!
                    r!(n−r)! 
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1. 

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, 
are greater than one-million?

ANSWER = 4075
"""

def fact(num):
    ans = 1
    i=0
    for i in range(1,num+1):
        ans *= i
    return ans

def nCr(n,r):
    return fact(n)/(fact(r)*fact(n-r))
    
    
count = 0
for n in range(23,101):
    if(n%2!=0):
        rr = int((n-1)/2)
    else:
        rr = int(n/2)
    for r in range(1,rr+1):
        nCrVal = nCr(n,r)
        if nCrVal>1000000:
            if(n%2==0 and r==n/2):
                count+=1
            else:
                count+=2
            print n,'C',r, ' = ', nCrVal

print count