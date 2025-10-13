from pyowm import OWM


API_KEY = "ef2206ff5da67de63306d0b143e20872"
owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather(city):
    obs = mgr.weather_at_place(city)
    return obs.weather





