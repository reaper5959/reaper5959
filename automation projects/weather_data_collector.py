import requests

api_keys = "d4cf226715c97f60535d0227bf425246"
api_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Write your city:")

response = requests.get(
    url=api_url,
    params={
        "q": city,
        "appid": api_keys,
        "units": "metric"
    }
)

weather_data = response.json()
print(city, "tempuature is", weather_data['main']['temp'])
