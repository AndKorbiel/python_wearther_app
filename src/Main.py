import requests
import os
import json

from dotenv import load_dotenv
load_dotenv()

from datetime import date

api_key = os.getenv('API_KEY')

current_forecast = {
    'city_name': '',
    'temp': '',
    'pressure': '',
    'wind': '',
    'overall': '',
    'weatherIconUrl': '../Public/img/001-sun.png'
}

# Get Forecast
def getForecast():
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?id=3094802&appid={api_key}&units=metric')
    data = response.json()
    print(json.dumps(data, indent=4))

    current_forecast['cityName'] = data['name']
    current_forecast['temp'] = data['main']['temp']
    current_forecast['pressure'] = data['main']['pressure']
    current_forecast['wind'] = data['wind']['speed']
    current_forecast['overall'] = data['weather'][0]['description']

getForecast()
for key, value in current_forecast.items():
    print(value)

today = date.today()
formatted_date = "%s.%s.%s" % (today.day, today.month, today.year)
today_name = today.strftime("%A")

def getWeatherIcon(value):
    return {
        'few clouds': '../Public/img/001-sun.png',
        'broken clouds':'../Public/img/001-sun.png',
        'light rain': '../Public/img/004-drop.png',
        'rain': '../Public/img/004-drop.png',
        'shower rain': '../Public/img/004-drop.png',
        'moderate rain': '../Public/img/004-drop.png',
        'clear sky': '../Public/img/002-sunny.png',
        'scattered clouds': '../Public/img/003-clouds.png',
        'thunderstorm': '../Public/img/006-thunder.png',
        'snow': '../Public/img/005-snowflake.png',
    }.get(value, 'clear sky')

current_forecast['weatherIconUrl'] = getWeatherIcon(current_forecast['overall'])
