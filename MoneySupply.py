#!/usr/bin/python
# -*- coding: UTF-8 -*-
import html
import http
import json
import urllib

import requests

from Spider import Spider


class MoneySupply(Spider):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "wzws_cid = a9f577734c34b0592dba6fc7d402acfb94bd7d1f430797832261efab07d5eb6adfad989d8f24f7109233da6a61924a7a176cc5127c3b0d926d17926413a09253f0efe08cc6af6c6404aae18fe53455ed",
        "Host": "www.pbc.gov.cn",
        "Pragma": "no-cache",
        "Referer": "http://www.pbc.gov.cn/diaochatongjisi/116219/116319/3750274/3750284/index.html",
        "Upgrade-Insecure-Requests": "1"
    }

    def get_url(self, page=None):
        url = "http://www.pbc.gov.cn/diaochatongjisi/116219/116319/3750274/3750284/index.html"
        cookie = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        req = urllib.request.Request(url)
        reponse = opener.open(req)
        data = reponse.read().decode('utf8')
        tree = html.fromstring(data)
        url = tree.xpath('//*[@id="con"]/table[3]/tbody/tr/td/table[5]/tbody/tr/td[2]/a/@href')
        url = "http://www.pbc.gov.cn/" + url
        return url

    def get_data(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'utf-8'
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
        title = tree.xpath('//*[@id="201910信贷收支表_8284"]/table/tbody/tr[@height][6]')
        print(title)
