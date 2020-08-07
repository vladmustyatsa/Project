import view
from app import app


if __name__ == "__main__":
	if app.config['MAIL_PASSWORD']:
		app.run()
	else:
		print(f'MAIL_PASSWORD={app.config["MAIL_PASSWORD"]}\nEnter MAIL_PASSWORD as environment variable')