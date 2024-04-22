# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:12:27 2024

@author: bushc
"""

def mp(p, r, n): 
    mir = r / 12
    monthly_payment = p * (mir * (1 + mir)**n) / ((1 + mir)**n - 1)
    return monthly_payment

def ip(p, r, n, c):
    remaining_principal = p * (1 - (c / n))
    mir = r / 12
    interest_payment = remaining_principal * mir
    return interest_payment

def pp(a, r, n, c):
    remaining_principal = a * ((1 + r/12)**n - (1 + r/12)**c) / ((1 + r/12)**n - 1)
    interest_payment = a * r / 12
    principal_payment = remaining_principal - interest_payment
    return principal_payment




