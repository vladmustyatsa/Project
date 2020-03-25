import re
import os
from flask import request, url_for
from flask_wtf import Form
from flask_wtf.file import FileAllowed
from flask_security.forms import RegisterForm, Required
from wtforms import StringField, TextAreaField, FileField, validators
from wtforms_alchemy import Unique, ModelForm
from app import app
from models import User

class ExtendedRegisterForm(RegisterForm):
    email =  StringField('Email',[Required(),validators.email('Invalid email')])
    nickname = StringField('Nickname', [Required()])
    about_me = TextAreaField('About')
    avatar = FileField('Avatar')
    def validate(self):

        validation = Form.validate(self)
        is_valid = True
        if not validation:
           is_valid = False
        	
        is_valid_nickname = re.search(r'^[a-zA-Z][a-zA-Z0-9-_\.]{1,15}$',self.nickname.data)
        if not is_valid_nickname:
            self.nickname.errors.append('Invalid nickname')
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

        avatar_file = request.files.get('avatar')

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
                self.avatar.data = url_for('static', filename=filename)


        return is_valid