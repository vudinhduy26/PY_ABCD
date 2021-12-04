import json, requests, sys
import openpyxl
import pprint

if len(sys.argv) <0:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

#location = 

url ='https://api.openweathermap.org/data/2.5/weather?q=London&appid=046ed82fdc128819ea1aa4826b3d8243'
response = requests.get(url)
response.raise_for_status()

"""
resultFile = open('weather.py','w')
resultFile.write('weather = '+ pprint.pformat(response.text))
resultFile.close()
print('DOne')
"""

weatherData = json.loads(response.text)

print(weatherData[0])