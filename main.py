import requests

API_KEY = "de08c640dcc678462a0a237f3beeec0f" 
url = f"http://api.openweathermap.org/data/2.5/weather?q=Chennai&appid={API_KEY}"


response = requests.get(url)
print(response.text)

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Condition: {data['weather'][0]['description']}")
    else:
        print("❌ City not found or invalid API key!")


def main():
    print("=== Weather App ===")
    city = input("Enter city name: ")
    get_weather(city)


if __name__ == "__main__":
    main()
