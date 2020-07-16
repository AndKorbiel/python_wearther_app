import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
Window.size = (350, 300)

Window.clearcolor = (255/255, 240/255, 200/255, 1)

from Main import current_forecast, formatted_date, today_name

class AppLayout(Widget):
    pass

class MyApp(App):
    city_name = f"{current_forecast['cityName']}"
    temperature = f"Temperature: {current_forecast['temp']}" + u" \u00B0C"
    todays_name = today_name
    date = formatted_date
    pressure = f"{current_forecast['pressure']} hPa"
    windSpeed = f"{current_forecast['wind']} km/h"
    overall = f"{current_forecast['overall']},\n{int(current_forecast['temp'])}" + u" \u00B0C"
    weather_icon = f"{current_forecast['weatherIconUrl']}"

    def build(self):
        return AppLayout()

if __name__ == '__main__':
    MyApp().run()