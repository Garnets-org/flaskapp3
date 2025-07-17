# FlaskApp3 - Weather Simulation API

This is a simple Flask web app that simulates weather conditions for a user-specified state or location. Users can enter a state name in a web form, and the app will return a randomly selected weather condition like "Rainy", "Sunny", or "Cloudy".

---

## 🌦 Features

- 🌍 HTML form to input a state or region
- 🔁 Simulates weather using random selection
- 📺 Displays results immediately in the browser
- 🐳 Dockerized for easy container-based usage

---

## 🐳 How to Run (Docker Only)

### 🔧 1. Build the Docker Image
```bash
docker build -t flaskapp3 .
docker run -d -p 5003:5000 flaskapp3

