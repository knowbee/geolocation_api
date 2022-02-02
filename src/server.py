from flask import Flask

from flask_migrate import Migrate

from src.database.db import db
from src.database.config import config
from dotenv import load_dotenv
from sqlalchemy_utils.functions import database_exists, create_database
from src.routes.initializer import initialize_routes
from src.utils.swagger_setup import configure_swagger
from src.helpers import GeocodingWrapper

import os


load_dotenv()


class MyApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.geocoding_wrapper: GeocodingWrapper = GeocodingWrapper()

    def create_app(self, test_config=None):

        env = os.environ.get("FLASK_ENV")

        if test_config:
            self.app.config.from_mapping(**test_config)
        else:
            self.app.config.from_object(config[env])

        db.init_app(self.app)
        with self.app.app_context():
            if not database_exists(self.app.config["SQLALCHEMY_DATABASE_URI"]):
                create_database(self.app.config["SQLALCHEMY_DATABASE_URI"])
            db.create_all()

        Migrate(self.app, db)

        initialize_routes(self.geocoding_wrapper, self.app)
        configure_swagger(self.app)

        return self.app
