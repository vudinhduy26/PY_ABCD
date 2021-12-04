# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:14:47 2021

@author: duy
"""
from fractions import gcd
#gcd(20,8)
try:
    number1 = int(input("Enter number 1 : "))
    number2 = int(input("Enter number 2 : "))
    s = []
    if number1 >= number2:
        for i in range(1,number1+1):
            if number1%i == 0 and number2%i == 0:
                print(i)
    if number2 > number1:
        for i in range(1,number2+1):
            if number1%i == 0 and number2%i == 0:
                print(i)
except:
    print("Please enter number !!!")