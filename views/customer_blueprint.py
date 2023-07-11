from flask import Blueprint

customer_bp = Blueprint('customer', __name__)


@customer_bp.route('/', methods=['POST'])
def create_customer():
    pass


@customer_bp.route('/<int:identifier>', methods=['GET'])
def get_customer(identifier):
    pass


@customer_bp.route('/<int:iidentifierd>', methods=['PUT'])
def update_customer(identifier):
    pass


@customer_bp.route('/<int:identifier>', methods=['DELETE'])
def delete_customer(identifier):
    pass
