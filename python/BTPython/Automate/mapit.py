import webbrowser , sys,pyperclip
import requests
"""
if len(sys.argv) > 1:
     # Lấy địa chỉ từ dòng lệnh.
     address = ''.join(sys.argv[1:])
else:
     # Lấy địa chỉ từ khay nhớ tạm.
     address = pyperclip.paste()

webbrowser.open ('https://www.google.com/maps/place/' + address)
"""

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
     res.raise_for_status()
except Exception as exc:
     print('There was a problem: %s' % (exc))

playfile = open('RomeoAndJuliet.txt','wb')
for chuck in res.iter_content(100000):
     playfile.write(chuck)

playfile.close()