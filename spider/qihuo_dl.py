#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import http
import json
import urllib

import requests
from spider.dbutils import DB
from datetime import datetime

class qihuo_dl():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    urls = []

    def get_url(self, page=None):
        return "http://index.dce.com.cn:10000/dce-webapp-indexquote-1.0-RELEASE/quoteDetail/indexQuote?indexTypeFlag=null&v=04920099850405435"

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
        return row

    def insert(self, data):
        db = DB()
        dt = datetime.now()
        datestr = str(data['tradeDate'])
        if datestr != dt.strftime('%Y%m%d'):
            pass
        sql = "delete from SGBA_ODS_WB_QH where qh_day = '"+ datestr +"' and qh_code ='"+data['indexCode']+"'"
        db.execute(sql)
        db.commit()
        sql = "INSERT INTO SGBA_ODS_WB_QH(QH_DAY,QH_CODE,QH_NAME,QH_KP,QH_ZG,QH_ZD,QH_ZX,QH_ZDS,QH_ZDF,QH_SP,QH_JS,QH_ZSP,QH_ZJS) " \
              "VALUES(" +datestr+",'"+ data['indexCode']+"','"+data['indexName']+"',"+data['openPrice']+","+data['highPrice']+","+data['lowPrice']+","+data['lastPrice']+","+data['netChange']+","+data['chgPercent'].replace("%","")+","+data['closePrice'].replace("--","0")+","+data['clearPrice'].replace("--","0")+","+data['lastClose']+","+data['lastClearPrice']+")"
        db.execute(sql)
        db.commit()
        db.close()

    def run(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'【'+__name__+'】')
        url = self.get_url()
        rows = self.get_data(url)
        #铁矿石
        data = rows['data'][23]
        #print(data)
        self.insert(data)
        #焦炭
        data = rows['data'][21]
        #print(data)
        self.insert(data)
        #焦煤
        data = rows['data'][22]
        #print(data)
        self.insert(data)
