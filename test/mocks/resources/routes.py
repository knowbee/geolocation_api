from .geolocation import GeoLocationMock


def initialize_routes(api):
    api.add_resource(GeoLocationMock, "/")
