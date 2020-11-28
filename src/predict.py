import schedule
import numpy as np
from sqlalchemy import desc
from src.model import *

def train(results):
    results = results.clear()
    
    # is_wathing==TrueのユーザーIDをリストに格納
    watching_user_id = db.session.query(User.id).filter(User.is_watch).all()
    print(watching_user_id)
    watching_list = []
    for w in watching_user_id:
        w = int(w[0])
        print(w)
        print(type(w))
        watching_list.append(w)
    
    # watching_userの集中力をそれぞれ取得
    watching_users_cv = {}
    for i in watching_list:
        cv_list = []
        watching_user_cv = db.session.query(ConcentrationValue.concentration_value)\
            .filter(ConcentrationValue.user_id == i)\
            .order_by(desc(ConcentrationValue.created_at)) \
            .all()
        for w in watching_user_cv:
            w = int(w[0])
            cv_list.append(w)
        watching_users_cv[i] = cv_list
        print(watching_users_cv) 

    #ユーザーごとに、直前６個の平均と標準偏差を計算
    for watching_user_cv in watching_users_cv.items():
        try:
            # print(values)
            user_pre_cv = []
            user_id = watching_user_cv[0]
            values = watching_user_cv[1]
            for i in range(1,len(values)):
                if values[i] <= 4 and values[i-1] > 4:
                    user_pre_cv.append(values[i-6:i])#本当は[i-36:i-30]+エラー処理が必要
            user_pre_cv_array = np.array(user_pre_cv)#行列に変換
            # print(user_pre_cv_array)
            means = np.round(user_pre_cv_array.mean(axis=0),2)#直前6個の平均
            means = means.tolist()
            sds = np.round(user_pre_cv_array.std(axis=0),2)#直線6個の標準偏差
            sds = sds.tolist()
        except:
            print("デフォルトの予測を使用します")
            means = [5,5,5,6,6,6]
            sds = [0,0,1,1,1,1]

        r = []
        r.append(means)
        r.append(sds)
        results[user_id]=r



results = {}
# #初期値をセット（最大10人分対応可能）
# for n in range(10):
#     means = [5,5,5,6,6,6]
#     sds = [0,0,1,1,1,1]
#     r = []
#     r.append(means)
#     r.append(sds)
#     results.append(r)

#30分おきに、値をアップデート
try:
    schedule.every(30).minutes.do(train(results))
except:
    results = {}

def main():
    return results