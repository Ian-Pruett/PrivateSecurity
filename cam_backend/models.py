from flask import current_app
from cam_backend import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    device_registration = db.Column(db.String(8), unique=True)
    email = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    phone_num = db.Column(db.String(16), nullable=False)
    firstName = db.Column(db.String(64), nullable=False)
    lastName = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    status = db.Column(db.Boolean)