import os
from flask import redirect, url_for, request, render_template, abort
from flask import send_from_directory, make_response
from flask_security import current_user, logout_user
from flask_login import login_required
from flask_wtf import Form
from app import app, db
from models import User
from forms import ExtendedRegisterForm
from additional import randomString, get_ending

@app.route('/')
def index():
	return render_template('home.html')

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html'), 404

@app.route('/change-user')
def change_user():
	logout_user()
	return redirect(url_for('security.login'))

@app.route('/users/<username>')
def get_profile(username):
	user = User.query.filter(User.nickname==username).first()
	if not user:
		abort(404)
	nickname = user.nickname
	about = user.about_me
	avatar_file = user.avatar
	return render_template('profile.html',nickname=nickname,about=about,avatar_file=avatar_file)

@login_required
@app.route('/edit',methods=['GET','POST'])
def edit():
	if request.method == 'POST':
		status = request.form.get('status')
		user = User.query.filter(User.nickname==current_user.nickname).first()
		if status == 'for_avatar':
			avatar_file = request.files['avatar_file']
			filename = f'avatars/{randomString(20)}{get_ending(avatar_file.filename)}'
			print(f"[DEBUG]::{app.config['UPLOAD_FOLDER']}")
			avatar_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

			

			os.remove(os.path.join(app.config['UPLOAD_FOLDER'],f"avatars/{user.avatar.replace('/static/avatars','')}"))
			user.avatar = url_for('static',filename=filename)
			db.session.commit()
			print('[INFO] :: Success setting new avatar')
			return make_response({'filename' : filename}, 200)
		else:
			form = ExtendedRegisterForm(request.form)
			is_nick_edit = False
			is_email_edit = False
			if user.nickname != request.form['nickname']:
				is_nick_edit = True 
			if user.email != request.form['email']:
				is_email_edit = True 
			is_valid = True
			validation = Form.validate(form)
			form.password.errors.clear()
			form.password_confirm.errors.clear()
			'''if not validation:
				is_valid = False'''
			if form.email.errors != []:
				is_valid = False
			if not form.nick_validate(is_nick_edit):
				is_valid = False
			if not form.email_validate(is_email_edit):
				is_valid = False
			if not form.about_me_validate():
				is_valid = False
			print(f'[DEBUG]::is_nick_edit:{is_nick_edit}')
			print(f'[DEBUG]::is_email_edit:{is_email_edit}')


			if is_valid:
				print('[INFO]::IS VALID EDIT')
				user.nickname = form.nickname.data
				user.email =  form.email.data
				user.about_me =  form.about_me.data
				db.session.commit()
				return redirect(url_for('get_profile',username=user.nickname))
			else:
				nickname = current_user.nickname
				email = current_user.email
				avatar_path = current_user.avatar
				print(f'[DEBUG]:: {avatar_path}')
				about_me = current_user.about_me
				
				return render_template('edit_profile.html',
					form=form,
					nickname=nickname,
					email=email,
					avatar_path=avatar_path,
					about_me=about_me
				)


	form = ExtendedRegisterForm()
	nickname = current_user.nickname
	email = current_user.email
	avatar_path = current_user.avatar
	print(f'[DEBUG]:: {avatar_path}')
	about_me = current_user.about_me
	
	print(f'[DEBUG]::input about {about_me}')
	return render_template('edit_profile.html',
		form=form,
		nickname=nickname,
		email=email,
		avatar_path=avatar_path,
		about_me=about_me
	)


#---------------------------------

@app.route('/p')
def index1():
	return render_template('base.html')

@app.route('/test', methods=['GET','POST'])
def test():
	if request.method == 'POST':
		avatar_file = request.files['avatar_file']
		filename = avatar_file.filename
		avatar_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		print('[INFO] :: Success')
		return make_response({'filename' : filename}, 200)
	return render_template('test.html')
