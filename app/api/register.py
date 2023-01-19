from app import app,db
from flask import jsonify, request
from app.models.User import User
import re

@app.route("/api/register", methods=["POST"])
def register():
    body = request.get_json()
    fullname = body.get("fullname")
    email = body.get("email")
    password = body.get("password")
    if not fullname or not email or not password:
        return jsonify({"error": "Not every field entered"}), 400
    
    email.strip() # remove whitespace
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex, email):
        return jsonify({"error": "Invalid email"}), 400
    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters long"}), 400
    
    try:
        newuser = User(fullname=body['fullname'],email=body['email'],password = body['password'])
        db.session.add(newuser)
        db.session.commit()
        respUser = newuser.as_dict()
    except BaseException as err:
        print(err)
        return jsonify({"error": "User exists with the given email"}), 400

    return jsonify({"success":"account created", "user" : respUser}) , 201