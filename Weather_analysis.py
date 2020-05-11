import requests




def format_response(weather):
    try:
        name = weather['name'] #informacje z dictionary
        description = weather['weather'][0]['description'] #wheather wyrzuca całą tabelę, więc trzeba sprecyzowaać [0]
        temp = weather['main']['temp']
        final= 'City: %s \nConditions: %s \nTemperature: %s\N{DEGREE SIGN}C' % (name, description, temp)
    except:
        final = 'Please write a correct city name'
    return final

def  get_weather(city):
    weather_key = 'ce5aac7c1aacbd6070822b7c504a0ef9'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units':'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

