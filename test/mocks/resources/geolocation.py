from flask import jsonify, request
from flask_restful import Resource
from test.mocks.services.geocoder_service_mock import GeocodingMock
from database.models import Location, locations_schema
from database.db import db


class GeoLocationMock(Resource):
    def get(self):
        location = Location.query.all()
        result = locations_schema.dump(location)
        return jsonify(result)

    def post(self):
        body = request.get_json()
        geolocator = GeocodingMock()
        street_name = body.get("street_name")
        if street_name != None:
            address = geolocator.geocode(street_name)
            data = {"street_name": street_name, "latitude": address["latitude"], "longitude": address["longitude"]}
            result = Location(**data)
            db.session.add(result)
            db.session.commit()
            return jsonify(data)
        else:
            latitude = body.get("latitude")
            longitude = body.get("longitude")
            address = geolocator.address_lookup(latitude, longitude)

            result = Location(**address)
            db.session.add(result)
            db.session.commit()

            return jsonify({"street_name": address["street_name"]})
