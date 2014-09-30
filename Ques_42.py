# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 15:13:26 2014

@author: Harsh Sharma

Coded triangle numbers

Problem 42
Published on Friday, 25th April 2003, 06:00 pm; Solved by 40658

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using p042_words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

Answer =  162
"""
from math import sqrt
    
def isTriNum(num):
    disc = sqrt(1+8*num)
    return int(disc) - disc == 0
		
		
def letterToNum(x):
    x = x.upper()
    if(x=='"'):
        return 0
    return ord(x)-64

    
fid = open('p042_words.txt','r')
count = 0
i=0
text = fid.readline()
wordArr = text.split(',')
for i in range(0, len(wordArr)):
    num =0
    s=wordArr[i]
    for x in s:
        num+=letterToNum(x)
    if(isTriNum(num)):
        count+=1
        
print 'Answer = ', count
    