# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 13:43:19 2014

@author: Harsh Sharma

Problem 25
Published on Friday, 30th August 2002, 06:00 pm; Solved by 80884

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

 F1 = 1
 F2 = 1
 F3 = 2
 F4 = 3
 F5 = 5
 F6 = 8
 F7 = 13
 F8 = 21
 F9 = 34
 F10 = 55
 F11 = 89
 F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

ANSWER - 4782
"""

fn1 = 1
fn2 = 1
fn = 2
i=2
while True:
    fn  = fn1+fn2
    fn1 = fn2
    fn2 = fn
    i+=1
    if(len(str(fn))>=1000):
        print fn
        print'\n ', i
        break
    
    