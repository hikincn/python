#!/usr/bin/python
# -*- coding: UTF-8 -*-
import http
import json
import time
import urllib

import requests

from Spider import Spider


class Deal(Spider):
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
        print(data)

    def run(self):
        url = self.get_url()
        rows = self.get_data(url)
        print(rows)