#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
from lxml import html
from spider.dbutils import DB
from datetime import datetime

from spider.Spider import Spider


class shibor(Spider):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    def get_url(self, page=None):
        return "http://www.shibor.org/shibor/web/html/shibor.html"

    def get_data(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'gb2312'
        data = req.text
        return data

    def parse(self, row):
        return row

    def insert(self, data):
        db = DB()
        sql = "select count(*) from sgba_ods_wb_hl where hl_day = '"+str(data[0])+"' and hl_code='shibor'"
        db.execute(sql)
        results = db.fetchone()
        if results[0] == 0:
            #hl_tb = float(data[2]) * float(data[3])
            db.execute("insert into SGBA_ODS_WB_HL(HL_DAY,HL_CODE,HL_NAME,HL_DATA,HL_TB) values('" + str(data[0]) + "','shibor','隔夜利率(%) o/n'," + data[1] + ")")
            db.commit()
        db.close()

    def run(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'【'+__name__+'】')
        url = self.get_url()
        data = self.get_data(url)
        tree = html.fromstring(data)
        shibor = tree.xpath('//*/table[@class="shiborquxian"]/tr[1]/td[3]/text()')
        float = tree.xpath('//*/table[@class="shiborquxian"]/tr[1]/td[4]/img/@src')
        shibor2 = tree.xpath('//*/table[@class="shiborquxian"]/tr[1]/td[5]/text()')
        datetimes = tree.xpath('//*/table[1]/tr[1]/td[1]/text()')
        time = (datetimes[0][:10]).replace('-', '')
        value = shibor[0]
        value2 = shibor2[0][2:]
        float = float[0]
        if "upicon.gif" in float:
            float = "1"
        else:
            float = "-1"
        # print([time, value, float, value2])
        self.insert([time, value, float, value2])
