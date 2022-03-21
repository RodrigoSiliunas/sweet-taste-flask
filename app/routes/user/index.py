from app.models.User import User
from app.database import *
from flask import Blueprint, request, jsonify

blueprint = Blueprint('user', __name__)


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


@blueprint.route('/user/<id>', methods=['GET'])
def get_user(id: str):
    user = User.objects(id=id).first()

    return jsonify(user), 200


@blueprint.route('/user/<id>', methods=['PUT'])
def update_user(id: str):
    body = request.get_json()

    user = User.objects.get_or_404(id=id)
    user.update(**body)

    return jsonify(str(user.id)), 200


@blueprint.route('/user/<id>', methods=['DELETE'])
def delete_user(id: str):
    user = User.objects.get_or_404(id=id)
    user.delete()

    return jsonify(str(user.id)), 200
