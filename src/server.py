from flask import Flask

from flask_migrate import Migrate

from src.database.db import db
from src.database.config import config
from dotenv import load_dotenv
from sqlalchemy_utils.functions import database_exists, create_database
from src.routes.initializer import initialize_routes
from src.utils.swagger_setup import configure_swagger

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
    configure_swagger(app)

    return app
