"""
Plan
- Create interface for user (text field + button)
- Get user input
- Display mood options to users
- Get weather data from API
    - Do a call 10 times for the number of moods
- Associate weather data with moods
    Walk the json and add the value the mood
    - Call weather data
    - get value and store into as value for mood
- Find Mood and return associated weather
"""



# def main():
#     "Enable user to input mood and get the corresponding weather in return"
#     print("Info About Weather My Mood")
#     user_mood = input("What is your mood based on list above?")
#     print("\n")
#
#
# if __name__ == '__main__':
#     main()

import configparser
import requests
import sys


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
    r = requests.get(url)
    return r.json()

def main():
    if len(sys.argv) != 2:
        exit("Usage: {} LOCATION".format(sys.argv[0]))
    location = sys.argv[1]
    print(f"This is location: {location}")

    api_key = get_api_key()
    weather = get_weather(api_key, location)

    print(weather['weather'][0]['description'])
    # inner_weather = weather['weather']
    # descriptive_weather = inner_weather['description']
    print('\n')
    print(weather)


if __name__ == '__main__':
    main()
