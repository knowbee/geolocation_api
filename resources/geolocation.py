from flask import jsonify
from flask_restful import Resource


class GeoLocation(Resource):
    def get(self):
        result = {"message": "welcome"}
        return jsonify(result)
