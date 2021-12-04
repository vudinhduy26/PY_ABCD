import pyperclip, re
from typing import Pattern, Text
"""string = 'Batmobile lost a wheel'
batRegex = re.compile(r'(B|b)at(man|mobile|copter|bat)')
mo = batRegex.findall(string)
print(mo)"""

#string = 'The Adventures of Batwoman'
"""string = 'Cell: 415-555-9999 Work: 212-555-0000'
patten = r'\d{3}-\d{3}-\d{4}' 
result = re.findall(patten,string)
print(result)"""

"""pattern = re.compile(r'\d+\s\w+') #chuoi chua 1 hoac nhieu so , dau cach , mot hoac nhieu chu hoac so
string = "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"
result = re.findall(pattern,string)
print(result)"""

"""agentNamesRegex = re.compile(r'Agent (\w)\w*')
string = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
result = agentNamesRegex.sub(r'\1****',string) #sub thay the chuoi 
print(result)"""

"""phoneRegex = re.compile(r'(\d{3}-)?(\s|-|\.)?')
string  = 'Cell: 415-555-9999 Work: 212-555-0000'
result = phoneRegex.search(string)
print(result)"""

"""pattern = re.compile(r'[a-zA-Z0-9._%+-]+@+[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})',re.VERBOSE)
string = "pikaduy26@gmail.com"
rl = pattern.search(string)
print(rl)"""

"""
f1 = open('sinhvien.txt', 'r', encoding='UTF-8')
text = f1.read()


#emailRegex = re.compile(r'([a-zA-Z0-9._%+-]+@{1}[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,5}))',re.VERBOSE)
emailRegex = re.compile(r'.*?')

matches = []
for group in emailRegex.findall(text):
    matches.append(group)


if len(matches) > 0:
    #pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print(''.join(matches))
else:
    print('No phone numbers or email addresses found.')
"""

"""
pattern = re.compile(r'\d+')
string = '12 drummers, 11 pipers, five rings, 3 hens'
rl = pattern.findall(string)
print(rl)
"""

"""
#lay so co dau phay
Pattern = re.compile(r'(\d+,\d+,\d+)|(\d+,\d+)')
string = '6,368,745 community or local schools 1,2 as well , as through study'
rl = Pattern.findall(string)
print(rl)
"""

"""
#lay ho va ten co chu cai dau viet hoa
Pattern = re.compile(r'\b[A-Z][a-zA-Z]+\s\b[A-Z][a-zA-Z]+')
string = 'RoboCop Watanabe'
rl = Pattern.findall(string)
if len(rl) == 0:
    print("None")
else:
    print(''.join(rl))
"""
"""
#hoac
Pattern = re.compile(r'(Alice|Bob|Carol)\s(eat|pet|throw)s\s(apples|cats|baseballs)\.',re.I | re.VERBOSE)
string = 'BOB EATS CATS.'
rl = Pattern.findall(string)
print(rl)
"""

Pattern = re.compile(r'(\w+\d+\S+)')
passs = 'Pikaduy26!'
rl = Pattern.findall(passs)
print(rl)