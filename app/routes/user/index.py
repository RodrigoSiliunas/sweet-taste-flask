import datetime, json
from app.models.User import User
from app.database import *
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

blueprint = Blueprint('user', __name__)


@blueprint.route('/user', methods=['POST'])
def create_user():
    body = request.get_json()
    user = User.objects.create(
        name=body['name'],
        email=body['email'],
        password=body['password'],
        birthday=body['birthday'],
        personal_phone=body['personal_phone'],
        personal_celphone=body['personal_celphone'],
    )

    return jsonify(user), 201


@blueprint.route('/user/<id>', methods=['GET'])
def get_user(id: str):
    user = User.objects.get_or_404(id=id)

    return jsonify(user), 200


@blueprint.route('/user', methods=['PUT'])
@jwt_required()
def update_user():
    body = request.get_json()
    body['updated_at'] = datetime.datetime.utcnow

    current_user = get_jwt_identity()
    user = User.objects.get_or_404(email=current_user)
    user.update(**body)

    return jsonify(str(user.id)), 200

@blueprint.route('/user/<id>', methods=['DELETE'])
def delete_user(id: str):
    user = User.objects.get_or_404(id=id)
    user.delete()

    return jsonify(str(user.id)), 200


@blueprint.route('/user/login', methods=["POST"])
def login():
    try:
        data = request.json
    except:
        return jsonify({
            "message": "Please provide user details",
            "data": None,
            "error": "Bad request"
        }), 400

    valid_user = User.objects(email=data['email'], password=data['password']).first()

    if valid_user is None:
        return jsonify({
            "message": "Error fetching auth token!, invalid email or password",
            "data": None,
            "error": "Unauthorized"
        }), 404

    try:
        acess_token = create_access_token(identity=valid_user['email'])

        user = {
            'id': str(valid_user['id']),
            'name': valid_user['name'],
            'email': valid_user['email'],
            'birthday': valid_user['birthday'],
            'personal_phone': valid_user['personal_phone'],
            'personal_celphone': valid_user['personal_celphone']
        }

        return jsonify({
            "message": "Successfully fetched auth token. You are logged in.",
            "token": acess_token,
            "user": user
        })
    except Exception as e:
        return jsonify({
            "error": "Something went wrong",
            "message": str(e)
        }), 500