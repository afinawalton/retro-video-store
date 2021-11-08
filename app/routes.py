from flask import Blueprint, jsonify, make_response
from flask.globals import request
from app.models.customer import Customer
from app import db

# --------------------------------
# -------- CUSTOMER ROUTES -------
# --------------------------------
customers_bp = Blueprint("customers", __name__, url_prefix="/customers")

@customers_bp.route("", methods=["POST"])
def create_goal():
    request_body = request.get_json()
    pass

@customers_bp.route("", methods=["GET"])
def read_goals():
    customers = Customer.query.all()

    response_body = []

    if not customers:
        return jsonify([]), 200

    for customer in customers:
        response_body.append(customer.to_dict())
    
    return response_body, 200

@customers_bp.route("/<id>", methods=["GET"])
def read_one_goal(id):
    customer = Customer.query.get(id)

    if not customer:
        return {"message": f"Customer {id} was not found"}, 404

    return customer.to_dict(), 200

@customers_bp.route("", methods=["PUT", "PATCH"])
def update_goal():
    pass

@customers_bp.route("", methods=["DELETE"])
def delete_goal():
    pass