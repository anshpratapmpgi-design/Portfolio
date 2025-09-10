
weather_data = {
    "kanpur": "Sunny 🌞, 35°C",
    "delhi": "Cloudy ☁, 32°C",
    "mumbai": "Rainy 🌧, 28°C",
    "lucknow": "Hot 🔥, 38°C"
}

while True:
    city = input("Enter city name (or type 'exit' to quit): ").lower()

    if city == "exit":
        print("Thank you! ❄")
        break

    if city in weather_data:
        print("Weather in", city.title(), "is:", weather_data[city])
    else:
        print("Sorry! Weather data not available for", city.title())