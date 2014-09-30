# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 13:36:34 2014

@author: Harsh Sharma

Truncatable primes

Problem 37
Published on Friday, 14th February 2003, 06:00 pm; Solved by 38676

The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly 
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable 
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

ANSWER - 748317
"""
def isPrime(n):
    if(n==1):
        return False
    half = n/2+1
    for i in range(2,int(half)):
        if(n%i==0):
            return False
    return True
    

sum1 =23+37+53+73+313+317+373+797+3137+3797
num = 539390
count = 10
while True:
    i = num
    j = num
    if(num%10==3 or num%10==7):
        while i!=0:
            power = len(str(i))-1
            if(isPrime(i)):
                i = i%pow(10, power)
            else:
                break
    while j!=0:
        if(isPrime(j)):
            j=j/10
        else:
            break
        
    if(i==0 and j ==0):
        print '     num = ', num
        count+=1
        sum1+=num
        if(count ==11):
            break
    num+=1
    
print 'Final Count = ',count
print 'Sum = ',sum1

