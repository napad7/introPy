# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:22:12 2018

@author: Primary
"""
import string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    output = ''
    for num in range(len(all_letters)):
        if all_letters[num] not in lettersGuessed:
            output += all_letters[num]

    return output


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
