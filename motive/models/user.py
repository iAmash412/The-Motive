from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    email = db.Column(db.String(500), unique=True)
    password = db.Column(db.String(255), nullable=False)
#     reviews = db.relationship("Reviews")


# class Reviews(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
