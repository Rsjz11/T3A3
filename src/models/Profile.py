from main import db                                                                  # This is the db instance created by SQLAlchemy

from models.My_Anime import My_Anime
from models.ProfileImage import ProfileImage

class Profile(db.Model):                                                             # Creating a Profile class inheriting from db.Model
    __tablename__ = "profiles"                                                       # Explicitally providing the name of the table

    id = db.Column(db.Integer, primary_key=True)                                     # Creates a column called id and sets it on the primary key
    username = db.Column(db.String(), nullable=False, unique=True)                   # Profilename, string, must be present, must be unique
    fname = db.Column(db.String(), nullable=False)                                   # Firstname, string, must be present
    lname = db.Column(db.String(), nullable=False)                                   # Lastname, string, must be present
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)       # user_id is an integer and the Foreign key comes from the users table id. It is required
    my_anime_entries = db.relationship(My_Anime, backref="Profile", lazy="dynamic")  # Relationship added: links Profile to My_Anime, adds Profile property, using dynamic to apply additional filters
    profile_image = db.relationship(ProfileImage, uselist=True)                      # Relatonship added: links Profile to ProfileImage

    def __repr__(self):                                                              # Reresentitive state
        return f"<Profile {self.username}>"                                          # When the Profile is printed it now shows the username instead of the id