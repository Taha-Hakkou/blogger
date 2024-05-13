#!/usr/bin/python3
""" config """
import os
from flask_appbuilder.security.manager import AUTH_DB


basedir = os.path.abspath(os.path.dirname(__file__))

# App secret key
SECRET_KEY = "bloggerbloggerblogger"

# --------------------------------
# MYSQL ENVIRONMENT VARIABLES
# --------------------------------
BLOGGER_MYSQL_USER = 'root'
BLOGGER_MYSQL_PWD = os.environ.get('BLOGGER_MYSQL_PWD')
BLOGGER_MYSQL_HOST = 'localhost'
BLOGGER_MYSQL_DB = 'blogger_dev_db'

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(BLOGGER_MYSQL_USER,
                                                       BLOGGER_MYSQL_PWD,
                                                       BLOGGER_MYSQL_HOST,
                                                       BLOGGER_MYSQL_DB)

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# ------------------------------
# GLOBALS FOR APP Builder
# ------------------------------
# APP_NAME = "My App Name"
# APP_ICON = "static/img/logo.jpg"

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
AUTH_TYPE = AUTH_DB

# Uncomment to setup Full admin role name
AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Public"

# to remove some warnings !
SQLALCHEMY_TRACK_MODIFICATIONS = False

# ---------------------------------------------------
# Image and file configuration
# ---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload url, when using models with images
IMG_UPLOAD_URL = "/static/uploads/"
# Setup image size default is (300, 200, True)
# IMG_SIZE = (300, 200, True)

# ----------------------------------------------------
# Email server
# ----------------------------------------------------
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'taha.hakkou42@gmail.com' #os.environ.get('EMAIL_USER')
MAIL_PASSWORD = os.environ.get('EMAIL_PASS')