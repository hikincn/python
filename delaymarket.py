#!/usr/bin/python
# -*- coding: UTF-8 -*-
import http
import json
import time
import urllib

import requests
from lxml import etree, html

from Spider import Spider


class Delaymarket(Spider):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    def get_url(self, page=None):
        return "http://quote.eastmoney.com/sz000959.html"

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
        print(data)

    def run(self):
        url = "http://www.shfe.com.cn/data/delaymarket_rb.dat"
        rows = self.get_data(url)
        print(rows)

