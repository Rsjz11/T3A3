from main import db, ma                                                                     # Import the serialization object from database and main
from schemas.UserSchema import UserSchema
from models.Profile import Profile
from models.ProfileImage import ProfileImage
from marshmallow.validate import Length

class ProfileImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProfileImage

    filename = ma.String(required=True, validate=Length(min=1))

profile_image_schema = ProfileImageSchema()