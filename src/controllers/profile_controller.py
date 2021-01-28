
from main import db                                                    # This is the db instance created by SQLAlchemy
from flask import Blueprint, request, jsonify, abort                   # Import flask and various sub packages
from schemas.ProfileSchema import profile_schema, profiles_schema      # Importing the Profile Schema
from schemas.My_AnimeSchema import My_Animes_schema, My_Anime_schema   # Importing the My_Anime Schema
from flask_jwt_extended import jwt_required, get_jwt_identity          # Packages for authorization via JWTs
from models.Profile import Profile                                     # Importing the Profile Model
from models.User import User                                           # Importing the User Model
from models.My_Anime import My_Anime                                   # Importing the My Anime model
from sqlalchemy import text                                            # Importing text from SQLAlchemy

profiles = Blueprint("profiles", __name__, url_prefix="/profile")      # Creating the profile blueprint 


@profiles.route("/", methods=["POST"])                                 
@jwt_required                                                          # JWT token is required for this route
@verify_user                                                           # Auth service to make sure the correct user owns this profile
def profile_create(user):                                              

    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return abort(401, description="Do I know you?")
    
    profile_fields = profile_schema.load(request.json)
    is_profile = Profile.query.get(user.id)

    if not is_profile:
    
        new_profile = Profile()
        new_profile.username = profile_fields["username"]
        new_profile.fname = profile_fields["fname"]
        new_profile.lname = profile_fields["lname"]
        
        user.profile_id.append(new_profile)                           # user = defined above; client_id is linked as relationship to user: client_id = db.relationship("Client", backref=backref("users", uselist=False)) in users table
        
        db.session.add(new_profile)
        db.session.commit()
        
        return jsonify(client_schema.dump(new_profile))
    
    else:
        return abort(401, description='Profile already exists')

@profiles.route("/", methods=["GET"])
@jwt_required
def get_profile_details():                                            # function that returns profile details
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid profile")

    details = Profile.query.filter_by(id=user.id).first()

    return jsonify(profile_schema.dump(details))

@profiles.route("/", methods=["PUT", "PATCH"])
@jwt_required
def profile_details_update():
    user_id = get_jwt_identity()                                    # Update a journal entry
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid profile")

    details = Profile.query.filter_by(id=user.id)
    detail_fields = profile_schema.load(request.json)
    details.update(detail_fields)
    db.session.commit()
    return jsonify(detail_fields)



@profiles.route("/", methods=["GET"])                                  
def profile_index():                                                   
                                                      
    profiles = Profile.query.options(joinedload("user")).all()         # Retrieving all profiles from the db
    return jsonify(profiles_schema.dump(profiles))                     # Returning all the profiles in json

    
