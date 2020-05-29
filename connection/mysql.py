# -*- coding: utf-8 -*-

import pymysql
import sys

sys.path.append("..")
import config.database as d


def new_master_conn():
    try:
        conn = pymysql.connect(host=d.MASTER_DB_HOST,
                               port=d.MASTER_DB_PORT,
                               user=d.MASTER_DB_USER,
                               password=d.MASTER_DB_PASSWORD,
                               database=d.MASTER_DB_NAME,
                               charset="utf8")
    except Exception as e:
        print("连接数据库失败:", e)
    return conn
