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
        html1 = req.text

        tree = html.fromstring(html1)
        name = tree.xpath('//*[@id="price9"]/text()')
        print(name)


    def parse(self, row):
        return row

    def insert(self, data):
        print(data)

    def run(self):
        url = self.get_url()
        rows = self.get_data(url)
