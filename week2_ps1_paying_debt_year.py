# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 18:49:46 2018

@author: Primary
"""

annual_interest_rate = 0.2
monthly_payment_rate = 0.04


def monthlyPayment(balance):
    month = 13
    monthly_interest_rate = annual_interest_rate / 12.0
    updated_balance = balance
    for i in range(1, month):
        minimum_monthly_payment = monthly_payment_rate * updated_balance
        #print(i, 'minimum_monthly_payment', minimum_monthly_payment)
        monthly_unpaid_balance = updated_balance - minimum_monthly_payment
        #print(i, 'monthly_unpaid_balance', monthly_unpaid_balance)
        updated_balance = monthly_unpaid_balance + (monthly_unpaid_balance * monthly_interest_rate)
        #print(i, "Remaining balance: ", round(updated_balance, 2))
    return round(updated_balance, 2)

balance = 42
print("Remaining balance: ", monthlyPayment(balance))
