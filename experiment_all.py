nc# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 15:20:42 2018

@author: Primary
"""

balance = 3926
annualInterestRate = 0.2
monthly_interest_rate = annualInterestRate / 12.0
# minimum_monthly_payment = 10
min = balance / 12
max = (balance * (1 + monthly_interest_rate) ** 12) / 12.0

print(min, max, (min+max)/2)


