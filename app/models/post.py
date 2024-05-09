from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime
from flask import current_app


from app import db
class Post(db.Model):
    #__tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # , nullable=False
    # author = default=current_user.id

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"