from .db import db


class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.String(20), unique=True, nullable=False)
    longitude = db.Column(db.String(20), unique=True, nullable=False)
    street_name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, latitude, longitude, street_name):
        self.latitude = latitude
        self.longitude = longitude
        self.street_name = street_name
