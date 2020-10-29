import weather
import weather_mock
from dynaconf import settings

if __name__ == '__main__':
    settings = settings.from_env('development')
    client = None

    if settings.MESSAGE == 'production':
        client = weather.Weather(
            api_url=settings.get('api_url'),
            api_key=settings.get('api_key'),
        )
    if settings.MESSAGE == 'development':
        client = weather_mock.MockWeather(
            api_url=settings.get('api_url'),
            api_key=settings.get('api_key'),
        )

    print(client.get_by_city_name(city_name='Houston'))