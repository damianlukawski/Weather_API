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


with open('city.list.json', encoding="utf8") as fd:
    json_data = json.load(fd)
    #pprint(json_data)

#for i in json_data:
#rint(type(json_data[0]['name']))
#print(json_data[1]['name'])
print(len(json_data))
i=0
list=[]
while i <len(json_data)-1:
    i += 1
    print (i)
    if type(json_data[i]['name']) == str:
        list.append(json_data[i]['name'])
    else:
        break

#print(len(get_weather(i)))
print(list)

#print(type(list))
#i=820
#while i<835:
#    print(i)
#    i+=1
#    if type(get_weather(i)) == str:
#       list.append(get_weather(i))
#       print(get_weather(i))
        #else:
        #    break
#list.append(get_weather(833))
#print(list)



#print(json_dumps)
#input("type anything to end")

#f = open("city.list.json", "r")
#print(f.read())
#i=1
#while i<1000:
#    try:
#        resp = requests.get(url, params=parameters)

