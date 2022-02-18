from test.BaseCase import BaseCase
import json


class TestGeolocationService(BaseCase):
    def test_0_drop_database(self):
        self.db.session.remove()
        self.db.drop_all()
        self.db.create_all()

    def test_1_get_empty_geolocation(self):
        response = self.client.get("/")
        self.assertEqual(response.json["message"], "No location found")
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

    def test_4_get_list_of_locations(self):
        response = self.client.get("/")
        self.assertIsInstance(response.json, list)
        self.assertEqual(response.status_code, 200)

    def test_5_returns_error_message_if_street_name_is_empty(self):
        street_name = ""
        payload = json.dumps({"street_name": street_name})

        response = self.client.post("/", headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(response.json["message"], "Failed to retrieve geolocation information")
        self.assertEqual(response.status_code, 200)

    def test_6_returns_error_message_if_latitude_and_longitude_are_empty(self):
        latitude = ""
        longitude = ""
        payload = json.dumps({"latitude": latitude, "longitude": longitude})

        response = self.client.post("/", headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(response.json["message"], "Failed to retrieve geolocation information")
        self.assertEqual(response.status_code, 200)

    def test_7_returns_error_message_if_empty_object_is_posted(self):
        payload = json.dumps({})

        response = self.client.post("/", headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(response.json["message"], "Failed to retrieve geolocation information")
        self.assertEqual(response.status_code, 200)

    def test_8_returns_invalid_coordinates_error_message_if_coordinates_are_not_valid(self):
        latitude = "latitude"
        longitude = "longitude"
        payload = json.dumps({"latitude": latitude, "longitude": longitude})

        response = self.client.post("/", headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(response.json["message"], "Invalid coordinates")
        self.assertEqual(response.status_code, 200)

    def test_9_returns_invalid_street_name_error_message_if_street_name_is_not_valid(self):
        street_name = "+++++++"
        payload = json.dumps({"street_name": street_name})

        response = self.client.post("/", headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(response.json["message"], "Failed to retrieve geolocation information")
        self.assertEqual(response.status_code, 200)

    def test_10_returns_invalid_coordinates_error_message_if_coordinates_are_not_out_of_bounds(self):
        latitude = "500"
        longitude = "500"
        payload = json.dumps({"latitude": latitude, "longitude": longitude})

        response = self.client.post("/", headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(response.json["message"], "Invalid coordinates")
        self.assertEqual(response.status_code, 200)
