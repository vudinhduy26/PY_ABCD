# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:34:15 2021

@author: duy
"""

def LongestWord(sen):

  # code goes here
  flag = True
  arr = ""
  result = ""
  for i in sen:
      if not (ord(i) <= 47 and ord(i) >= 33):
          arr +=i
  Brr = [i for i in arr.split()]
  for j in range(len(Brr)-1):
      if len(Brr[j]) > len(Brr[j+1]):
          result = Brr[j]
      elif len(Brr[j]) == len(Brr[j+1]):
          result = Brr[j]
      elif len(Brr[j]) < len(Brr[j+1]):
          result = Brr[j+1]
  return result

# keep this function call here 
print(LongestWord(input()))