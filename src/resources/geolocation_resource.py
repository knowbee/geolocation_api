from flask_restful import Resource
from src.services import GeolocationService
from flasgger import swag_from


class GeoLocationResource(Resource):
    geocoding = None

    @classmethod
    @swag_from("../swagger/geolocation/GET.yml")
    def get(cls):
        return GeolocationService(geocoding=cls.geocoding).get_location()

    @classmethod
    @swag_from("../swagger/geolocation/POST.yml")
    def post(cls):
        return GeolocationService(geocoding=cls.geocoding).create_location()
