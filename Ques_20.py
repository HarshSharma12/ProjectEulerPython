# -*- coding: utf-8 -*-
"""
Solved on - 2/10/2011

@author: Harsh Sharma

Problem 20

n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

ANSWER - 648
"""

def f(p,r=(1,100)):
	l=range(r[0],r[1])
	k=map(p,l)
	return reduce(lambda x,y: x*y,k)

def p(x):
	return x

x=f(p)
n=0
l=[]
while x>0:
    n=x%10
    x=x/10
    l.append(n)

i=0
sum1=0
Sum of digits
while i<len(l):
    sum1+=l[i]
    i+=1

print 'Sum is '
print sum1
