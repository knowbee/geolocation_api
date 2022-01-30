from flask import Blueprint
from flask_restful import Api

from resources import GeoLocationResource

LOCATION_BLUEPRINT = Blueprint("location", __name__)
Api(LOCATION_BLUEPRINT).add_resource(GeoLocationResource, "/")
