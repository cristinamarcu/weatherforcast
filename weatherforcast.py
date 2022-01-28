import sys
import requests
import json
import datetime


def valid_city(cityName: str) -> bool:
    city_list = open('city.list.json', encoding="utf8")
    content = city_list.read()
    valid_city_list = json.loads(content)
    valid = False

    for validCity in valid_city_list:
        if cityName == validCity['name']:
            valid = True
    return valid


def printdayinfo(weatherdata):
    print(weatherdata['dt_txt'])
    print(weatherdata['weather'][0]['description'])
    print('Temperature:', weatherdata['main']['temp'])


def printweather(cityName: str, apikey: str):
    try:
        res = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={cityName}&appid={apikey}')
    except:
        print("Could not get weather data")
        return

    textJSON_dict = json.loads(res.text)
    print(f"{textJSON_dict['city']['name']}")
    print('Today:')
    printdayinfo(textJSON_dict['list'][0])
    today = datetime.datetime.fromisoformat(textJSON_dict['list'][0]['dt_txt'])
    print('Tomorrow:')
    tomorrow = today + datetime.timedelta(days=1)
    for weatherdata in textJSON_dict['list']:
        if datetime.datetime.fromisoformat(weatherdata['dt_txt']) == tomorrow:
            printdayinfo(weatherdata)


'''
This program returns the weather forecast for a city for today and tomorrow.
Exemple usage:
weatherforcast.py London Apikey

Uses api from https://openweathermap.org/api
'''

cityName = sys.argv[1]
apiKey = sys.argv[2]

if valid_city(cityName):
    printweather(cityName, apiKey)
else:
    print('The city is not in our city list.')
