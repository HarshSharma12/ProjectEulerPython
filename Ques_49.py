# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 15:25:00 2014

@author: Harsh Sharma

Prime permutations

Problem 49
Published on Friday, 1st August 2003, 06:00 pm; Solved by 29614

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?


Answer - 296962999629
"""
def isPrime(n):
    if(n==1):
        return False
    half = n/2+1
    for i in range(2,int(half)):
        if(n%i==0):
            return False
    return True

def digits(num):
   x=num
   a=[]
   while(x!=0):
       a.append(x%10)
       x=x/10
   a.sort()
   return a

for i in range(1000, 3340):
    
    if(isPrime(i) and  isPrime(i+3330) and isPrime(i+3330+3330)):
        if(digits(i)==digits(i+3330) and digits(i)==digits(i+3330+3330) and i!=1487):
            print i
            print i+3330
            print i+3330+3330
            print 'Answer =',str(i)+str(i+3330)+str(i+3330+3330)
        