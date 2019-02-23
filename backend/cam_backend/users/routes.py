from flask import request, Blueprint
from Cam_Backend import db, bcrypt
from Cam_Backend.models import User

users = Blueprint('users', __name__)

# TODO adds a user to database
@users.route('/create', methods=['GET', 'POST'])
def create():
    pass


# TODO logs a user into app and returns user info
@users.route('/login', methods=['GET', 'POST'])
def login():
    pass

# TODO check and evaluate current location of user
@users.route('/update-location', methods=['POST'])
def update_location():
    pass
