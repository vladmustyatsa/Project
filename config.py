import os


class Configuration:
	DEBUG = True
	app_server_name = 'http://localhost:5000'
	SECRET_KEY = '1'
	UPLOAD_FOLDER = os.getcwd() + '/static'
	# SQLAlchemy
	SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:1@localhost/project"
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# Security
	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'sha512_crypt' 
	SECURITY_REGISTERABLE = True
	SECURITY_REGISTER_URL = '/signup'
	SECURITY_LOGIN_URL = '/signin'
	SECURITY_CHANGEABLE = True
	SECURITY_CHANGE_URL = '/change-password'

	# Mail
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = 'takestart.mail@gmail.com'
	MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
	MAIL_USE_TLS = False
	#DEFAULT_MAIL_SENDER='Danny from DPC'
	SECURITY_EMAIL_SENDER = 'takestart.mail@gmail.com'

	#Comment