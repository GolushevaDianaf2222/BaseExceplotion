import requests

class NetworkException(BaseException):
    pass

def get_weather_data(city):
    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=your-app-id')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise NetworkException(f"Error: {e}") from e

try:
    print(get_weather_data('Moscow'))
except NetworkException as e:
    print(f'Error: {e}')

 

