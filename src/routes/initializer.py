import os
import src.routes as routes
from flask.blueprints import Blueprint
from src.resources import GeoLocationResource

APPLICATION_ROOT = os.getenv("APPLICATION_ROOT", "/")


def initialize_routes(geocoding_wrapper, app):

    GeoLocationResource.geocoding_wrapper = geocoding_wrapper

    for blueprint in vars(routes).values():
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint, url_prefix=APPLICATION_ROOT)
