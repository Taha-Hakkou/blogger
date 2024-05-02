from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime
import uuid
from itsdangerous import URLSafeTimedSerializer as Serializer

from flask import current_app
from flask_login import UserMixin


###
from app import login_manager
@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)
###

from app import db
class User(UserMixin, Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)#, default=str(uuid.uuid4()))
    username = db.Column(db.String(20), unique=True, nullable=False, default='username')
    email = db.Column(db.String(120), unique=True, nullable=False, default='username@home.xyz')
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False, default='password')
    posts = db.relationship('Post', backref='author', cascade='all, delete, delete-orphan')#, lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return db.session.query(User).get(user_id)
