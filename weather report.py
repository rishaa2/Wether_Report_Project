import requests #can be installed using .pip install request
import os
from datetime import datetime

user_api = os.environ['weatherData']
location = input('Enter the ciity name: ')
#pasted from website:  api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print('Invalid City: {}, Please check your City name'.format(location))
else:
    #create variable to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("____________________________________________________________")
    print("Weather States for - {} || {}".format(location.upper(),date_time))
    print("____________________________________________________________")

    print("Current temparature i        : {:.2f} deg C".format(temp_city))
    print("Current wewather description : ",weather_desc)
    print("Current Humidity             :",hmdt, '%')
    print("Current wind speed           :",wind_spd,"kmph")