import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from PIL import ImageTk, Image
import requests
from tkinter import font
import time
import numpy as np
import matplotlib.pyplot as plt


def plot_weather():
    root = tk.Tk()

    canvas = tk.Canvas(root, width=800, height=500)
    canvas.pack()
    lista = []

    def format_response(weather):
        try:
            i = 0
            temp = []
            while i < 40:
                temp.append(float(weather['list'][i]['main']['temp']))
                i += 1
            final = np.array(temp)
        except:
            final = 0
        return final

    def get_weather(city):
        weather_key = 'ce5aac7c1aacbd6070822b7c504a0ef9'
        url = 'http://api.openweathermap.org/data/2.5/forecast'
        params = {'APPID': weather_key, 'q': city, 'cnt': '40', 'units': 'Metric', 'lang': 'pl'}
        response = requests.request('get', url, params=params)  # albo requests.get(...)
        weather = response.json()
        label["text"] = "press graph to print out"

        def graph():
            x = np.arange(0, 40, 1.0)
            y = format_response(weather)
            plt.plot(x, y)
            plt.xlabel("Time [hours]")
            plt.ylabel("Temperature [\N{DEGREE SIGN}C]")
            plt.show()


        button2 = tk.Button(upper_frame, text="graph",
                            font=("Calibri", 12), command=graph)
        button2.place(rely=0.45, relx=0.7, relwidth=0.3, relheight=0.3)

    background_image = tk.PhotoImage(master = canvas, file='weather_image.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    upper_frame = tk.Frame(root, bg="#80c1ff", bd=5)
    upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75,
                      relheight=0.2, anchor='n')  # relative width and height

    label1 = tk.Label(upper_frame, text="Podaj nazwe miasta: ", font=("Calibri", 12))
    label1.place(rely=0.05, relwidth=0.6, relheight=0.25)
    #label2 = tk.Label(upper_frame, text="Za ile godzin: ", font=("Calibri", 12))
    #label2.place(rely=0.05, relx=0.45, relwidth=0.2, relheight=0.25)

    entry1 = tk.Entry(upper_frame, font=("Calibri", 12))
    entry1.place(rely=0.45, relwidth=0.6, relheight=0.4)
    # entry2 = tk.Entry(upper_frame, font=("Calibri",12))
    # entry2.place(rely=0.45, relx=0.45, relwidth=0.2, relheight=0.4)
    lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.5, anchor='n')
    label = tk.Label(lower_frame, text="Podaj nazwę miasta by wyświetlić pogodę",
                     fg="black", font=("Calibri", 16), justify="left", anchor="w")
    label.place(relwidth=1, relheight=1)
    button1 = tk.Button(upper_frame, text="Check weather",
                        font=("Calibri", 12), command=lambda: get_weather(entry1.get()))
    button1.place(relx=0.7, relwidth=0.3, relheight=0.3)

    tk.mainloop()
    # If you put root.destroy() here, it will cause an error if the window is
    # closed with the window manager.