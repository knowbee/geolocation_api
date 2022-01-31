import unittest
from src.server import create_app
from src.database.db import db
from test.mocks.helpers.geocoding_mock import GeocodingMock
import os


app = create_app(geocoding=GeocodingMock())


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
        self.app = create_app(test_config=config_dict, geocoding=GeocodingMock())
        self.app.app_context().push()
        self.client = self.app.test_client()
        self.db = db
