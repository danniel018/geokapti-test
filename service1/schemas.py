from marshmallow import Schema, fields, validate, post_dump


class LocationsSchema(Schema):
    class Meta:
        ordered = True
    location_id = fields.String(dump_only = True)
    name = fields.String(required=False,validate=validate.Length(max=30))
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
   