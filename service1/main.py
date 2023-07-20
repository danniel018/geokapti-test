from flask import Flask
from flask_restful import  Api
import os
from config import Production, Development
from resources import LocationsResource
from extensions import db


env = os.environ.get('ENV', 'Development')
if env == 'Production':
    config = Production()
else:
    config = Development()
    

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
api = Api(app)
api.add_resource(LocationsResource,'/locations') 




if __name__ == "__main__":
    app.run()