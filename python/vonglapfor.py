# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:22:30 2021

@author: duy
"""

#for i in range(1, 5): 
    #for j in range(i):
   #     if j%2==0:
     #       print('0',end=' ')
    #    else:
     #       print('1',end=' ')
   # print()
        #print(i, end=' ')
    #print()
    
#dict = {}
#list = []
#dict['a'] = 1
#dict['b'] = 2
#dict['c'] = 3
#dict['d'] = 4
#for k,v in dict.items():
#    list.append(v) #them phan tu value vao danh sasch
#print(list)

#n = 5
#for i in range(1,n):
#    s = n - i
#    k = s*' '
#    print(k,end=' ')
#    print(((2*i)-1)*'*')
#print(' '*4,'|')

from time import sleep
import random 
import os

rnd2 = random.randint(1,30)

def CreateLeafs():
     for x in range (1, 30, 2): 
        global rnd2
        rnd1 = random.randint(1, rnd2) 
        if x == 1:
            ch = '$'
        elif rnd1 % 4 == 0:
            ch = 'o'
        elif rnd1 % 3 == 0:
            ch = 'i'
        else:
            ch = '*'
        print("{:^33}".format(ch*x))

def CreateRoot():
    print("{:^33}".format("|||"))
    print("{:^33}".format("|||"))
    print("{:^33}".format("======================================"))
    print("Dear Friends - MERRY X'S MAS AND HAPPY NEWYEAR!")
    
def CreateChristmasTree():
    os.system('cls')
    os.system('color')
    CreateLeafs()
    CreateRoot()
    sleep(.75)
    
while True:
    CreateChristmasTree()