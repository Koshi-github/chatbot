import requests
import json

city_name = 'gifu'
API_KEY = '1da5bd12bcc61752b8aab620df1fcec6'
api = 'http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}'

url = api.format(city = city_name, key = API_KEY)

def judgeTenki(tenki):
    if tenki == 'Clear':
        return '晴れ'
    elif tenki == 'Clouds':
        return '曇り'
    elif tenki == 'Rain':
        return '雨'
    elif tenki == 'Snow':
        return '雪'
    else:
        return '不明'

def getTenki():

    response = requests.get(url)

    data = response.json()

    tenki = data['weather'][0]['main']

    return judgeTenki(tenki)