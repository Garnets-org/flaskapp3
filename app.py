from flask import Flask, request, render_template
import random

app = Flask(__name__)

weather_options = ["Sunny", "Rainy", "Cloudy", "Stormy", "Windy", "Foggy"]

@app.route('/')
def index():
    return render_template("index.html", forecast=None)

@app.route('/weather', methods=['POST'])
def get_weather():
    state = request.form['state']
    forecast = random.choice(weather_options)
    return render_template("index.html", forecast=forecast, state=state)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

