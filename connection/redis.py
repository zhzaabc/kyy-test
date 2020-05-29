# -*- coding: utf-8 -*-

import redis
import sys

sys.path.append("..")
import config.database as d


def new_redis_conn():
    try:
        conn = redis.Redis(host=d.REDIS_HOST, port=d.REDIS_PORT, decode_responses=True)
    except Exception as e:
        print("连接redis失败:", e)
    return conn
