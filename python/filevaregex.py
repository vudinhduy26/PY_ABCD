# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 23:40:47 2021

@author: duy
"""
import re
import os
#file = open('Document.txt','w')
#file.close()
#os.rename('Document.txt'),'hello.txt'
#n = file.read()


#regex1 = re.findall(r'anh(.*?)qua',n)
#print(regex1)

#ghi tieng viet
#def writefile(filename,nd_file):
#    file = open(filename,mode = 'a',encoding="utf-8")
#    file.write(nd_file + '\n')
#    file.close()

file = open('Document.txt','r')
n = file.read()
k = re.findall(r'\w+',n)
print(k)