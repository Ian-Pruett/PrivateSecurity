from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from Cam_Backend.config import DefaultConfig


db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(config_class=DefaultConfig):
    app = Flask(__name__)
    app.config.from_object(DefaultConfig)
    return app