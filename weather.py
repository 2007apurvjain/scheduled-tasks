import requests
import smtplib
import os
MY_EMAIL= os.environ.get("MY_EMAIL")
MY_PASSWORD=os.environ.get("MY_PASSWORD")
weather_api = os.environ.get("MY_WEATHER_API")
APP_ID = os.environ.get("MY_WEATHER_APP_ID")
LAT = os.environ.get("LAT")
LON = os.environ.get("LON")
OWM_WEATHER = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {"lat":LAT,"lon":LON,"appid":APP_ID,"cnt":4}




response = requests.get(OWM_WEATHER,params = weather_params)
response.raise_for_status()
data = response.json()



weather_ids = [entry["weather"][0]["id"] for entry in data["list"]]

if any(weather_id >= 500 and weather_id < 600 for weather_id in weather_ids):
    with smtplib.SMTP("smtp.gmail.com",587)as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(MY_EMAIL,MY_EMAIL,msg="Subject:Rain update\n\nhey it will rain today please carry an umbrela with your self")

