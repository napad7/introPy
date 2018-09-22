# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 19:43:25 2018
balance = 3329/4773/3926
annualInterestRate = 0.2
Lowest Payment: 310/440/360
@author: Primary
"""

balance = 120
annualInterestRate = 0.0
number = 0
# minimum_monthly_payment = 10


def monthlyPayment(balance, monthly_guess()):
    month = 13
    monthly_interest_rate = annualInterestRate / 12.0
    updated_balance = balance
    for i in range(1, month):
        minimum_monthly_payment = calculated_guess
        #print(i, 'minimum_monthly_payment', minimum_monthly_payment)
        monthly_unpaid_balance = updated_balance - minimum_monthly_payment
        #print(i, 'monthly_unpaid_balance', monthly_unpaid_balance)
        updated_balance = monthly_unpaid_balance + (monthly_unpaid_balance * monthly_interest_rate)
        #print(i, "Remaining balance: ", round(updated_balance, 2))
    return round(updated_balance, 2)

monthly_guess():
    guess = guess + 10
    send_guess = guess
    return send_guess
    
