from flask import Blueprint
# CUSTOMER ROUTES #

customers_bp = Blueprint("customers", __name__, url_prefix="/customers")

@customers_bp.route("", methods=["POST"])
def create_goal():
    pass

def read_goals():
    pass

def read_one_goal():
    pass

def update_goal():
    pass

def delete_goal():
    pass