from flask import redirect, url_for, request
from flask_security import current_user, logout_user
from app import app

@app.route('/')
def index():
	try:
		return str(current_user.nickname)
	except:
		return 'logout'

@app.route('/change-account')
def change_account():
	logout_user()
	return redirect(url_for('security.login'))
