import requests

class WeatherService:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def get_hourly_temperature(self):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&hourly=temperature_2m"
        response = requests.get(url)
        data = response.json()
        return data
