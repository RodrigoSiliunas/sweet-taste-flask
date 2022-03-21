import re
from app.models.User import User
from app.database import *
from flask import Blueprint, request, jsonify

blueprint = Blueprint('users', __name__)

@blueprint.route('/user', methods=['POST'])
def create_user():
    body = request.get_json()
    user = User.objects.create(
        name=body['name'],
        email=body['email'],
        birthday=body['birthday'],
        personal_phone=body['personal_phone'],
        personal_celphone=body['personal_celphone'],
    )

    return jsonify(user), 201
