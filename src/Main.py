import requests

response  = requests.get('https://api.openweathermap.org/data/2.5/forecast?q=krakow&APPID=c2edcc30e09fae917b1292ad18964e60&units=metric')
message = 'Hello world!'

print(response.json())