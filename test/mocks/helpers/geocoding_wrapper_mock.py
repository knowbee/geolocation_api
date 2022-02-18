from decimal import Decimal


class GeocodingWrapperMock:
    def __init__(self):
        self.geolocator = NominatimMock(user_agent="geolocationapi")

    def address_lookup(self, latitude: Decimal, longitude: Decimal):
        result = self.geolocator.reverse(latitude, longitude)
        return result

    def geocode(self, street_name):
        result = self.geolocator.geocode(street_name)
        return result


class NominatimMock:
    def __init__(self, user_agent):
        self.user_agent = user_agent

    def reverse(self, latitude: Decimal, longitude: Decimal):
        street_name = "Kigali KK"
        return {"latitude": latitude, "longitude": longitude, "street_name": street_name}

    def geocode(self, street_name):
        latitude = "-1.954690"
        longitude = "30.092750"
        return {"latitude": latitude, "longitude": longitude, "street_name": street_name}
