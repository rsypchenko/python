import requests
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 145)

def say(text):
    engine.say(text)
    engine.runAndWait()

def weather_bot(city):
    weather_key = "ff7082235ef776e3a338f10ec37de41a";
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={weather_key}"
    response = requests.get(url)
    weather_data = response.json()
    print( weather_data)
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    say(f"The current weather in {city} is {description} with temperature {temperature} and humidity {humidity}")

print("Enter city:")
city = input()
weather_bot(city)