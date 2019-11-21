from flask import Flask
from flask_bcrypt import Bcrypt
from flask import*
from app.config.config import Config
from flask_login import LoginManager
from app.database.models import User

# Creating Flask Object
app = Flask(__name__)
# BCrypt Object For Encrypting Data
bcrypt = Bcrypt(app)

# Login Manager Object
login_manager = LoginManager(app)
login_manager.login_view = 'Authentication.login'
login_manager.login_message_category  = 'info'

# User Loader For Login Operation
@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

##Configurations for the server from a seperate file
app.config.from_object(Config)

from app.Routes.Authentication.route import admin
from app.Routes.Website.route import website
from app.Routes.Posts.route import posts
from app.Routes.Vacancy.route import vacancy
from app.Routes.Product.route import product
from app.Routes.Request.route import request
from app.Routes.Feedback.route import feedback
from app.Routes.GetBasicData.route import GetBasicData
##Register Blue print
app.register_blueprint(admin)
app.register_blueprint(website)
app.register_blueprint(posts)
app.register_blueprint(vacancy)
app.register_blueprint(product)
app.register_blueprint(request)
app.register_blueprint(feedback)
app.register_blueprint(GetBasicData)