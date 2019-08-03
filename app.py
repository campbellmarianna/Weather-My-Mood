"""
Plan
- Create interface for user (text field + button)
- [x] Get user input
- Display mood options to users
- [x] Get weather data from API
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

#locations = [London, Detroit, Lansing, Dallas, Los Angeles, San Francisco, Atlantia, Washingtion.DC, Boston, Baltimore]'''
city_ids = [ 6058560, 4990729, 4998830, 4058076, 5368361, 5391959, 4180439, 2634716, 4317656, 4347778]
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

def main():
    # display message if location not given in terminal
    # if len(sys.argv) != 2:
    #     exit("Usage: {} LOCATION".format(sys.argv[0]))
    location = 6058560 #sys.argv[1]
    # gets data from API
    api_key = get_api_key()
    weather = get_weather(api_key, location)
    # gets the description
    print(weather['list'][10]['weather'][0]['description'])


if __name__ == '__main__':
    main()
