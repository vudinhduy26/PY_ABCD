import requests
import json
from pprint import pprint

name = input('Name : ')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=046ed82fdc128819ea1aa4826b3d8243&units=metric'.format(name)
res = requests.get(url) #thuc thi url

data = res.json()
#get data from json weather
country = data['sys']['country']
temp = data['main']['temp']
wind_speed = data['wind']['speed']
latitude = data['coord']['lat']
longitude = data['coord']['lon']
description = data['weather'][0]['description']

print('Country : {}'.format(country))
print('Temp : {}'.format(temp))
print('Wind Speed : {}'.format(wind_speed))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('Description : {}'.format(description))