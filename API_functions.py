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

