# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 19:43:25 2018
balance = 3329/4773/3926
annualInterestRate = 0.2
Lowest Payment: 310/440/360
@author: Primary
"""

balance = 120
annualInterestRate = 0.2
montlyInterestRate = 0.2 / 12.0
number = 0
# minimum_monthly_payment = 10
def guess(number):
    number = number + 10
    temp = number + temp
    return temp


def monthly_payment(balance):
    guess_number = guess(number)
    monthly_balance = balance
    for i in range(1, 13):
        monthly_balance = monthly_balance - guess_number
        print(i, monthly_balance, guess_number)

    return monthly_balance

number = 0
while (monthly_payment(balance) > 0):
    guess(number)

    
