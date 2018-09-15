# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:01:47 2018
A regular polygon has n number of sides. Each side has length s.

    The area of a regular polygon is: 

    The perimeter of a polygon is: length of the boundary of the polygon


Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the regular polygon. 
The function returns the sum, rounded to 4 decimal places.

polysum(3, 7) - 462.2176
polysum(51, 13) - 474504.5343
@author: Primary
"""
import math


def polysum(n, s):
    def area(n, s):
        upper = 0.25*n*(s**2)
        lower = math.tan(math.pi/n)
        return upper / lower

    def perimeter(n, s):
        per = n * s
        return per**2

    ans = area(n, s) + perimeter(n, s)
    print(round(ans, 4))

polysum(51, 13)
