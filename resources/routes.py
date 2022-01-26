from .geolocation import GeoLocation


def initialize_routes(api):
    api.add_resource(GeoLocation, "/")
