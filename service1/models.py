from extensions import db
import uuid

class Locations(db.Model):
    __tablename__ = 'locations'

    location_id = db.Column(db.String(36), default=uuid.uuid4, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    @classmethod
    def get_by_id(cls,location_id):

        return cls.query.filter(cls.location_id == location_id)
    