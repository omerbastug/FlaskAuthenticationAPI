from app import app, db
from flask import jsonify, request
from app.models.User import User


@app.route("/api/users", methods=["GET"])
def get_all_users():
    return jsonify({"users": [user.as_dict() for user in User.query.all()]})