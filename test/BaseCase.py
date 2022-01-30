import unittest
from server import create_app
from database.db import db
from test.mocks.services.geocoding_service_mock import GeocodingServiceMock
import time
import os


app = create_app(geocoding=GeocodingServiceMock())


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
        self.app = create_app(test_config=config_dict, geocoding=GeocodingServiceMock())
        self.app.app_context().push()
        self.client = self.app.test_client()
        self.db = db
