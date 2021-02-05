# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:57:04 2020

@author: Karthik Shekar
"""


'''
Compound Interest
'''
Acc_num = int(input("PLease enter your account number"))
Pr_Amount = int(input("Enter the principal amount"))
Time_period = int(input("ENter the time"))

def compound_interest():
    
    if ( Time_period == 1):
        CI = Pr_Amount * (1 + 7.30)**1
    elif( Time_period == 2):
        CI = Pr_Amount * (1 + 7.40)**2
    elif( Time_period == 3):
        CI = Pr_Amount * (1 + 7.55)**3
    elif( Time_period == 4):
        CI = Pr_Amount * (1 + 8)**4
        
    print('Your CI is', int(CI))

compound_interest()