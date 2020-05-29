# -*- coding: utf-8 -*-

import pymongo
import sys

sys.path.append("..")
import config.database as d


def new_mongo_conn():
    try:
        conn = pymongo.MongoClient(d.MONGO_DB_ADDRESS, serverSelectionTimeoutMS=2000, socketTimeoutMS=2000)
    except Exception as e:
        print("连接mongo失败:", e)
    return conn
