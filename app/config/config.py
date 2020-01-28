import os


class Config():
    os.environ['EMAIL_USER'] = 'pula0404@gmail.com'
    os.environ['EMAIL_PASS'] = 'Unrealisticsolutions'
    SECRET_KEY = '0e4480cd48ea25e8e0b79cf20d1759a2'
    MONGO_URI = "mongodb://localhost:27017/MaamDB"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_DEBUG = False
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "pula0404@gmail.com"
    MAIL_PASSWORD = "Unrealisticsolutions"
    MAIL_SUPPRESS_SEND = False
    IMAGES_FOLDER = "/static/Images/"
    IMAGES_PATH = "Images/"
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    TESTING = True
    ADMIN_MAILS = ['shaheekanaleem1995@gmail.com']
