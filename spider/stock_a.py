#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import http
import json
import urllib
import time
import requests
from lxml import etree, html
from spider.dbutils import DB
from datetime import datetime


class stock_a():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    def get_url(self, page=None):
        return "http://quote.eastmoney.com/sz000959.html"

    def get_data(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text
        html=html[html.index("(")+1:]
        html=html[:html.index(");"):]
        try:
            product_dic = json.loads(html)
            return product_dic
        except Exception:
            return ""

    def parse(self, row):
        return row

    def insert(self, data):
        db = DB()
        time.sleep(1)
        dt = datetime.now()
        ltime = time.localtime(data['f86'])
        datestr = time.strftime("%Y%m%d", ltime)
        if datestr != dt.strftime("%Y%m%d"):
            pass
        timeStr = time.strftime("%Y%m%d%H%M%S", ltime)

        sql = "delete from SGBA_ODS_WB_GP where gp_day = '"+ datestr+"' and gp_code ='000959'"
        db.execute(sql)
        db.commit()

        sql = "INSERT INTO SGBA_ODS_WB_GP(GP_ID,GP_DAY,GP_CODE,GP_NAME,GP_ZSZ,GP_ZRSPJ,GP_JRKPJ,GP_JRZGJ,GP_JRZDJ,GP_SSJG) " \
              " VALUES('" +timeStr+"','"+datestr+"','"+ str(data['f57'])+ "','" + str(data['f58']).replace("'","")+ "'," +str(data['f116'])+ "," +str(data['f60'])+ "," +str(data['f46'])+ "," +str(data['f44'])+ "," +str(data['f45'])+ "," +str(data['f43'])+ ")"
        db.execute(sql)
        db.commit()
        db.close()
        #print(sql)

    def run(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'【'+__name__+'】')
        ##首钢股份
        url = "http://push2.eastmoney.com/api/qt/stock/get?ut=fa5fd1943c7b386f172d6893dbfba10b&invt=2&fltt=2&fields=f43,f57,f58,f169,f170,f46,f44,f51,f168,f47,f164,f163,f116,f60,f45,f52,f50,f48,f167,f117,f71,f161,f49,f530,f135,f136,f137,f138,f139,f141,f142,f144,f145,f147,f148,f140,f143,f146,f149,f55,f62,f162,f92,f173,f104,f105,f84,f85,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f107,f111,f86,f177,f78,f110,f262,f263,f264,f267,f268,f250,f251,f252,f253,f254,f255,f256,f257,f258,f266,f269,f270,f271,f273,f274,f275,f127,f199,f128,f193,f196,f194,f195,f197,f80,f280,f281,f282,f284,f285,f286,f287&secid=0.000959&cb=jQuery1124019522835879794087_1575471574506&_=1575471574507"
        rows = self.get_data(url)
        data=rows['data']
        self.insert(data)
