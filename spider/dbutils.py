#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import cx_Oracle
class DB:
    def __init__(self):

        # 打开数据库连接
        #self.db = cx_Oracle.connect('lc10029999/aaaaaa@127.0.0.1:1521/orcl')
        self.db = cx_Oracle.connect('LC10019999/liu647@10.1.249.158:1521/oradb')
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def execute(self, sql):
        # 使用execute方法执行SQL语句
        #sql.encode(encoding='UTF-8',errors='strict')
        self.cursor.execute(sql)

    def fetchone(self):
        # 使用 fetchone() 方法获取一条数据
        return self.cursor.fetchone()

    def close(self):
        self.db.close()

    def commit(self):
        self.db.commit()
