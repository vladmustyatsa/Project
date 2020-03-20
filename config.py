class Configuration:
	DEBUG = True
	SECRET_KEY = '1'

	# SQLAlchemy
	SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:1@localhost/project"
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# Security
	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'sha512_crypt' 
	SECURITY_REGISTERABLE = True
	SECURITY_REGISTER_URL = '/signup'
	SECURITY_LOGIN_URL = '/signin'

	# Mail
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USE_SSL = True
	MAIL_USERNAME = 'vladislavmustyatsa@gmail.com'
	MAIL_PASSWORD = 'Riopara2005'
	MAIL_USE_TLS = False
	#DEFAULT_MAIL_SENDER='Danny from DPC'
	SECURITY_EMAIL_SENDER = 'vladislavmustyatsa@gmail.com'

	#Comment