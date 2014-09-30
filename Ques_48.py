# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 15:02:48 2014

@author: Harsh Sharma

Self powers


Problem 48
Published on Friday, 18th July 2003, 06:00 pm; Solved by 64195

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

Ans = 9110846700

"""
sum = 0
for i in range(1,1000):
    sum+=pow(i,i)

a = str(sum)
print a[len(a)-10:len(a)]