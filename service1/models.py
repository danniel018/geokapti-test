from extensions import db
import uuid

class Locations(db.Model):
    __tablename__ = 'locations'

    location_id = db.Column(db.UUID(as_uuid = True), default=uuid.uuid4, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    latitude = db.Column(db.String(30), nullable=False)
    longitude = db.Column(db.String(30), nullable=False)
    