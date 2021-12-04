# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 11:51:44 2021

@author: duy
"""
import fasttext
chars = ""
enter = input("Enter : ")
chars = "{}".format(enter)
#tao dictionary rong
count = {}
for char in chars:
    if char in count:
        count[char] +=1
    else:
        count[char] =1
for i in sorted(count, key=count.get, reverse=False):
    print(i,count[i])