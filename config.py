class Configuration:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:1@localhost/project"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1'