from main import db                                                                                                                  # db instance created from SQLAlchemy
from sqlalchemy import text
from datetime import datetime 


# create class and table name for tables in database
class My_Anime(db.Model):                                                                                                            # creating a My_Anime class  inheriting from db.model
    __tablename__ = "My_Anime"                                                                                                       # explicitly providing the name of the table

    id = db.Column(db.Integer, primary_key=True)                                                                                     # column id, integer set onto a primary key, must be unique
    anime_title = db.Column(db.String())                                                                                             # anime title, string
    anime_started = db.Column(db.DateTime, default=datetime.fromisoformat)                                                                     # anime started, date
    anime_finished = db.Column(db.DateTime, default=datetime.fromisoformat)                                                          # anime finished, date
    rating /100 = db.Column(db.Integer())                                                                                            # anime rating out of 100, integer
    profile_id_fk = db.Column(db.Integer, db.ForeignKey("profile.id"), nullable=False)                                               # foreign key linked to Profile, integer, must be present

    @classmethod
    def date_filter(cls, year, month, day, user_id):                                                                                 # data filtering function
        sql_query = text("SELECT * FROM  My_Anime WHERE DATE(anime_started) = ':year-:month-:day' and profile_id_fk=':user_id';")    # sql query, anime_started: year, month, day and profile id
        sql_query = text("SELECT * FROM  My_Anime WHERE DATE(anime_finished) = ':year-:month-:day' and profile_id_fk=':user_id';")   # sql query, anime_finished: year, month, day and profile id
        return  db.engine.execute(sql_query, {"year":year, "month": month, "day": day, "user_id": user_id})

    def __repr__(self):
        return f"<My_Anime {self.journal_entry}>"