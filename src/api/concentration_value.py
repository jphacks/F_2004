import datetime
from distutils.util import strtobool

from flask import Blueprint, jsonify, request
from sqlalchemy import desc

from src.model import *

import src.predict as predict

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
    concentration_value = request.form["concentration_value"]

    #警告を通知
    if int(concentration_value) <= 4:
        user_name = db.session.query(User.name)\
        .filter(User.id == user_id)\
        .all()
        
        user_name = str(user_name[0][0])
        msg =  "@" + user_name + "さん！　お疲れのようですので、少し休みましょう！"
        post_url = 'https://slack.com/api/chat.postMessage'
        payload = {
            'token':'xoxb-1506483628352-1476246434710-awhAYeScSKJplDE0hb5Xjw9A',
            "channel": "#general",
            "text": msg,
            "scope": "chat:write:bot"
        }
        res = requests.post(post_url, payload)
        print(res.status_code, res.text)    

    #データベースに追加
    try:
        concentration_value = ConcentrationValue(
            user_id=int(user_id),
            concentration_value=int(concentration_value),
            is_sitting=strtobool(is_sitting),
        )
        db.session.add(concentration_value)
        db.session.commit()

    except BaseException as e:
        print(e)
        return jsonify({"status": "failed", "message": "Error while database session"})

    response = {"status": "success", "concentration_value": concentration_value.to_dict()}
    print(response)
    # return jsonify(response)

    #機械学種を用いた事前警告
    concentration_values = db.session.query(ConcentrationValue.concentration_value) \
        .filter(ConcentrationValue.user_id == user_id) \
        .order_by(desc(ConcentrationValue.created_at)) \
        .all()

    cv_list = []
    for cv in concentration_values[-6:]:#最近の6個の流れを取得
        cv = int(cv[0])
        cv_list.append(cv)
    print(cv_list)
    try:
        results = predict()
        user_pattern = results[user_id]
    except:
        user_pattern = [[5,5,5,6,6,6],[0,0,1,1,1,1]]
    
    for i in range(6):
        if i == 5:
            if cv_list[i] <= user_pattern[0][i] + user_pattern[1][i]:
                user_name = db.session.query(User.name)\
                    .filter(User.id == user_id)\
                    .all()
                msg =  "@" + user_name + "さん！そろそろコーヒーでも飲みませんか？"
                post_url = 'https://slack.com/api/chat.postMessage'
                payload = {
                    'token':'xoxb-1506483628352-1476246434710-awhAYeScSKJplDE0hb5Xjw9A',
                    "channel": "#general",
                    "text": msg,
                    "scope": "chat:write:bot"
                }
                res = requests.post(post_url, payload)
                print(res.status_code, res.text)
            else:
                break

        if cv_list[i] <= user_pattern[0][i] + user_pattern[1][i]:
            continue
        else:
            print("まだ休む必要はなさそう")
            break
    
    return jsonify(response)

    




@api.route("/get_v", methods=["GET"])
def aaa() -> object:
    user_id = 1
    # watching_user_id = db.session.query(User.name)\
    #     .filter(User.id == user_id)\
    #     .all()
    # a = watching_user_id[0][0]
    # print(str(a))
    
    # concentration_values = db.session.query(ConcentrationValue.concentration_value) \
    #     .filter(ConcentrationValue.user_id == user_id) \
    #     .order_by(desc(ConcentrationValue.created_at)) \
    #     .all()
    
    # cv_list = []
    # for cv in concentration_values[-6:]:#最近の6個の流れを取得
    #     cv = int(cv[0])
    #     cv_list.append(cv)
    # print(cv_list)
    # try:
    #     results = predict()
    #     user_pattern = results[user_id]
    # except:
    #     user_pattern = [[5,5,5,6,6,6],[0,0,1,1,1,1]]
    
    # for i in range(6):
    #     if i == 5:
    #         if cv_list[i] =< user_pattern[0][i] + user_pattern[1][i]:
    #             user_name = db.session.query(User.name)\
    #                 .filter(User.id == user_id)\
    #                 .all()
    #             msg =  "@" + user_name + "さん！そろそろコーヒーでも飲みませんか？"
    #             post_url = 'https://slack.com/api/chat.postMessage'
    #             payload = {
    #                 'token':'xoxb-1506483628352-1476246434710-awhAYeScSKJplDE0hb5Xjw9A',
    #                 "channel": "#general",
    #                 "text": msg,
    #                 "scope": "chat:write:bot"
    #             }
    #             res = requests.post(post_url, payload)
    #             print(res.status_code, res.text)

    #     if cv_list[i] =< user_pattern[0][i] + user_pattern[1][i]:
    #         continue
    #     else:
    #         break

    
    
    # now_con = concentration_values[0].ConcentrationValue.concentration_value
    # pre_con = concentration_values[1].ConcentrationValue.concentration_value
    # [<ConcentrationValue 1(2020-11-27 19:27:54.075818):5,True>, 
    # <ConcentrationValue 1(2020-11-27 19:27:23.970197):6,True>,
    #  <ConcentrationValue 1(2020-11-27 19:26:23.314433):6,True>,
    #   <ConcentrationValue 1(2020-11-27 19:26:13.748792):9,True>,
    #   <ConcentrationValue 1(2020-11-27 19:26:08.001778):9,True>,
    #    <ConcentrationValue 1(2020-11-27 19:25:42.548548):8,True>]

    # if now_con <= 2 and pre_con <= 2:
    #     msg = concentration_values.User.name + "さん！　集中力が下がっています！　休憩しましょう！！"
    #     print(msg)

    
