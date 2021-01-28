from main import db                                                                             # This is the db instance created by SQLAlchemy


class ProfileImage(db.Model):                                                                   
    __tablename__ = "profile_images"                                                            # explicitly providing the name of the table

    id = db.Column(db.Integer, primary_key=True)                                                # creates a column called id, sets it as an integer and links it to a primary key
    filename = db.Column(db.String(), nullable=False, unique=True)                              # profilename, string, must be present
    profile_id = db.Column(db.Integer, db.ForeignKey(".id"), nullable=False)                    # profile id, integer, foreign key, must be present

    def __repr__(self):
        return f"<ProfileImage {self.filename}>"