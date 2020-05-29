#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:24:37 2020

@author: justin
"""

import sys

sys.path.append("..")
from utils.common import generateToken
from random import randint
import connection.mysql as mysql
import connection.redis as redis
import utils.common as common
import json


# 获取列名
def get_columns():
    conn = mysql.new_master_conn()
    with conn.cursor() as cursor:
        cursor.execute("SHOW COLUMNS FROM khome_space")
        data = cursor.fetchall()
        columns = []
        for v in data:
            columns.append(v[0])
        return columns


columns = get_columns()


# 获取最大的用户id
def get_max_user_id():
    conn = mysql.new_master_conn()
    with conn.cursor() as cursor:
        cursor.execute("SELECT MAX(uid) FROM `khome_space`")
        data = cursor.fetchone()
        if len(data) == 0:
            print("getMaxUserID failed")
            return 0
        return data[0]
    conn.close()


def parse_data(data):
    parsed_data = {}
    for i in range(len(data)):
        parsed_data[columns[i]] = data[i]
    return parsed_data


def get_random_user(max_user_id):
    conn = mysql.new_master_conn()
    random_uid = randint(1, max_user_id)
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM `khome_space`  where uid = %s  limit 1", [random_uid])
        data = cursor.fetchone()
    conn.close()
    if data is None:
        data = get_random_user(max_user_id)
    return data


def get_random_user_dict(max_user_id):
    data = get_random_user(max_user_id)
    return parse_data(data)


def login(uid, username):
    token = common.generateToken()
    conn = redis.new_redis_conn()
    user_info = {"user_id": uid, "username": username}
    conn.setex(token, 86400, json.dumps(user_info))
    return token


# 获取一个随机的用户列表并置为登陆状态 num 列表长度
def get_rand_login_user_list(num):
    user_dict = {}
    max_uid = get_max_user_id()
    while len(user_dict) < num:
        user_info = get_random_user_dict(max_uid)
        token = login(user_info["uid"], user_info["username"])
        user_info["token"] = token
        # 生成一个随机openid
        user_info["openID"] = generateToken()
        user_dict[user_info["uid"]] = user_info
    user_list = []
    for i in user_dict:
        user_list.append(user_dict[i])
    return user_list
