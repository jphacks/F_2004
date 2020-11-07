import datetime
from distutils.util import strtobool

from flask import Blueprint, jsonify, request
from sqlalchemy import desc

from src.model import *

api = Blueprint("api_concentration_value", __name__)


@api.route("/concentration_values/<int:user_id>", methods=["GET"])
def get_concentration_values(user_id: int) -> object:
    limit = request.args.get("limit", default=100, type=int)
    date = request.args.get("date", default=None, type=str)

    try:
        query = db.session.query(ConcentrationValue).filter(ConcentrationValue.user_id == user_id)

        if date is not None:
            one_day_after = datetime.datetime.strptime(date, "%Y-%m-%d") + datetime.timedelta(
                days=1)
            query = query.filter(
                ConcentrationValue.created_at >= date,
                ConcentrationValue.created_at <= one_day_after,
            )

        concentration_values = query \
            .order_by(desc(ConcentrationValue.created_at)) \
            .limit(limit) \
            .all()
    except BaseException as e:
        print(e)
        return jsonify({"status": "failed", "message": "Error while database session"})

    response = {
        "status": "success",
        "concentration_values": [
            concentration_value.to_dict() for concentration_value in concentration_values
        ]
    }
    return jsonify(response)


@api.route("/concentration_values", methods=["POST"])
def add_concentration_value() -> object:
    print(request.form)
    if not (
            "user_id" in request.form and
            "concentration_value" in request.form and
            "is_sitting" in request.form
    ):
        return jsonify({"status": "failed", "message": "Required argument is missing"})

    user_id = request.form["user_id"]
    is_sitting = request.form["is_sitting"]

    try:
        concentration_value = ConcentrationValue(
            user_id=int(user_id),
            concentration_value=int(request.form["concentration_value"]),
            is_sitting=strtobool(is_sitting),
        )
        db.session.add(concentration_value)
        db.session.commit()
    except BaseException as e:
        print(e)
        return jsonify({"status": "failed", "message": "Error while database session"})

    response = {"status": "success", "concentration_value": concentration_value.to_dict()}

    # if not is_sitting:
    #     return jsonify(response)
    #
    # concentration_values = db.session.query(ConcentrationValue, User.name) \
    #     .join(User, User.id == ConcentrationValue.user_id) \
    #     .filter(User.id == user_id and User.is_watch) \
    #     .order_by(desc(ConcentrationValue.created_at)) \
    #     .all()
    #
    # now_con = concentration_values[0].ConcentrationValue.concentration_value
    # pre_con = concentration_values[1].ConcentrationValue.concentration_value
    # if now_con <= 2 and pre_con <= 2:
    #     msg = concentration_values.User.name + "さん！　集中力が下がっています！　休憩しましょう！！"
    #     print(msg)

    return jsonify(response)
