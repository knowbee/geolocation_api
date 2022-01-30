from flask import Flask

from flask_migrate import Migrate

from database.db import db
from database.config import config
from dotenv import load_dotenv
from sqlalchemy_utils.functions import database_exists, create_database
from routes.initializer import initialize_routes
from flask_swagger_ui import get_swaggerui_blueprint

import os


load_dotenv()


def create_app(geocoding, test_config=None):

    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV")

    if test_config:
        app.config.from_mapping(**test_config)
    else:
        app.config.from_object(config[env])

    db.init_app(app)
    with app.app_context():
        if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
            create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        db.create_all()

    Migrate(app, db)

    initialize_routes(geocoding, app)

    SWAGGER_URL = "/api/docs"
    API_URL = "/static/swagger.json"

    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={"app_name": "Geolocation-Swagger-UI"})

    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

    return app
