#!/usr/bin/python
# -*- coding: UTF-8 -*-
import http
import json
import time
import urllib

import requests
from lxml import etree, html

from Spider import Spider


class Stock(Spider):
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
        print(data)

    def run(self):
        ##首钢
        url = "http://push2.eastmoney.com/api/qt/stock/get?ut=fa5fd1943c7b386f172d6893dbfba10b&invt=2&fltt=2&fields=f43,f57,f58,f169,f170,f46,f44,f51,f168,f47,f164,f163,f116,f60,f45,f52,f50,f48,f167,f117,f71,f161,f49,f530,f135,f136,f137,f138,f139,f141,f142,f144,f145,f147,f148,f140,f143,f146,f149,f55,f62,f162,f92,f173,f104,f105,f84,f85,f183,f184,f185,f186,f187,f188,f189,f190,f191,f192,f107,f111,f86,f177,f78,f110,f262,f263,f264,f267,f268,f250,f251,f252,f253,f254,f255,f256,f257,f258,f266,f269,f270,f271,f273,f274,f275,f127,f199,f128,f193,f196,f194,f195,f197,f80,f280,f281,f282,f284,f285,f286,f287&secid=0.000959&cb=jQuery1124019522835879794087_1575471574506&_=1575471574507"
        rows = self.get_data(url)
        print(rows['data']['f57'],rows['data']['f58'],rows['data']['f43'],rows['data']['f44'],rows['data']['f45'],rows['data']['f46'],rows['data']['f60'],rows['data']['f116'])

        ##首长宝佳
        #url="http://push2.eastmoney.com/api/qt/clist/get?&ut=bd1d9ddb04089700cf9c27f6f7426281&pi=0&pz=7&po=1&fid=f3&fs=b:HKBLOCK|HK6&cb=jQuery.jQuery20008296812465476_1575803588337&_=1575803588153"
        #rows = self.get_data(url)
        #print(rows)

        ##首长国际
        url="http://push2.eastmoney.com/api/qt/stock/get?secid=116.00697&fields=f18,f59,f51,f52,f57,f58,f106,f105,f62,f108,f177,f43,f46,f60,f44,f45,f47,f48,f49,f113,f114,f115,f85,f84,f169,f170,f161,f163,f164,f171,f126,f168,f162,f116,f55,f92,f71,f50,f167,f117,f86,f172,f174,f175&ut=e1e6871893c6386c5ff6967026016627&fltt=2&cb=jQuery.jQuery6357659128144333_1575804401225&_=1575804401199"
        rows = self.get_data(url)
        print(rows['data']['f57'],rows['data']['f58'],rows['data']['f43'],rows['data']['f44'],rows['data']['f45'],rows['data']['f46'],rows['data']['f60'],rows['data']['f116'])

        ##首长四方
        url = "http://push2.eastmoney.com/api/qt/stock/get?secid=116.00730&fields=f18,f59,f51,f52,f57,f58,f106,f105,f62,f108,f177,f43,f46,f60,f44,f45,f47,f48,f49,f113,f114,f115,f85,f84,f169,f170,f161,f163,f164,f171,f126,f168,f162,f116,f55,f92,f71,f50,f167,f117,f86,f172,f174,f175&ut=e1e6871893c6386c5ff6967026016627&fltt=2&cb=jQuery.jQuery6656167064657854_1575804593864&_=1575804593837"
        rows = self.get_data(url)
        print(rows['data']['f57'],rows['data']['f58'],rows['data']['f43'],rows['data']['f44'],rows['data']['f45'],rows['data']['f46'],rows['data']['f60'],rows['data']['f116'])

        ##环球数码
        url = "http://push2.eastmoney.com/api/qt/stock/get?secid=116.08271&fields=f18,f59,f51,f52,f57,f58,f106,f105,f62,f108,f177,f43,f46,f60,f44,f45,f47,f48,f49,f113,f114,f115,f85,f84,f169,f170,f161,f163,f164,f171,f126,f168,f162,f116,f55,f92,f71,f50,f167,f117,f86,f172,f174,f175&ut=e1e6871893c6386c5ff6967026016627&fltt=2&cb=jQuery.jQuery0369881698775536_1575804681552&_=1575804681526"
        rows = self.get_data(url)
        print(rows['data']['f57'],rows['data']['f58'],rows['data']['f43'],rows['data']['f44'],rows['data']['f45'],rows['data']['f46'],rows['data']['f60'],rows['data']['f116'])

        ##首钢资源
        url="http://push2.eastmoney.com/api/qt/stock/get?secid=116.00639&fields=f18,f59,f51,f52,f57,f58,f106,f105,f62,f108,f177,f43,f46,f60,f44,f45,f47,f48,f49,f113,f114,f115,f85,f84,f169,f170,f161,f163,f164,f171,f126,f168,f162,f116,f55,f92,f71,f50,f167,f117,f86,f172,f174,f175&ut=e1e6871893c6386c5ff6967026016627&fltt=2&cb=jQuery.jQuery49354200090608247_1575804725899&_=1575804725854"
        rows = self.get_data(url)
        print(rows['data']['f57'],rows['data']['f58'],rows['data']['f43'],rows['data']['f44'],rows['data']['f45'],rows['data']['f46'],rows['data']['f60'],rows['data']['f116'])
