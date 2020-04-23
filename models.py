from flask_security import UserMixin, RoleMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)#
    email = db.Column(db.String(255), unique=True)#
    nickname = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(255))#
    about_me = db.Column(db.String(1000))
    avatar = db.Column(db.String(100))
    active = db.Column(db.Boolean())#


    ownprojects = db.relationship('Project', backref='admin', lazy='dynamic')


    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)


    @hybrid_property
    def roles(self):
        return []

    @roles.setter
    def roles(self, role):
        pass


project_subscribers = db.Table('project_subscribers',
                      db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
                      )

project_members = db.Table('project_members',
                      db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
                      )

project_tags = db.Table('project_tags',
                      db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
                      db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                      )


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    team_name = db.Column(db.String(16), unique=True)
    project_name = db.Column(db.String(80), unique=True)
    about = db.Column(db.String(1000))
    create_date = db.Column(db.DateTime)
    avatar = db.Column(db.String(100))
    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subscribers = db.relationship('User', secondary=project_subscribers, backref=db.backref('subscriptions',lazy='dynamic'))
    members = db.relationship('User', secondary=project_members, backref=db.backref('myprojects',lazy='dynamic'))
    tags = db.relationship('Tag', secondary=project_tags, backref=db.backref('projects',lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args,**kwargs)
        self.create_date = datetime.now()
        


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    
    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args,**kwargs)
        self.name = self.name.replace('#','')
