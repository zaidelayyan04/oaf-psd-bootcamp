import unittest
from builder import WeatherBuilder

class TestWeatherHandler(unittest.TestCase):

    def test_handle_temperature_request(self):
        # Define cities with their coordinates
        cities = [
            {"name": "Berlin", "latitude": 52.52, "longitude": 13.419998},
            {"name": "Paris", "latitude": 48.8566, "longitude": 2.3522}
        ]
        
        for city in cities:
            builder = WeatherBuilder(city["latitude"], city["longitude"])
            handler = builder.create_weather_handler()
            temperature_data = handler.handle_temperature_request()

            print(f"City: {city['name']}")
            print(f"Temperatures: {temperature_data}")
            print()

            # Optionally, you can add assertions if needed
            self.assertIsInstance(temperature_data, list)
            self.assertTrue(all(isinstance(temp, (int, float)) for temp in temperature_data))

if __name__ == '__main__':
    unittest.main()