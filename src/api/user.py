from flask import Blueprint, jsonify, request
import requests

from src.model import *

api = Blueprint("api_user", __name__)


@api.route("/users", methods=["GET"])
def get_all_users() -> object:
    try:
        users = db.session.query(User).all()
    except BaseException as e:
        print(e)
        return jsonify({"status": "failed",
                        "message": "Error while database session"})

    response = {
        "status": "success", "users": [
            user.to_dict() for user in users]}
    return jsonify(response)


@api.route("/users", methods=["POST"])
def add_user() -> object:
    if not ("id" in request.form and "name" in request.form):
        return jsonify({"status": "failed",
                        "message": "Required argument is missing"})

    try:
        user = User(id=int(request.form["id"]), name=request.form["name"])
        db.session.add(user)
        db.session.commit()
    except BaseException as e:
        print(e)
        return jsonify({"status": "failed",
                        "message": "Error while database session"})

    response = {"status": "success", "user": user.to_dict()}
    return jsonify(response)


@api.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id: int) -> object:
    try:
        user = db.session.query(User).filter(User.id == user_id).first()
    except BaseException as e:
        print(e)
        return jsonify({"status": "failed",
                        "message": "Error while database session"})

    response = {"status": "success", "user": user.to_dict()}
    return jsonify(response)


@api.route("/test", methods=["POST"])
def test() -> object:
    body = request.get_data().decode()
    print(body)

    list = {}
    for item in body.split("&"):
        split_item = item.split("=")
        list[split_item[0]] = split_item[1]

    user_id = list["text"].split("+")[0]

    user = db.session.query(User).filter(User.id == user_id).first()
    user.is_watch = True

    db.session.commit()

    response = {
        "text": "ユーザーのセットが完了しました！",
        "response_type": "in_channel"
    }

    return jsonify(response)


@api.route("/test2", methods=["GET"])
def post_notification():
    post_url = 'https://slack.com/api/chat.postMessage'
    payload = {
        'token': "xoxb-1506483628352-1476246434710-AKQT2LbfRb29LtsT4UugbsiE",
        "channel_name": "#general",
        "user_name": "t.watanabe0452",
        "text": "Hello Flask",
        "scope": "chat:write:bot"
    }

    res = requests.post(post_url, payload)
    print(res.status_code, res.text)

    return jsonify("hello")


@api.route("/test3", methods=["POST"])
def test_3():
    response = {
        "text": "ユーザーのセットを解除しました！",
        "response_type": "in_channel"
    }

    return jsonify(response)
