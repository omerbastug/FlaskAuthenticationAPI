from app import app,db
from flask import jsonify, request
from app.models.User import User

@app.route("/api/register", methods=["POST"])
def register():
    body = request.get_json()
    try:
        print(body)
        newuser = User(fullname=body['fullname'],email=body['email'],password = body['password'])
        db.session.add(newuser)
        db.session.commit()
        respUser = newuser.as_dict()
    except BaseException as err:
        print(err)
        return jsonify({"error":err}), 400

    return jsonify({"success":"account created", "user" : respUser}) , 201