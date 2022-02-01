from src.database.db import db
from decimal import Decimal
from .abc import BaseModel, MetaBaseModel
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class Location(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "locations"

    id: int = db.Column(db.Integer, primary_key=True)
    latitude: Decimal = db.Column(db.Numeric(8, 6), nullable=False)
    longitude: Decimal = db.Column(db.Numeric(9, 6), nullable=False)
    street_name: str = db.Column(db.String(), nullable=False)

    def __init__(self, latitude: Decimal, longitude: Decimal, street_name: str):
        self.latitude = latitude
        self.longitude = longitude
        self.street_name = street_name


class LocationSchema(ma.Schema):
    class Meta:
        fields = ("id", "latitude", "longitude", "street_name")


location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)
