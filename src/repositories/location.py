from src.models import Location


class LocationRepository:
    def __init__(self, geocoding=None):
        self.geocoding = geocoding

    @staticmethod
    def get():
        return Location.query.all()

    def create(self, data):
        if "street_name" in data:
            address = self.geocoding.geocode(data["street_name"])
            result = Location(
                latitude=address["latitude"], longitude=address["longitude"], street_name=address["street_name"]
            )
            return result.save
        else:
            address = self.geocoding.address_lookup(data["latitude"], data["longitude"])
            result = Location(
                latitude=address["latitude"], longitude=address["longitude"], street_name=address["street_name"]
            )
            return result.save
