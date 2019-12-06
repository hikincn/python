#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb


class DB:
    def __init__(self):
        # 打开数据库连接
        self.db = MySQLdb.connect("127.0.0.1", "root", "admin", "sgba", charset='utf8')
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def execute(self, sql):
        # 使用execute方法执行SQL语句
        self.cursor.execute(sql)

    def fetchone(self):
        # 使用 fetchone() 方法获取一条数据
        return self.cursor.fetchone()

    def close(self):
        self.db.close()

    def commit(self):
        self.db.commit()
