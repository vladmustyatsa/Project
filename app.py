from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_security import Security, SQLAlchemyUserDatastore
from config import Configuration


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