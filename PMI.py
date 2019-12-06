#!/usr/bin/python
# -*- coding: UTF-8 -*-
import http
import json
import time
import urllib

import requests

from Spider import Spider


class PMI(Spider):
    data = {"id": "zb", "dbcode": "hgyd", "wdcode": "zb", "m": "getTree"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    urls = []

    def get_url(self, page=None):
        if page is None:
            return "http://data.stats.gov.cn/search.htm?s=PMI&m=searchdata&db=&p=0"
        else:
            return "http://data.stats.gov.cn/search.htm?s=PMI&m=searchdata&db=&p=" + str(page)

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
        page = 0
        while True:
            url = self.get_url(page)
            rows = self.get_data(url)
            pagecount = rows["pagecount"]
            pagecurrent = rows["pagecurrent"]
            result = rows["result"]

            for row in result:
                data = self.parse(row)
                self.insert(data)

            if pagecurrent < pagecount:
                page = int(pagecurrent) + 1
