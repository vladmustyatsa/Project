from flask import redirect, url_for, request, render_template, abort
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

@app.route('/test')
def test():
	return render_template('test.html')
