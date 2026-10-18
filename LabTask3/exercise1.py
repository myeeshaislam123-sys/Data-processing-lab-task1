
import requests
import pandas as pd

weather_url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=23.8103&longitude=90.4125"
    "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
    "&timezone=Asia%2FDhaka&forecast_days=7"
)


response = requests.get(weather_url, timeout=20)


print("HTTP status code:", response.status_code)


response.raise_for_status()


data = response.json()


print(data.keys())
