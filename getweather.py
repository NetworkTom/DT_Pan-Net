#!/usr/bin/python
import requests
import os

url = "https://api.openweathermap.org/data/2.5/weather?"
city = os.getenv("OWM_CITY")
apiKey = os.getenv("OWM_API_KEY")
# upadting the URL
getUrl = url + "q=" + city + "&appid=" + apiKey
# HTTP request
response = requests.get(getUrl)
# checking the status code of the request
if response.status_code == 200:
   data = response.json()
   print("city=\"" + city + "\", description=\"" + data['weather'][0]['description'] + "\", temp=" + str(data['main']['temp']) + ", humidity=" + str(data['main']['humidity']))
else:
   print("Response Code: " + str(response.status_code) + " - Error in the HTTP request")
