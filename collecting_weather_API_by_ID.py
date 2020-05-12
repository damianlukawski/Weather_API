import requests
import json
from pprint import pprint

# current weather from https://openweathermap.org/current
# API call by city name: api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
def format_response(weather):
    try:
        name = weather['name'] #informacje z dictionary
        final=name
    except:
        final=0
    return final

def  get_weather(id):
    weather_key = 'ce5aac7c1aacbd6070822b7c504a0ef9'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID': weather_key, 'id': int(id)}
    response = requests.get(url, params=parameters)
    weather = response.json()
    return format_response(weather)


#with open('city.list.json', encoding="utf8") as fd:
#    json_data = json.load(fd)
    #pprint(json_data)

#for i in json_data:
#rint(type(json_data[0]['name']))
#print(json_data[1]['name'])
with open('city.list.json', 'r', encoding="utf-8") as fd:
   json_data = json.load(fd)


length=len(json_data)
i=0
list=[]
while i <100000:
    id = json_data[i]['id']
    print(id)
    i += 1
    if type(id) == int:
        list.append(id)

print(list)