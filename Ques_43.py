# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 10:38:12 2014

@author: Harsh Sharma

Problem 43
The number, 1406357289, is a 0 to 9 pandigital number because it is
 made up of each of the digits 0 to 9 in some order, but it also 
 has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, 
we note the following:
•d2d3d4=406 is divisible by 2
•d3d4d5=063 is divisible by 3
•d4d5d6=635 is divisible by 5
•d5d6d7=357 is divisible by 7
•d6d7d8=572 is divisible by 11
•d7d8d9=728 is divisible by 13
•d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

Pending - DEVELOP A BETTER ALGO

Answer =  16695334890

"""

sum1 =0;
num=0
d1, d2, d3, d4, d5 = 0,0,0,0,0
d6, d7, d8, d9, d10 = 0,0,0,0,0
for d1 in range(1,10):
    for d2 in range(0,10):
        if (d1!=d2):
            for d3 in range(0,10):
                if(d3!=d1 and d3!=d2 and d3<10):
                    for d4 in range(0,10,2):
                        if(d4!=d1 and d4!=d2 and d4!=d3 and d4<10):
                            for d5 in range(0,10):
                                if(d5!=d1 and d5!=d2 and d5!=d3 and d5!=d4 and d5<10):
                                    for d6 in range(0,10,5):
                                        if(d6!=d1 and d6!=d2 and d6!=d3 and d6!=d4 and d6!=d5 and d6<10):
                                            for d7 in range(0,10):
                                                if(d7!=d1 and d7!=d2 and d7!=d3 and d7!=d4 and d7!=d5 and d7!=d6 and d7<10):
                                                    for d8 in range(0,10):
                                                        if(d8!=d1 and d8!=d2 and d8!=d3 and d8!=d4 and d8!=d5 and d8!=d6 and d8!=d7 and d8<10):
                                                            for d9 in range(0,10):
                                                                if(d9!=d1 and d9!=d2 and d9!=d3 and d9!=d4 and d9!=d5 and d9!=d6 and d9!=d7 and d9!=d8 and d9<10):
                                                                    for d10 in range(0,10):
                                                                        if(d10!=d1 and d10!=d2 and d10!=d3 and d10!=d4 and d10!=d5 and d10!=d6 and d10!=d7 and d10!=d8 and d10!=d9 and d10<10):
                                                                            if((d3+d4+d5)%3==0):
                                                                                if((d5*100+d6*10+d7)%7==0):
                                                                                    if((d6*100+d7*10+d8)%11==0):
                                                                                        if((d7*100+d8*10+d9)%13==0):
                                                                                            if((d8*100+d9*10+d10)%17==0):
                                                                                                num = d1*pow(10,9)+d2*pow(10,8)+d3*pow(10,7)+d4*pow(10,6)+d5*pow(10,5)+d6*pow(10,4)+d7*pow(10,3)+d8*pow(10,2)+d9*pow(10,1)+d10*pow(10,0)
                                                                                                print num
                                                                                                sum1+=num
                                                                                                
print 'SUM = ', sum1