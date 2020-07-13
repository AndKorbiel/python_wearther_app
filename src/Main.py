import requests
import os
import json

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('API_KEY')

current_forecast = {
    'city_name': '',
    'temp': '',
    'pressure': '',
    'wind': ''
}

# Get Forecast
def getForecast():
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?id=3094802&appid={api_key}&units=metric')
    data = response.json()
    # print(json.dumps(data, indent=4))

    current_forecast['cityName'] = data['name']
    current_forecast['temp'] = data['main']['temp']
    current_forecast['pressure'] = data['main']['pressure']
    current_forecast['wind'] = data['wind']['speed']

getForecast()
for key, value in current_forecast.items():
    print(value)

# print(json.dumps(data, indent=4))

# res = requests.get('https://jsonplaceholder.typicode.com/todos/1')
# data = res.json()

# for key,value in data.items():
#     print(f'Key: {key}, Value: {value}')
