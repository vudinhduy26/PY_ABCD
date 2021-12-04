# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 11:28:18 2021

@author: duy
"""
#i = 0
#while i < 100 :
 #   print("Hello")
  #  i += 1
  
#### bai 2
from datetime import datetime

print("Enter 0 , which exit to command !!!")
while True:
    try:
        YearBorn = int(input("Enter your year born : "))
        YearOld = 0
        YearNow = datetime.now().year
        if YearBorn == 0:
            break
        if YearBorn < 1990 or YearBorn > YearNow:
            print("year from 1990 to 2021")
            continue
        YearOld = str(YearNow - YearBorn)
        
        print("Your year old "+YearOld)
    except:
        print("Please enter year ")