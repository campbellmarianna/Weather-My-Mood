"""
Plan
- [x] Create interface for user (text field + button)
- [x] Get user input
- [x] Display mood options to users
- [x] Get weather data from API
    - Do a call 10 times for the number of moods
- [x] Associate weather data with moods
    Walk the json and add the value the mood
    - Call weather data
    - get value and store into as value for mood
- [x] Find Mood and return associated weather
"""



# def main():
    # "Enable user to input mood and get the corresponding weather in return"
    # print("Info About Weather My Mood")
    # user_mood = input("What is your mood based on list above?")
    # print("\n")
#
#
# if __name__ == '__main__':
#     main()

import configparser
import requests
import sys

#locations = [London, Detroit, Lansing, Dallas, Los Angeles, San Francisco, Atlantia, Washingtion.DC, Boston, Baltimore]'''
city_ids = [ 6058560, 4990729, 4998830, 4058076, 5368361, 5391959, 4180439, 2634716, 4317656, 4347778]
moods = ['Extremely Happy', 'Cheerful', 'Whimsical', 'Humorous', 'Reflective', 'Apathetic', 'Gloomy', 'Frustrated', 'Annoyed', 'Angry']
mood_and_weather = {}
weather_description_data = []
def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather(api_key, city):
    """Return weather based on city ID"""
    # for city in city_ids:
    url = "https://api.openweathermap.org/data/2.5/forecast?id={}&appid={}".format(city, api_key)
    r = requests.get(url)
    return r.json()

def get_weather_description(weather):
    "Gets the weather description"
    for num_moods in range(0, 10):
        description = weather['list'][num_moods]['weather'][0]['description']
        weather_description_data.append(description)
    return weather_description_data

def set_mood_to_weather_description(weather_description_data):
    "Return a dictionary that contains moods (key) with associated weather descriptions [value]"
    for num in range(0,10):
        mood = moods[num]
        weather_description = weather_description_data[num]
        mood_and_weather[mood] = weather_description
    return mood_and_weather

def find_weather_for_mood(user_mood):
    "Return the weather associated with user mood"
    if user_mood in mood_and_weather:
        return mood_and_weather[user_mood]
    else:
        "Invalid Mood Description - Use List Above"



def main():
    # display message if location not given in terminal
    # if len(sys.argv) != 2:
    #     exit("Usage: {} LOCATION".format(sys.argv[0]))
    location = 6058560 #sys.argv[1]
    # gets data from API
    api_key = get_api_key()
    weather = get_weather(api_key, location)
    # gets the description
    # print(weather['list'][10]['weather'][0]['description'])
    weather_description_data = get_weather_description(weather)
    set_mood_to_weather_description(weather_description_data)
    "Enable user to input mood and get the corresponding weather in return"
    print("Info About Weather My Mood")
    user_mood = input("What is your mood based on list above? ")
    # Find moood in description and return weather_description
    print("\n")
    print(find_weather_for_mood(user_mood))




if __name__ == '__main__':
    main()
************
import os

from flask import Flask, render_template
import configparser
import requests



def create_app(test_config=None):
    # create the app
    app = Flask(__name__)

    # logic for app
    city_ids = [ 6058560, 4990729, 4998830, 4058076, 5368361, 5391959, 4180439, 2634716, 4317656, 4347778]
    moods = ['Extremely Happy', 'Cheerful', 'Whimsical', 'Humorous', 'Reflective', 'Apathetic', 'Gloomy', 'Frustrated', 'Annoyed', 'Angry']
    mood_and_weather = {}
    weather_description_data = []
    def get_api_key():
        config = configparser.ConfigParser()
        config.read('config.ini')
        print("************READING*****************")
        return config['openweathermap']['api']

    def get_weather(api_key, city):
        """Return weather based on city ID"""
        # for city in city_ids:
        url = "https://api.openweathermap.org/data/2.5/forecast?id={}&appid={}".format(city, api_key)
        r = requests.get(url)
        return r.json()

    def get_weather_description(weather):
        "Gets the weather description"
        for num_moods in range(0, 10):
            description = weather['list'][num_moods]['weather'][0]['description']
            weather_description_data.append(description)
        return weather_description_data

    def set_mood_to_weather_description(weather_description_data):
        "Return a dictionary that contains moods (key) with associated weather descriptions [value]"
        for num in range(0,10):
            mood = moods[num]
            weather_description = weather_description_data[num]
            mood_and_weather[mood] = weather_description
        return mood_and_weather

    def find_weather_for_mood(user_mood):
        "Return the weather associated with user mood"
        if user_mood in mood_and_weather:
            return mood_and_weather[user_mood]
        else:
            "Invalid Mood Description - Use List Above"

    # a simple page that says hello
    @app.route('/')
    def homepage():
        location = 6058560
        api_key = get_api_key()
        weather = get_weather(api_key, location)
        return render_template("base.html", weather=weather)



    return app
