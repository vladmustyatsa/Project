from flask_security import UserMixin, RoleMixin
from sqlalchemy.ext.hybrid import hybrid_property
from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    nickname = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(255))
    about_me = db.Column(db.String(500))
    avatar = db.Column(db.String(100))
    active = db.Column(db.Boolean())

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)


    @hybrid_property
    def roles(self):
        return []

    @roles.setter
    def roles(self, role):
        pass