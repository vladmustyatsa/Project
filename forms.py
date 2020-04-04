import re
import os
from flask import request, url_for
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
    def validate(self):

        validation = Form.validate(self)
        is_valid = True
        if not validation:
           is_valid = False
        	
        is_valid_nickname = re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,15}$',self.nickname.data)
        if not is_valid_nickname:
            self.nickname.errors.append(r"Only letters,ciphers, '-', '_' and '.'<br>(no more than 16 characters)")
            is_valid = False
        	#return False
        # Check if nickname already exists       
        user = User.query.filter_by(
            nickname=self.nickname.data).first()
        if user is not None:
            # Text displayed to the user
            self.nickname.errors.append('Nickname already exists')
            is_valid = False
            #return False
        email = User.query.filter_by(
            email=self.email.data).first()
        if email is not None:
            # Text displayed to the user
            self.email.errors.append('Email already exists')
            is_valid = False

        if len(self.about_me.data) > 1000:
            self.about_me.errors.append('No more than 1000 characters')
            is_valid = False

        if is_valid:
            filename = self.nickname.data+'.jpg'
            avatar_file = open(os.getcwd()+'/static/avatars/'+filename,'wb')
            default_avatar = open(os.getcwd()+'/static/site-images/'+'default-avatar.jpg','rb')
            avatar_file.write(default_avatar.read())
            avatar_file.close()
            default_avatar.close()
            #self.avatar.data = '/static/avatars/'+filename
            self.avatar.data = url_for('static',filename=f'avatars/{filename}')

        '''if self.password.data != self.password_confirm.data:
            self.password_confirm.errors.append('Not equals')
            is_valid = False'''

        '''avatar_file = request.files.get('avatar')

        if avatar_file:
            is_valid_fileformat = re.search(r'([^\s]+(\.(?i)(jpg|png|gif|bmp|jpeg))$)',avatar_file.filename)
            if not is_valid_fileformat:
                self.avatar.errors.append('Inapropriate format')
                is_valid = False
            elif is_valid:
                filename = avatar_file.filename
                filename = filename[::-1]
                ending = filename[:filename.index('.')+1]
                ending = ending[::-1]
                filename = self.nickname.data + ending
                avatar_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                self.avatar.data = url_for('static', filename=filename)'''


        return is_valid
