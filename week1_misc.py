# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 08:00:36 2018
beggh

s = 'azcbobobegghakl'
count = 0
for letter in range(len(s) - 1):
    if s[letter] < s[letter + 1]:
        print("inside")
        print(s[letter], s[letter + 1])
        
        count += 1
print("count", count)
@author: Primary
"""


def iterPower(base, exp):
    result = 1
    for i in range(exp):
        result = base * result
    return result


def recurPower(base, exp):
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return (base * recurPower(base, (exp - 1)))

print(iterPower(2, 0))
print(recurPower(2, 6))
