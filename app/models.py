from datetime import datetime
from app import db

class User(db.Model):  # db.Model - base class for all models from Flask-SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)  # fields are created as instances of the db.Column class
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')  # relationship between users and posts

    def __repr__(self):  # method that tells Python how to print objects of this class
        return '<User {}>'.format(self.username)

class Post(db.Model):  # class represents blog posts written by users
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # timestamp field, indexed
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # foreign key to user.id (from another table)

    def __repr__(self):
        return '<Post {}>'.format(self.body)