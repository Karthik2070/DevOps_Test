# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:39:26 2020

@author: Karthik Shekar
"""
'''
even or odd
'''

number = int(input("Enter a number"))

if (number%2==0):
    print(number, 'The number is even')
else: 
    print(number, 'The number is odd')
    
'''
Celcius to Farenheit and Farenheit to Celcius
'''

def converter():
    deg = input("Enter which parameter needs to be converted")
    if(deg=='f'):
        deg_num = int(input('Enter the Farenheit to be converted to Celcius'))
        Degree = (deg_num-32)*5/7
        print('in celcius the temperature is:', Degree)
    elif(deg=='c'):
        deg_num = int(input('Enter the Celcius to be converted to Farenheit'))
        Degree = (deg_num*9/5)+32
        print('in farenheit the temperature is:', Degree)
        
converter()

