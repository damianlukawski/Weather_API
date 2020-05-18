import requests
import json

#the main app for weather analysis
with open('country-capitals.json', 'r', encoding="utf-8") as country_capitals:
    json_data1 = json.load(country_capitals)
    json_object = json.dumps(json_data1, indent = 2)

#print(json_data[1])
list_of_capitals = [x['CapitalName'] for x in json_data1 if x['CapitalName'] != 'N/A']
list_of_capitals.sort()
print(list_of_capitals)




