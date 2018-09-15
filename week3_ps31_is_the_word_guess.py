# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 04:18:56 2018

@author: Primary
"""

secretWord = 'lettuce'
lettersGuessed = ['z', 'x', 'q', 'l', 'e', 't', 't', 'u', 'c', 'e']
# print(secretWord == letterGuessed)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

print(isWordGuessed(secretWord, lettersGuessed))
