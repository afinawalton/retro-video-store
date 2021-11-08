from flask import Blueprint, jsonify, make_response
from flask.globals import request
from app.models.customer import Customer
from app import db

# --------------------------------
# -------- CUSTOMER ROUTES -------
# --------------------------------
customers_bp = Blueprint("customers", __name__, url_prefix="/customers")

@customers_bp.route("", methods=["POST"])
def create_customer():
    request_body = request.get_json()

    missing = ""
    if "name" not in request_body:
        missing = "name"
    elif "postal_code" not in request_body:
        missing = "postal_code"
    elif "phone" not in request_body:
        missing = "phone"
    if missing:
        return {"details": f"Request body must include {missing}."}, 400

    new_customer = Customer(
        name=request_body["name"],
        postal_code=request_body["postal_code"],
        phone=request_body["phone"]
    )

    db.session.add(new_customer)
    db.session.commit()

    return {"id": new_customer.id}, 201

@customers_bp.route("", methods=["GET"])
def read_customers():
    customers = Customer.query.all()

    response_body = []

    if not customers:
        return jsonify([]), 200

    for customer in customers:
        response_body.append(customer.to_dict())
    
    return jsonify(response_body), 200

@customers_bp.route("/<id>", methods=["GET"])
def read_one_customer(id):
    if not isinstance(id, int):
        return {"message": f"{id} is not a valid id"}, 400

    customer = Customer.query.get(id)

    if not customer:
        return {"message": f"Customer {id} was not found"}, 404

    return customer.to_dict(), 200

@customers_bp.route("/<id>", methods=["PUT", "PATCH"])
def update_customer(id):
    request_body = request.get_json()

    customer = Customer.query.get(id)

    if not customer:
        return {"message": f"Customer {id} was not found"}, 404

    if "name" not in request_body or "phone" not in request_body \
    or "postal_code" not in request_body:
        return {"details": "Invalid request"}, 400

    customer.name = request_body["name"]
    customer.phone = request_body["phone"]
    customer.postal_code = request_body["postal_code"]

    db.session.commit()

    return customer.to_dict(), 200

@customers_bp.route("/<id>", methods=["DELETE"])
def delete_customer(id):
    customer = Customer.query.get(id)

    if not customer:
        return {"message": f"Customer {id} was not found"}, 404

    db.session.delete(customer)
    db.session.commit()

    return {"id": customer.id}, 200