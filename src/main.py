
# Loading environment variables
from dotenv import load_dotenv                              # Package to access environment variables
load_dotenv()                                               # Retrieve the env variables from .env

# Flask application creation
from flask import Flask, jsonify                            # Import flask class and jsonify to send responses in JSON format
from marshmallow.exceptions import ValidationError          # Raises an error when validation fails on a field
from flask_sqlalchemy import  SQLAlchemy                    # This is the ORM
from flask_marshmallow import Marshmallow                   # Importing the Marshmallow class
from flask_bcrypt import Bcrypt                             # Hashing package
from flask_jwt_extended import JWTManager                   # Retrieves information form JWT
from flask_migrate import Migrate                           # Package to handle migrations

# Tools used in other files
db = SQLAlchemy()                                           # New instance of SQLAlchemym named db
ma = Marshmallow()                                          # New instance of marshmallow named ma. This is for serialization
bcrypt = Bcrypt()                                           # New instance of Bcrypt, Hashing package
jwt = JWTManager()                                          # New instance of JWT Manager
migrate = Migrate()                                         # Makes new instance of migrate

def create_app():
    app = Flask(__name__)                                   # Creating an instnace of Flask named app
    app.config.from_object('default_settings.app_config')   # Loads the configuration for the app object from default_settings.py
    # # Configure application to store JWTs in cookies
    # app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    # app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
    # app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
    # app.config['JWT_COOKIE_CSRF_PROTECT'] = True

    # register db and marshmallow on app 
    db.init_app(app)                                        # This is gives these packages context to the correct 'app' object
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db) 

    from commands import db_commands                        # Imports db_commands so they can be registered
    app.register_blueprint(db_commands)                     # Registering db_commands blueprint with app

    # Constroller registration
    from controllers import registerable_controllers        # Import the registerable_controllers blueprint so it can be registered
    for controller in registerable_controllers:
        app.register_blueprint(controller)                  # Register each controller with app
    
    # Error handler for bad 400 requests
    @app.errorhandler(ValidationError)                      # Inherits from Marshmallow ValidationError
    def handle_bad_request(error):  
        return(jsonify(error.messages), 400)               

    # Error handler for server errors 500
    @app.errorhandler(500)                                  
    def handle_500(error):
        app.logger.error(error)
        return ("Server error", 500)

    return app                                              # Return the app object