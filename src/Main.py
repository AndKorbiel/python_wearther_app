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
    'overall': ''
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
    current_forecast['overall'] = data['weather']

getForecast()
for key, value in current_forecast.items():
    print(value)

today = date.today()
formatted_date = "%s-%s-%s" % (today.day, today.month, today.year)
today_name = today.strftime("%A")