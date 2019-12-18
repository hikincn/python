#!/usr/bin/python
# -*- coding: UTF-8 -*-
import http
import json
import time
import urllib

import requests
from lxml import etree, html
from dbutils import DB
from datetime import datetime

from spider.Spider import Spider

class qihuo_sh(Spider):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    def get_url(self, page=None):
        return "http://www.shfe.com.cn/data/delaymarket_rb.dat"

    def get_data(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text
        try:
            product_dic = json.loads(html)
            return product_dic
        except Exception:
            return ""

    def parse(self, row):
        print(row)

    def insert(self, data):
        db = DB()
        dt = datetime.now()
        sql = "INSERT INTO SGBA_ODS_WB_QH(QH_TIME,QH_CODE,QH_NAME,QH_KP,QH_ZG,QH_ZD,QH_ZX,QH_ZDS,QH_ZJS) VALUES" \
              "(" +dt.strftime('%Y%m%d%H%M%S')+",'"+ data['contractname']+"','螺纹钢"+data['contractname']+"',"+data['openprice'].replace("--","0")+","+data['highprice'].replace("--","0")+","+data['lowerprice'].replace("--","0")+","+data['lastprice']+","+data['upperdown']+","+data['presettlementprice']+")"
        db.execute(sql)
        db.commit()
        db.close()

    def run(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'【'+__name__+'】')
        url = self.get_url()
        rows = self.get_data(url)
        j = len(rows['delaymarket'])
        #print(str(j))
        #print(rows['delaymarket'][j-1])
        for i in range(0,j-1):
            self.insert(rows['delaymarket'][i])