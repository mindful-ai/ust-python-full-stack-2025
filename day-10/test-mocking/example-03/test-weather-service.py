import unittest
from unittest.mock import patch, mock_open
from weather_service import get_weather_for_city_from_file

class TestWeatherService(unittest.TestCase):

    @patch("weather_service.requests.get")
    @patch("builtins.open", new_callable=mock_open, read_data="Bengaluru\n" )
    def test_weather_service_from_file(self, mock_file, mock_get):

        # response of mock_get -> response.json() -> set both response's value and json's value
        mock_get.return_value.json.return_value = {
                "city": "Bengaluru",
                "temperature": 32,
                "unit": 'C'
        }

        # actual function call
        result = get_weather_for_city_from_file('city.txt')

        # assertions for inputs
        mock_file.assert_called_once_with('city.txt', 'r')
        mock_get.assert_called_once_with("https://api.weather.com/Bengaluru")

        # assertions for output
        expected_data = {
                "city": "Bengaluru", "temperature": 32, "unit": 'C'
        }
        self.assertEqual(result, expected_data)

if __name__ == "__main__":

    unittest.main()