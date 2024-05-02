import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

"""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
db.init_app(app)
"""

# bcrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# login_manager
from flask_login import LoginManager

# mail
"""
from flask_mail import Mail
mail = Mail()
"""

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")

bcrypt.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.init_app(app)
"""
mail.init_app(app)
"""

db = SQLA(app)
appbuilder = AppBuilder(app, db.session, base_template='home.html')


from . import views

from app.routes.users import users
from app.routes.posts import posts
from app.routes.main import main
from app.errors.handlers import errors
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)