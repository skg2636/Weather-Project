import time

import requests, json


def fetch_weather_details(city_name):
    api_key = "API_KEY"

    url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    return x









