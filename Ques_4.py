# -*- coding: utf-8 -*-
"""
Solved on - 2/10/2011

@author: Harsh Sharma
 
Largest palindrome product

Problem 4
Published on Friday, 16th November 2001, 06:00 pm; Solved by 212933

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

ANSWER - 993*913 = 906609

"""
l=[]

def pal():
    n=0
    a=1
    while n<(len(l)/2):
        a=1
        if (l[n]==l[-n-1]):
            pass
        else:
            a=0
            break
        n+=1
    if (a==1):
        return 1
    else:
        return 2

for a in range(100,999):
    for x in range(100,999):
        l=[]
        i=a*x
        while i>0:
            m=i%10
            i=i/10
            l.append(m)
        value=pal()
        if(value==1):
                print 'pal'
                print l
                print a
                print x
                break
        x+=1
    a+=1

