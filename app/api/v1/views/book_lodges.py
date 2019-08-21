import json
from flask import make_response, jsonify, request, Blueprint
from app.api.v1.models.book_lodges import LodgesModel
from app.api.v1.models.users_model import UsersModel
from app.api.v1.models.add_hotels import HotelsModel
from utils.v1.validations import check_lodges_keys, raise_error, convert_to_int
from flask_jwt_extended import jwt_required

lodges_v1 = Blueprint('lodges_v1', __name__)


@lodges_v1.route('/lodges', methods=['POST'])
@jwt_required
def book_lodge():
    """A registered user can book a lodge."""
    errors = check_lodges_keys(request)
    if errors:
        return raise_error(400, "Invalid {} key".format(', '.join(errors)))
    details = request.get_json()
    booked_by = details['booked_by']
    hotel_name = details['hotel_name']
    lodge_no = details['lodge_no']

    value = convert_to_int(booked_by)
    value2 = convert_to_int(hotel_name)
    if type(value) is not int:
        return raise_error(400, "only positive integer is accepted")
    if type(value2) is not int:
        return raise_error(400, "only positive integer is accepted")
    if UsersModel().get_username(booked_by):
        if HotelsModel().get_hotel(hotel_name):
            lodge = LodgesModel(booked_by, hotel_name, lodge_no).save()
            if "error" in lodge:
                return raise_error(400, "Please check your input and try again!")
            return make_response(jsonify({
                "status": "201",
                "message": "You have successfully booked the hotel!",
                "lodge": lodge
            }), 201)
        return raise_error(400, "Please check your input and try again!")
    return raise_error(400, "Please check your input and try again!")

@lodges_v1.route('/lodges', methods=['GET'])
@jwt_required
def get_all_lodges():
    '''Fetch all the existing lodges.'''

    return make_response(jsonify({
        "status": "200",
        "message": "success",
        "lodges": json.loads(LodgesModel().get_lodges())
    }), 200)

@lodges_v1.route('/lodges/<int:booked_by>', methods=['GET'])
@jwt_required
def get_lodge(booked_by):
    """Fetch a specific lodge."""

    lodge = LodgesModel().get_lodge(booked_by)
    lodge = json.loads(lodge)
    if lodge:
        return make_response(jsonify({
            "status": "200",
            "message": "success",
            "lodge": lodge
        }), 200)
    return make_response(jsonify({
        "status": "404",
        "message": "lodge not found"
        }), 404)

@lodges_v1.route('/lodges/cancel/<int:lodge_id>', methods=['PUT'])
@jwt_required
def cancel_booking(lodge_id):
    '''cancel a specific booking.'''

    lodge = LodgesModel().get_lodge_by_id(lodge_id)
    if lodge:
        status = lodge['status']
        if ((status != "Booked") and (status != "Active") and (status != "Completed")):
            return make_response(jsonify({
                "status": "200",
                "message": "Lodging already {}".format(status)
            }), 400)
        LodgesModel().cancel(lodge_id)
        return make_response(jsonify({
            "status": "200",
            "message": "Lodging cancelled"
        }), 200)

    return make_response(jsonify({
        "status": "404",
        "message": "Lodge not found"
    }), 404)

@lodges_v1.route('/lodges/complete/<int:lodge_id>', methods=['PUT'])
@jwt_required
def complete_lodging(lodge_id):
    '''complete specific Lodging.'''

    lodge = LodgesModel().get_lodge_by_id(lodge_id)
    if lodge:
        status = lodge['status']
        if ((status != "Booked") and (status != "Active") and (status != "Cancelled")):
            return make_response(jsonify({
                "status": "200",
                "message": "Lodging already {}".format(status)
            }), 400)
        LodgesModel().complete(lodge_id)
        return make_response(jsonify({
            "status": "200",
            "message": "Lodging completed"
        }), 200)

    return make_response(jsonify({
        "status": "404",
        "message": "Lodge not found"
    }), 404)

@lodges_v1.route('/lodges/activate/<int:lodge_id>', methods=['PUT'])
@jwt_required
def activate_booking(lodge_id):
    '''Activate a booking.'''

    lodge = LodgesModel().get_lodge_by_id(lodge_id)
    if lodge:
        status = lodge['status']
        if ((status != "Booked") and (status != "Completed") and (status != "Cancelled")):
            return make_response(jsonify({
                "status": "200",
                "message": "Lodging already {}".format(status)
            }), 400)
        LodgesModel().activate(lodge_id)
        return make_response(jsonify({
            "status": "200",
            "message": "Lodging is now activate"
        }), 200)

    return make_response(jsonify({
        "status": "404",
        "message": "Lodge not found"
    }), 404)
