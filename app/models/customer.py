from app import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    postal_code = db.Column(db.String(5))
    phone_num = db.Column(db.String(14))
    register_at = db.Column(db.DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "registered_at": self.register_at,
            "postal_code": self.postal_code,
            "phone": self.phone_num
        }