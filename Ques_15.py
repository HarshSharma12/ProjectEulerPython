# -*- coding: utf-8 -*-
"""
Solved on - 2/10/2011

@author: Harsh Sharma

Problem 15

Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?

Answer - 137846528820

"""
def pascals_triangle(n):
    x=[[1]]
    for i in range(n-1):
        x.append([sum(i) for i in zip([0]+x[-1],x[-1]+[0])])
    return x

def solve():
    # It turns out that the number of paths follow the pattern as
    # The middle number of pascal triangle in the odd numbered rows
    # For a 20x20 grid
    rows = 20
    columns = 20
    triangle = pascals_triangle(2*rows + 1)
    return triangle[2*rows][columns]
    
print "Answer :", solve()
