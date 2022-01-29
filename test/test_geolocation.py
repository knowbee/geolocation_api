from test.BaseCase import BaseCase
import json


class TestGeolocationService(BaseCase):
    def test_1_get_empty_geolocation(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_2_returns_a_street_name_when_given_coordinates(self):
        latitude = "-1.954690"
        longitude = "30.092750"
        payload = json.dumps({"latitude": latitude, "longitude": longitude})

        response = self.client.post("/", headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(response.json["street_name"], "Kigali KK")
        self.assertEqual(response.status_code, 200)

    def test_3_returns_coordinates_when_given_street_name(self):
        street_name = "Kigali KK"
        payload = json.dumps({"street_name": street_name})

        response = self.client.post("/", headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(response.json["latitude"], "-1.954690")
        self.assertEqual(response.json["longitude"], "30.092750")
        self.assertEqual(response.status_code, 200)
