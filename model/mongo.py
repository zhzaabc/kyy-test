#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 21:24:44 2020

@author: justin
"""

import sys

sys.path.append("..")
import connection.mongo as mongo


def insert_one(data, collection_name):
    db = mongo.new_mongo_conn()["kyy_test"]
    db[collection_name].insert_one(data)
