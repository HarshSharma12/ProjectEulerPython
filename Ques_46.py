# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 15:47:53 2014

@author: Harsh Sharma

Goldbach's other conjecture

Problem 46
Published on Friday, 20th June 2003, 06:00 pm; Solved by 31210

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
 15 = 7 + 2×2^2
 21 = 3 + 2×3^2
 25 = 7 + 2×3^2
 27 = 19 + 2×2^2
 33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


Answer = 5777
"""
def isPrime(n):
    if(n==1):
        return False
    half = n/2+1
    for i in range(2,int(half)):
        if(n%i==0):
            return False
    return True

n=7
diff = 3
while True:
    n+=2
    if(not isPrime(n)):
        flag=0
        i=1
        diff=3
        while (diff>2):
            diff = n - (2*(i**2))
            i+=1
            if(diff>0):
                if(isPrime(diff)):
                    flag=1
        if(flag==0):
            print n
            break