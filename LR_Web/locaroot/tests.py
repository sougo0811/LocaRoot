from django.test import TestCase
import requests
import json

url = "http://127.0.0.1:8000/M5stack/"
sess = requests.session()

print(sess.get(url))

csrftoken = sess.cookies['csrftoken']
print(csrftoken)
# ヘッダ
headers = {'Content-type': 'application/json', "X-CSRFToken": csrftoken}

# 送信データ
prm = {"param1": "パラメータ１", "param2": "パラメータ２"}

# JSON変換
params = json.dumps(prm)


# POST送信
print(url,headers,params)
res = sess.post(url, data=params, headers=headers)

# 戻り値を表示
print("--戻り値----------------------------")
print(json.loads(res.text))
