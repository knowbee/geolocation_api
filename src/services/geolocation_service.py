from flask import jsonify, request, Response
from src.models import Location, locations_schema
from src.repositories.location import LocationRepository
from geopy.geocoders import Nominatim
from src.helpers.geocoding_wrapper import GeocodingWrapper
import json
import sqlalchemy


class GeolocationService:
    def __init__(self, geocoding_wrapper: Nominatim):
        self.geocoding_wrapper: GeocodingWrapper = geocoding_wrapper

    def is_valid_street_name(self, street_name):
        return street_name.replace(" ", "").isalpha()

    def has_street_name(self, data) -> bool:
        if "street_name" in data and data["street_name"] != None and data["street_name"].strip() != "":
            return self.is_valid_street_name(data["street_name"])
        else:
            return False

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
            try:
                res = self.geocoding_wrapper.geocode(body["street_name"])
                return self.add_new_entry(res)
            except (AttributeError):
                return jsonify({"message": "Invalid street name"})

        elif self.has_latitude_and_longitude(body):
            try:
                res = self.geocoding_wrapper.address_lookup(body["latitude"], body["longitude"])
                return self.add_new_entry(res)
            except sqlalchemy.exc.DataError:
                return jsonify({"message": "Invalid coordinates"})
        else:
            return jsonify({"message": "Failed to retrieve geolocation information"})
