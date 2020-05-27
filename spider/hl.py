#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
from lxml import html
import random
import time
from spider.dbutils import DB
from datetime import datetime


class hl():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    def get_data(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'utf-8'
        html1 = req.text

        tree = html.fromstring(html1)
        for i in range(1, 10):
            xpath = tree.xpath('//*/tr[@class="first"][' + str(i) + ']/td')
            a1 = str.strip(xpath[0].text).replace("-","")
            a2 = str.strip(xpath[1].text)
            a3 = str.strip(xpath[2].text)
            rows=[a1,a2,a3]
            self.insert(rows)

    def get_data_gcjgzs(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'utf-8'
        html1 = req.text
        tree = html.fromstring(html1)
        for i in range(0,30):
            xpath = tree.xpath('//*/table[@class="mod_tab"]//tr/td')
            a1 = xpath[i*4].text.replace("-", "")
            a2 = xpath[i*4+1].text
            rows=[a1,a2]
            self.insert_gcjgzs(rows)

    def get_data_tkszs(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'utf-8'
        html1 = req.text
        tree = html.fromstring(html1)
        for i in range(0,30):
            xpath = tree.xpath('//*/table[@class="mod_tab"]//tr/td')
            a1 = xpath[i*4].text.replace("-", "")
            a2 = xpath[i*4+1].text
            rows=[a1,a2]
            self.insert_tkszs(rows)

    def parse(self, row):
        return row

    def insert(self, data):
        db = DB()
        sql = "select count(*) from sgba_ods_wb_hl where hl_day = '"+data[0]+"' and hl_code='USD'"
        db.execute(sql)
        results = db.fetchone()
        if results[0] == 0:
            hl_id =  time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(100000,999999))
            sql = "INSERT INTO SGBA_ODS_WB_hl(HL_ID,HL_DAY,HL_CODE,HL_NAME,HL_DATA) VALUES("+hl_id +","+data[0]+",'USD','美元汇率中间价',"+ data[1] +  ")"
            db.execute(sql)
            db.commit()
        sql = "select count(*) from sgba_ods_wb_hl where hl_day = '"+data[0]+"' and hl_code='EUR'"
        db.execute(sql)
        results = db.fetchone()
        if results[0] == 0:
            hl_id =  time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(100000,999999))
            sql = "INSERT INTO SGBA_ODS_WB_hl(HL_ID,HL_DAY,HL_CODE,HL_NAME,HL_DATA) VALUES("+hl_id +","+data[0]+",'EUR','欧元汇率中间价',"+ data[2] +  ")"
            db.execute(sql)
            db.commit()
        db.close()

    def insert_gcjgzs(self, data):
        db = DB()
        sql = "select count(*) from sgba_ods_wb_hl where hl_day = '"+data[0]+"' and hl_code='GTJGZS'"
        db.execute(sql)
        results = db.fetchone()
        if results[0] == 0:
            hl_id =  time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(100000,999999))
            sql = "INSERT INTO SGBA_ODS_WB_hl(HL_ID,HL_DAY,HL_CODE,HL_NAME,HL_DATA) VALUES("+hl_id +"," +data[0]+",'GTJGZS','钢材价格指数',"+ data[1] +  ")"
            db.execute(sql)
            db.commit()
        db.close()

    def insert_tkszs(self, data):
        db = DB()
        sql = "select count(*) from sgba_ods_wb_hl where hl_day = '"+data[0]+"' and hl_code='TKSZS'"
        db.execute(sql)
        results = db.fetchone()
        if results[0] == 0:
            hl_id =  time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(100000,999999))
            sql = "INSERT INTO SGBA_ODS_WB_hl(HL_ID,HL_DAY,HL_CODE,HL_NAME,HL_DATA) VALUES("+hl_id +"," +data[0]+",'TKSZS','62%铁矿石普氏',"+ data[1] +  ")"
            db.execute(sql)
            db.commit()
        db.close()

    def run(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'【'+__name__+'】')
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'---美元欧元汇率')
        self.get_data("http://www.safe.gov.cn/AppStructured/hlw/RMBQuery.do")
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'---钢材价格指数')
        self.get_data_gcjgzs("http://www.96369.net/indices/65")
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'---62%铁矿石普氏')
        self.get_data_tkszs("http://www.96369.net/Indices/125")
