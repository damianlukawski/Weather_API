import requests
import json
from API_functions import format_response_2
#the main app for weather analysis

def  get_weather(city):
    weather_key = 'ce5aac7c1aacbd6070822b7c504a0ef9'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID': weather_key, 'q': city, 'units':'Metric'}
    response = requests.get(url, params=parameters)
    weather = response.json()
    return weather



with open('country-capitals.json', 'r', encoding="utf-8") as country_capitals:
    json_data1 = json.load(country_capitals)
    json_object = json.dumps(json_data1, indent = 2)

assert type(json_data1) == list
list_of_capitals = [x['CapitalName'] for x in json_data1 if x['CapitalName'] != 'N/A']
list_of_countries = [x['CountryName'] for x in json_data1 if x['CapitalName'] != 'N/A']
#list_of_capitals.sort()
#print(list_of_capitals)

#a=json.dumps(get_weather('Kair'), indent=2)
#print(a)



list_of_holiday_locations = []
list_of_holiday_temp = []
list_of_holiday_countries = []
i=0
while i <len(list_of_capitals)-1:
    try:
        w = get_weather(list_of_capitals[i])
        if w['main']['temp'] > 15 and w['main']['temp'] < 25 and w['weather'][0]['description'] == "clear sky" and w['wind']['speed'] < 3:
            list_of_holiday_locations.append(w['name'])
            list_of_holiday_temp.append(w['main']['temp'])
            list_of_holiday_countries.append(list_of_countries[i])
            #print(list_of_holiday_countries)
        else:
            #print("bad weather conditions in %s" % (w['name']))
            "bad weather"
    except:
        "None"
        #print("No city %s in our API database" %(list_of_capitals[i]))
    i += 1

list_city_temp = zip(list_of_holiday_locations,list_of_holiday_temp, list_of_holiday_countries)
list_city_temps = list(list_city_temp)
print("if you wish to rest in a capital with temperature in range 15-25\N{DEGREE SIGN}C, no clouds and only slight wind please visit one of the following:")

for i, city in enumerate(list_city_temps):
    result = '%s. %s (%s), %s \N{DEGREE SIGN}C' %(str(i+1), city[0], city[2], str(city[1]))
    print(result)


