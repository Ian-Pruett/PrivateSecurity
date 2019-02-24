from flask import request, jsonify, Blueprint
from cam_backend import db, bcrypt
from cam_backend.models import User
from geopy.geocoders import Nominatim
import urllib
import certifi


users = Blueprint('users', __name__)


def uo(args, **kwargs):
    return urllib.request.urlopen(args, cafile=certifi.where(), **kwargs)


def convert_coordinates(addr):
    geolocator = Nominatim()
    geolocator.urlopen = uo
    location = geolocator.geocode(addr)
    return location.latitude, location.longitude


@users.route('/create', methods=['GET', 'POST'])
def create():
    print(request.json)
    user = User(**request.json)
    pw_hash = bcrypt.generate_password_hash(user.password).decode('utf-8')
    user.password = pw_hash
    user.latitude, user.longitude = convert_coordinates(user.address)
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    return jsonify({'status': 1}), 200


@users.route('/login', methods=['GET', 'POST'])
def login():
    print(request.json)
    r = request.json
    email = r.get('email')
    password = r.get('password')
    query = User.query.filter_by(email=email).first()
    if bcrypt.check_password_hash(query.password, password):
        return jsonify({
            'status': 1, 
            'firstName': query.firstName, 
            'lastName': query.lastName,
            'email': query.email
        }), 200
    else:
        return jsonify({'status': 2, 'user': None}), 200


@users.route('/update-location', methods=['POST'])
def update_location():
    print(request.json)
    r = request.json
