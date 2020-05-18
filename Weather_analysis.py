import requests
import json

#the main app for weather analysis

def  get_weather(city):
    weather_key = 'ce5aac7c1aacbd6070822b7c504a0ef9'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID': weather_key, 'q': city, 'units':'Metric'}
    response = requests.get(url, params=parameters)
    weather = response.json()
    return weather['main']['temp']



with open('country-capitals.json', 'r', encoding="utf-8") as country_capitals:
    json_data1 = json.load(country_capitals)
    json_object = json.dumps(json_data1, indent = 2)

assert type(json_data1) == list
list_of_capitals = [x['CapitalName'] for x in json_data1 if x['CapitalName'] != 'N/A']
list_of_capitals.sort()
#print(list_of_capitals)
'''
temps = []
i=0
while i < 100:
    try:
        temp = get_weather(list_of_capitals[i])
        print(str(list_of_capitals[i]) + " " + str(temp))
        temps.append(temp)
    except:
        print("No city %s in our API database" %(list_of_capitals[i]))

    i += 1

print(temps)
'''
