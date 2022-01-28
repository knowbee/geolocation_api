from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from resources.routes import initialize_routes
from database.db import db
from database.config import config
from dotenv import load_dotenv


import os

load_dotenv()


def create_app(test_config=None):

    app = Flask(__name__)
    env = os.environ.get("FLASK_ENV")

    if test_config:
        app.config.from_mapping(**test_config)
    else:
        app.config.from_object(config[env])

    with app.app_context():
        db.init_app(app)
        db.create_all()

    Migrate(app, db)

    api = Api(app)
    initialize_routes(api)

    return app
