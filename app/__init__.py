#!/usr/bin/python3
""" app """
from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object("config")

# Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
# Bcrypt
bcrypt = Bcrypt(app)
# Mail
mail = Mail(app)

db = SQLA(app)
appbuilder = AppBuilder(app, db.session,
                        base_template='home.html')

from . import views
from app.routes.users import users
from app.routes.posts import posts
from app.routes.main import main
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

db.create_all()