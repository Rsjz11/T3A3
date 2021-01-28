from main import ma                                                                 # Import serialisation object from main
from models.My_Anime import My_Anime                                                # Import My_Anime model
from schemas.UserSchema import UserSchema                                           # Import UserSchema schema

class My_AnimeSchema(ma.SQLAlchemyAutoSchema):                                       # Automatically generates schema
    class Meta:
        model = My_Anime                                                            # Generates schema from My_Anime model
        users = ma.Nested(UserSchema)                                               # Attaches UserSchema to My_AnimeSchema

my_anime_schema = My_AnimeSchema()                                                  # Schema for a single My_Anime page
my_animes_schema = My_AnimeSchema(many=True)                                        # Schema for multiple My_Anime pages