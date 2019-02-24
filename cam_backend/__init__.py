from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from cam_backend.config import DefaultConfig


db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(config_class=DefaultConfig):
    from cam_backend.models import User
    app = Flask(__name__)
    app.config.from_object(DefaultConfig)

    bcrypt.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from cam_backend.users.routes import users
    app.register_blueprint(users)
    
    return app