# -*- coding: utf-8 -*-
"""
Created on Sat May  1 22:20:14 2021

@author: duy
"""

def FindIntersection(strArr):

  # code goes here
  Strr = ""
  Strs = ""
  i = 2
  j = -3
  Arr = []
  while i >= 0:
      if strArr[i] != '"':
          Strr += strArr[i]
          i+=1
      else:
          break
  while j < 0:
      if strArr[j] != '"':
          Strs += strArr[j]
          j-=1
      else:
          break
  for k in Strr.split(","):
      for h in Strs[::-1].split(","):
          if k == h:
              Arr.append(k)
  return ','.join(Arr)

# keep this function call here 
print(FindIntersection(input()))