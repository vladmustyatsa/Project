class Configuration:
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:1@localhost/project"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = '1'
	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'sha512_crypt' 
    