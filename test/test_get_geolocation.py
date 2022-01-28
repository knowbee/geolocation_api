from test.BaseCase import BaseCase


class TestGeolocationService(BaseCase):
    def test_get_geolocation(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "welcome")
