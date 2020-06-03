import requests
import json
import tkinter as tk


from API_functions import format_response_2
#the main app for weather analysis

def find_capitals():
    def finding_holidays():
        def get_weather(city):
            weather_key = 'ce5aac7c1aacbd6070822b7c504a0ef9'
            url = 'https://api.openweathermap.org/data/2.5/weather'
            parameters = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
            response = requests.get(url, params=parameters)
            weather = response.json()
            return weather

        with open('country-capitals.json', 'r', encoding="utf-8") as country_capitals:
            json_data1 = json.load(country_capitals)
            json_object = json.dumps(json_data1, indent=2)

        assert type(json_data1) == list
        list_of_capitals = [x['CapitalName'] for x in json_data1 if x['CapitalName'] != 'N/A']
        list_of_countries = [x['CountryName'] for x in json_data1 if x['CapitalName'] != 'N/A']

        list_of_holiday_locations = []
        list_of_holiday_temp = []
        list_of_holiday_countries = []
        i = 0
        while i < len(list_of_capitals) - 1:
            try:
                w = get_weather(list_of_capitals[i])
                if w['main']['temp'] > 15 and w['main']['temp'] < 25 and w['weather'][0][
                    'description'] == "clear sky" and w['wind']['speed'] < 3:
                    list_of_holiday_locations.append(w['name'])
                    list_of_holiday_temp.append(w['main']['temp'])
                    list_of_holiday_countries.append(list_of_countries[i])
                else:
                    "bad weather"
            except:
                "None"
            i += 1

        list_city_temp = zip(list_of_holiday_locations, list_of_holiday_temp, list_of_holiday_countries)
        list_city_temps = list(list_city_temp)
        # print(
        #    "if you wish to rest in a capital with temperature in range 15-25\N{DEGREE SIGN}C, no clouds and only slight wind please visit one of the following:")
        result_final = ''
        for i, city in enumerate(list_city_temps):
            result = '%s. %s (%s), %s \N{DEGREE SIGN}C \n' % (str(i + 1), city[0], city[2], str(city[1]))
            result_final = result_final + result
        return result_final

    # print(finding_holidays())

    def OnButton():
        label2['text'] = "Please wait for the data to be collected  from openweathermap.org and analyzed..."
        label2['text'] = finding_holidays()

    root = tk.Tk()

    canvas = tk.Canvas(root, width=800, height=500)
    canvas.pack()

    upper_frame = tk.Frame(root, bg="#80c1ff", bd=5)
    upper_frame.place(relx=0.5, rely=0.1, relwidth=1,
                      relheight=0.3, anchor='n')  # relative width and height

    label1 = tk.Label(upper_frame,
                      text="if you wish to rest in a capital with temperature in range 15-25\N{DEGREE SIGN}C, "
                           "no clouds and only slight wind please visit one of the following:", justify="left",
                      wraplength=400, font=("Calibri", 12))
    label1.place(relwidth=0.5, relheight=1)

    button1 = tk.Button(upper_frame, text="Check weather", font=("Calibri", 12), command=lambda: OnButton())
    button1.place(relx=0.7, relwidth=0.3, relheight=1)

    lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
    lower_frame.place(relx=0.5, rely=0.35, relwidth=1, relheight=0.5, anchor='n')
    label2 = tk.Label(lower_frame, text="Type city name to see current weather", fg="black", font=("Calibri", 12),
                      justify="left", anchor="w", wraplength=400)
    label2.place(relwidth=1, relheight=1)

    root.mainloop()