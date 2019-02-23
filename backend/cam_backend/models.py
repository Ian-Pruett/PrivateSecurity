from flask import current_app
from Cam_Backend import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    device_registration = db.Column(db.String(8), unique=True)
    email = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    current_location = db.Column(db.String(128))
    phone_num = db.Column(db.String(16), nullable=False)
    firstName = db.Column(db.String(64), nullable=False)
    lastName = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)


class Video(db.Model):
    # __tablename__ = 'videos'
    pass


class Picture(db.Model):
    pass