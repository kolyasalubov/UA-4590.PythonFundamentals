from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(city: str):
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    desc = w.detailed_status.capitalize()
    humidity = w.humidity
    wind_speed = w.wind()['speed']

    return f"City: {city}\nTemperature: {temp:.1f}°C\nDescription: {desc}\nHumidity: {humidity}%\nWind: {wind_speed} m/s"

