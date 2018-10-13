# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 19:43:25 2018
balance = 3329/4773/3926
annualInterestRate = 0.2
Lowest Payment: 310/440/360
@author: Primary
i = 0
while monthlyPayment(balance) and i != 1:
    i = i + 1
    print(i)
monthlyPayment(balance) != 0 
"""

balance = 3926
annualInterestRate = 0.2
# minimum_monthly_payment = 10
guess = 0

def monthlyPayment(balance):
    month = 13
    monthly_interest_rate = annualInterestRate / 12.0
    updated_balance = balance
    # print('payment coming from guess', guess)
    yearly_guess = guess
    # print('yearly payment assigning guess', yearly_guess)
    monthly_guess = yearly_guess
    # print('monthly payment coming from yearly guess', monthly_guess)
    for i in range(1, month):
        # minimum_monthly_payment = calculated_monthly
        # print(i, 'minimum_monthly_payment', minimum_monthly_payment)
        # print('evey month payment', monthly_guess)
        monthly_unpaid_balance = updated_balance - monthly_guess
        # print(i, 'monthly_unpaid_balance', int(monthly_unpaid_balance))
        updated_balance = monthly_unpaid_balance + (monthly_unpaid_balance * monthly_interest_rate)
        #print(i, "Remaining balance: ", int(updated_balance))

    return updated_balance

while monthlyPayment(balance) !=0 and monthlyPayment(balance) > 0:
    guess = guess + 10

print('Lowest Payment:',  guess)
    

