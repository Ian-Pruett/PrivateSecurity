from flask import request, jsonify, Blueprint
from cam_backend import db, bcrypt
from cam_backend.models import User
from geopy.geocoders import Nominatim
from geopy.distance import geodesic, great_circle
import urllib
import certifi


users = Blueprint('users', __name__)


def uo(args, **kwargs):
    return urllib.request.urlopen(args, cafile=certifi.where(), **kwargs)


def geolocation(addr):
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
    location = geolocation(user.address)
    if location is None:
        return jsonify({
            'status': 0,
            'validAddress': False,
            'validPhoneNumber': True,
            'validEmail': True,
            'user': None
            }), 200
    user.latitude, user.longitude = location.latitude, location.longitude
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    return jsonify({
        'status': 1,
        'validAddress': True,
        'validPhoneNumber': True,
        'validEmail': True,
        'user': jsonify(row_to_user(user))
        }), 200


@users.route('/login', methods=['GET', 'POST'])
def login():
    print(request.json)
    r = request.json
    email = r.get('email')
    password = r.get('password')
    query = User.query.filter_by(email=email).first()
    if bcrypt.check_password_hash(query.password, password):
        return jsonify(row_to_user(query)), 200
    else:
        return jsonify({'status': 2, 'user': None}), 200


@users.route('/update-location', methods=['POST'])
def update_location():
    print(request.json)
    r = request.json
    user = User.query.get(r.id)
    current = (r.latitude, r.longitude)
    home = (user.latitude, user.longitude)  
    dist = min(geodesic(current, home).miles, 
        great_circle(current, home).miles)
    if dist >= 1:
        user.status = False
    else:
        user.status = True
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    return jsonify({'status': 1}), 200
    
     
def row_to_user(row):
    return {
        'status': 1,
        'id': row.id,
        'device_registration': row.device_registration,
        'email': row.email,
        'address': row.address,
        'phone_num': row.phone_num,
        'firstName': row.firstName,
        'lastName': row.lastName,
    }