from flask import Blueprint, jsonify
from flask.globals import request
from app.models.customer import Customer
from app import db

# CUSTOMER ROUTES #
customers_bp = Blueprint("customers", __name__, url_prefix="/customers")

@customers_bp.route("", methods=["POST"])
def create_goal():
    request_body = request.get_json()
    pass

def read_goals():
    customers = Customer.query.all()
    # Gives instance of customer

    response_body = []

    if not customers:
        return jsonify([]), 200

    for customer in customers:
        response_body.append(customer)
    pass

def read_one_goal():
    pass

def update_goal():
    pass

def delete_goal():
    pass