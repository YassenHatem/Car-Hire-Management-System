from flask import Blueprint, request, jsonify
from utils.db_helper import DBManager
from dao.customer_dao import CustomerDAO
from dto.customer_dto import CustomerDTO

customer_bp = Blueprint('customer', __name__)
db_manager = DBManager(host="localhost", port=3306, user="myuser", password="mypassword", database="myapp")

# Initialize the customer DAO
customer_dao = CustomerDAO(db_manager)


@customer_bp.route('/', methods=['POST'])
def create_customer():
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        phone_number = data['phone_number']
        address = data['address']
        customer = CustomerDTO(None, name, email, phone_number, address)
        customer_dao.create(customer)
        return jsonify({'message': "customer created"}), 201
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid JSON data'}), 400


@customer_bp.route('/<int:identifier>', methods=['GET'])
def get_customer(identifier):
    customer = customer_dao.get(identifier)
    if customer:
        return jsonify(vars(customer)), 200
    else:
        return jsonify({'error': 'Customer not found'}), 404


@customer_bp.route('/<int:identifier>', methods=['PUT'])
def update_customer(identifier):
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        phone_number = data['phone_number']
        address = data['address']

        customer = CustomerDTO(identifier, name, email, phone_number, address)
        customer_dao.update(customer)
        return jsonify({"message": "customer data updated"}), 202
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid JSON data'}), 400


@customer_bp.route('/<int:identifier>', methods=['DELETE'])
def delete_customer(identifier):
    customer_id = customer_dao.delete(identifier)
    return jsonify({'customer_id': customer_id}), 200
