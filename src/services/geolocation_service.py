from flask import jsonify, request, Response
from src.models import Location, locations_schema
from src.repositories.location import LocationRepository
from geopy.geocoders import Nominatim
import json


class GeolocationService:
    def __init__(self, geocoding_wrapper: Nominatim):
        self.geocoding_wrapper: Nominatim = geocoding_wrapper

    def has_street_name(self, data) -> bool:
        return "street_name" in data and data["street_name"] != None and data["street_name"].strip() != ""

    def has_latitude_and_longitude(self, data) -> bool:
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
            res = json.dumps({"message": "No location found"})
            return Response(res, status=200, mimetype="application/json")

    def add_new_entry(self, address):
        location = LocationRepository().create(address)
        return jsonify(location().json)

    def create_location(self):
        body = request.get_json()
        if self.has_street_name(body):
            address = self.geocoding_wrapper.geocode(body["street_name"])
            return self.add_new_entry(address)

        elif self.has_latitude_and_longitude(body):
            address = self.geocoding_wrapper.address_lookup(body["latitude"], body["longitude"])
            return self.add_new_entry(address)

        else:
            return jsonify({"message": "Failed to retrieve geolocation information"})
