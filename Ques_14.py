# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 10:57:45 2014

@author: Harsh Sharma

Longest Collatz sequence

Problem 14
Published on Friday, 5th April 2002, 06:00 pm; Solved by 111090

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

No of elements in sequence =  524
Answer =  837799

"""

num = 1000000
count2 = 0
#seq = []

for i in range(num,1,-1):
    if(i%10000==0):
        print i
    x=i
    count = 0
    #arr = []
    while x!=1:
        #arr.append(x)
        if(x%2==0):
            x=x/2
        else:
            x=3*x+1
        count+=1
        
    count2 = max(count2, count)
    if(count2==count):
        ans = i
        #seq = arr

#print seq
print 'No of elements in sequence = ', count2
print 'Answer = ', ans
        