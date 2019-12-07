#!/usr/bin/python
# -*- coding: UTF-8 -*-
import http
import json
import os
import time
import urllib
import pickle

import requests

from Spider import Spider


class GDZCTZ(Spider):
    data = {"id": "zb", "dbcode": "hgyd", "wdcode": "zb", "m": "getTree"}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    code = ''
    tree = {}

    def get_tree(self, parent=None):
        url = 'http://data.stats.gov.cn/easyquery.htm'
        if parent is not None:
            self.data["id"] = parent['id']
        req = requests.post(url=url, data=self.data, headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text
        product_dic = json.loads(html)
        if len(product_dic) > 0:
            if product_dic[0]["isParent"]:
                for product in product_dic:
                    time.sleep(0.5)
                    self.get_tree(product)
            else:
                for product in product_dic:
                    url2 = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=[]&dfwds=[{"wdcode":"zb","valuecode":"' + product[
                        "id"] + '"}]&k1=1575347790952&h=1'
                    self.tree[product['name']] = url2

    def get_url(self, param=None):
        if os.path.exists("dict.file"):
            with open("dict.file", "rb") as f:
                self.tree = pickle.load(f)
        else:
            self.get_tree()
            self.dump()
        return self.tree[param]

    def get_data(self, url):
        time.sleep(1)
        cookie = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        request = urllib.request.Request(url)
        reponse = opener.open(request)
        html = reponse.read().decode('utf8')
        try:
            product_dic = json.loads(html)
            return product_dic
        except Exception:
            return ""

    def parse(self, rows, param):
        nodes = rows['returndata']['wdnodes'][0]['nodes']
        for node in nodes:
            if param in node['cname']:
                self.code = node['code']
                break

        code = 'zb.' + self.code + '_sj'
        for item in rows['returndata']['datanodes']:
            if code in item['code'] and item['data']['hasdata']:
                return item['data']['strdata']
                break

    def insert(self, data):
        print(str(data))

    def dump(self):
        with open("dict.file", "wb") as f:
            pickle.dump(self.tree, f)

    def run(self):
        url = self.get_url('全国居民消费价格分类指数(上年同月=100)(2016-)')
        rows = self.get_data(url)
        value = self.parse(rows, '居民消费价格指数(上年同月=100)')
        print(value)

        url = self.get_url('按行业分固定资产投资增速（2018-）')
        rows = self.get_data(url)
        value = self.parse(rows, '采矿业固定资产投资额_累计增长')
        print(value)
        value = self.parse(rows, '黑色金属矿采选业固定资产投资额')
        print(value)
