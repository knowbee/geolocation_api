from .db import db


class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    street_name = db.Column(db.String(120), nullable=False)

    def __init__(self, latitude: float, longitude: float, street_name: str):
        self.latitude = latitude
        self.longitude = longitude
        self.street_name = street_name
