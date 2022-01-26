from flask import jsonify
from flask_restful import Resource


class GeoLocation(Resource):
    def get(self):
        return jsonify([{"Latitude": "Longitude"}])
