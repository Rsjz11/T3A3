from main import db                                             # This is the db instance created by SQLAlchemy
from flask import Blueprint                                     # Use blueprints instead of passing the app object around 

db_commands = Blueprint("db-custom", __name__)                  # Creating the blueprint

@db_commands.cli.command("drop")                                # this function will run when "flask db-custom drop" is run"
def drop_db():
    db.drop_all()                                               # Drop all tables  
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")  # Drop table for migrations
    print("Tables deleted")                                     # Print message to indicate tables are dropped



@db_commands.cli.command("seed")                                # this function will run when "flask db-custom seed" is run"
def seed_db():                                                  # Models are connected to the commands below
    from models.User import User                                # Importing the User model
    from models.Profile import Profile                          # Importing the Profile model
    from models.My_Anime import My_Anime                        # Importing My_Anime model
    from models.ProfileImage import ProfileImage                # Importing ProfileImage model
    from main import bcrypt                                     # Hashing module for the passwords
    from faker import Faker                                     # Importing the faker module for fake data
    import random                                               # Importing random from the python standard library

    faker = Faker()
    users = []

    for i in range(5):                                                           # Do this 5 times
        user = User()                                                           # Create an user object from the User model
        user.email = f"test{i+1}@test.com"                                      # Assign an email to the user object
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8") # Assign ta hashed password to the user object
        db.session.add(user)                                                    # Add the user to the db session
        users.append(user)                                                      # Append the user to the users list
        print(user)

    db.session.commit()                                                         # Commit the seeion to the db 

    Profiles = []

    for i in range(1,6):
        client = Client()
        client.username = f"username{i}"
        client.fname = f"firstname{i}"
        client.lname = f"lastname{i}"
        clients.append(client)
        client.user_id = users[i-1].id
        db.session.add(client)
        print(client)

    db.session.commit()  

    for i in range(1, 11):
        anime = My_Anime()
        anime.anime_titles = faker.catch_phrase()
        anime.profile_id_fk = random.choice(profiles).id
        db.session.add(anime)

    db.session.commit()
    print("Tables seeded")