import requests

from config import weather_api_key, lat, lon, units, exclude
from src.graphics import draw_weather    

def get_weather():
    request_url = 'https://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+lon+'&units='+units+'&appid='+weather_api_key
    return requests.get(request_url).json()

def get_forecast():
    request_url = 'https://api.openweathermap.org/data/2.5/forecast?lat='+lat+'&lon='+lon+'&units='+units+'&appid='+weather_api_key+'&cnt=2'
    return requests.get(request_url).json()

def show_weather():
    weather = get_weather()
    forecast = get_forecast()
    print(forecast)
    icon_path = weather.get('weather')[0].get('icon')[:-1] + 'n.png'
    temperature = round(weather.get('main').get('temp'))
    feels_like = round(weather.get('main').get('feels_like'))
    forecast = forecast.get('list')[1].get('weather')[0].get('description')
    draw_weather(icon_path, temperature, feels_like, forecast)