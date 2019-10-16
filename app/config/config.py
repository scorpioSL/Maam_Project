import os
class Config():
	os.environ['EMAIL_USER'] = ''
	os.environ['EMAIL_PASS'] = ''
	SECRET_KEY = '0e4480cd48ea25e8e0b79cf20d1759a2'
	MONGO_URI = "mongodb://localhost:27017/MaamDB"
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
	IMAGES_FOLDER = "/static/Images/"
	ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
	TESTING = True