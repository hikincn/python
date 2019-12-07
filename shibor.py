#!/usr/bin/python
# -*- coding: UTF-8 -*-
from lxml import etree, html

import requests

from Spider import Spider


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
        print(data)

    def run(self):
        url = self.get_url()
        data = self.get_data(url)
        tree = html.fromstring(data)
        shibor = tree.xpath('//*/table[@class="shiborquxian"]/tr[1]/td[3]/text()')
        datetime = tree.xpath('//*/table[1]/tr[1]/td[1]/text()')
        time=datetime[0][:16]
        value=shibor[0]
        print(value, time)
