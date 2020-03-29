from flask import redirect, url_for, request, render_template
from flask_security import current_user, logout_user
from app import app

@app.route('/')
def index():
	return render_template('home.html')
@app.route('/base')
def base():
	return render_template('signin.html')

@app.route('/change-user')
def change_user():
	logout_user()
	return redirect(url_for('security.login'))

@app.route('/p')
def index1():
	return render_template('base.html')

@app.route('/test')
def test():
	return render_template('test.html')
