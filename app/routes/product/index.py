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