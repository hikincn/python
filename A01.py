#!/usr/bin/python
# -*- coding: UTF-8 -*-
import http
import json
import time
import urllib

import requests

from Spider import Spider


class A01(Spider):
    data = {"id": "zb", "dbcode": "hgyd", "wdcode": "zb", "m": "getTree"}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    urls = []

    def get_urls(self, param=None):
        self.get_tree()
        return self.urls

    def get_tree(self, tree_id=None):
        url = 'http://data.stats.gov.cn/easyquery.htm'
        if tree_id is not None:
            self.data["id"] = tree_id
        req = requests.post(url=url, data=self.data, headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text
        product_dic = json.loads(html)
        if len(product_dic) > 0:
            if product_dic[0]["isParent"]:
                for product in product_dic:
                    self.get_tree(product["id"])
                    print(product["id"])
            else:
                for product in product_dic:
                    url2 = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=[]&dfwds=[{"wdcode":"zb","valuecode":"' + product[
                        "id"] + '"}]&k1=1575347790952&h=1'
                    self.urls.append(url2)

    def get_data(self, url):
        cookie = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        request = urllib.request.Request(url)
        reponse = opener.open(request)
        html = reponse.read().decode('utf8')
        time.sleep(1)
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
        urls = self.get_urls()
        for url in urls:
            rows = self.get_data(url)
            for row in rows:
                data = self.parse(row)
                self.insert(data)
