from geopy.geocoders import Nominatim


class GeocodingWrapper:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="geolocationapi")

    def address_lookup(self, latitude, longitude):
        street_name = self.geolocator.reverse(f"{latitude}, {longitude}")
        return {"street_name": str(street_name), "latitude": latitude, "longitude": longitude}

    def geocode(self, street_name):
        location = self.geolocator.geocode(street_name)
        return {
            "street_name": str(street_name),
            "latitude": str(location.latitude),
            "longitude": str(location.longitude),
        }
