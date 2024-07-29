from abc import ABC, abstractmethod

class WeatherAPI(ABC):
    @abstractmethod
    def get_temperature(self, city):
        pass
    def get_humidity(self, city):
        pass
class WeatherService(WeatherAPI):
    def __init__(self, api_url):
        self.api_url = api_url

    def get_temperature(self):
        pass
    
    def get_humidity(self):
        pass
