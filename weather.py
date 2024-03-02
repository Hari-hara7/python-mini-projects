import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit or 'metric' for Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def display_weather(data):
    if data:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Unable to fetch weather data.")

def main():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your actual API key
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
