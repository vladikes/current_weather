# Current weather API

Application to probe current weather from the openweathermap API

## Installation

Run pip3 install -r requirements.txt (Python 3) to install the packages

## Usage
Insert the correct API key and URL in settings.toml production settings
See app.py for an example
Run app.py for results

For API parameters and guide please see:
https://openweathermap.org/current

Example:

```python
import weather
from dynaconf import settings

client = weather.Weather(
    api_url=settings.get('api_url'),
    api_key=settings.get('api_key'),
)

print(client.get_by_city_name(city_name='Houston'))
```