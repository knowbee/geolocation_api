from flask import jsonify, request
from src.models import locations_schema
from src.repositories.location import LocationRepository


class GeolocationService:
    def __init__(self, geocoding):
        self.geocoding = geocoding

    def get_location(self):
        location = LocationRepository(geocoding=self.geocoding).get()
        if len(location) > 0:
            return jsonify(locations_schema.dump(location))
        else:
            return jsonify({"message": "No location found"})

    def create_location(self):
        body = request.get_json()
        location = LocationRepository(geocoding=self.geocoding).create(body)
        return jsonify(location().json)
