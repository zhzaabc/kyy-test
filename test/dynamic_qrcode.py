# -*- coding: utf-8 -*-
import sys

sys.path.append("..")
import model.user as user_model
import model.mongo as mongo

import requests
import multiprocessing
from random import randint
import time

BASE_PAGE_URL = "http://192.168.118.174:9998"
BASE_URL = "http://192.168.118.174:9999"


def get_dynamic_qrcode(token, reqBody):
    headers = {"X-Token": token}
    req = requests.post(BASE_URL + "/api/v1/activity/dynamicQrcode/getDynamicQrcode", headers=headers, json=reqBody)
    try:
        data = req.json()
        if "result" in data:
            return data
        else:
            print(req.text)
    except:
        print(req.text)


def add_dynamic_qrcode_count(token, reqBody):
    headers = {"X-Token": token}
    req = requests.post(BASE_URL + "/api/v1/activity/dynamicQrcode/addDynamicQrcodeCount", headers=headers,
                        json=reqBody)
    try:
        data = req.json()
        if "result" in data:
            return data
        else:
            print(req.text)
    except:
        print(req.text)


user_list = user_model.get_rand_login_user_list(10)


def get_random_user():
    global user_list
    return user_list[randint(1, 1000) % len(user_list)]


def test(dynamicQrcodeID):
    user_info = get_random_user()
    open_id = user_info["openID"]
    uid = user_info["uid"]
    token = user_info["token"]
    req_body = {"id": dynamicQrcodeID, "openID": open_id}
    data = get_dynamic_qrcode(token, req_body)
    data["reqBody"] = req_body
    data["reqUid"] = uid
    mongo.insert_one(data, "getDynamicQrcode")
    if "departmentID" in data["result"]:
        req_body = {"id": dynamicQrcodeID, "openID": open_id, "departmentID": data["result"]["departmentID"],
                    "dynamicQrcodeImageID": data["result"]["dynamicQrcodeImageID"]}
        data = add_dynamic_qrcode_count(token, req_body)
        data["reqBody"] = req_body
        data["reqUid"] = uid
        mongo.insert_one(data, "addDynamicQrcodeCount")


# 获取需要测试的活码id
def get_id():
    id_list = [53, 54, 55, 56]
    return id_list[randint(1, 1000) % len(id_list)]


# 开始测试
pool = multiprocessing.Pool(processes=10)
for i in range(1000):
    dynamicQrcodeID = get_id()
    pool.apply_async(test, (dynamicQrcodeID,))

pool.close()
pool.join()
