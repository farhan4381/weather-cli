import requests

API_KEY = "9e2c10d8f2475dab3e81ea4436f044e7"  # Your OpenWeatherMap API key

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    print(f"Requesting URL: {url}")  # Debug line to see the API URL
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Condition: {weather['description']}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    get_weather(city)
