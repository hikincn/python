#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
from lxml import html
import random
import time
from spider.dbutils import DB
from datetime import datetime

class shibor():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

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
            hl_id =  time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(random.randint(100000,999999))
            db.execute("insert into SGBA_ODS_WB_HL(HL_ID,HL_DAY,HL_CODE,HL_NAME,HL_DATA) values('" +hl_id +"','"+ str(data[0]) + "','shibor','隔夜利率(%) o/n'," + data[1] + ")")
            db.commit()
        db.close()

    def run(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'【'+__name__+'】')
        url = "http://www.shibor.org/shibor/web/html/shibor.html"
        data = self.get_data(url)
        tree = html.fromstring(data)
        shibor = tree.xpath('//*/table[@class="shiborquxian"]/tr[1]/td[3]/text()')
        float = tree.xpath('//*/table[@class="shiborquxian"]/tr[1]/td[4]/img/@src')
        shibor2 = tree.xpath('//*/table[@class="shiborquxian"]/tr[1]/td[5]/text()')
        datetimes = tree.xpath('//*/table[1]/tr[1]/td[1]/text()')
        time = (datetimes[0][:10]).replace('-', '')
        value = shibor[0]
        self.insert([time, value])
