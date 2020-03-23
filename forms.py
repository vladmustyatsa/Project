from flask_wtf import Form
from flask_security.forms import RegisterForm, Required
from wtforms import StringField, TextAreaField, FileField, validators
from wtforms_alchemy import Unique, ModelForm
from models import User

class ExtendedRegisterForm(RegisterForm):
    email =  StringField('Email',[Required()])
    nickname = StringField('Nickname', [Required()])
    about_me = TextAreaField('About')
    avatar = FileField('Avatar')
    def validate(self):
        """ Add nicknae validation
        
            :return: True is the form is valid
        """
        # Use standart validator

        validation = Form.validate(self)
        is_valid = True
        if not validation:
           return is_valid
        print(self.email.errors)
        if 'Invalid email address' not in self.email.errors:

	        if '@' not in self.email.data:
	        	self.email.errors.append('Invalid email')
	        	is_valid = False
	        	#return False
	        
	        else:
	        	smtp_server = self.email.data[self.email.data.index('@'):]
	        	print(smtp_server)
	        	if '.' not in smtp_server or len(smtp_server) == 2 or smtp_server[:smtp_server.index('.')]:
	        		print('asdasd')
	        		self.email.errors.append('Invalid email')
	        		is_valid = False
	        		#return False
        	
        if len(self.nickname.data) > 16:
        	self.nickname.errors.append('Nickname is too long')
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

        filename = self.avatar.data
        if filename:
        	end = filename[::-1][:filename[::-1].index('.')]
        	end = end[::-1]
        	if end not in ['png','jpg','jpeg','gif']:
        		self.avatar.errors.append('Inappropriate format')
        		is_valid = False
        		#return False

        return is_valid
