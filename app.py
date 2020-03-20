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

# DateBase
db = SQLAlchemy(app)

# Migration
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import User
# Security
user_datastore = SQLAlchemyUserDatastore(db, User, None)
security = Security(app, user_datastore)

# Admin
admin = Admin(app, 'MyApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(UserAdminView(User, db.session))

# Mail
mail = Mail(app)