# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 05:42:01 2018

@author: Primary
"""

print("Please think of a number between 0 to 100!")

# print(type(guess))
min = 0
max = 100
guess = int((min + max) / 2)
number = 83

print("Is your secret number ", guess, end="")
print("?")

while (number != guess):
    print("Enter 'h' to indicate the guess is too high."
          "Enter 'l' to indicate the guess is too low."
          "Enter 'c' to indicate I guessed correctly.")
    if (number < guess):
        print("h")
        min = min
        max = guess
    else:
        print("l")
        max = max
        min = guess

    guess = int((min + max) / 2)
    print("Is your secret number ", guess, end="")
    print("?")

print("Enter 'h' to indicate the guess is too high."
      "Enter 'l' to indicate the guess is too low."
      "Enter 'c' to indicate I guessed correctly.")
print("c")
print("Game over. you number was: ", guess)
