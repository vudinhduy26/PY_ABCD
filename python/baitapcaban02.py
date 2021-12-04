# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 09:46:26 2021

@author: duy
"""
#s = 0
#for i in range(1,6):
#    s = s + i
#print(s)

##### continue & break
#while True:
#    HoTen = input('Nhap : ')
#    if HoTen == "":
#        print('please you are not write')
#        continue
#    else:
#        break
#print(HoTen)

###### so nguyen to
try:
    prime = True
    SoNguyen = int(input('Enter : '))
    if SoNguyen < 2:
        print('can not prime')
        prime = False #tao co
    else:
        i = 2
        while (i <= (SoNguyen/2)):
            if SoNguyen%i == 0: #neu i la uoc cua songuyen
                prime = False #so nguyen do ko phai la so nguyen to
                break
            i = i + 1
    if prime == True:
         print('This is prime ',SoNguyen)
    else:
        print('Not')
except:
    print("Please enter values is int !!!")