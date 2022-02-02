import unittest
from src.server import MyApp
from src.database.db import db
from test.mocks.helpers.geocoding_wrapper_mock import GeocodingWrapperMock
import os


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
        self.app_instance = MyApp()
        self.app_instance.geocoding_wrapper = GeocodingWrapperMock()
        self.app = self.app_instance.create_app(config_dict)

        self.app.app_context().push()
        self.client = self.app.test_client()
        self.db = db
