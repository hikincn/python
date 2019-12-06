#!/usr/bin/python
# -*- coding: UTF-8 -*-
import http
import json
import time
import urllib

import requests
from lxml import etree, html
from numpy.core.defchararray import isnumeric

from Spider import Spider


class Waihui(Spider):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    def get_url(self, page=None):
        return "http://www.safe.gov.cn/AppStructured/hlw/RMBQuery.do"

    def get_data(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'utf-8'
        html1 = req.text

        tree = html.fromstring(html1)
        xpath = tree.xpath('//*/tr[@class="first"][1]/td')
        for item in xpath:
            if item.text != "":
                print(item.text)

    def parse(self, row):
        return row

    def insert(self, data):
        print(data)

    def run(self):
        url = self.get_url()
        rows = self.get_data(url)
