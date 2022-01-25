from flask import jsonify
from flask_restful import Resource


class GeoLocation(Resource):
    def get(self, latitude, longitude):
        return jsonify({"Latitude": "Longitude"})
