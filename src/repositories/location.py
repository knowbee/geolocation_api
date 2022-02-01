from src.models import Location


class LocationRepository:
    @staticmethod
    def get():
        return Location.query.all()

    def create(self, data):
        result = Location(**data)
        return result.save
