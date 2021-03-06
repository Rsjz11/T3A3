import os                                                           # Operating System package used to retrieve env variables

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False                          # Documentaion says this should be false unless needed
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024                            # Max size for file uplaod
    JWT_SECRET_KEY = "anime"                                        # Key used for development


    @property
    def AWS_ACCESS_KEY_ID(self):                                    # This is a function that will be used for all envs
        value = os.getenv("AWS_ACCESS_KEY_ID")                      # Retrieve the AWS_ACCESS_KEY_ID for IAM from the .env file.
        if not value:
            raise ValueError("AWS_ACCESS_KEY_ID is not set")        # Raise error if it is not set
        return value


    @property
    def AWS_SECRET_ACCESS_KEY(self):                                # This is a function that will be used for all envs
        value = os.getenv("AWS_SECRET_ACCESS_KEY")                  # Retrieve the AWS_SECRET_ACCESS_KEY for IAM from the .env file.
        if not value:
            raise ValueError("AWS_SECRET_ACCESS_KEY is not set")    # Raise error if it is not set
        return value


    @property
    def AWS_S3_BUCKET(self):                                        # This is a function that will be used for all envs
        value = os.getenv("AWS_S3_BUCKET")                          # Retrieve the AWS_S3_BUCKET for IAM from the .env file.
        if not value:
            raise ValueError("AWS_S3_BUCKET is not set")            # Raise error if it is not set
        return value


    @property
    def SQLALCHEMY_DATABASE_URI(self):                                                                                                                  # This is a function that will be used for all envs
        value = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"                # Retrieve the DB_URI from the .env file to connect to DB
        if not value:
            raise ValueError("DB_URI is not set")                                                                                                       # Raise error if it is not set
        return value    


class DevelopmentConfig(Config):                                    # Inherits from config
    DEBUG = True                                                    # Adds in the debugging mode for development
    

class ProductionConfig(Config):                                     # Inherits from config
    @property
    def JWT_SECRET_KEY(self):
        value = os.getenv("JWT_SECRET_KEY")                         # Use the production JWT secret
        if not value:
            raise ValueError("JWT Secret Key is not set")           # If no JWT then raise "JWT Secret Key is not set" error

        return value                                                # Rrturn the JWT

class TestingConfig(Config):                                        # Inherits from config
    TESTING = True                                                  # Adds in the testing env-var

class WorkflowConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


environment = os.getenv("FLASK_ENV")                                # Retrieve the the flask env variable

if environment == "production":                                     # If the flask env variable is production
    app_config = ProductionConfig()                                 # Then use the production config
elif environment == "testing":                                      # If the flask env variable is testing
    app_config = TestingConfig()                                    # Then use the testing config
elif environment == "workflow":                                     # If the flask env variable is workflow
    app_config = WorkflowConfig()                                   # Then use the workflow config
else:
    app_config = DevelopmentConfig()                                # Else use the development config