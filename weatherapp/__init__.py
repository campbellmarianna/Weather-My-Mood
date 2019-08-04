"""
App that enable anonymous users to input their mood each day corresponding to
the weather.

Input:
'Extremely Happy'
Output:
'clear sky'
"""
from flask import Flask, render_template, request
import requests


def create_app(test_config=None):
    """Create the Flask weather app and access config file."""
    app = Flask(__name__)
    app.config.from_pyfile('config.cfg')

    # Necessary variables
    moods = ['Extremely Happy', 'Cheerful', 'Whimsical', 'Humorous',
        'Reflective', 'Apathetic', 'Gloomy', 'Frustrated', 'Annoyed', 'Angry']
    mood_and_weather = {}
    weather_description_data = []

    # Helper functions
    def get_api_key():
        """Return API KEY."""
        return app.config['API_KEY']

    def get_weather(api_key, city):
        """Return weather based on city ID."""
        url = "https://api.openweathermap.org/data/2.5/forecast?id={}&appid={}".format(city, api_key)
        r = requests.get(url)
        return r.json()

    def get_weather_description(weather):
        """Return the weather description."""
        for num_moods in range(0, 10):
            description = weather['list'][num_moods]['weather'][0]['description']
            weather_description_data.append(description)
        return weather_description_data

    def set_mood_to_weather_description(weather_description_data):
        """
        Return a dictionary that contains moods (key) with associated weather
        descriptions (value).
        """
        for num in range(0,10):
            mood = moods[num]
            weather_description = weather_description_data[num]
            mood_and_weather[mood] = weather_description
        return mood_and_weather

    def find_weather_for_mood(user_mood):
        """Return the weather associated with user mood."""
        if user_mood in mood_and_weather:
            return mood_and_weather[user_mood]
        else:
            return "Mood Not Found"

    @app.route('/', methods=('GET', 'POST'))
    def homepage():
        """
        Get the users mood and on the submission of the form direct the user to
        see the corresponding weather to their mood.
        """
        if request.method == 'POST':
            location = 6058560
            api_key = get_api_key()
            weather = get_weather(api_key, location)
            weather_description_data = get_weather_description(weather)
            set_mood_to_weather_description(weather_description_data)
            user_mood = request.form['mood']
            mood_weather = find_weather_for_mood(user_mood)
            if mood_weather == "Mood Not Found":
                message = "Invalid Mood Description - Use Provided List"
                return render_template("moods.html", message=message)
            else:
                return render_template("results.html", weather=mood_weather)
        return render_template("moods.html")

    return app
