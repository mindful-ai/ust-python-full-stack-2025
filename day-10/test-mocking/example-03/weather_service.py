import requests

def get_weather_for_city_from_file(filename):
    with open(filename, 'r') as file:
        city = file.readline().strip()

    response = requests.get(f"https://api.weather.com/{city}")
    return response.json()
