import re
import os
from flask import request, url_for, request
from flask_wtf import Form
from flask_wtf.file import FileAllowed
from flask_security.forms import RegisterForm, Required
from wtforms import StringField, TextAreaField, FileField, validators
from wtforms_alchemy import Unique, ModelForm # for checking wheather in appenv
from app import app
from models import User

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
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
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
