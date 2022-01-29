import unittest
from server import create_app
from database.db import db
from test.mocks.resources.routes import initialize_routes
import time
import os


app = create_app(initialize_routes)


class BaseCase(unittest.TestCase):
    def setUp(self) -> None:
        if os.environ.get("FLASK_ENV") == "docker":
            self.db_url = os.environ.get("DATABASE_URL_TEST_DOCKER")
        else:
            self.db_url = os.environ.get("DATABASE_URL_TEST")
        config_dict = {
            "SQLALCHEMY_DATABASE_URI": self.db_url,
            "DEBUG": True,
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
        self.app = create_app(initialize_routes, config_dict)
        self.app.app_context().push()
        self.client = self.app.test_client()
        self.db = db

        time.sleep(2)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
