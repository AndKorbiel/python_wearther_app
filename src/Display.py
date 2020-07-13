import kivy
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

from Main import current_forecast

print(current_forecast)

class AppLayout(GridLayout):
    def __init__(self, **kwargs):
        super(AppLayout, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text=f"City: {current_forecast['cityName']}"))
        self.add_widget(Label(text=f"Temperature: {current_forecast['temp']}" + u" \u00B0C"))


class MyApp(App):
    def build(self):
        return AppLayout()

if __name__ == '__main__':
    MyApp().run()