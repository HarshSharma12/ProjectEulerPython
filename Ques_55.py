# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 11:44:43 2014

@author: Harsh Sharma


Problem 55
Published on Friday, 24th October 2003, 06:00 pm; Solved by 29378

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, 
like 196, never produce a palindrome. A number that never forms 
a palindrome through the reverse and add process is called a Lychrel number.
 Due to the theoretical nature of these numbers, and for the purpose of this problem,
 we shall assume that a number is Lychrel until proven otherwise. 
 In addition you are given that for every number below ten-thousand, 
 it will either (i) become a palindrome in less than fifty iterations, or, 
 (ii) no one, with all the computing power that exists, has managed so far to map 
 it to a palindrome. In fact, 10677 is the first number to be shown to require 
 over fifty iterations before producing a palindrome: 4668731596684224866951378664 
 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; 
the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

###Upto 1000 -  COUNT = 249

"""


count = 0
def revNum(i):
    rem, rev = 0,0
    while (i!=0):
        rem = i%10
        i=i/10
        rev = rev*10+rem
    return rev

def isPal(i):
    return (i==revNum(i))
    
maxSteps = 5000
for num in range(0, 10000):
    steps=0
    num2 = num
    while steps<maxSteps:
        newNum = num2+revNum(num2)
        if(isPal(newNum)):
            break
        steps+=1
        num2=newNum
    if steps==maxSteps:
        count+=1
        print 'Number = ', num        
        
print 'count = ', count

