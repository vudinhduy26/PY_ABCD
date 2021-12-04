# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:09:52 2021

@author: duy
"""

import openpyxl

#doc file excel
def get_value_excel(filename,cellname):
    wb = openpyxl.load_workbook(filename)
    sheet1 = wb['Sheet1']
    wb.close()
    return sheet1[cellname].value

#filename = input()
#cellname = input()
#check = get_value_excel(filename, cellname)
#print(check)

"""
#update or viet vao file
def update_value_excel(filename,cellname,value):
    wb = openpyxl.load_workbook(filename)
    sheet1 = wb["Sheet1"]
    sheet1[cellname].value = value
    wb.close()
    wb.save(filename)
    
filename = input()
cellname = input()
text_value = input()
update_value_excel(filename, cellname, text_value)
"""

col_name_acc = "A"
col_name_pass = "B"
filename = input()
for row in range(1,3):
    col_name_acc = "%s%s"%(col_name_acc,row)
    col_name_pass = "%s%s"%(col_name_pass,row)
    account = get_value_excel(filename, col_name_acc)
    password = get_value_excel(filename, col_name_pass)
    print(account,password)




