# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 13:15:18 2014

@author: Harsh Sharma

Published on Friday, 16th August 2002, 06:00 pm; Solved by 59793

A permutation is an ordered arrangement of objects. For example, 
3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


ansArraywer - 2783915460
"""



def factorial(n):
    fact=1    
    if(n<=1):
        return fact
    for i in range(1, n+1):
        fact*=i
    return fact

limit = 1000000-1   #Count Starts from 0


i=10
ansArray=[]
ans=0
arr=range(0,10)
z=0
while(limit>0):
    i-=1
    x=0
    num = 0
    while True:
        x+=1
        if(x*factorial(i)>limit):
            print i
            print x-1
            n = arr.pop(x-1)
            print n
            ansArray.append(n)
            break
    num+= (x-1)*factorial(i)
    limit = limit-num
    print 'Limit = ', limit
        
n = arr.pop(0)
ansArray.append(n)
print ansArray
for i in ansArray:
    ans=ans*10+i

print 'Answer = ', ans