# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 21:47:26 2018

@author: Primary
x = ('I', 'am', 'a', 'test', 'tuple')
def oddTuples(x):
    return x[::2]

print(oddTuples(x))

testList = [1, -4, 8, -9]

def applyToEach(testList, abs):
    for i in range(len(testList)):
        testList[i] = testList[i] * testList[i]
    return testList

print(applyToEach(testList, abs))

def how_many(animals):
    total = 0
    for i in animals:
        total = total + len(animals.v)
"""
animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(animals):
    sum = 0
    for i in animals:
        temp = (len(animals[i]))
        sum = sum + temp
    return sum
