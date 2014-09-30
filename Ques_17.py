# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 11:14:11 2014

@author: Harsh Sharma

Number letter counts

Problem 17
Published on Friday, 17th May 2002, 06:00 pm; Solved by 76356

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used? 

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

ANSWER = 21124
"""

names = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven',
         8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 
         14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen',
         19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty',
         70:'Seventy', 80:'Eighty', 90:'Ninety', 100:'Hundred', 1000:'Thousand'}
ans = 0
numName = ''
#numName = numName.replace(' ', '')
for i in range(1, 1001):
    
    if (i%1000)==0:
        numName+=names[i/1000]+names[1000]
    elif (i%100==0):
        numName+=names[i/100]+names[100]
        
#    elif(i/1000!=0):
#        x=int(i/1000)
#        numName+=names[x]+names[1000]
#        y=i%1000
#        x=int(y/100)
#        if(x!=0):
#            numName+=names[x]+names[100]+'and'
#        else:
#            numName+='and'
#        y=i%100
#        z=int(y/10)*10
#        if(z == 10 or z==0):
#            numName+=names[y]
#        else:
#            try:
#                numName+= names[z]
#                numName+= names[y%10]
#            except(KeyError):
#                numName+= ''
#    
    elif(i/100!=0):
        x=int(i/100)
        numName+=names[x]+names[100]+'and'
        y=i%100
        z=int(y/10)*10
        if(z == 10 or z==0):
            if(y==0):
                numName+=names[z]
            else:
                numName+=names[y]
        else:
            try:
                numName+= names[z]
                numName+= names[y%10]
            except(KeyError):
                numName+= ''
    elif(i/10!=0):
        y=i%10
        z=int(i/10)*10
        if(z == 10):
            if(y==0):
                numName+=names[z]
            else:
                numName+=names[i]
        else:
            try:
                numName+= names[z]
                numName+= names[y%10]
            except(KeyError):
                numName+= ''
    else:
        numName+=names[i]
    ans+=len(numName)
    numName = ''
print 'Answer = ',ans 
        
    