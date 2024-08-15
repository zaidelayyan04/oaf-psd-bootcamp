# weather_handler.py

from weather_service import WeatherService

class WeatherHandler:
    def __init__(self, service: WeatherService):
        self.service = service

    def handle_temperature_request(self):
        data = self.service.get_hourly_temperature()
        # Extract temperatures from the data
        temperatures = data.get("hourly", {}).get("temperature_2m", [])
        return temperatures
