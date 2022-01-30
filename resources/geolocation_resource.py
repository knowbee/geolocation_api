from flask import jsonify, request
from flask_restful import Resource
from models import locations_schema
from repositories.location import LocationRepository


class GeoLocationResource(Resource):
    geocoding = None

    @classmethod
    def get(cls):
        location = LocationRepository(geocoding=cls.geocoding).get()
        if len(location) > 0:
            return jsonify(locations_schema.dump(location))
        else:
            return jsonify({"message": "No location found"})

    @classmethod
    def post(cls):
        body = request.get_json()
        location = LocationRepository(geocoding=cls.geocoding).create(body)
        return jsonify(location().json)
