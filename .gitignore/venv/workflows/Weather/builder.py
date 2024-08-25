# builder.py

from weather_service import WeatherService
from weather_handler import WeatherHandler

class WeatherBuilder:
     def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

     def create_weather_service(self) -> WeatherService:
        return WeatherService(self.latitude, self.longitude)

     def create_weather_handler(self) -> WeatherHandler:
        service = self.create_weather_service()
        return WeatherHandler(service)
