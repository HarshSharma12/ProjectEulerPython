# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 19:05:51 2014

@author: Harsh Sharma

Problem 9

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer:
	142913828922
"""

from math import sqrt
from itertools import count, ifilter, takewhile

def memoize(f, maxcache=None, cache={}):
    """Decorator to keep a cache of input/output for a given function"""
    cachelen = [0]
    def g(*args, **kwargs):
        key = (f, tuple(args), frozenset(kwargs.items()))
        if maxcache is not None and cachelen[0] >= maxcache:
            return f(*args, **kwargs)
        if key not in cache:
            cache[key] = f(*args, **kwargs)
            cachelen[0] += 1
        return cache[key]
    return g

def is_prime(n):
    """Return True if n is a prime number (1 is not considered prime)."""
    if n < 3:
        return (n == 2)
    elif n % 2 == 0:
        return False
    elif any(((n % x) == 0) for x in xrange(3, int(sqrt(n))+1, 2)):
        return False
    return True     


def get_primes(start=2, memoized=False):
    """Yield prime numbers from 'start'"""
    is_prime_fun = (memoize(is_prime) if memoized else is_prime)
    return ifilter(is_prime_fun, count(start))
    


print sum(takewhile(lambda x: x<2e6, get_primes()))
