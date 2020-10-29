import requests
import dataclasses


@dataclasses.dataclass
class Weather:
    api_url: str
    api_key: str
    mode: str = None
    units: str = 'Metric'
    lang: str = 'English'

    try:
        session = requests.Session()
    except requests.exceptions.RequestException as error:
        print(error)

    def get_by_city_name(
            self,
            city_name,
    ):

        queries = {'city_name': city_name}
        joined_queries = ','.join(queries.values())

        response = self.session.get(
            url='{api_url}data/2.5/weather?q={query}&appid={api_key}&mode={mode}&units{units}&lang={lang}'.format(
                api_url=self.api_url,
                query=joined_queries,
                api_key=self.api_key,
                mode=self.mode,
                units=self.units,
                lang=self.lang,
            ),

        )

        return response.text

    def get_by_city_id(
            self,
            city_id,
    ):

        response = self.session.get(
            url='{api_url}data/2.5/weather?q={city_id}&appid={api_key}&mode={mode}&units{units}&lang={lang}'.format(
                api_url=self.api_url,
                city_id=city_id,
                api_key=self.api_key,
                mode=self.mode,
                units=self.units,
                lang=self.lang,
            ),

        )

        return response.text

    def get_by_geographic_coordinates(
            self,
            latitude,
            longtitude,
    ):

        response = self.session.get(
            url='{api_url}data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&mode={mode}&units{units}&lang={lang}'.format(
                api_url=self.api_url,
                lat=latitude,
                lon=longtitude,
                api_key=self.api_key,
                mode=self.mode,
                units=self.units,
                lang=self.lang,
            ),

        )

        return response.text

    def get_by_zip_code(self, zip_code):

        response = self.session.get(
            url='{api_url}data/2.5/weather?zip={zip}&appid={api_key}&mode={mode}&units{units}&lang={lang}'.format(
                api_url=self.api_url,
                zip=zip_code,
                api_key=self.api_key,
                mode=self.mode,
                units=self.units,
                lang=self.lang,
            ),

        )

        return response.text

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

        joined_zone = ','.join(rectangle_zone.values())

        response = self.session.get(
            url='{api_url}data/2.5/box/city?bbox={bbox}&appid={api_key}&units{units}&lang={lang}'.format(
                api_url=self.api_url,
                bbox=joined_zone,
                api_key=self.api_key,
                units=self.units,
                lang=self.lang,
            ),

        )

        return response.text

    def get_by_circles(
            self,
            latitude,
            longtitude,
            cnt,
    ):

        response = self.session.get(
            url='{api_url}data/2.5/find?lat={lat}&lon={lon}&cnt={cnt}&appid={api_key}&units{units}&lang={lang}'.format(
                api_url=self.api_url,
                lat=latitude,
                lon=longtitude,
                cnt=cnt,
                api_key=self.api_key,
                units=self.units,
                lang=self.lang,
            ),

        )

        return response.text

    def get_for_several_city_ids(self, list_of_ids):

        comma_separated_ids = ','.join(list_of_ids)

        response = self.session.get(
            url='{api_url}data/2.5/group?id={ids}&appid={api_key}&mode={mode}&units{units}&lang={lang}'.format(
                api_url=self.api_url,
                ids=comma_separated_ids,
                api_key=self.api_key,
                mode=self.mode,
                units=self.units,
                lang=self.lang,
            ),

        )

        return response.text
