# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 05:00:36 2018
output=''
for num in range(len(secretWord)):
    if secretWord[num] in lettersGuessed:
        output+=secretWord[num]
        output+=' '
    else:
        output+='_ '
return output
@author: Primary
"""

secretWord = 'c'
lettersGuessed = ['a']
# print(secretWord == letterGuessed)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    list_secreteWord = []
    for letter in secretWord:
        if letter not in lettersGuessed:
            list_secreteWord.append('_ ')
        else:
            list_secreteWord.append(letter)
    return (''.join(list_secreteWord))

print(isWordGuessed(secretWord, lettersGuessed))
