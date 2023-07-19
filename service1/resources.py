from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models import Locations
from extensions import db

class LocationsResource(Resource):

    #@jwt_required()
    def post(self):
    
        try:
            data = request.get_json()
            for value in data.values():
                if not isinstance(value, str):
                    return {'error':'400 bad request','message':'validation error. not valid data'}, HTTPStatus.BAD_REQUEST
            
            new_location = Locations(**data)
            db.session.add(new_location)
            db.session.commit()

            return new_location, HTTPStatus.CREATED
        except Exception as e:
            print(e)
            db.session.rollback()

