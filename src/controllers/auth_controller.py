from main import db, bcrypt
from flask import Blueprint, abort, jsonify, request
from flask_jwt_extended import create_access_token
from schemas.UserSchema import user_schema
from datetime import timedelta
from models.User import User


auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/register", methods=["POST"])
def auth_register():
    user_fields = user_schema.load(request.json)
    user = User.query.filter_by(email=user_fields["email"]).first()
    if user:
        return abort(400, description="Email already registered")
    
    user = User()
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")              # utf-8 online tool that is an encoder/decoder

    db.session.add(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))

@auth.route("/login", methods=["POST"])
def auth_login():
    user_fields = user_schema.load(request.json)
    user = User.query.filter_by(email=user_fields["email"]).first()
    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username and password")

    expiry = timedelta(days=1)                                                                         # set the access cookies in the browser that sent the request
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)                    # set_access_cookies(resp, access_token)

    return jsonify({ "token": access_token })                                                  