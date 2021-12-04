# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:58:24 2021

@author: duy
"""
#d = input("nhap : ")
file = open('a.txt','r')
data = file.read()
words = data.split()
dictt = {}
for i in words:
    if i in dictt:
        dictt[i] +=1
    else:
        dictt[i] =1
    print(i,":",dictt[i])