from flask import Blueprint, jsonify, request
from typing import List
from distutils.util import strtobool

from src.model import *

api = Blueprint("api_concentration_value", __name__)


@api.route("/concentration_values/<int:user_id>", methods=["GET"])
def get_concentration_values(user_id: int) -> object:
    try:
        concentration_values: List[ConcentrationValue] = db.session.query(ConcentrationValue) \
            .filter(ConcentrationValue.user_id == user_id) \
            .all()
    except BaseException as e:
        print(e)
        return jsonify({"status": "failed", "message": "Error while database session"})

    response: object = {
        "status": "success",
        "concentration_values": [
            concentration_value.to_dict() for concentration_value in concentration_values
        ]
    }
    return jsonify(response)


@api.route("/concentration_values", methods=["POST"])
def add_concentration_value() -> object:
    if not (
            "user_id" in request.form and
            "concentration_value" in request.form and
            "is_sitting" in request.form
    ):
        return jsonify({"status": "failed", "message": "Required argument is missing"})

    try:
        concentration_value: ConcentrationValue = ConcentrationValue(
            user_id=int(request.form["user_id"]),
            concentration_value=int(request.form["concentration_value"]),
            is_sitting=strtobool(request.form["is_sitting"]),
        )
        db.session.add(concentration_value)
        db.session.commit()
    except BaseException as e:
        print(e)
        return jsonify({"status": "failed", "message": "Error while database session"})

    response: object = {"status": "success", "concentration_value": concentration_value.to_dict()}
    return jsonify(response)
