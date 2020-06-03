import requests
from API_functions import format_response
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
from current_weather import Current_weather


def check_weather():
    root.destroy()
    Current_weather.create_window()



root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=500)
canvas.pack()



frame = tk.Frame(root, bg="#80c1ff", bd=15)
frame.place(relx=0, rely=0.5, relwidth=1, relheight=1, anchor='w')  # relative width and height

button1 = tk.Button(frame, text="Check current weather", font=("Calibri", 12), command=lambda:check_weather())
button1.place(relx=0, rely=0.03, relwidth=1, relheight=0.3, anchor="nw")

button2 = tk.Button(frame, text="Weather Graph", font=("Calibri", 12))
button2.place(relx=0, rely=0.36, relwidth=1, relheight=0.3, anchor="nw")

button3 = tk.Button(frame, text="Finding perfect holidays", font=("Calibri", 12))
button3.place(relx=0, rely=0.69, relwidth=1, relheight=0.3, anchor="nw")

'''
entry = tk.Entry(upper_frame, font=("Calibri",12))
entry.place(relwidth=0.65, relheight=1)
button1 = tk.Button(upper_frame, text = "Check weather",
                    font=("Calibri",12), command=lambda: get_weather(entry.get()))
button1.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
label = tk.Label(lower_frame, text = "Type city name to see current weather",
                 fg="black", font=("Calibri",24), justify="left", anchor="w")
label.place(relwidth=1, relheight=1)


'''
root.mainloop()



