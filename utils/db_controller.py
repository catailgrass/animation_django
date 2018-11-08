# -*- coding : utf-8 -*-
# 数据库控制台
import sqlite3
import os


def get_local_sqlite3_db():
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db = sqlite3.connect(project_path + '/animation.sqlite3')
    return db

