import requests
import json

lat_posi = '35.39111'
lon_posi = '136.72222'
part_day = 'hourly'
API_KEY = '1da5bd12bcc61752b8aab620df1fcec6'
api = api = 'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={key}&units=metric'

url = api.format(lat = lat_posi, lon = lon_posi, part = part_day, key = API_KEY)

class Tenki:
    def createMessage(self,message):
        returnList =[]

        if "天気" in message and "今日" in message:
            returnList.append("今日の" + self.getDayTenkiInfo(0))
        elif "天気" in message and "明日" in message:
            returnList.append("明日の" + self.getDayTenkiInfo(1))
        elif "天気" in message and "明後日" in message:
            returnList.append("明後日の" + self.getDayTenkiInfo(2))
        elif "天気" in message:
            returnList.append("現在の" + self.getTenkiInfo())

        return returnList

    def judgeTenki(self,tenki):
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

    def getTenkiInfo(self):
        
        response = requests.get(url)
        data = response.json()

        tenki = data['current']['weather'][0]['main']
        current_temp = data['current']['temp']
        pop = '{:.0%}'.format(data['daily'][0]['pop'])
        
        tenkiInfo = "現在の岐阜県の天気を教えるニャン" + '\n'
        tenkiInfo += "天候：" + self.judgeTenki(tenki) + '\n'
        tenkiInfo += "気温：" + str(current_temp) + "℃" + '\n'
        tenkiInfo += "降水確率：" + str(pop) + '\n'
        tenkiInfo += "今日も頑張ろうニャン！"
        
        return tenkiInfo

    def getDayTenkiInfo(self,days):

        response = requests.get(url)
        data = response.json()

        tenki = data['daily'][days]['weather'][0]['main']
        day_temp = data['daily'][days]['temp']['day']
        max_temp = data['daily'][days]['temp']['max']
        min_temp = data['daily'][days]['temp']['min']
        pop = '{:.0%}'.format(data['daily'][days]['pop'])
        
        tenkiInfo = "岐阜県の天気を教えるニャン" + '\n'
        tenkiInfo += "天候：" + self.judgeTenki(tenki) + '\n'    
        tenkiInfo += "気温：" + str(day_temp) + "℃" + '\n'
        tenkiInfo += "最高気温" + str(max_temp) + "℃" + '\n'
        tenkiInfo += "最低気温" + str(min_temp) + "℃" + '\n'
        tenkiInfo += "降水確率：" + str(pop)
        
        return tenkiInfo