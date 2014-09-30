# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 14:35:07 2014

@author: Harsh Sharma

Champernowne's constant

Problem 40
Published on Friday, 28th March 2003, 06:00 pm; Solved by 42578

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

Answer =  210
"""

i = '0.1'
x=1
last = 1000000
while len(i)<last+3:
    x+=1
    i+=str(x)

i = i[2:]
x = 1
pr = 1
while(x<last+1):
    #if(int(i[x-1])!=0):
    print int(i[x-1])
    pr*=int(i[x-1])
    x*=10
    
print 'Answer = ', pr
    
