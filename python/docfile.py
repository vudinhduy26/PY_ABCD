file = open('Document.txt','r+')
str = file.read()
tachstr = str.split()
tachstr.append("HO")
print(tachstr)