#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import http
import json
import urllib
import random
import time
import requests
from lxml import etree, html
from spider.dbutils import DB
from datetime import datetime



class stock_hk():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

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
        dt = datetime.now()
        ltime = time.localtime(data['f86'])
        datestr = time.strftime("%Y%m%d", ltime)
        if datestr != dt.strftime("%Y%m%d"):
            pass
        GP_ID = time.strftime("%Y%m%d%H%M%S", ltime) + str(random.randint(100000,999999))
        sql = "delete from SGBA_ODS_WB_GP where gp_day = '"+ datestr+"' and gp_code = '"+str(data['f57'])+"'"
        db.execute(sql)
        db.commit()
        sql = "INSERT INTO SGBA_ODS_WB_GP(GP_ID,GP_DAY,GP_CODE,GP_NAME,GP_ZSZ,GP_ZRSPJ,GP_JRKPJ,GP_JRZGJ,GP_JRZDJ,GP_SSJG) " \
              "VALUES('" +GP_ID+"','"+datestr+"','"+  str(data['f57'])+ "','" + str(data['f58']).replace("'","")+ "'," +str(data['f116'])+ "," +str(data['f60'])+ "," +str(data['f46'])+ "," +str(data['f44'])+ "," +str(data['f45'])+ "," +str(data['f43'])+ ")"
        db.execute(sql)
        db.commit()
        db.close()

    def run(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'【'+__name__+'】')
        ##首长宝佳
        url="http://push2.eastmoney.com/api/qt/stock/get?secid=116.00103&fields=f18,f59,f51,f52,f57,f58,f106,f105,f62,f108,f177,f43,f46,f60,f44,f45,f47,f48,f49,f113,f114,f115,f85,f84,f169,f170,f161,f163,f164,f171,f126,f168,f162,f116,f55,f92,f71,f50,f167,f117,f86,f172,f174,f175&ut=e1e6871893c6386c5ff6967026016627&fltt=2&cb=jQuery.jQuery8984096671674673_1575897409998&_=1575897409888"
        rows = self.get_data(url)
        data=rows['data']
        self.insert(data)

        ##首长国际
        url="http://push2.eastmoney.com/api/qt/stock/get?secid=116.00697&fields=f18,f59,f51,f52,f57,f58,f106,f105,f62,f108,f177,f43,f46,f60,f44,f45,f47,f48,f49,f113,f114,f115,f85,f84,f169,f170,f161,f163,f164,f171,f126,f168,f162,f116,f55,f92,f71,f50,f167,f117,f86,f172,f174,f175&ut=e1e6871893c6386c5ff6967026016627&fltt=2&cb=jQuery.jQuery6357659128144333_1575804401225&_=1575804401199"
        rows = self.get_data(url)
        data=rows['data']
        self.insert(data)

        ##首长四方
        url = "http://push2.eastmoney.com/api/qt/stock/get?secid=116.00730&fields=f18,f59,f51,f52,f57,f58,f106,f105,f62,f108,f177,f43,f46,f60,f44,f45,f47,f48,f49,f113,f114,f115,f85,f84,f169,f170,f161,f163,f164,f171,f126,f168,f162,f116,f55,f92,f71,f50,f167,f117,f86,f172,f174,f175&ut=e1e6871893c6386c5ff6967026016627&fltt=2&cb=jQuery.jQuery6656167064657854_1575804593864&_=1575804593837"
        rows = self.get_data(url)
        data=rows['data']
        self.insert(data)

        ##环球数码
        url = "http://push2.eastmoney.com/api/qt/stock/get?secid=116.08271&fields=f18,f59,f51,f52,f57,f58,f106,f105,f62,f108,f177,f43,f46,f60,f44,f45,f47,f48,f49,f113,f114,f115,f85,f84,f169,f170,f161,f163,f164,f171,f126,f168,f162,f116,f55,f92,f71,f50,f167,f117,f86,f172,f174,f175&ut=e1e6871893c6386c5ff6967026016627&fltt=2&cb=jQuery.jQuery0369881698775536_1575804681552&_=1575804681526"
        rows = self.get_data(url)
        data=rows['data']
        self.insert(data)
        ##首钢资源
        url="http://push2.eastmoney.com/api/qt/stock/get?secid=116.00639&fields=f18,f59,f51,f52,f57,f58,f106,f105,f62,f108,f177,f43,f46,f60,f44,f45,f47,f48,f49,f113,f114,f115,f85,f84,f169,f170,f161,f163,f164,f171,f126,f168,f162,f116,f55,f92,f71,f50,f167,f117,f86,f172,f174,f175&ut=e1e6871893c6386c5ff6967026016627&fltt=2&cb=jQuery.jQuery49354200090608247_1575804725899&_=1575804725854"
        rows = self.get_data(url)
        data=rows['data']
        self.insert(data)
