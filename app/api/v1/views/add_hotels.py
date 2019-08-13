import json
from flask import make_response, jsonify, request, Blueprint
from app.api.v1.models.add_hotels import HotelsModel
from app.api.v1.models.users_model import UsersModel
from utils.v1.validations import check_hotels_keys, raise_error, convert_to_int
from flask_jwt_extended import jwt_required

hotels_v1 = Blueprint('hotels_v1', __name__)


@hotels_v1.route('/hotels', methods=['POST'])
@jwt_required
def add_hotel():
    """A registered user can book a hotel."""
    errors = check_hotels_keys(request)
    if errors:
        return raise_error(400, "Invalid {} key".format(', '.join(errors)))
    details = request.get_json()
    name = details['name']
    location = details['location']
    lodges = details['lodges']
    conference_rooms = details['conference_rooms']
    img_url = details['img_url']
    category = details['category']

    hotel = HotelsModel(name, location, lodges, conference_rooms, img_url, category).save()
    hotel = json.loads(hotel)
    return make_response(jsonify({
        "status": "201",
        "message": "You have successfully booked the hotel!",
        "hotel": hotel
    }), 201)

@hotels_v1.route('/hotels', methods=['GET'])
@jwt_required
def get_all_hotels():
    '''Fetch all the existing hotels.'''

    return make_response(jsonify({
        "status": "200",
        "message": "success",
        "hotels": json.loads(HotelsModel().get_hotels())
    }), 200)

@hotels_v1.route('/hotels/<string:name>', methods=['GET'])
@jwt_required
def get_hotel(name):
    """Fetch a specific hotel."""

    hotel = HotelsModel().get_hotel(name)
    hotel = json.loads(hotel)
    if hotel:
        return make_response(jsonify({
            "status": "200",
            "message": "success",
            "hotel": hotel
        }), 200)
    return make_response(jsonify({
        "status": "404",
        "message": "hotel not found"
        }), 404)
