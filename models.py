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
    ownrequests = db.relationship('ProjectUserRequest', backref='sender', lazy='dynamic')


    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<User #{self.id}, nickname={self.nickname}, email={self.email}>'

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
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                      db.PrimaryKeyConstraint('project_id', 'user_id')
                      )

project_tags = db.Table('project_tags',
                      db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
                      db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                      )


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    team_name = db.Column(db.String(16), unique=True)
    project_name = db.Column(db.String(80))
    about = db.Column(db.String(1000))
    create_date = db.Column(db.DateTime)
    logo = db.Column(db.String(100))
    admin_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subscribers = db.relationship('User', secondary=project_subscribers, backref=db.backref('subscriptions',lazy='dynamic'))
    members = db.relationship('User', secondary=project_members, backref=db.backref('myprojects',lazy='dynamic'))
    tags = db.relationship('Tag', secondary=project_tags, backref=db.backref('projects',lazy='dynamic'))

    requests = db.relationship('ProjectUserRequest', backref='project', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args,**kwargs)
        self.create_date = datetime.now()

    def __repr__(self):
        return f'<Project #{self.id}, team_name={self.team_name}, admin={self.admin}, created at {self.create_date}>\n'

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    
    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args,**kwargs)
        self.name = self.name.replace('#','')

    def __repr__(self):
        return f'<Tag #{self.id}, name={self.name}>'


class ProjectUserRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)   
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    positive_status = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return f'<ProjectUserRequest #{self.id}, \nsender={self.sender}, \nproject={self.project}, \npositive_status={self.positive_status}>\n'

