lud# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 19:43:25 2018
balance = 320000/999999/7792/359790
annualInterestRate = 0.2
Lowest Payment: 29157.09/90325.03/709.98/33271.45
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

balance = 3329
annualInterestRate = 0.2
monthly_interest_rate = annualInterestRate / 12.0
# minimum_monthly_payment = 10
min = balance / 12
max = (balance * (1 + monthly_interest_rate) ** 12) / 12.0
guess = round((min + max) / 2, 2)
month = 13


def monthlyPayment(balance):
    month = 13
    updated_balance = balance
    print('payment coming from guess', guess)
    yearly_guess = guess
    print('yearly payment assigning guess', yearly_guess)
    monthly_guess = yearly_guess
    print('monthly payment coming from yearly guess', monthly_guess)
    for i in range(1, month):
        # minimum_monthly_payment = calculated_monthly
        # print(i, 'minimum_monthly_payment', minimum_monthly_payment)
        print('evey month payment', monthly_guess)
        monthly_unpaid_balance = updated_balance - monthly_guess
        print(i, 'monthly_unpaid_balance', round(monthly_unpaid_balance, 2))
        updated_balance = (monthly_unpaid_balance + (monthly_unpaid_balance *
                                                     monthly_interest_rate))
        print(i, "Remaining balance: ", round(updated_balance, 2))

    return round(updated_balance, 2)


while not (monthlyPayment(balance) <= 1 and monthlyPayment(balance) >= -1):
    balance_left = monthlyPayment(balance)
    if balance_left >= 0:
        min = guess
        max = max        
    else:
        max = guess
        min = min
        
    guess = round((min + max) / 2, 2)
    

   
    print('guess', guess)
 

print('Lowest Payment:',  guess)
