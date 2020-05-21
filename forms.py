import re
import os
from flask import request, url_for, request
from flask_wtf import Form, FlaskForm
from flask_wtf.file import FileAllowed
from flask_security.forms import RegisterForm, Required
from wtforms import StringField, TextAreaField, FileField, validators, SelectMultipleField
from wtforms_alchemy import Unique, ModelForm # for checking wheather in appenv
from app import app
from models import User, Tag, Project

class ExtendedRegisterForm(RegisterForm):
    email =  StringField('Email',[Required(),validators.email('Invalid email')])
    nickname = StringField('Nickname', [Required()])
    about_me = TextAreaField('About me')
    avatar = FileField('Avatar')

    def nick_validate(self, is_edit=True):
        print('[DEBUG]:: nick_validate')
        is_valid_nickname = re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,15}$',self.nickname.data)
        is_valid = True
        if not is_valid_nickname:
            self.nickname.errors.append(r"Only letters,ciphers, '-', '_' and '.'<br>(no more than 16 characters)")
            is_valid = False
            #return False

        # Check if nickname already exists       
        user = User.query.filter_by(
            nickname=self.nickname.data).first()
        if user is not None and is_edit:
            
            # Text displayed to the user
            self.nickname.errors.append('Nickname already exists')
            is_valid = False
        
        return is_valid

    def email_validate(self, is_edit=True):
        is_valid = True
        email = User.query.filter_by(
            email=self.email.data).first()
        if email is not None and is_edit:
            # Text displayed to the user
            self.email.errors.append('Email already exists')
            is_valid = False

        return is_valid

    def about_me_validate(self):
        is_valid = True
        if len(self.about_me.data) > 1000:
            self.about_me.errors.append('No more than 1000 characters')
            is_valid = False
        print(f'[DEBUG]::about_me:{self.about_me.data}')
        self.about_me.data = self.about_me.data.replace('\r\n',' ')
        print(f'[DEBUG]::about_me:{self.about_me.data}')
        return is_valid

    def validate(self):
        url = request.url
        url = url.replace(app.config['app_server_name'],'')
        print(f'[INFO] URL: {url}')
        is_valid = True
        # Standart validation
        
        validation = Form.validate(self)
            
        if not validation:
            is_valid = False
        # Nickname validation	
        
        if not self.nick_validate():
            is_valid = False
        # email validation
        
        if not self.email_validate():
            is_valid = False

        # About_me validation
        if not self.about_me_validate():
            is_valid = False


        # Creting default avatar
        if is_valid and url != '/edit':
            filename = self.nickname.data+'.jpg'
            avatar_file = open(os.getcwd()+'/static/avatars/'+filename,'wb')
            default_avatar = open(os.getcwd()+'/static/site-images/'+'default-avatar.jpg','rb')
            avatar_file.write(default_avatar.read())
            avatar_file.close()
            default_avatar.close()
            #self.avatar.data = '/static/avatars/'+filename
            self.avatar.data = url_for('static',filename=f'avatars/{filename}')


        return is_valid


class ProjectForm(FlaskForm):
    team_name =  StringField('Team name',[Required()])
    project_name = StringField('Project name', [Required()])
    about = TextAreaField('About project')
    tags = SelectMultipleField('Tags')
    selected_tags = []

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        tags_from_model = Tag.query.all()
        choices = []
        for tag in tags_from_model:
            choices.append(tuple([tag.name, tag.name]))
        self.tags.choices = choices
        

    def team_name_validate(self, instance):
        is_valid_team_name = re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,15}$',self.team_name.data)
        is_valid = True
        if not is_valid_team_name:
            self.team_name.errors.append(r"Only letters,ciphers, '-', '_' and '.'<br>(no more than 16 characters)")
            is_valid = False
            #return False
        if self.team_name.data == 'create':
            self.team_name.errors.append('Banned name')
            is_valid = False
        # Check if nickname already exists  
        
        project = Project.query.filter_by(
            team_name=self.team_name.data).first()
        if project is not None and (instance == None or instance.team_name != self.team_name.data):
                
            # Text displayed to the user
            self.team_name.errors.append('Project already exists')
            is_valid = False
        print(f'[INFO] :: team_name_validate - {is_valid}')
        return is_valid
    
    def project_name_validate(self):
        is_valid = True
        if len(self.project_name.data) > 80 or len(self.project_name.data) < 6:
            self.project_name.errors.append(r'Name of your project<br>(at least 6 characters and no more than 80 characters)')
            is_valid = False
        return is_valid

    def about_validate(self):
        is_valid = True
        if len(self.about.data) > 1000:
            self.about.errors.append(r'No more than 1000 characters')
            is_valid = False

        print(f'[INFO] :: about_validate - {is_valid}')
        return is_valid

    def validate(self, instance=None):
        url = request.url
        url = url.replace(app.config['app_server_name'],'')
        print(f'[INFO] URL: {url}')
        validation = Form.validate(self)
        is_valid = True
        
        print(f'[INFO]::selected tags :: {self.tags.data}')
        if not self.team_name_validate(instance):
            is_valid = False
        if not self.project_name_validate():
            is_valid = False
        if not self.about_validate():
            is_valid = False

        self.selected_tags = self.tags.data
        return is_valid

