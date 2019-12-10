#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from lxml import html

from Spider import Spider
from dbutils import DB


class Shibor(Spider):
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
        db.execute("insert into SGBA_ODS_WB_SHIBOR(shibor_rq,shibor_dqll,shibor_xdfd,shibor_bfbl) values('" + str(
            data[0]) + "'," + data[1] + ",'" + data[2] + "'," + data[3] + ")")
        db.commit()
        db.close()

    def run(self):
        url = self.get_url()
        data = self.get_data(url)
        tree = html.fromstring(data)
        shibor = tree.xpath('//*/table[@class="shiborquxian"]/tr[1]/td[3]/text()')
        float = tree.xpath('//*/table[@class="shiborquxian"]/tr[1]/td[4]/img/@src')
        shibor2 = tree.xpath('//*/table[@class="shiborquxian"]/tr[1]/td[5]/text()')
        datetime = tree.xpath('//*/table[1]/tr[1]/td[1]/text()')
        time = (datetime[0][:10]).replace('-', '')
        value = shibor[0]
        value2 = shibor2[0][2:]
        float = float[0]
        if "upicon.gif" in float:
            float = "上浮"
        else:
            float = "下跌"
        # print([time, value, float, value2])
        self.insert([time, value, float, value2])
