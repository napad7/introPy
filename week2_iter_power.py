# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 05:42:01 2018

The greatest common divisor of two positive integers is the largest integer
that divides each of them without remainder. For example,
gcd(2, 12) = 2
gcd(9, 12) = 3
gcd(17, 12) = 1

@author: Primary
"""


def gcd(a, b):
    print('inside def', a, b)
    if(a > b):
        big = a
        small = b
    else:
        big = b
        small = a
    div = small
    print('something')
    if (big % div == 0):
        return div
    else:
        while (div > 0):
            if(small % div == 0 and big % div == 0):
                return div
            else:
                div = div - 1

print(gcd(9, 12))
