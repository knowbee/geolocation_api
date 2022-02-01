from flask import jsonify, request
from src.models import Location, locations_schema
from src.repositories.location import LocationRepository
from geopy.geocoders import Nominatim


class GeolocationService:
    def __init__(self, geocoding: Nominatim):
        self.geocoding: Nominatim = geocoding

    def hasStreetName(self, data) -> bool:
        return "street_name" in data and data["street_name"] != None and data["street_name"].strip() != ""

    def hasLatitudeAndLongitude(self, data) -> bool:
        return (
            "latitude" in data
            and "longitude" in data
            and data["latitude"] != None
            and data["longitude"] != None
            and data["latitude"].strip() != ""
            and data["longitude"].strip() != ""
        )

    def get_location(self):
        location: Location = LocationRepository().get()
        if len(location) > 0:
            return jsonify(locations_schema.dump(location))
        else:
            return jsonify({"message": "No location found"})

    def create_location(self):
        body = request.get_json()
        if self.hasStreetName(body):
            address = self.geocoding.geocode(body["street_name"])
            location = LocationRepository().create(address)
            return jsonify(location().json)

        elif self.hasLatitudeAndLongitude(body):
            address = self.geocoding.address_lookup(body["latitude"], body["longitude"])
            location = LocationRepository().create(address)
            return jsonify(location().json)

        else:
            return jsonify({"message": "Failed to retrieve geolocation information"})
