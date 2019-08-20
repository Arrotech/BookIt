import json
from flask import make_response, jsonify, request, Blueprint
from app.api.v1.models.book_trips import TripsModel
from app.api.v1.models.users_model import UsersModel
from utils.v1.validations import check_trips_keys, raise_error, convert_to_int
from flask_jwt_extended import jwt_required

trips_v1 = Blueprint('trips_v1', __name__)


@trips_v1.route('/trips', methods=['POST'])
@jwt_required
def book_trip():
    """A registered user can book a trip."""
    errors = check_trips_keys(request)
    if errors:
        return raise_error(400, "Invalid {} key".format(', '.join(errors)))
    details = request.get_json()
    booked_by = details['booked_by']
    pickup = details['pickup']
    destination = details['destination']
    means = details['means']

    value = convert_to_int(booked_by)
    if type(value) is not int:
        return raise_error(400, "only positive integer is accepted")
    if UsersModel().get_username(booked_by):
        trip = TripsModel(booked_by, pickup, destination, means).save()
        if "error" in trip:
            return raise_error(400, "Please check your input and try again!")
        return make_response(jsonify({
            "status": "201",
            "message": "You have successfully booked the trip!",
            "trip": trip
        }), 201)
    return raise_error(400, "User with that username does not exist!")

@trips_v1.route('/trips', methods=['GET'])
@jwt_required
def get_all_trips():
    '''Fetch all the existing trips.'''

    return make_response(jsonify({
        "status": "200",
        "message": "success",
        "trips": json.loads(TripsModel().get_trips())
    }), 200)

@trips_v1.route('/trips/<int:booked_by>', methods=['GET'])
@jwt_required
def get_trip(booked_by):
    """Fetch a specific trip."""

    trip = TripsModel().get_trip(booked_by)
    trip = json.loads(trip)
    if trip:
        return make_response(jsonify({
            "status": "200",
            "message": "success",
            "trip": trip
        }), 200)
    return make_response(jsonify({
        "status": "404",
        "message": "trip not found"
        }), 404)

@trips_v1.route('/trips/cancel/<int:trip_id>', methods=['PUT'])
@jwt_required
def cancel_trip(trip_id):
    '''cancel a specific trip.'''

    trip = TripsModel().get_trip_by_id(trip_id)
    if trip:
        status = trip['status']
        if ((status != "Booked") and (status != "In progress") and (status != "Completed")):
            return make_response(jsonify({
                "status": "200",
                "message": "Trip already {}".format(status)
            }), 400)
        TripsModel().cancel(trip_id)
        return make_response(jsonify({
            "status": "200",
            "message": "Trip cancelled"
        }), 200)

    return make_response(jsonify({
        "status": "404",
        "message": "Trip not found"
    }), 404)

@trips_v1.route('/trips/complete/<int:trip_id>', methods=['PUT'])
@jwt_required
def complete_trip(trip_id):
    '''complete a specific trip.'''

    trip = TripsModel().get_trip_by_id(trip_id)
    if trip:
        status = trip['status']
        if ((status != "Booked") and (status != "In progress") and (status != "Cancelled")):
            return make_response(jsonify({
                "status": "200",
                "message": "Trip already {}".format(status)
            }), 400)
        TripsModel().complete(trip_id)
        return make_response(jsonify({
            "status": "200",
            "message": "Trip completed"
        }), 200)

    return make_response(jsonify({
        "status": "404",
        "message": "Trip not found"
    }), 404)

@trips_v1.route('/trips/in-progress/<int:trip_id>', methods=['PUT'])
@jwt_required
def trip_in_progress(trip_id):
    '''Mark a trip in progress.'''

    trip = TripsModel().get_trip_by_id(trip_id)
    if trip:
        status = trip['status']
        if ((status != "Booked") and (status != "Completed") and (status != "Cancelled")):
            return make_response(jsonify({
                "status": "200",
                "message": "Trip already {}".format(status)
            }), 400)
        TripsModel().progress(trip_id)
        return make_response(jsonify({
            "status": "200",
            "message": "Trip in progress"
        }), 200)

    return make_response(jsonify({
        "status": "404",
        "message": "Trip not found"
    }), 404)
