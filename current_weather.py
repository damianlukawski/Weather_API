import requests
from API_functions import format_response
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font



class Current_weather:
    @staticmethod
    def create_window():
        def get_weather(city):
            weather_key = 'ce5aac7c1aacbd6070822b7c504a0ef9'
            url = 'https://api.openweathermap.org/data/2.5/weather'
            parameters = {'APPID': weather_key, 'q': city, 'units':'Metric'}
            response = requests.get(url, params=parameters)
            weather = response.json()
            #print(format_response(weather))
            label['text'] = format_response(weather)


        root = tk.Tk()

        canvas = tk.Canvas(root, width=800, height=500)
        canvas.pack()

        background_image = tk.PhotoImage(file='weather_image.png')
        background_label = tk.Label(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        upper_frame = tk.Frame(root, bg="#80c1ff", bd=5)
        upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75,
                          relheight=0.1, anchor='n')  # relative width and height

        entry = tk.Entry(upper_frame, font=("Calibri", 12))
        entry.place(relwidth=0.65, relheight=1)

        button1 = tk.Button(upper_frame, text="Check weather",
                            font=("Calibri", 12), command=lambda: get_weather(entry.get()))
        button1.place(relx=0.7, relwidth=0.3, relheight=1)

        lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
        label = tk.Label(lower_frame, text="Type city name to see current weather",
                         fg="black", font=("Calibri", 24), justify="left", anchor="w")
        label.place(relwidth=1, relheight=1)

        root.mainloop()



