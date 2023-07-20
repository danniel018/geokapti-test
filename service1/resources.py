from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models import Locations
from extensions import db
from schemas import LocationsSchema
from marshmallow.exceptions import ValidationError

class LocationsResource(Resource):

    def post(self):
    
        locations_schema = LocationsSchema()
        try:
            data = request.get_json()
            loaded_location = locations_schema.load(data = data)
            
            new_location = Locations(**data)
            db.session.add(new_location)
            db.session.commit()

            return locations_schema.dump(new_location), HTTPStatus.CREATED
    
        except ValidationError as e:
            print(e)
            return {'error':400,'message':str(e)},HTTPStatus.BAD_REQUEST

        except Exception as e:
            print(e)
            db.session.rollback()
            return {'error':500,'message':'server error'},HTTPStatus.INTERNAL_SERVER_ERROR


class LocationResource(Resource):

    def get(self,location_id):
    
        locations_schema = LocationsSchema()
        
        location = Locations.get_by_id(location_id) 
        if location == None:
            return {'error':404,'message':'resouce not found'}, HTTPStatus.NOT_FOUND
        
        return locations_schema.dump(location), HTTPStatus.OK
        
        

