# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:41:02 2014

@author: Harsh Sharma

Distinct primes factors

Problem 47
Published on Friday, 4th July 2003, 06:00 pm; Solved by 29858

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?

Answer = 134043
"""

def getFactors(n):
    arr = []
    i=2
    x=n
    while i<n+1:
        if(x%i==0 and i!=1):
            arr.append(i)
            x=x/i
            arr.sort()
            i-=1
        i+=1
    return arr

def disFacts(n):
    dfac = []
    fac = getFactors(n)
    for i in fac:
        if(not i in dfac):
            dfac.append(i)
    return dfac

i=645
count = 0
while count!=4:
    count = 0
    i+=1
    if(len(disFacts(i))==4):
        count+=1
        if(len(disFacts(i+1))==4):
            count+=1
            if(len(disFacts(i+2))==4):
                count+=1
                if(len(disFacts(i+3))==4):
                    count+=1
                
print 'Answer = ', i