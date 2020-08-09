import requests
import json

lat_posi = '35.7809'
lon_posi = '137.054'
part_day = 'hourly'
API_KEY = '1da5bd12bcc61752b8aab620df1fcec6'
api = api = 'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={key}&units=metric'

url = api.format(lat = lat_posi, lon = lon_posi, part = part_day, key = API_KEY)


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

def getTenkiInfo():
    
    response = requests.get(url)
    data = response.json()

    tenki = data['current']['weather'][0]['main']
    current_temp = data['current']['temp']
    pop = '{:.0%}'.format(data['daily'][0]['pop'])
    
    tenkiInfo = "岐阜県の天気を教えるニャン" + '\n'
    tenkiInfo += "天気：" + judgeTenki(tenki) + '\n'
    tenkiInfo += "気温：" + str(current_temp) + "℃" + '\n'
    tenkiInfo += "降水確率：" + str(pop) + '\n'
    tenkiInfo += "今日も頑張ろうニャン！"
    
    return tenkiInfo

