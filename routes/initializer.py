import os
import routes
from flask.blueprints import Blueprint
from resources import GeoLocationResource

APPLICATION_ROOT = os.getenv("APPLICATION_ROOT", "/")


def initialize_routes(geocoding, app):

    GeoLocationResource.geocoding = geocoding

    for blueprint in vars(routes).values():
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint, url_prefix=APPLICATION_ROOT)
