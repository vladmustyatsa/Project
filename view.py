import os
from flask import redirect, url_for, request, render_template, abort
from flask import send_from_directory, make_response
from flask_security import current_user, logout_user
from app import app
from models import User


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
		return make_response({'filename' : filename}, 200)
	return render_template('test.html')
