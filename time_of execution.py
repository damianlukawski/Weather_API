import requests
import json
import time
import matplotlib.pyplot as plt
start_time = time.time()

#app for analyzing time of execution
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
#print(i)
city_list_time = time.time()
print("--- time of downloading the list of cities: %s seconds ---" % (time.time() - start_time))
#print(start_time)


def  getting_weather(number):
    temps = []
    b = 0
    time_gw = time.time()
    while b < number:
        temp = get_weather(list[b])
        temps.append(temp)
        b += 1
    API_time = time.time() - time_gw
    #print("---time of API for downloading %s cycles: %s seconds ---" % (str(b), API_time))
    return API_time



k=0
time_list =[]
list_k = []
time_k=0
while k<10:
    time_k = round((getting_weather(k) - time_k), 2)
    time_list.append(time_k)
    list_k.append(k+1)
    k += 1
#print(type(getting_weather(2)))
print(time_list)
print(list_k)



plt.scatter(list_k, time_list, marker= 'x')
plt.show()

#print(b)
#print(max(temps))
#
