import tkinter as tk
from tkinter import font
from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather

HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


def get_weather():
    place = entry_field.get().strip() or "Lviv,UA"  
    try:
        obs = mgr.weather_at_place(place)
        w = obs.weather

        temp = w.temperature('celsius')
        wind = w.wind()

        result = (
            f"Location: {place}\n"
            f"Status:   {w.detailed_status}\n"
            f"Temp:     {temp.get('temp', '?')}°C "
            f"(feels like {temp.get('feels_like', '?')}°C)\n"
            f"Min/Max:  {temp.get('temp_min', '?')}°C / {temp.get('temp_max', '?')}°C\n"
            f"Humidity: {w.humidity}%\n"
            f"Clouds:   {w.clouds}%\n"
            f"Wind:     {wind.get('speed', '?')} m/s, {wind.get('deg', '?')}°\n"
            f"Rain:     {w.rain if w.rain else '—'}"
        )
    except Exception as e:
        result = ("Incorrect city")
    label.config(text=result)


button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

