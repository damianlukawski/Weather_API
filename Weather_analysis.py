import requests
import json



def  get_weather(id):
    weather_key = 'ce5aac7c1aacbd6070822b7c504a0ef9'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID': weather_key, 'id': id, 'units':'Metric'}
    response = requests.get(url, params=parameters)
    weather = response.json()
    return weather['main']['temp']



with open('city.list.json', 'r', encoding="utf-8") as fd:
    json_data = json.load(fd)

length = len(json_data)
i = 0
list = []
while i < len(json_data)-1:
    id = json_data[i]['id']
    i += 1
    if type(id) == int:
        list.append(id)
#print(get_weather(list[0]))
print(i)

temps = []
b=0
while b < 100:
    temp = get_weather(list[b])
    #print(temp)
    b += 1
    temps.append(temp)
