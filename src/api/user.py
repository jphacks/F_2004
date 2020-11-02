from flask import Blueprint, jsonify, request

from src.model import *

api = Blueprint("api_user", __name__)


@api.route("/users", methods=["GET"])
def get_all_users() -> object:
    try:
        users = db.session.query(User).all()
    except BaseException as e:
        print(e)
        return jsonify({"status": "failed", "message": "Error while database session"})

    response = {"status": "success", "users": [user.to_dict() for user in users]}
    return jsonify(response)


@api.route("/users", methods=["POST"])
def add_user() -> object:
    if not ("id" in request.form and "name" in request.form):
        return jsonify({"status": "failed", "message": "Required argument is missing"})

    try:
        user = User(id=int(request.form["id"]), name=request.form["name"])
        db.session.add(user)
        db.session.commit()
    except BaseException as e:
        print(e)
        return jsonify({"status": "failed", "message": "Error while database session"})

    response = {"status": "success", "user": user.to_dict()}
    return jsonify(response)
