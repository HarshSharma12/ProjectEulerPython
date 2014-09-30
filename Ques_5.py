# -*- coding: utf-8 -*-
"""
Solved on -1/8/2011

@author: Harsh Sharma
 
Smallest multiple
Problem 5
Published on Friday, 30th November 2001, 06:00 pm; Solved by 226206

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



TAKES LONG TIME TO GENERATE THE VALUE. PLEASE BE PATIENT.
 
ANSWER - 232792560

 
"""

n=1
while n<232792561:
    a=1
    i=2
    while i<21:
        if(n%i==0 and n!=1):
            pass
        else:
            a=0
            break
        i+=1
    if(a==1):
        print n
        break
    n+=1

