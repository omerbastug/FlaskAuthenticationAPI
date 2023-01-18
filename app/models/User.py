from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, fullname, email, password):
        self.fullname = fullname
        self.email = email
        self.password = generate_password_hash(password)

    def matchPassword(self, password):
        return check_password_hash(self.password, password)
        
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
