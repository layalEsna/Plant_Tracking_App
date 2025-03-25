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
class Signup(Resource):
    def post(self):

        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        confirmed_password = data.get('confirmed_password')

        if not all([username, password, confirmed_password]):
            return {'error': 'All fields are required.'}, 400
        if User.query.filter(User.username == username).first():
            return {'error': 'Username already exists.'}, 400
        if password != confirmed_password:
            return {'error': "Password doesn't match"}, 400
        
        new_user = User(
            username = username,
            password =password,
        )
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        session.permanent = True 

        return jsonify({
            'username': new_user.username,
            'id': new_user.id
        }), 201
    
class UserById(Resource):
    def get(self, user_id):
        user_session_id = session.get('user_id')
        if user_session_id is None or user_session_id != user_id:
            return {'error': 'Unauthorized or user not found.'}, 403
        user = User.query.get(user_id)
        if not user:
            return {'error': 'User not found.'}, 404
        user_schema = UserSchema()
        return jsonify(user_schema.dump(user)), 200
        

        
api.add_resource(Signup, '/signup')
api.add_resource(UserById, '/users/<int:user_id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)


# # python server/app.py