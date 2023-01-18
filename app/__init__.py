from flask_restful import Resource, Api, reqparse
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask("AuthenticationAPI")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
from app.models.User import User
from app.api import login, register, getUsers


with app.app_context():
    db.create_all()
