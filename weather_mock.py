import json
import dataclasses


@dataclasses.dataclass
class MockWeather:
    api_url: str
    api_key: str
    mode: str = None
    units: str = 'Metric'
    lang: str = 'English'


    def get_by_city_name(
            self,
            city_name,
    ):

        queries = {'city_name': city_name}
        joined_queries = ','.join(queries.values())

        with open('mock.json', 'r') as myfile:
            data = myfile.read()

        response = json.loads(data)

        return response

    def get_by_city_id(
            self,
            city_id,
    ):
        queries = {'city_name': city_id}
        joined_queries = ','.join(queries.values())

        with open('mock.json', 'r') as myfile:
            data = myfile.read()

        response = json.loads(data)

        return response

    def get_by_geographic_coordinates(
            self,
            latitude,
            longtitude,
    ):

        queries = {'city_name': latitude}
        joined_queries = ','.join(queries.values())

        with open('mock.json', 'r') as myfile:
            data = myfile.read()

        response = json.loads(data)

        return response

    def get_by_zip_code(self, zip_code):
        queries = {'city_name': zip_code}
        joined_queries = ','.join(queries.values())

        with open('mock.json', 'r') as myfile:
            data = myfile.read()

        response = json.loads(data)

        return response

    def get_by_rectangle_zone(
            self,
            lon_left,
            lat_bottom,
            lon_right,
            lat_top,
            zoom,
    ):

        rectangle_zone = {
            'lon_left': lon_left,
            'lat_bottom': lat_bottom,
            'lon_right': lon_right,
            'lat_top': lat_top,
            'zoom': zoom,
        }

        queries = {'city_name': lon_left}
        joined_queries = ','.join(queries.values())

        with open('mock.json', 'r') as myfile:
            data = myfile.read()

        response = json.loads(data)

        return response

    def get_by_circles(
            self,

            latitude,
            longtitude,
            cnt,
    ):
        queries = {'city_name': longtitude}
        joined_queries = ','.join(queries.values())

        with open('mock.json', 'r') as myfile:
            data = myfile.read()

        response = json.loads(data)

        return response

    def get_for_several_city_ids(self, list_of_ids):

        queries = {'city_name': list_of_ids}
        joined_queries = ','.join(queries.values())

        with open('mock.json', 'r') as myfile:
            data = myfile.read()

        response = json.loads(data)

        return response