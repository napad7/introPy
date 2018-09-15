# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 05:42:01 2018

@author: Primary
"""

print("Please think of a number between 0 and 100!")

# print(type(guess))
min = 0
max = 100
guess = int((min + max) / 2)
number = 83
user_ans = ''

print("Is your secret number", guess, end="")
print("?")

while (user_ans != 'c'):
    user_ans = input("Enter 'h' to indicate the guess is too high. "
                     "Enter 'l' to indicate the guess is too low. "
                     "Enter 'c' to indicate I guessed correctly. ")
    if(user_ans != 'h' and user_ans != 'l' and user_ans != 'c'):
        print("Sorry, I did not understand your input")
    elif (user_ans == 'h'):
        min = min
        max = guess
    elif(user_ans == 'l'):
        max = max
        min = guess
    else:
        print("Game over. Your secret number was:", guess)
        break

    guess = int((min + max) / 2)
    print("Is your secret number", guess, end="")
    print("?")


