# # #!/usr/bin/env python3

# # # Standard library imports

# # # Remote library imports
# # from flask import request
# # from flask_restful import Resource

# # # Local imports
# # from config import app, db, api

# ##################################

# from flask import Flask, request, make_response, jsonify, session
# from flask_cors import CORS
# from flask_migrate import Migrate
# from flask_restful import Api, Resource




# from config import Config  
# from models import db, bcrypt  

# # Instantiate app
# app = Flask(__name__)
# app.config.from_object(Config)

# # Initialize extensions
# db.init_app(app)
# bcrypt.init_app(app)
# migrate = Migrate(app, db)

# # Instantiate REST API
# api = Api(app)
# # Instantiate CORS
# CORS(app)

# # Import models after initializing db to prevent circular imports
# # Add your model imports
# from models import Plant, Category, CareNote, User

# # Views go here!

# @app.route('/')
# def index():
#     return '<h1>Project Server</h1>'


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)


from flask import Flask, request, make_response, jsonify, session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from config import Config  
from models import db, bcrypt  

# Instantiate app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)

# Instantiate REST API
api = Api(app)
# Instantiate CORS
CORS(app)

# Import models after initializing db to prevent circular imports
from models import *
# Plant, Category, CareNote, User

# Views go here!
@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class CheckSession(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user_id:
            return {'error': 'Unauthorized.'}, 401
        
        user_schema = UserSchema()
        return user_schema.dump(user), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)


# # python server/app.py