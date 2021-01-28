from main import db, ma                                                                     # Import the serialization object from database and main
from schemas.UserSchema import UserSchema                                                   # Import UserSchema schema
from models.Profile import Profile                                                          # Import Profile model
from models.ProfileImage import ProfileImage                                                # Import ProfileImage model
from marshmallow.validate import Length                                                     # Import the length class that will allow us to validate the length of the string

class ProfileImageSchema(ma.SQLAlchemyAutoSchema):                                          # Generate schema automatically
    class Meta:
        model = ProfileImage                                                                # Generate schema using ProfileImage model

    filename = ma.String(required=True, validate=Length(min=1))                             # filename, a string of atleast 1 character must be present

profile_image_schema = ProfileImageSchema()                                                 # Schema for a single Profile Image