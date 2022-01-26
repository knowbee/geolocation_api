import unittest
from app import app


class TestGeolocationService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_geolocation_service(self):
        response = self.app.get("/")
        self.assertListEqual(response.json, [{"Latitude": "Longitude"}])
        self.assertEqual(response.status_code, 200)
