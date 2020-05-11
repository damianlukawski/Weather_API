import requests
import json


# current weather from https://openweathermap.org/current
# API call by city name: api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

weather_key = 'ce5aac7c1aacbd6070822b7c504a0ef9'
url = 'https://api.openweathermap.org/data/2.5/weather'
parameters = {'APPID': weather_key, 'q': 'Warsaw'}
resp = requests.get(url, params=parameters)
#print(type(resp))
#print(resp.text)
#json_dict= resp.json()
json_load=json.loads(resp.text)

json_dumps= json.dumps(json_load, sort_keys=True, indent=2)

print(json_dumps)

