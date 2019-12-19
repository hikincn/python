#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import time
from lxml import html

from spider.Spider import Spider
from spider.dbutils import DB
from datetime import datetime


class hl(Spider):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    def get_url(self, page=None):
        return "http://www.safe.gov.cn/AppStructured/hlw/RMBQuery.do"

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
            #print(a1, a2, a3)
            self.insert(rows)

    def parse(self, row):
        return row

    def insert(self, data):
        db = DB()
        sql = "select count(*) from sgba_ods_wb_hl where hl_day = '"+data[0]+"' and hl_code='USD'"
        db.execute(sql)
        results = db.fetchone()
        if results[0] == 0:
            time.sleep(1)
            sql = "INSERT INTO SGBA_ODS_WB_hl(HL_DAY,HL_CODE,HL_NAME,HL_DATA) VALUES(" +data[0]+",'USD','美元汇率',"+ data[1] +  ")"
            db.execute(sql)
            db.commit()
        sql = "select count(*) from sgba_ods_wb_hl where hl_day = '"+data[0]+"' and hl_code='EUR'"
        db.execute(sql)
        results = db.fetchone()
        if results[0] == 0:
            time.sleep(1)
            sql = "INSERT INTO SGBA_ODS_WB_hl(HL_DAY,HL_CODE,HL_NAME,HL_DATA) VALUES(" +data[0]+",'EUR','欧元汇率',"+ data[2] +  ")"
            db.execute(sql)
            db.commit()
        db.close()

    def run(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'【'+__name__+'】')
        url = self.get_url()
        rows = self.get_data(url)
