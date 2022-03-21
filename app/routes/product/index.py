from app.models.Product import Product
from app.database import *
from flask import Blueprint, request, jsonify

blueprint = Blueprint('product', __name__)


@blueprint.route('/product', methods=['POST'])
def create_product():
    body = request.get_json()

    product = Product.objects.create(
        name=body['name'],
        description=body['description'],
        price=body['price'],
        category=body['category']
    )

    return jsonify(product), 201


@blueprint.route('/product', methods=['GET'])
def get_product():
    product = Product.objects()

    return jsonify(product), 200


@blueprint.route('/product/<id>', methods=['GET'])
def get_product_id(id: str):
    product = Product.objects(id=id).first()

    return jsonify(product), 200


@blueprint.route('/product/<id>', methods=['PUT'])
def update_product(id: str):
    body = request.get_json()

    product = Product.objects.get_or_404(id=id)
    product.update(**body)

    return jsonify(str(product.id)), 200


@blueprint.route('/product/<id>',methods=['DELETE'])
def delete_product(id: str):
    movie = Product.objects.get_or_404(id=id)
    movie.delete()

    return jsonify(str(movie.id)), 200
