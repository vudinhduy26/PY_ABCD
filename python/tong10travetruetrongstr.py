# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:03:30 2021

@author: duy
"""

def QuestionsMarks(strParam):

  # code goes here
  arr = []
  flag = "false"
  crr = []
  for i in strParam:
      if ord(i) <= 57 and ord(i) >= 49:
          arr.append(i)
  brr = [int(i) for i in arr]
  for j in range(len(brr)-1):
      for h in range(j+1,len(brr)):
          if brr[j]+brr[h] == 10:
              flag="true"
  return flag

# keep this function call here 
print(QuestionsMarks(input()))