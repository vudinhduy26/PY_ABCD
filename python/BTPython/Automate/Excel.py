import openpyxl
import re


wb = openpyxl.load_workbook('example.xlsx')
#sheet = wb["Sheet1"]
#c = sheet['A1']
#print('Row : %s, Column : %s, value : %s'%(c.row,c.column,c.value))

"""
#lay gia tri le
for i in range(1,8,2):
    print(i, sheet.cell(row=i,column=2).value)
"""

"""
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')
"""
sheet = wb.active
Column = list(sheet.columns)[1]
for i in Column:
    print(i.value)