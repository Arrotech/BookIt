import re

from flask import jsonify, make_response


def raise_error(status, msg):
    return make_response(jsonify({
        "status": "400",
        "message": msg
    }), status)

def check_register_keys(request):
    res_keys = ['firstname', 'lastname', 'phone', 'username', 'email', 'password']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_login_keys(request):
    res_keys = [ 'email', 'password']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_trips_keys(request):
    res_keys = ["booked_by", "pickup", "destination", "means"]
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_lodges_keys(request):
    res_keys = ["booked_by", "hotel_name", "lodge_no"]
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_hotels_keys(request):
    res_keys = ["name", "location", "lodges", "conference_rooms", "category"]
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def convert_to_int(id):
    try:
        value = int(id)
        if value > 0:
            return value
        return raise_error(400, "cannot be a negative number")
    except Exception as e:
        return {"message": e}

def is_valid_email(variable):
    """Check if email is a valid mail."""
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$)",
                variable):
        return True
    return False

def is_valid_phone(variable):
    """Check if email is a valid mail."""
    if re.match(r"(^(?:254|\+254|0)?(7(?:(?:[129][0-9])|(?:0[0-8])|(4[0-1]))[0-9]{6})$)",
                variable):
        return True
    return False

def is_valid_password(variable):
    """Check if password is a valid password."""
    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", variable):
        return True
    return False
