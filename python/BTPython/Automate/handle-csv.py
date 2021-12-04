import csv

exampleFile = open('addresses.csv')
exampleReader = csv.reader(exampleFile)
#exampleData = list(exampleReader)
"""
a = [i for i in range(1,len(exampleData)+1)]
for number,row in zip(a,exampleData):
    print(number,row)
"""
#print(exampleData)
"""
for row in exampleReader:
    print('Row #'+str(exampleReader.line_num)+''+str(row))
"""
#write file
"""
outputFile = open('output.csv','w',newline='')
outputWrite = csv.writer(outputFile)
outputWrite.writerow(['spam', 'eggs', 'bacon', 'ham']) #moi gia tri se dc dat trong 1 o cua sheet
outputFile.close()
"""
#DictReader and DictWriter CSV Objects
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['John'])