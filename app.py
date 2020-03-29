from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_security import Security, SQLAlchemyUserDatastore, current_user
from config import Configuration
from flask_admin import Admin
from admin import HomeAdminView, UserAdminView
from flask_mail import Mail


# App
app = Flask(__name__)
app.config.from_object(Configuration)
def is_login():
	try:
		return current_user.nickname
	except:
		return ''
	
		

app.jinja_env.globals.update(is_login=is_login)

# DateBase
db = SQLAlchemy(app)
from forms import ExtendedRegisterForm
# Migration
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import User
# Security
user_datastore = SQLAlchemyUserDatastore(db, User, None)
security = Security(app, user_datastore,register_form=ExtendedRegisterForm)

# Admin
admin = Admin(app, 'MyApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(UserAdminView(User, db.session))

# Mail
mail = Mail(app)

