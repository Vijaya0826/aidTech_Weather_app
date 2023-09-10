import requests


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]

        weather_data = data["weather"]
        weather_description = weather_data[0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("City not found")

api_key = "605eae8c50868712f27fe71049c52a2b"  

while True:
    city = input("Enter city name (or type 'exit' to quit): ")
    
    if city.lower() == 'exit':
        break  
    
    get_weather(api_key, city)

