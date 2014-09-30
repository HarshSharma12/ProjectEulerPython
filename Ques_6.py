# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 21:50:01 2014

@author: Harsh Sharma

Problem 6
Published on Friday, 14th December 2001, 06:00 pm; Solved by 227917

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

Answer - 25164150

"""
num =100
sumNumbers = (num*(num+1))/2
sumSquares = 0
for i in range(1,num+1):
    sumSquares += i*i

print 'Difference = ', abs(sumSquares - (sumNumbers**2))