# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:37:00 2021

@author: duy
"""
#def week(i):
 #   switcher={0:'Sunday',1:'Monday',2:'Tuesday',
 #               3:'Wednesday',
 #               4:'Thursday',
 #               5:'Friday',
 #               6:'Saturday'
 #            }
 #   return switcher.get(i,"Invalid day of week")

#while True :
 #   try:
 #       i = int(input('Nhap : '))
 #       print(week(i))
 #       if week(i) == "Invalid day of week":
  #          break
 #   except:
  #      print('May khong nhap ak ???')
  
class python_switch:
    def switch(self, day_of_week):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(day_of_week), lambda: default)()
 
    def case_1(self):
        return "Monday"
 
    def case_2(self):
        return "Tuesday"
 
    def case_3(self):
        return "Wednesday"
while True:
    try:
        day_of_week = int(input('Nhap : '))
        s = python_switch()
        print(s.switch(day_of_week))
        if s.switch(day_of_week) == "Incorrect day":
            break
    except:
        print("what do you mean ???")

        
    
    